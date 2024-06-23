# Deadline Service

### AggregationId
- **Type**: string
- **Pattern**: `^[0-9a-f]{32}$`

### AmountCapabilityName
- **Type**: string
- **Pattern**: `^([a-zA-Z][a-zA-Z0-9]{0,63}:)?amount(\.[a-zA-Z][a-zA-Z0-9]{0,63})+$`
- **Min Length**: 1
- **Max Length**: 100

### AttributeCapabilityName
- **Type**: string
- **Pattern**: `^([a-zA-Z][a-zA-Z0-9]{0,63}:)?attr(\.[a-zA-Z][a-zA-Z0-9]{0,63})+$`
- **Min Length**: 1
- **Max Length**: 100

### AttributeCapabilityValue
- **Type**: string
- **Pattern**: `^[a-zA-Z_]([a-zA-Z0-9_\-]{0,99})$`
- **Min Length**: 1
- **Max Length**: 100

### BudgetId
- **Type**: string
- **Pattern**: `^budget-[0-9a-f]{32}$`

### DnsName
- **Type**: string
- **Pattern**: `^vpce-[\w]+-[\w]+.vpce-svc-[\w]+.*.vpce.amazonaws.com$`

### EnvironmentId
- **Type**: string
- **Pattern**: `^(STEP:step-[0-9a-f]{32}:.*)|(JOB:job-[0-9a-f]{32}:.*)$`
- **Min Length**: 1
- **Max Length**: 1024

### FarmId
- **Type**: string
- **Pattern**: `^farm-[0-9a-f]{32}$`

### FileSystemLocationName
- **Type**: string
- **Pattern**: `^[0-9A-Za-z ]*$`
- **Min Length**: 1
- **Max Length**: 64

### FleetId
- **Type**: string
- **Pattern**: `^fleet-[0-9a-f]{32}$`

### FloatString
- **Type**: string
- **Pattern**: `^[-]?(0|[1-9][0-9]*)([.][0-9]+)?([eE][+-]?[0-9]+)?$`
- **Min Length**: 1
- **Max Length**: 26

### HostName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\.\-]{0,255}$`

### IamRoleArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z-]*):iam::\d{12}:role(/[!-.0-~]+)*/[\w+=,.@-]+$`

### IdentityCenterInstanceArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}$`

### IdentityCenterPrincipalId
- **Type**: string
- **Pattern**: `^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`
- **Min Length**: 1
- **Max Length**: 47

### IdentityStoreId
- **Type**: string
- **Pattern**: `^d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
- **Min Length**: 1
- **Max Length**: 36

### InstanceType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$`

### IntString
- **Type**: string
- **Pattern**: `^[-]?(0|[1-9][0-9]*)$`
- **Min Length**: 1
- **Max Length**: 20

### IpV4Address
- **Type**: string
- **Pattern**: `^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$`

### IpV6Address
- **Type**: string
- **Pattern**: `^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$`

### JobId
- **Type**: string
- **Pattern**: `^job-[0-9a-f]{32}$`

### KmsKeyArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z-]*):kms:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:key/[\w-]{1,120}$`

### LicenseEndpointId
- **Type**: string
- **Pattern**: `^le-[0-9a-f]{32}$`

### MeteredProductId
- **Type**: string
- **Pattern**: `^[0-9a-z]{1,32}-[.0-9a-z]{1,32}$`

### MonitorId
- **Type**: string
- **Pattern**: `^monitor-[0-9a-f]{32}$`

### PosixUserGroupString
- **Type**: string
- **Pattern**: `^(?:[a-z][a-z0-9-]{0,30})?$`
- **Min Length**: 0
- **Max Length**: 31

### PosixUserUserString
- **Type**: string
- **Pattern**: `^(?:[a-z][a-z0-9-]{0,30})?$`
- **Min Length**: 0
- **Max Length**: 31

### QueueEnvironmentId
- **Type**: string
- **Pattern**: `^queueenv-[0-9a-f]{32}$`

### QueueId
- **Type**: string
- **Pattern**: `^queue-[0-9a-f]{32}$`

### SecurityGroupId
- **Type**: string
- **Pattern**: `^sg-[\w]{1,120}$`

### SessionActionId
- **Type**: string
- **Pattern**: `^sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))$`

### SessionId
- **Type**: string
- **Pattern**: `^session-[0-9a-f]{32}$`

### StepId
- **Type**: string
- **Pattern**: `^step-[0-9a-f]{32}$`

### StorageProfileId
- **Type**: string
- **Pattern**: `^sp-[0-9a-f]{32}$`

### Subdomain
- **Type**: string
- **Pattern**: `^[a-z0-9-]{1,100}$`

### SubnetId
- **Type**: string
- **Pattern**: `^subnet-[\w]{1,120}$`
- **Min Length**: 1
- **Max Length**: 32

### TaskId
- **Type**: string
- **Pattern**: `^task-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))$`

### Timezone
- **Type**: string
- **Pattern**: `^UTC[-+][01][0-9]:(30|00)$`
- **Min Length**: 9
- **Max Length**: 9

### VpcId
- **Type**: string
- **Pattern**: `^vpc-[\w]{1,120}$`
- **Min Length**: 1
- **Max Length**: 32

### WindowsUserPasswordArnString
- **Type**: string
- **Pattern**: `^arn:(aws[a-zA-Z-]*):secretsmanager:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:secret:[a-zA-Z0-9-/_+=.@]{1,2028}$`
- **Min Length**: 20
- **Max Length**: 2048

### WindowsUserUserString
- **Type**: string
- **Pattern**: `^[^"\'/\[\]:;|=,+*?<>\s]*$`
- **Min Length**: 0
- **Max Length**: 111

### WorkerId
- **Type**: string
- **Pattern**: `^worker-[0-9a-f]{32}$`

