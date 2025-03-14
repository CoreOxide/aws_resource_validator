# Networkmanager Service

### AWSAccountId
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 12
- **Max Length**: 12

### AttachmentId
- **Type**: string
- **Pattern**: `^attachment-([0-9a-f]{8,17})$`
- **Min Length**: 0
- **Max Length**: 50

### ClientToken
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 256

### ConnectPeerId
- **Type**: string
- **Pattern**: `^connect-peer-([0-9a-f]{8,17})$`
- **Min Length**: 0
- **Max Length**: 50

### ConnectionArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 500

### ConnectionId
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 50

### ConstrainedString
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 256

### CoreNetworkArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 500

### CoreNetworkId
- **Type**: string
- **Pattern**: `^core-network-([0-9a-f]{8,17})$`
- **Min Length**: 0
- **Max Length**: 50

### CoreNetworkPolicyDocument
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 10000000

### CustomerGatewayArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 500

### DeviceArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 500

### DeviceId
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 50

### DirectConnectGatewayArn
- **Type**: string
- **Pattern**: `^arn:[^:]{1,63}:directconnect::[^:]{0,63}:dx-gateway\/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$`
- **Min Length**: 0
- **Max Length**: 500

### ExternalRegionCode
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 63

### FilterName
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z\.-]*$`
- **Max Length**: 128

### FilterValue
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z\*\.\\/\?-]*$`
- **Max Length**: 255

### GlobalNetworkArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 500

### GlobalNetworkId
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 50

### IPAddress
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 50

### LinkArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 500

### LinkId
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 50

### NetworkFunctionGroupName
- **Type**: string
- **Pattern**: `[\s\S]*`

### NextToken
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 2048

### OrganizationId
- **Type**: string
- **Pattern**: `^o-([0-9a-f]{8,17})$`
- **Min Length**: 0
- **Max Length**: 50

### PeeringId
- **Type**: string
- **Pattern**: `^peering-([0-9a-f]{8,17})$`
- **Min Length**: 0
- **Max Length**: 50

### ReasonContextKey
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 10000000

### ReasonContextValue
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 10000000

### ResourceArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 1500

### ResourcePolicyDocument
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 10000000

### ServerSideString
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 10000000

### SiteArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 500

### SiteId
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 50

### SubnetArn
- **Type**: string
- **Pattern**: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:subnet\/subnet-[0-9a-f]{8,17}$|^$`
- **Min Length**: 0
- **Max Length**: 500

### TagKey
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 10000000

### TagValue
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 10000000

### TransitGatewayArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 500

### TransitGatewayAttachmentArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 500

### TransitGatewayAttachmentId
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 50

### TransitGatewayConnectPeerArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 500

### TransitGatewayPeeringAttachmentId
- **Type**: string
- **Pattern**: `^tgw-attach-([0-9a-f]{8,17})$`
- **Min Length**: 0
- **Max Length**: 50

### TransitGatewayRouteTableArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 500

### VpcArn
- **Type**: string
- **Pattern**: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:vpc\/vpc-[0-9a-f]{8,17}$`
- **Min Length**: 0
- **Max Length**: 500

### VpnConnectionArn
- **Type**: string
- **Pattern**: `^arn:[^:]{1,63}:ec2:[^:]{0,63}:[^:]{0,63}:vpn-connection\/vpn-[0-9a-f]{8,17}$`
- **Min Length**: 0
- **Max Length**: 500

