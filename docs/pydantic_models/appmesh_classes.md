# Appmesh Classes

# AccessLog

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.FileAccessLog]


# AccessLogOutput

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.FileAccessLogOutput]


# AwsCloudMapInstanceAttribute

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# AwsCloudMapServiceDiscovery

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.AwsCloudMapInstanceAttribute]]

### ipPreference
- **Type**: typing.Optional[typing.Literal['IPv4_ONLY', 'IPv4_PREFERRED', 'IPv6_ONLY', 'IPv6_PREFERRED']]


# AwsCloudMapServiceDiscoveryOutput

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.AwsCloudMapInstanceAttribute]]

### ipPreference
- **Type**: typing.Optional[typing.Literal['IPv4_ONLY', 'IPv4_PREFERRED', 'IPv6_ONLY', 'IPv6_PREFERRED']]


# Backend

### virtualService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceBackend]


# BackendDefaults

### clientPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientPolicy]


# BackendDefaultsOutput

### clientPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientPolicyOutput]


# BackendOutput

### virtualService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceBackendOutput]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClientPolicy

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientPolicyTls]


# ClientPolicyOutput

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientPolicyTlsOutput]


# ClientPolicyTls

### validation
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContext'>
- **Required**: Yes

### certificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientTlsCertificate]

### enforce
- **Type**: typing.Optional[bool]

### ports
- **Type**: typing.Optional[typing.Sequence[int]]


# ClientPolicyTlsOutput

### validation
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextOutput'>
- **Required**: Yes

### certificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientTlsCertificate]

### enforce
- **Type**: typing.Optional[bool]

### ports
- **Type**: typing.Optional[typing.List[int]]


# ClientTlsCertificate

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsFileCertificate]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsSdsCertificate]


# CreateGatewayRouteInput

### gatewayRouteName
- **Type**: <class 'str'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteSpecUnion'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRef]]


# CreateGatewayRouteOutput

### gatewayRoute
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMeshInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### spec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.MeshSpec]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRef]]


# CreateMeshOutput

### mesh
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.MeshData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRouteInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### routeName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteSpecUnion'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRef]]


# CreateRouteOutput

### route
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVirtualGatewayInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewaySpecUnion'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRef]]


# CreateVirtualGatewayOutput

### virtualGateway
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVirtualNodeInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeSpecUnion'>
- **Required**: Yes

### virtualNodeName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRef]]


# CreateVirtualNodeOutput

### virtualNode
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVirtualRouterInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterSpecUnion'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRef]]


# CreateVirtualRouterOutput

### virtualRouter
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVirtualServiceInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceSpec'>
- **Required**: Yes

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRef]]


# CreateVirtualServiceOutput

### virtualService
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGatewayRouteInput

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


# DeleteGatewayRouteOutput

### gatewayRoute
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMeshInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMeshOutput

### mesh
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.MeshData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRouteInput

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


# DeleteRouteOutput

### route
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVirtualGatewayInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DeleteVirtualGatewayOutput

### virtualGateway
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVirtualNodeInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualNodeName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DeleteVirtualNodeOutput

### virtualNode
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVirtualRouterInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DeleteVirtualRouterOutput

### virtualRouter
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVirtualServiceInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DeleteVirtualServiceOutput

### virtualService
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGatewayRouteInput

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


# DescribeGatewayRouteOutput

### gatewayRoute
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMeshInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DescribeMeshOutput

### mesh
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.MeshData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRouteInput

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


# DescribeRouteOutput

### route
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVirtualGatewayInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DescribeVirtualGatewayOutput

### virtualGateway
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVirtualNodeInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualNodeName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DescribeVirtualNodeOutput

### virtualNode
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVirtualRouterInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DescribeVirtualRouterOutput

### virtualRouter
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVirtualServiceInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]


# DescribeVirtualServiceOutput

### virtualService
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# DnsServiceDiscovery

### hostname
- **Type**: <class 'str'>
- **Required**: Yes

### ipPreference
- **Type**: typing.Optional[typing.Literal['IPv4_ONLY', 'IPv4_PREFERRED', 'IPv6_ONLY', 'IPv6_PREFERRED']]

### responseType
- **Type**: typing.Optional[typing.Literal['ENDPOINTS', 'LOADBALANCER']]


# Duration

### unit
- **Type**: typing.Optional[typing.Literal['ms', 's']]

### value
- **Type**: typing.Optional[int]


# EgressFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FileAccessLog

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FileAccessLogOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GatewayRouteData

### gatewayRouteName
- **Type**: <class 'str'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResourceMetadata'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteSpecOutput'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteStatus'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes


# GatewayRouteHostnameMatch

### exact
- **Type**: typing.Optional[str]

### suffix
- **Type**: typing.Optional[str]


# GatewayRouteHostnameRewrite

### defaultTargetHostname
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# GatewayRouteRef

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


# GatewayRouteSpec

### grpcRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRoute]

### http2Route
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRoute]

### httpRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRoute]

### priority
- **Type**: typing.Optional[int]


# GatewayRouteSpecOutput

### grpcRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteOutput]

### http2Route
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteOutput]

### httpRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteOutput]

### priority
- **Type**: typing.Optional[int]


# GatewayRouteSpecUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GatewayRouteStatus

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# GatewayRouteTarget

### virtualService
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteVirtualService'>
- **Required**: Yes

### port
- **Type**: typing.Optional[int]


# GatewayRouteVirtualService

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes


# GrpcGatewayRoute

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteAction'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteMatch'>
- **Required**: Yes


# GrpcGatewayRouteAction

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteTarget'>
- **Required**: Yes

### rewrite
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteRewrite]


# GrpcGatewayRouteMatch

### hostname
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteHostnameMatch]

### metadata
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteMetadata]]

### port
- **Type**: typing.Optional[int]

### serviceName
- **Type**: typing.Optional[str]


# GrpcGatewayRouteMatchOutput

### hostname
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteHostnameMatch]

### metadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteMetadata]]

### port
- **Type**: typing.Optional[int]

### serviceName
- **Type**: typing.Optional[str]


# GrpcGatewayRouteMetadata

### name
- **Type**: <class 'str'>
- **Required**: Yes

### invert
- **Type**: typing.Optional[bool]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcMetadataMatchMethod]


# GrpcGatewayRouteOutput

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteAction'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteMatchOutput'>
- **Required**: Yes


# GrpcGatewayRouteRewrite

### hostname
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteHostnameRewrite]


# GrpcMetadataMatchMethod

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GrpcRetryPolicy

### maxRetries
- **Type**: <class 'int'>
- **Required**: Yes

### perRetryTimeout
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.Duration'>
- **Required**: Yes

### grpcRetryEvents
- **Type**: typing.Optional[typing.Sequence[typing.Literal['cancelled', 'deadline-exceeded', 'internal', 'resource-exhausted', 'unavailable']]]

### httpRetryEvents
- **Type**: typing.Optional[typing.Sequence[str]]

### tcpRetryEvents
- **Type**: typing.Optional[typing.Sequence[typing.Literal['connection-error']]]


# GrpcRetryPolicyOutput

### maxRetries
- **Type**: <class 'int'>
- **Required**: Yes

### perRetryTimeout
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.Duration'>
- **Required**: Yes

### grpcRetryEvents
- **Type**: typing.Optional[typing.List[typing.Literal['cancelled', 'deadline-exceeded', 'internal', 'resource-exhausted', 'unavailable']]]

### httpRetryEvents
- **Type**: typing.Optional[typing.List[str]]

### tcpRetryEvents
- **Type**: typing.Optional[typing.List[typing.Literal['connection-error']]]


# GrpcRoute

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteAction'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteMatch'>
- **Required**: Yes

### retryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRetryPolicy]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcTimeout]


# GrpcRouteAction

### weightedTargets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.WeightedTarget]
- **Required**: Yes


# GrpcRouteActionOutput

### weightedTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.WeightedTarget]
- **Required**: Yes


# GrpcRouteMatch

### metadata
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteMetadata]]

### methodName
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### serviceName
- **Type**: typing.Optional[str]


# GrpcRouteMatchOutput

### metadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteMetadata]]

### methodName
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### serviceName
- **Type**: typing.Optional[str]


# GrpcRouteMetadata

### name
- **Type**: <class 'str'>
- **Required**: Yes

### invert
- **Type**: typing.Optional[bool]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteMetadataMatchMethod]


# GrpcRouteMetadataMatchMethod

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GrpcRouteOutput

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteActionOutput'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteMatchOutput'>
- **Required**: Yes

### retryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRetryPolicyOutput]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcTimeout]


# GrpcTimeout

### idle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.Duration]

### perRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.Duration]


# HeaderMatchMethod

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HealthCheckPolicy

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


# HttpGatewayRoute

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteAction'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteMatch'>
- **Required**: Yes


# HttpGatewayRouteAction

### target
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteTarget'>
- **Required**: Yes

### rewrite
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteRewrite]


# HttpGatewayRouteHeader

### name
- **Type**: <class 'str'>
- **Required**: Yes

### invert
- **Type**: typing.Optional[bool]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HeaderMatchMethod]


# HttpGatewayRouteMatch

### headers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteHeader]]

### hostname
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteHostnameMatch]

### method
- **Type**: typing.Optional[typing.Literal['CONNECT', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE']]

### path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpPathMatch]

### port
- **Type**: typing.Optional[int]

### prefix
- **Type**: typing.Optional[str]

### queryParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.HttpQueryParameter]]


# HttpGatewayRouteMatchOutput

### headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteHeader]]

### hostname
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteHostnameMatch]

### method
- **Type**: typing.Optional[typing.Literal['CONNECT', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE']]

### path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpPathMatch]

### port
- **Type**: typing.Optional[int]

### prefix
- **Type**: typing.Optional[str]

### queryParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.HttpQueryParameter]]


# HttpGatewayRouteOutput

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteAction'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteMatchOutput'>
- **Required**: Yes


# HttpGatewayRoutePathRewrite

### exact
- **Type**: typing.Optional[str]


# HttpGatewayRoutePrefixRewrite

### defaultPrefix
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### value
- **Type**: typing.Optional[str]


# HttpGatewayRouteRewrite

### hostname
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteHostnameRewrite]

### path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRoutePathRewrite]

### prefix
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRoutePrefixRewrite]


# HttpPathMatch

### exact
- **Type**: typing.Optional[str]

### regex
- **Type**: typing.Optional[str]


# HttpQueryParameter

### name
- **Type**: <class 'str'>
- **Required**: Yes

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.QueryParameterMatch]


# HttpRetryPolicy

### maxRetries
- **Type**: <class 'int'>
- **Required**: Yes

### perRetryTimeout
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.Duration'>
- **Required**: Yes

### httpRetryEvents
- **Type**: typing.Optional[typing.Sequence[str]]

### tcpRetryEvents
- **Type**: typing.Optional[typing.Sequence[typing.Literal['connection-error']]]


# HttpRetryPolicyOutput

### maxRetries
- **Type**: <class 'int'>
- **Required**: Yes

### perRetryTimeout
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.Duration'>
- **Required**: Yes

### httpRetryEvents
- **Type**: typing.Optional[typing.List[str]]

### tcpRetryEvents
- **Type**: typing.Optional[typing.List[typing.Literal['connection-error']]]


# HttpRoute

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteAction'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteMatch'>
- **Required**: Yes

### retryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpRetryPolicy]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpTimeout]


# HttpRouteAction

### weightedTargets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.WeightedTarget]
- **Required**: Yes


# HttpRouteActionOutput

### weightedTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.WeightedTarget]
- **Required**: Yes


# HttpRouteHeader

### name
- **Type**: <class 'str'>
- **Required**: Yes

### invert
- **Type**: typing.Optional[bool]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HeaderMatchMethod]


# HttpRouteMatch

### headers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteHeader]]

### method
- **Type**: typing.Optional[typing.Literal['CONNECT', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE']]

### path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpPathMatch]

### port
- **Type**: typing.Optional[int]

### prefix
- **Type**: typing.Optional[str]

### queryParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.HttpQueryParameter]]

### scheme
- **Type**: typing.Optional[typing.Literal['http', 'https']]


# HttpRouteMatchOutput

### headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteHeader]]

### method
- **Type**: typing.Optional[typing.Literal['CONNECT', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE']]

### path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpPathMatch]

### port
- **Type**: typing.Optional[int]

### prefix
- **Type**: typing.Optional[str]

### queryParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.HttpQueryParameter]]

### scheme
- **Type**: typing.Optional[typing.Literal['http', 'https']]


# HttpRouteOutput

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteActionOutput'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteMatchOutput'>
- **Required**: Yes

### retryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpRetryPolicyOutput]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpTimeout]


# HttpTimeout

### idle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.Duration]

### perRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.Duration]


# JsonFormatRef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# ListGatewayRoutesInput

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


# ListGatewayRoutesInputPaginate

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfig]


# ListGatewayRoutesOutput

### gatewayRoutes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteRef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMeshesInput

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMeshesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfig]


# ListMeshesOutput

### meshes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.MeshRef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRoutesInput

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


# ListRoutesInputPaginate

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfig]


# ListRoutesOutput

### routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.RouteRef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputPaginate

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfig]


# ListTagsForResourceOutput

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.TagRef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualGatewaysInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### meshOwner
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualGatewaysInputPaginate

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfig]


# ListVirtualGatewaysOutput

### virtualGateways
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayRef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualNodesInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### meshOwner
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualNodesInputPaginate

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfig]


# ListVirtualNodesOutput

### virtualNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeRef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualRoutersInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### meshOwner
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualRoutersInputPaginate

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfig]


# ListVirtualRoutersOutput

### virtualRouters
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterRef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualServicesInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### meshOwner
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualServicesInputPaginate

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfig]


# ListVirtualServicesOutput

### virtualServices
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceRef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Listener

### portMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.PortMapping'>
- **Required**: Yes

### connectionPool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeConnectionPool]

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HealthCheckPolicy]

### outlierDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.OutlierDetection]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTimeout]

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTls]


# ListenerOutput

### portMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.PortMapping'>
- **Required**: Yes

### connectionPool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeConnectionPool]

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HealthCheckPolicy]

### outlierDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.OutlierDetection]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTimeout]

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsOutput]


# ListenerTimeout

### grpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcTimeout]

### http
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpTimeout]

### http2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpTimeout]

### tcp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TcpTimeout]


# ListenerTls

### certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsCertificate'>
- **Required**: Yes

### mode
- **Type**: typing.Literal['DISABLED', 'PERMISSIVE', 'STRICT']
- **Required**: Yes

### validation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsValidationContext]


# ListenerTlsAcmCertificate

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListenerTlsCertificate

### acm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsAcmCertificate]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsFileCertificate]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsSdsCertificate]


# ListenerTlsFileCertificate

### certificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### privateKey
- **Type**: <class 'str'>
- **Required**: Yes


# ListenerTlsOutput

### certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsCertificate'>
- **Required**: Yes

### mode
- **Type**: typing.Literal['DISABLED', 'PERMISSIVE', 'STRICT']
- **Required**: Yes

### validation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsValidationContextOutput]


# ListenerTlsSdsCertificate

### secretName
- **Type**: <class 'str'>
- **Required**: Yes


# ListenerTlsValidationContext

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsValidationContextTrust'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNames]


# ListenerTlsValidationContextOutput

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsValidationContextTrust'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNamesOutput]


# ListenerTlsValidationContextTrust

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextFileTrust]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextSdsTrust]


# Logging

### accessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.AccessLog]


# LoggingFormat

### json
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.JsonFormatRef]]

### text
- **Type**: typing.Optional[str]


# LoggingFormatOutput

### json
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.JsonFormatRef]]

### text
- **Type**: typing.Optional[str]


# LoggingOutput

### accessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.AccessLogOutput]


# MatchRange

### end
- **Type**: <class 'int'>
- **Required**: Yes

### start
- **Type**: <class 'int'>
- **Required**: Yes


# MeshData

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResourceMetadata'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.MeshSpec'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.MeshStatus'>
- **Required**: Yes


# MeshRef

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


# MeshServiceDiscovery

### ipPreference
- **Type**: typing.Optional[typing.Literal['IPv4_ONLY', 'IPv4_PREFERRED', 'IPv6_ONLY', 'IPv6_PREFERRED']]


# MeshSpec

### egressFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.EgressFilter]

### serviceDiscovery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.MeshServiceDiscovery]


# MeshStatus

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']]


# OutlierDetection

### baseEjectionDuration
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.Duration'>
- **Required**: Yes

### interval
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.Duration'>
- **Required**: Yes

### maxEjectionPercent
- **Type**: <class 'int'>
- **Required**: Yes

### maxServerErrors
- **Type**: <class 'int'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PortMapping

### port
- **Type**: <class 'int'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['grpc', 'http', 'http2', 'tcp']
- **Required**: Yes


# QueryParameterMatch

### exact
- **Type**: typing.Optional[str]


# ResourceMetadata

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


# ResponseMetadata

### RequestId
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

### HostId
- **Type**: typing.Optional[str]


# RouteData

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResourceMetadata'>
- **Required**: Yes

### routeName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteSpecOutput'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteStatus'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes


# RouteRef

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


# RouteSpec

### grpcRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRoute]

### http2Route
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpRoute]

### httpRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpRoute]

### priority
- **Type**: typing.Optional[int]

### tcpRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TcpRoute]


# RouteSpecOutput

### grpcRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteOutput]

### http2Route
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteOutput]

### httpRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteOutput]

### priority
- **Type**: typing.Optional[int]

### tcpRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TcpRouteOutput]


# RouteSpecUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RouteStatus

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# ServiceDiscovery

### awsCloudMap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.AwsCloudMapServiceDiscovery]

### dns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.DnsServiceDiscovery]


# ServiceDiscoveryOutput

### awsCloudMap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.AwsCloudMapServiceDiscoveryOutput]

### dns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.DnsServiceDiscovery]


# SubjectAlternativeNameMatchers

### exact
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SubjectAlternativeNameMatchersOutput

### exact
- **Type**: typing.List[str]
- **Required**: Yes


# SubjectAlternativeNames

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNameMatchers'>
- **Required**: Yes


# SubjectAlternativeNamesOutput

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNameMatchersOutput'>
- **Required**: Yes


# TagRef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRef]
- **Required**: Yes


# TcpRoute

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.TcpRouteAction'>
- **Required**: Yes

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TcpRouteMatch]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TcpTimeout]


# TcpRouteAction

### weightedTargets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.WeightedTarget]
- **Required**: Yes


# TcpRouteActionOutput

### weightedTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.WeightedTarget]
- **Required**: Yes


# TcpRouteMatch

### port
- **Type**: typing.Optional[int]


# TcpRouteOutput

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.TcpRouteActionOutput'>
- **Required**: Yes

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TcpRouteMatch]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TcpTimeout]


# TcpTimeout

### idle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.Duration]


# TlsValidationContext

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextTrust'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNames]


# TlsValidationContextAcmTrust

### certificateAuthorityArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# TlsValidationContextAcmTrustOutput

### certificateAuthorityArns
- **Type**: typing.List[str]
- **Required**: Yes


# TlsValidationContextFileTrust

### certificateChain
- **Type**: <class 'str'>
- **Required**: Yes


# TlsValidationContextOutput

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextTrustOutput'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNamesOutput]


# TlsValidationContextSdsTrust

### secretName
- **Type**: <class 'str'>
- **Required**: Yes


# TlsValidationContextTrust

### acm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextAcmTrust]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextFileTrust]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextSdsTrust]


# TlsValidationContextTrustOutput

### acm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextAcmTrustOutput]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextFileTrust]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextSdsTrust]


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateGatewayRouteInput

### gatewayRouteName
- **Type**: <class 'str'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteSpecUnion'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]


# UpdateGatewayRouteOutput

### gatewayRoute
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMeshInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### spec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.MeshSpec]


# UpdateMeshOutput

### mesh
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.MeshData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRouteInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### routeName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteSpecUnion'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]


# UpdateRouteOutput

### route
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVirtualGatewayInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewaySpecUnion'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]


# UpdateVirtualGatewayOutput

### virtualGateway
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVirtualNodeInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeSpecUnion'>
- **Required**: Yes

### virtualNodeName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]


# UpdateVirtualNodeOutput

### virtualNode
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVirtualRouterInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterSpecUnion'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]


# UpdateVirtualRouterOutput

### virtualRouter
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVirtualServiceInput

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceSpec'>
- **Required**: Yes

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### meshOwner
- **Type**: typing.Optional[str]


# UpdateVirtualServiceOutput

### virtualService
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadata'>
- **Required**: Yes


# VirtualGatewayAccessLog

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayFileAccessLog]


# VirtualGatewayAccessLogOutput

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayFileAccessLogOutput]


# VirtualGatewayBackendDefaults

### clientPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayClientPolicy]


# VirtualGatewayBackendDefaultsOutput

### clientPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayClientPolicyOutput]


# VirtualGatewayClientPolicy

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayClientPolicyTls]


# VirtualGatewayClientPolicyOutput

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayClientPolicyTlsOutput]


# VirtualGatewayClientPolicyTls

### validation
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContext'>
- **Required**: Yes

### certificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayClientTlsCertificate]

### enforce
- **Type**: typing.Optional[bool]

### ports
- **Type**: typing.Optional[typing.Sequence[int]]


# VirtualGatewayClientPolicyTlsOutput

### validation
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextOutput'>
- **Required**: Yes

### certificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayClientTlsCertificate]

### enforce
- **Type**: typing.Optional[bool]

### ports
- **Type**: typing.Optional[typing.List[int]]


# VirtualGatewayClientTlsCertificate

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsFileCertificate]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsSdsCertificate]


# VirtualGatewayConnectionPool

### grpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayGrpcConnectionPool]

### http
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayHttpConnectionPool]

### http2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayHttp2ConnectionPool]


# VirtualGatewayData

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResourceMetadata'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewaySpecOutput'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayStatus'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayFileAccessLog

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VirtualGatewayFileAccessLogOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VirtualGatewayGrpcConnectionPool

### maxRequests
- **Type**: <class 'int'>
- **Required**: Yes


# VirtualGatewayHealthCheckPolicy

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


# VirtualGatewayHttp2ConnectionPool

### maxRequests
- **Type**: <class 'int'>
- **Required**: Yes


# VirtualGatewayHttpConnectionPool

### maxConnections
- **Type**: <class 'int'>
- **Required**: Yes

### maxPendingRequests
- **Type**: typing.Optional[int]


# VirtualGatewayListener

### portMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayPortMapping'>
- **Required**: Yes

### connectionPool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayConnectionPool]

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayHealthCheckPolicy]

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTls]


# VirtualGatewayListenerOutput

### portMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayPortMapping'>
- **Required**: Yes

### connectionPool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayConnectionPool]

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayHealthCheckPolicy]

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsOutput]


# VirtualGatewayListenerTls

### certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsCertificate'>
- **Required**: Yes

### mode
- **Type**: typing.Literal['DISABLED', 'PERMISSIVE', 'STRICT']
- **Required**: Yes

### validation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsValidationContext]


# VirtualGatewayListenerTlsAcmCertificate

### certificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayListenerTlsCertificate

### acm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsAcmCertificate]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsFileCertificate]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsSdsCertificate]


# VirtualGatewayListenerTlsFileCertificate

### certificateChain
- **Type**: <class 'str'>
- **Required**: Yes

### privateKey
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayListenerTlsOutput

### certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsCertificate'>
- **Required**: Yes

### mode
- **Type**: typing.Literal['DISABLED', 'PERMISSIVE', 'STRICT']
- **Required**: Yes

### validation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsValidationContextOutput]


# VirtualGatewayListenerTlsSdsCertificate

### secretName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayListenerTlsValidationContext

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsValidationContextTrust'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNames]


# VirtualGatewayListenerTlsValidationContextOutput

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsValidationContextTrust'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNamesOutput]


# VirtualGatewayListenerTlsValidationContextTrust

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextFileTrust]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextSdsTrust]


# VirtualGatewayLogging

### accessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayAccessLog]


# VirtualGatewayLoggingOutput

### accessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayAccessLogOutput]


# VirtualGatewayPortMapping

### port
- **Type**: <class 'int'>
- **Required**: Yes

### protocol
- **Type**: typing.Literal['grpc', 'http', 'http2']
- **Required**: Yes


# VirtualGatewayRef

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


# VirtualGatewaySpec

### listeners
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListener]
- **Required**: Yes

### backendDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayBackendDefaults]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayLogging]


# VirtualGatewaySpecOutput

### listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerOutput]
- **Required**: Yes

### backendDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayBackendDefaultsOutput]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayLoggingOutput]


# VirtualGatewaySpecUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VirtualGatewayStatus

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# VirtualGatewayTlsValidationContext

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextTrust'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNames]


# VirtualGatewayTlsValidationContextAcmTrust

### certificateAuthorityArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# VirtualGatewayTlsValidationContextAcmTrustOutput

### certificateAuthorityArns
- **Type**: typing.List[str]
- **Required**: Yes


# VirtualGatewayTlsValidationContextFileTrust

### certificateChain
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayTlsValidationContextOutput

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextTrustOutput'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNamesOutput]


# VirtualGatewayTlsValidationContextSdsTrust

### secretName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayTlsValidationContextTrust

### acm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextAcmTrust]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextFileTrust]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextSdsTrust]


# VirtualGatewayTlsValidationContextTrustOutput

### acm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextAcmTrustOutput]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextFileTrust]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextSdsTrust]


# VirtualNodeConnectionPool

### grpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeGrpcConnectionPool]

### http
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeHttpConnectionPool]

### http2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeHttp2ConnectionPool]

### tcp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeTcpConnectionPool]


# VirtualNodeData

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResourceMetadata'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeSpecOutput'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeStatus'>
- **Required**: Yes

### virtualNodeName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualNodeGrpcConnectionPool

### maxRequests
- **Type**: <class 'int'>
- **Required**: Yes


# VirtualNodeHttp2ConnectionPool

### maxRequests
- **Type**: <class 'int'>
- **Required**: Yes


# VirtualNodeHttpConnectionPool

### maxConnections
- **Type**: <class 'int'>
- **Required**: Yes

### maxPendingRequests
- **Type**: typing.Optional[int]


# VirtualNodeRef

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


# VirtualNodeServiceProvider

### virtualNodeName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualNodeSpec

### backendDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.BackendDefaults]

### backends
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.Backend]]

### listeners
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.Listener]]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.Logging]

### serviceDiscovery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ServiceDiscovery]


# VirtualNodeSpecOutput

### backendDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.BackendDefaultsOutput]

### backends
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.BackendOutput]]

### listeners
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.ListenerOutput]]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.LoggingOutput]

### serviceDiscovery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ServiceDiscoveryOutput]


# VirtualNodeSpecUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VirtualNodeStatus

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# VirtualNodeTcpConnectionPool

### maxConnections
- **Type**: <class 'int'>
- **Required**: Yes


# VirtualRouterData

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResourceMetadata'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterSpecOutput'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterStatus'>
- **Required**: Yes

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualRouterListener

### portMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.PortMapping'>
- **Required**: Yes


# VirtualRouterRef

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


# VirtualRouterServiceProvider

### virtualRouterName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualRouterSpec

### listeners
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterListener]]


# VirtualRouterSpecOutput

### listeners
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterListener]]


# VirtualRouterSpecUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VirtualRouterStatus

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# VirtualServiceBackend

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### clientPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientPolicy]


# VirtualServiceBackendOutput

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### clientPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientPolicyOutput]


# VirtualServiceData

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResourceMetadata'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceSpec'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceStatus'>
- **Required**: Yes

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualServiceProvider

### virtualNode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeServiceProvider]

### virtualRouter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterServiceProvider]


# VirtualServiceRef

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


# VirtualServiceSpec

### provider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceProvider]


# VirtualServiceStatus

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# WeightedTarget

### virtualNode
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: <class 'int'>
- **Required**: Yes

### port
- **Type**: typing.Optional[int]


