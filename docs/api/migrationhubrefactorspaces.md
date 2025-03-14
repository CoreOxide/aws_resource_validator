# Migrationhubrefactorspaces Service

### AccountId
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### ApiGatewayId
- **Type**: string
- **Pattern**: `^[a-z0-9]{10}$`
- **Min Length**: 10
- **Max Length**: 10

### ApplicationId
- **Type**: string
- **Pattern**: `^app-[0-9A-Za-z]{10}$`
- **Min Length**: 14
- **Max Length**: 14

### ApplicationName
- **Type**: string
- **Pattern**: `^(?!app-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+$`
- **Min Length**: 3
- **Max Length**: 63

### ClientToken
- **Type**: string
- **Pattern**: `^[\x20-\x7E]{1,64}$`
- **Min Length**: 1
- **Max Length**: 64

### Description
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-_\s.!*#@\']+$`
- **Min Length**: 1
- **Max Length**: 256

### Ec2TagValue
- **Type**: string
- **Pattern**: `^.*$`
- **Min Length**: 0
- **Max Length**: 255

### EnvironmentId
- **Type**: string
- **Pattern**: `^env-[0-9A-Za-z]{10}$`
- **Min Length**: 14
- **Max Length**: 14

### EnvironmentName
- **Type**: string
- **Pattern**: `^(?!env-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+$`
- **Min Length**: 3
- **Max Length**: 63

### ErrorMessage
- **Type**: string
- **Pattern**: `^[\p{Alnum}\p{Punct}\p{Blank}]*$`
- **Min Length**: 0
- **Max Length**: 255

### LambdaArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$`
- **Min Length**: 1
- **Max Length**: 2048

### NextToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9/\+\=]{0,2048}$`
- **Min Length**: 1
- **Max Length**: 2048

### NlbArn
- **Type**: string
- **Pattern**: `^arn:aws:elasticloadbalancing:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+$`
- **Min Length**: 20
- **Max Length**: 2048

### NlbName
- **Type**: string
- **Pattern**: `^(?!internal-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+.*[^-]$`
- **Min Length**: 1
- **Max Length**: 32

### PathResourceToIdValue
- **Type**: string
- **Pattern**: `^[a-z0-9]{10}$`
- **Min Length**: 10
- **Max Length**: 10

### PolicyString
- **Type**: string
- **Pattern**: `^.*\S.*$`
- **Min Length**: 1
- **Max Length**: 300000

### ResourceArn
- **Type**: string
- **Pattern**: `^arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+$`
- **Min Length**: 20
- **Max Length**: 2048

### ResourceIdentifier
- **Type**: string
- **Pattern**: `(^(env|svc|pxy|rte|app)-([0-9A-Za-z]{10}$))`
- **Min Length**: 3
- **Max Length**: 63

### ResourcePolicyIdentifier
- **Type**: string
- **Pattern**: `^arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+$`
- **Min Length**: 20
- **Max Length**: 2048

### RouteId
- **Type**: string
- **Pattern**: `^rte-[0-9A-Za-z]{10}$`
- **Min Length**: 14
- **Max Length**: 14

### ServiceId
- **Type**: string
- **Pattern**: `^svc-[0-9A-Za-z]{10}$`
- **Min Length**: 14
- **Max Length**: 14

### ServiceName
- **Type**: string
- **Pattern**: `^(?!svc-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+$`
- **Min Length**: 3
- **Max Length**: 63

### StageName
- **Type**: string
- **Pattern**: `^[-a-zA-Z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 128

### TagMapKeyString
- **Type**: string
- **Pattern**: `^(?!aws:).+`
- **Min Length**: 1
- **Max Length**: 128

### TransitGatewayId
- **Type**: string
- **Pattern**: `^tgw-[-a-f0-9]{17}$`
- **Min Length**: 21
- **Max Length**: 21

### Uri
- **Type**: string
- **Pattern**: `^https?://[-a-zA-Z0-9+\x38@#/%?=~_|!:,.;]*[-a-zA-Z0-9+\x38@#/%=~_|]$`
- **Min Length**: 1
- **Max Length**: 2048

### UriPath
- **Type**: string
- **Pattern**: `^(/([a-zA-Z0-9._:-]+|\{[a-zA-Z0-9._:-]+\}))+$`
- **Min Length**: 1
- **Max Length**: 2048

### VpcId
- **Type**: string
- **Pattern**: `^vpc-[-a-f0-9]{8}([-a-f0-9]{9})?$`
- **Min Length**: 12
- **Max Length**: 21

### VpcLinkId
- **Type**: string
- **Pattern**: `^[a-z0-9]{10}$`
- **Min Length**: 10
- **Max Length**: 10

