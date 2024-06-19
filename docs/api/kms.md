# Kms Service

### AliasNameType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9:/_-]+$`
- **Min Length**: 1
- **Max Length**: 256

### CloudHsmClusterIdType
- **Type**: string
- **Pattern**: `cluster-[2-7a-zA-Z]{11,16}`
- **Min Length**: 19
- **Max Length**: 24

### GrantNameType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9:/_-]+$`
- **Min Length**: 1
- **Max Length**: 256

### MarkerType
- **Type**: string
- **Pattern**: `[\u0020-\u00FF]*`
- **Min Length**: 1
- **Max Length**: 1024

### PolicyNameType
- **Type**: string
- **Pattern**: `[\w]+`
- **Min Length**: 1
- **Max Length**: 128

### PolicyType
- **Type**: string
- **Pattern**: `[\u0009\u000A\u000D\u0020-\u00FF]+`
- **Min Length**: 1
- **Max Length**: 131072

### PrincipalIdType
- **Type**: string
- **Pattern**: `^[\w+=,.@:/-]+$`
- **Min Length**: 1
- **Max Length**: 256

### RegionType
- **Type**: string
- **Pattern**: `^([a-z]+-){2,3}\d+$`
- **Min Length**: 1
- **Max Length**: 32

### XksKeyIdType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_.]+$`
- **Min Length**: 1
- **Max Length**: 128

### XksProxyAuthenticationAccessKeyIdType
- **Type**: string
- **Pattern**: `^[A-Z2-7]+$`
- **Min Length**: 20
- **Max Length**: 30

### XksProxyAuthenticationRawSecretAccessKeyType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/+=]+$`
- **Min Length**: 43
- **Max Length**: 64

### XksProxyUriEndpointType
- **Type**: string
- **Pattern**: `^https://[a-zA-Z0-9.-]+$`
- **Min Length**: 10
- **Max Length**: 128

### XksProxyUriPathType
- **Type**: string
- **Pattern**: `^(/[a-zA-Z0-9\/_-]+/kms/xks/v\d{1,2})$|^(/kms/xks/v\d{1,2})$`
- **Min Length**: 10
- **Max Length**: 128

### XksProxyVpcEndpointServiceNameType
- **Type**: string
- **Pattern**: `^com\.amazonaws\.vpce\.([a-z]+-){2,3}\d+\.vpce-svc-[0-9a-z]+$`
- **Min Length**: 20
- **Max Length**: 64

