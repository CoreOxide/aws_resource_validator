# Elbv2 Service

### CustomerOwnedIpv4Pool
- **Type**: string
- **Pattern**: `^(ipv4pool-coip-)[a-zA-Z0-9]+$`
- **Max Length**: 256

### FixedResponseActionStatusCode
- **Type**: string
- **Pattern**: `^(2|4|5)\d\d$`

### LoadBalancerAttributeKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._]+$`
- **Max Length**: 256

### RedirectActionProtocol
- **Type**: string
- **Pattern**: `^(HTTPS?|#\{protocol\})$`

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 0
- **Max Length**: 256

### TargetGroupAttributeKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._]+$`
- **Max Length**: 256

### TrustStoreName
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9]+-)*[a-zA-Z0-9]+$`
- **Min Length**: 1
- **Max Length**: 32

