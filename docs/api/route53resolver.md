# Route53resolver Service

### Name
- **Type**: string
- **Pattern**: `(?!^[0-9]+$)([a-zA-Z0-9\-_\' \']+)`
- **Max Length**: 64

### OutpostArn
- **Type**: string
- **Pattern**: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
- **Min Length**: 1
- **Max Length**: 255

### ResolverQueryLogConfigName
- **Type**: string
- **Pattern**: `(?!^[0-9]+$)([a-zA-Z0-9\-_\' \']+)`
- **Min Length**: 1
- **Max Length**: 64

