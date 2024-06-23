# S3outposts Service

### AwsAccountId
- **Type**: string
- **Pattern**: `^\d{12}$`

### CustomerOwnedIpv4Pool
- **Type**: string
- **Pattern**: `^ipv4pool-coip-([0-9a-f]{17})$`

### EndpointArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):s3-outposts:[a-z\-0-9]*:[0-9]{12}:outpost/(op-[a-f0-9]{17}|ec2)/endpoint/[a-zA-Z0-9]{19}$`

### EndpointId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{19}$`

### NextToken
- **Type**: string
- **Pattern**: `^[A-Za-z0-9\+\:\/\=\?\#-_]+$`
- **Min Length**: 1
- **Max Length**: 1024

### OutpostArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):outposts:[a-z\-0-9]*:[0-9]{12}:outpost/(op-[a-f0-9]{17}|ec2)$`

### OutpostId
- **Type**: string
- **Pattern**: `^(op-[a-f0-9]{17}|\d{12}|ec2)$`

### S3OutpostArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):s3-outposts:[a-z\-0-9]*:[0-9]{12}:outpost/(op-[a-f0-9]{17}|\d{12})/s3$`

### SecurityGroupId
- **Type**: string
- **Pattern**: `^sg-([0-9a-f]{8}|[0-9a-f]{17})$`

### SubnetId
- **Type**: string
- **Pattern**: `^subnet-([0-9a-f]{8}|[0-9a-f]{17})$`

