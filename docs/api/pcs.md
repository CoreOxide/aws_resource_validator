# Pcs Service

### AmiId
- **Type**: string
- **Pattern**: `ami-[a-z0-9]+`

### Arn
- **Type**: string
- **Pattern**: `arn:aws*:pcs:.*:[0-9]{12}:.*/[a-z0-9_\-]+`
- **Min Length**: 1
- **Max Length**: 1011

### BootstrapId
- **Type**: string
- **Pattern**: `[\S]+`
- **Min Length**: 1
- **Max Length**: 1000

### ClusterIdentifier
- **Type**: string
- **Pattern**: `(pcs_[a-zA-Z0-9]+|[A-Za-z][A-Za-z0-9-]{1,40})`

### ClusterName
- **Type**: string
- **Pattern**: `(?!pcs_)^(?![A-Za-z0-9]{10}$)[A-Za-z][A-Za-z0-9-]+`
- **Min Length**: 1
- **Max Length**: 40

### ComputeNodeGroupIdentifier
- **Type**: string
- **Pattern**: `(pcs_[a-zA-Z0-9]+|[A-Za-z][A-Za-z0-9-]{1,25})`

### ComputeNodeGroupName
- **Type**: string
- **Pattern**: `(?!pcs_)^(?![A-Za-z0-9]{10}$)[A-Za-z][A-Za-z0-9-]+`
- **Min Length**: 1
- **Max Length**: 25

### InstanceProfileArn
- **Type**: string
- **Pattern**: `arn:aws([a-zA-Z-]{0,10})?:iam::[0-9]{12}:instance-profile/.{1,128}`

### QueueIdentifier
- **Type**: string
- **Pattern**: `(pcs_[a-zA-Z0-9]+|[A-Za-z][A-Za-z0-9-]{1,25})`

### QueueName
- **Type**: string
- **Pattern**: `(?!pcs_)^(?![A-Za-z0-9]{10}$)[A-Za-z][A-Za-z0-9-]+`
- **Min Length**: 1
- **Max Length**: 25

### SecurityGroupId
- **Type**: string
- **Pattern**: `sg-\w{8,17}`

### SubnetId
- **Type**: string
- **Pattern**: `subnet-\w{8,17}`

