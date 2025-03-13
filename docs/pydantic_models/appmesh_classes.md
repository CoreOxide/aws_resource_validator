# Appmesh Classes

# AccessLogOutputTypeDef

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.FileAccessLogOutputTypeDef]


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


# AwsCloudMapServiceDiscoveryOutputTypeDef

### namespaceName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.AwsCloudMapInstanceAttributeTypeDef]]

### ipPreference
- **Type**: typing.Optional[typing.Literal['IPv4_ONLY', 'IPv4_PREFERRED', 'IPv6_ONLY', 'IPv6_PREFERRED']]


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


# BackendDefaultsOutputTypeDef

### clientPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientPolicyOutputTypeDef]


# BackendDefaultsTypeDef

### clientPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientPolicyTypeDef]


# BackendOutputTypeDef

### virtualService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceBackendOutputTypeDef]


# BackendTypeDef

### virtualService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceBackendTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClientPolicyOutputTypeDef

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientPolicyTlsOutputTypeDef]


# ClientPolicyTlsOutputTypeDef

### validation
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextOutputTypeDef'>
- **Required**: Yes

### certificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientTlsCertificateTypeDef]

### enforce
- **Type**: typing.Optional[bool]

### ports
- **Type**: typing.Optional[typing.List[int]]


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


# CreateGatewayRouteInputTypeDef

### gatewayRouteName
- **Type**: <class 'str'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteSpecUnionTypeDef'>
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


# CreateMeshInputTypeDef

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


# CreateRouteInputTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### routeName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteSpecUnionTypeDef'>
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


# CreateVirtualGatewayInputTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewaySpecUnionTypeDef'>
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


# CreateVirtualNodeInputTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeSpecUnionTypeDef'>
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


# CreateVirtualRouterInputTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterSpecUnionTypeDef'>
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


# CreateVirtualServiceInputTypeDef

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


# DeleteGatewayRouteInputTypeDef

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


# DeleteMeshInputTypeDef

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


# DeleteRouteInputTypeDef

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


# DeleteVirtualGatewayInputTypeDef

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


# DeleteVirtualNodeInputTypeDef

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


# DeleteVirtualRouterInputTypeDef

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


# DeleteVirtualServiceInputTypeDef

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


# DescribeGatewayRouteInputTypeDef

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


# DescribeMeshInputTypeDef

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


# DescribeRouteInputTypeDef

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


# DescribeVirtualGatewayInputTypeDef

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


# DescribeVirtualNodeInputTypeDef

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


# DescribeVirtualRouterInputTypeDef

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


# DescribeVirtualServiceInputTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FileAccessLogOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FileAccessLogTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteSpecOutputTypeDef'>
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


# GatewayRouteSpecOutputTypeDef

### grpcRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteOutputTypeDef]

### http2Route
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteOutputTypeDef]

### httpRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteOutputTypeDef]

### priority
- **Type**: typing.Optional[int]


# GatewayRouteSpecTypeDef

### grpcRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteTypeDef]

### http2Route
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteTypeDef]

### httpRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteTypeDef]

### priority
- **Type**: typing.Optional[int]


# GatewayRouteSpecUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# GrpcGatewayRouteMatchOutputTypeDef

### hostname
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteHostnameMatchTypeDef]

### metadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteMetadataTypeDef]]

### port
- **Type**: typing.Optional[int]

### serviceName
- **Type**: typing.Optional[str]


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


# GrpcGatewayRouteOutputTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteActionTypeDef'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcGatewayRouteMatchOutputTypeDef'>
- **Required**: Yes


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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GrpcRetryPolicyOutputTypeDef

### maxRetries
- **Type**: <class 'int'>
- **Required**: Yes

### perRetryTimeout
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.DurationTypeDef'>
- **Required**: Yes

### grpcRetryEvents
- **Type**: typing.Optional[typing.List[typing.Literal['cancelled', 'deadline-exceeded', 'internal', 'resource-exhausted', 'unavailable']]]

### httpRetryEvents
- **Type**: typing.Optional[typing.List[str]]

### tcpRetryEvents
- **Type**: typing.Optional[typing.List[typing.Literal['connection-error']]]


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


# GrpcRouteActionOutputTypeDef

### weightedTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.WeightedTargetTypeDef]
- **Required**: Yes


# GrpcRouteActionTypeDef

### weightedTargets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.WeightedTargetTypeDef]
- **Required**: Yes


# GrpcRouteMatchOutputTypeDef

### metadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteMetadataTypeDef]]

### methodName
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### serviceName
- **Type**: typing.Optional[str]


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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GrpcRouteMetadataTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### invert
- **Type**: typing.Optional[bool]

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteMetadataMatchMethodTypeDef]


# GrpcRouteOutputTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteActionOutputTypeDef'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteMatchOutputTypeDef'>
- **Required**: Yes

### retryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRetryPolicyOutputTypeDef]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcTimeoutTypeDef]


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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# HttpGatewayRouteMatchOutputTypeDef

### headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteHeaderTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.HttpQueryParameterTypeDef]]


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


# HttpGatewayRouteOutputTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteActionTypeDef'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpGatewayRouteMatchOutputTypeDef'>
- **Required**: Yes


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


# HttpRetryPolicyOutputTypeDef

### maxRetries
- **Type**: <class 'int'>
- **Required**: Yes

### perRetryTimeout
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.DurationTypeDef'>
- **Required**: Yes

### httpRetryEvents
- **Type**: typing.Optional[typing.List[str]]

### tcpRetryEvents
- **Type**: typing.Optional[typing.List[typing.Literal['connection-error']]]


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


# HttpRouteActionOutputTypeDef

### weightedTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.WeightedTargetTypeDef]
- **Required**: Yes


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


# HttpRouteMatchOutputTypeDef

### headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteHeaderTypeDef]]

### method
- **Type**: typing.Optional[typing.Literal['CONNECT', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT', 'TRACE']]

### path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpPathMatchTypeDef]

### port
- **Type**: typing.Optional[int]

### prefix
- **Type**: typing.Optional[str]

### queryParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.HttpQueryParameterTypeDef]]

### scheme
- **Type**: typing.Optional[typing.Literal['http', 'https']]


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


# HttpRouteOutputTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteActionOutputTypeDef'>
- **Required**: Yes

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteMatchOutputTypeDef'>
- **Required**: Yes

### retryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpRetryPolicyOutputTypeDef]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpTimeoutTypeDef]


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


# ListGatewayRoutesInputPaginateTypeDef

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


# ListGatewayRoutesInputTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMeshesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfigTypeDef]


# ListMeshesInputTypeDef

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMeshesOutputTypeDef

### meshes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.MeshRefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRoutesInputPaginateTypeDef

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


# ListRoutesInputTypeDef

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

### routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.RouteRefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputPaginateTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfigTypeDef]


# ListTagsForResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.TagRefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualGatewaysInputPaginateTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfigTypeDef]


# ListVirtualGatewaysInputTypeDef

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

### virtualGateways
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayRefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualNodesInputPaginateTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfigTypeDef]


# ListVirtualNodesInputTypeDef

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

### virtualNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeRefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualRoutersInputPaginateTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfigTypeDef]


# ListVirtualRoutersInputTypeDef

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

### virtualRouters
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterRefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListVirtualServicesInputPaginateTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### meshOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.PaginatorConfigTypeDef]


# ListVirtualServicesInputTypeDef

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

### virtualServices
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualServiceRefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListenerOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsOutputTypeDef]


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


# ListenerTlsOutputTypeDef

### certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsCertificateTypeDef'>
- **Required**: Yes

### mode
- **Type**: typing.Literal['DISABLED', 'PERMISSIVE', 'STRICT']
- **Required**: Yes

### validation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsValidationContextOutputTypeDef]


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


# ListenerTlsValidationContextOutputTypeDef

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.ListenerTlsValidationContextTrustTypeDef'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNamesOutputTypeDef]


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


# LoggingFormatOutputTypeDef

### json
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.JsonFormatRefTypeDef]]

### text
- **Type**: typing.Optional[str]


# LoggingFormatTypeDef

### json
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.JsonFormatRefTypeDef]]

### text
- **Type**: typing.Optional[str]


# LoggingOutputTypeDef

### accessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.AccessLogOutputTypeDef]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteSpecOutputTypeDef'>
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


# RouteSpecOutputTypeDef

### grpcRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.GrpcRouteOutputTypeDef]

### http2Route
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteOutputTypeDef]

### httpRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.HttpRouteOutputTypeDef]

### priority
- **Type**: typing.Optional[int]

### tcpRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TcpRouteOutputTypeDef]


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


# RouteSpecUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RouteStatusTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# ServiceDiscoveryOutputTypeDef

### awsCloudMap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.AwsCloudMapServiceDiscoveryOutputTypeDef]

### dns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.DnsServiceDiscoveryTypeDef]


# ServiceDiscoveryTypeDef

### awsCloudMap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.AwsCloudMapServiceDiscoveryTypeDef]

### dns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.DnsServiceDiscoveryTypeDef]


# SubjectAlternativeNameMatchersOutputTypeDef

### exact
- **Type**: typing.List[str]
- **Required**: Yes


# SubjectAlternativeNameMatchersTypeDef

### exact
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SubjectAlternativeNamesOutputTypeDef

### match
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNameMatchersOutputTypeDef'>
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


# TagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.TagRefTypeDef]
- **Required**: Yes


# TcpRouteActionOutputTypeDef

### weightedTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.WeightedTargetTypeDef]
- **Required**: Yes


# TcpRouteActionTypeDef

### weightedTargets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.WeightedTargetTypeDef]
- **Required**: Yes


# TcpRouteMatchTypeDef

### port
- **Type**: typing.Optional[int]


# TcpRouteOutputTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.TcpRouteActionOutputTypeDef'>
- **Required**: Yes

### match
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TcpRouteMatchTypeDef]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TcpTimeoutTypeDef]


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


# TlsValidationContextAcmTrustOutputTypeDef

### certificateAuthorityArns
- **Type**: typing.List[str]
- **Required**: Yes


# TlsValidationContextAcmTrustTypeDef

### certificateAuthorityArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# TlsValidationContextFileTrustTypeDef

### certificateChain
- **Type**: <class 'str'>
- **Required**: Yes


# TlsValidationContextOutputTypeDef

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextTrustOutputTypeDef'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNamesOutputTypeDef]


# TlsValidationContextSdsTrustTypeDef

### secretName
- **Type**: <class 'str'>
- **Required**: Yes


# TlsValidationContextTrustOutputTypeDef

### acm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextAcmTrustOutputTypeDef]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextFileTrustTypeDef]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.TlsValidationContextSdsTrustTypeDef]


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


# UntagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateGatewayRouteInputTypeDef

### gatewayRouteName
- **Type**: <class 'str'>
- **Required**: Yes

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.GatewayRouteSpecUnionTypeDef'>
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


# UpdateMeshInputTypeDef

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


# UpdateRouteInputTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### routeName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.RouteSpecUnionTypeDef'>
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


# UpdateVirtualGatewayInputTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewaySpecUnionTypeDef'>
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


# UpdateVirtualNodeInputTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeSpecUnionTypeDef'>
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


# UpdateVirtualRouterInputTypeDef

### meshName
- **Type**: <class 'str'>
- **Required**: Yes

### spec
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterSpecUnionTypeDef'>
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


# UpdateVirtualServiceInputTypeDef

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


# VirtualGatewayAccessLogOutputTypeDef

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayFileAccessLogOutputTypeDef]


# VirtualGatewayAccessLogTypeDef

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayFileAccessLogTypeDef]


# VirtualGatewayBackendDefaultsOutputTypeDef

### clientPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayClientPolicyOutputTypeDef]


# VirtualGatewayBackendDefaultsTypeDef

### clientPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayClientPolicyTypeDef]


# VirtualGatewayClientPolicyOutputTypeDef

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayClientPolicyTlsOutputTypeDef]


# VirtualGatewayClientPolicyTlsOutputTypeDef

### validation
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextOutputTypeDef'>
- **Required**: Yes

### certificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayClientTlsCertificateTypeDef]

### enforce
- **Type**: typing.Optional[bool]

### ports
- **Type**: typing.Optional[typing.List[int]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewaySpecOutputTypeDef'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayStatusTypeDef'>
- **Required**: Yes

### virtualGatewayName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayFileAccessLogOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VirtualGatewayFileAccessLogTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# VirtualGatewayListenerOutputTypeDef

### portMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayPortMappingTypeDef'>
- **Required**: Yes

### connectionPool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayConnectionPoolTypeDef]

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayHealthCheckPolicyTypeDef]

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsOutputTypeDef]


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


# VirtualGatewayListenerTlsOutputTypeDef

### certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsCertificateTypeDef'>
- **Required**: Yes

### mode
- **Type**: typing.Literal['DISABLED', 'PERMISSIVE', 'STRICT']
- **Required**: Yes

### validation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsValidationContextOutputTypeDef]


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


# VirtualGatewayListenerTlsValidationContextOutputTypeDef

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTlsValidationContextTrustTypeDef'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNamesOutputTypeDef]


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


# VirtualGatewayLoggingOutputTypeDef

### accessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayAccessLogOutputTypeDef]


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


# VirtualGatewaySpecOutputTypeDef

### listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerOutputTypeDef]
- **Required**: Yes

### backendDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayBackendDefaultsOutputTypeDef]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayLoggingOutputTypeDef]


# VirtualGatewaySpecTypeDef

### listeners
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayListenerTypeDef]
- **Required**: Yes

### backendDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayBackendDefaultsTypeDef]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayLoggingTypeDef]


# VirtualGatewaySpecUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VirtualGatewayStatusTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef

### certificateAuthorityArns
- **Type**: typing.List[str]
- **Required**: Yes


# VirtualGatewayTlsValidationContextAcmTrustTypeDef

### certificateAuthorityArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# VirtualGatewayTlsValidationContextFileTrustTypeDef

### certificateChain
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayTlsValidationContextOutputTypeDef

### trust
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextTrustOutputTypeDef'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.SubjectAlternativeNamesOutputTypeDef]


# VirtualGatewayTlsValidationContextSdsTrustTypeDef

### secretName
- **Type**: <class 'str'>
- **Required**: Yes


# VirtualGatewayTlsValidationContextTrustOutputTypeDef

### acm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextFileTrustTypeDef]

### sds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.VirtualGatewayTlsValidationContextSdsTrustTypeDef]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualNodeSpecOutputTypeDef'>
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


# VirtualNodeSpecOutputTypeDef

### backendDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.BackendDefaultsOutputTypeDef]

### backends
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.BackendOutputTypeDef]]

### listeners
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.ListenerOutputTypeDef]]

### logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.LoggingOutputTypeDef]

### serviceDiscovery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ServiceDiscoveryOutputTypeDef]


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


# VirtualNodeSpecUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterSpecOutputTypeDef'>
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


# VirtualRouterSpecOutputTypeDef

### listeners
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterListenerTypeDef]]


# VirtualRouterSpecTypeDef

### listeners
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appmesh_classes.VirtualRouterListenerTypeDef]]


# VirtualRouterSpecUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VirtualRouterStatusTypeDef

### status
- **Type**: typing.Literal['ACTIVE', 'DELETED', 'INACTIVE']
- **Required**: Yes


# VirtualServiceBackendOutputTypeDef

### virtualServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### clientPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appmesh_classes.ClientPolicyOutputTypeDef]


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


