# Vpclattice Service

### AccessLogDestinationArn
- **Type**: string
- **Pattern**: `^arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?$`
- **Min Length**: 20
- **Max Length**: 2048

### AccessLogSubscriptionArn
- **Type**: string
- **Pattern**: `^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:accesslogsubscription/als-[0-9a-z]{17}$`
- **Min Length**: 20
- **Max Length**: 2048

### AccessLogSubscriptionId
- **Type**: string
- **Pattern**: `^als-[0-9a-z]{17}$`
- **Min Length**: 21
- **Max Length**: 21

### AccessLogSubscriptionIdentifier
- **Type**: string
- **Pattern**: `^((als-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:accesslogsubscription/als-[0-9a-z]{17}))$`
- **Min Length**: 17
- **Max Length**: 2048

### AccountId
- **Type**: string
- **Pattern**: `^[0-9]{12}$`
- **Min Length**: 1
- **Max Length**: 12

### Arn
- **Type**: string
- **Pattern**: `^arn:[a-z0-9][-.a-z0-9]{0,62}:vpc-lattice:([a-z0-9][-.a-z0-9]{0,62})?:\d{12}?:[^/].{0,1023}$`
- **Min Length**: 0
- **Max Length**: 1224

### CertificateArn
- **Type**: string
- **Pattern**: `^(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:certificate/[0-9a-z-]+)?$`
- **Min Length**: 0
- **Max Length**: 2048

### ClientToken
- **Type**: string
- **Pattern**: `[!-~]+`
- **Min Length**: 1
- **Max Length**: 64

### HealthCheckPath
- **Type**: string
- **Pattern**: `(^/[a-zA-Z0-9@:%_+.~#?&/=-]*$|(^$))`
- **Min Length**: 0
- **Max Length**: 2048

### HttpCodeMatcher
- **Type**: string
- **Pattern**: `(^[0-9-,]+$|(^$))`
- **Min Length**: 0
- **Max Length**: 2000

### ListenerArn
- **Type**: string
- **Pattern**: `^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}$`
- **Min Length**: 20
- **Max Length**: 2048

### ListenerId
- **Type**: string
- **Pattern**: `^listener-[0-9a-z]{17}$`
- **Min Length**: 26
- **Max Length**: 26

### ListenerIdentifier
- **Type**: string
- **Pattern**: `^((listener-[0-9a-z]{17})|(^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}$))$`
- **Min Length**: 20
- **Max Length**: 2048

### ListenerName
- **Type**: string
- **Pattern**: `^(?!listener-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$`
- **Min Length**: 3
- **Max Length**: 63

### PathMatchExact
- **Type**: string
- **Pattern**: `^/[a-zA-Z0-9@:%_+.~#?&/=-]*$`
- **Min Length**: 1
- **Max Length**: 200

### PathMatchPrefix
- **Type**: string
- **Pattern**: `^/[a-zA-Z0-9@:%_+.~#?&/=-]*$`
- **Min Length**: 1
- **Max Length**: 200

### PolicyString
- **Type**: string
- **Pattern**: `^.*\S.*$`
- **Min Length**: 1
- **Max Length**: 10000

### ResourceArn
- **Type**: string
- **Pattern**: `^arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(service/svc))-[0-9a-z]{17}$`
- **Min Length**: 20
- **Max Length**: 200

### ResourceId
- **Type**: string
- **Pattern**: `^((sn)|(svc))-[0-9a-z]{17}$`
- **Min Length**: 20
- **Max Length**: 50

### ResourceIdentifier
- **Type**: string
- **Pattern**: `^((((sn)|(svc))-[0-9a-z]{17})|(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(service/svc))-[0-9a-z]{17}))$`
- **Min Length**: 17
- **Max Length**: 200

### RuleArn
- **Type**: string
- **Pattern**: `^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}/rule/rule-[0-9a-z]{17}$`
- **Min Length**: 20
- **Max Length**: 2048

### RuleId
- **Type**: string
- **Pattern**: `^rule-[0-9a-z]{17}$`
- **Min Length**: 5
- **Max Length**: 22

### RuleIdentifier
- **Type**: string
- **Pattern**: `^((rule-[0-9a-z]{17})|(^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}/rule/rule-[0-9a-z]{17}$))$`
- **Min Length**: 20
- **Max Length**: 2048

### RuleName
- **Type**: string
- **Pattern**: `^(?!rule-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$`
- **Min Length**: 3
- **Max Length**: 63

### SecurityGroupId
- **Type**: string
- **Pattern**: `^sg-(([0-9a-z]{8})|([0-9a-z]{17}))$`
- **Min Length**: 5
- **Max Length**: 200

### ServiceArn
- **Type**: string
- **Pattern**: `^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}$`
- **Min Length**: 20
- **Max Length**: 2048

### ServiceId
- **Type**: string
- **Pattern**: `^svc-[0-9a-z]{17}$`
- **Min Length**: 21
- **Max Length**: 21

### ServiceIdentifier
- **Type**: string
- **Pattern**: `^((svc-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}))$`
- **Min Length**: 17
- **Max Length**: 2048

### ServiceName
- **Type**: string
- **Pattern**: `^(?!svc-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$`
- **Min Length**: 3
- **Max Length**: 40

### ServiceNetworkArn
- **Type**: string
- **Pattern**: `^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}$`
- **Min Length**: 32
- **Max Length**: 2048

### ServiceNetworkId
- **Type**: string
- **Pattern**: `^sn-[0-9a-z]{17}$`
- **Min Length**: 32
- **Max Length**: 32

### ServiceNetworkIdentifier
- **Type**: string
- **Pattern**: `^((sn-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}))$`
- **Min Length**: 3
- **Max Length**: 2048

### ServiceNetworkName
- **Type**: string
- **Pattern**: `^(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$`
- **Min Length**: 3
- **Max Length**: 63

### ServiceNetworkServiceAssociationArn
- **Type**: string
- **Pattern**: `^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkserviceassociation/snsa-[0-9a-z]{17}$`
- **Min Length**: 20
- **Max Length**: 2048

### ServiceNetworkServiceAssociationIdentifier
- **Type**: string
- **Pattern**: `^((snsa-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkserviceassociation/snsa-[0-9a-z]{17}))$`
- **Min Length**: 17
- **Max Length**: 2048

### ServiceNetworkVpcAssociationArn
- **Type**: string
- **Pattern**: `^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkvpcassociation/snva-[0-9a-z]{17}$`
- **Min Length**: 20
- **Max Length**: 2048

### ServiceNetworkVpcAssociationId
- **Type**: string
- **Pattern**: `^snva-[0-9a-z]{17}$`
- **Min Length**: 22
- **Max Length**: 22

### ServiceNetworkVpcAssociationIdentifier
- **Type**: string
- **Pattern**: `^((snva-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkvpcassociation/snva-[0-9a-z]{17}))$`
- **Min Length**: 17
- **Max Length**: 2048

### TargetGroupArn
- **Type**: string
- **Pattern**: `^arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:targetgroup/tg-[0-9a-z]{17}$`
- **Min Length**: 20
- **Max Length**: 2048

### TargetGroupId
- **Type**: string
- **Pattern**: `^tg-[0-9a-z]{17}$`
- **Min Length**: 20
- **Max Length**: 20

### TargetGroupIdentifier
- **Type**: string
- **Pattern**: `^((tg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:targetgroup/tg-[0-9a-z]{17}))$`
- **Min Length**: 17
- **Max Length**: 2048

### TargetGroupName
- **Type**: string
- **Pattern**: `^(?!tg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$`
- **Min Length**: 3
- **Max Length**: 128

### VpcId
- **Type**: string
- **Pattern**: `^vpc-(([0-9a-z]{8})|([0-9a-z]{17}))$`
- **Min Length**: 5
- **Max Length**: 50

