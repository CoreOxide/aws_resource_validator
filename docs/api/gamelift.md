# Gamelift Service

### AliasArn
- **Type**: string
- **Pattern**: `^arn:.*:alias\/alias-\S+`

### AliasId
- **Type**: string
- **Pattern**: `^alias-\S+`

### AliasIdOrArn
- **Type**: string
- **Pattern**: `^alias-\S+|^arn:.*:alias\/alias-\S+`

### ArnStringModel
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:/-]+`
- **Min Length**: 1
- **Max Length**: 256

### AutoScalingGroupArn
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
- **Min Length**: 0
- **Max Length**: 256

### BuildArn
- **Type**: string
- **Pattern**: `^arn:.*:build\/build-\S+`

### BuildId
- **Type**: string
- **Pattern**: `^build-\S+`

### BuildIdOrArn
- **Type**: string
- **Pattern**: `^build-\S+|^arn:.*:build\/build-\S+`

### ComputeArn
- **Type**: string
- **Pattern**: `^arn:.*:compute\/[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`
- **Max Length**: 1024

### ComputeAuthToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 64

### ComputeName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`
- **Min Length**: 1
- **Max Length**: 128

### ComputeNameOrArn
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?$|^arn:.*:compute\/[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`
- **Max Length**: 1024

### ContainerGroupDefinitionArn
- **Type**: string
- **Pattern**: `^arn:.*:containergroupdefinition\/containergroupdefinition-[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 512

### ContainerGroupDefinitionName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-]+$`
- **Min Length**: 1
- **Max Length**: 128

### ContainerGroupDefinitionNameOrArn
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-]+$|^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+$`
- **Min Length**: 1
- **Max Length**: 512

### CustomInputLocationStringModel
- **Type**: string
- **Pattern**: `^custom-[A-Za-z0-9\-]+`
- **Min Length**: 8
- **Max Length**: 64

### CustomLocationNameOrArnModel
- **Type**: string
- **Pattern**: `^custom-[A-Za-z0-9\-]+|^arn:.*:location\/custom-\S+`
- **Min Length**: 1
- **Max Length**: 128

### DnsNameInput
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z_\-\.]+`
- **Min Length**: 1
- **Max Length**: 256

### FleetArn
- **Type**: string
- **Pattern**: `^arn:.*:fleet\/fleet-\S+`

### FleetId
- **Type**: string
- **Pattern**: `^fleet-\S+`

### FleetIdOrArn
- **Type**: string
- **Pattern**: `^fleet-\S+|^arn:.*:fleet\/fleet-\S+`

### GameServerConnectionInfo
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 512

### GameServerData
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 1024

### GameServerGroupArn
- **Type**: string
- **Pattern**: `^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]*`
- **Min Length**: 1
- **Max Length**: 256

### GameServerGroupName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-\.]+`
- **Min Length**: 1
- **Max Length**: 128

### GameServerGroupNameOrArn
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-\.]+|^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]+`
- **Min Length**: 1
- **Max Length**: 256

### GameServerId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-\.]+`
- **Min Length**: 3
- **Max Length**: 128

### GameServerInstanceId
- **Type**: string
- **Pattern**: `^i-[0-9a-zA-Z]{17}$`
- **Min Length**: 19
- **Max Length**: 19

### GameSessionQueueArn
- **Type**: string
- **Pattern**: `^arn:.*:gamesessionqueue\/[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 256

### GameSessionQueueName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 128

### GameSessionQueueNameOrArn
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+|^arn:.*:gamesessionqueue\/[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 256

### IamRoleArn
- **Type**: string
- **Pattern**: `^arn:.*:role\/[\w+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 256

### IdStringModel
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 48

### ImageUriString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_\.@\/:]+$`
- **Min Length**: 1
- **Max Length**: 255

### InstanceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\.-]+`

### IpAddress
- **Type**: string
- **Pattern**: `^[0-9A-Fa-f\:\.]+`
- **Min Length**: 1
- **Max Length**: 128

### IpRange
- **Type**: string
- **Pattern**: `[^\s]+`

### LaunchParametersStringModel
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:.+\/\\\- =@;{},?\'\[\]"]+`
- **Min Length**: 1
- **Max Length**: 1024

### LaunchPathStringModel
- **Type**: string
- **Pattern**: `[A-Za-z0-9_:.+\/\\\- ]+`
- **Min Length**: 1
- **Max Length**: 1024

### LaunchTemplateId
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]+`
- **Min Length**: 1
- **Max Length**: 255

### LaunchTemplateName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\(\)\.\-/_]+`
- **Min Length**: 3
- **Max Length**: 128

### LaunchTemplateVersion
- **Type**: string
- **Pattern**: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]+`
- **Min Length**: 1
- **Max Length**: 128

### LocationArnModel
- **Type**: string
- **Pattern**: `^arn:.*:location\/custom-\S+`
- **Min Length**: 1
- **Max Length**: 128

### LocationStringModel
- **Type**: string
- **Pattern**: `^[A-Za-z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 64

### MatchmakingConfigurationArn
- **Type**: string
- **Pattern**: `^arn:.*:matchmakingconfiguration\/[a-zA-Z0-9-\.]*`

### MatchmakingConfigurationName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-\.]*|^arn:.*:matchmakingconfiguration\/[a-zA-Z0-9-\.]*`
- **Min Length**: 1
- **Max Length**: 256

### MatchmakingIdStringModel
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-\.]*`
- **Max Length**: 128

### MatchmakingRuleSetArn
- **Type**: string
- **Pattern**: `^arn:.*:matchmakingruleset\/[a-zA-Z0-9-\.]*`

### MatchmakingRuleSetName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-\.]*|^arn:.*:matchmakingruleset\/[a-zA-Z0-9-\.]*`
- **Min Length**: 1
- **Max Length**: 256

### NonBlankAndLengthConstraintString
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 1024

### NonNegativeLimitedLengthDouble
- **Type**: string
- **Pattern**: `^\d{1,5}(?:\.\d{1,5})?$`
- **Min Length**: 1
- **Max Length**: 11

### NonZeroAnd128MaxAsciiString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\-]+$`
- **Min Length**: 1
- **Max Length**: 128

### PlayerSessionId
- **Type**: string
- **Pattern**: `^psess-\S+`

### QueueCustomEventData
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 256

### QueueSnsArnStringModel
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]*(\.fifo)?`
- **Min Length**: 0
- **Max Length**: 300

### ScriptArn
- **Type**: string
- **Pattern**: `^arn:.*:script\/script-\S+`

### ScriptId
- **Type**: string
- **Pattern**: `^script-\S+`

### ScriptIdOrArn
- **Type**: string
- **Pattern**: `^script-\S+|^arn:.*:script\/script-\S+`

### ServerSdkVersion
- **Type**: string
- **Pattern**: `^\d+\.\d+\.\d+$`
- **Max Length**: 128

### Sha256
- **Type**: string
- **Pattern**: `^sha256:[a-fA-F0-9]{64}$`

### SnsArnStringModel
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_/-]*(.fifo)?`
- **Min Length**: 0
- **Max Length**: 300

### VpcSubnet
- **Type**: string
- **Pattern**: `^subnet-[0-9a-z]+$`
- **Min Length**: 15
- **Max Length**: 24

### WeightedCapacity
- **Type**: string
- **Pattern**: `^[\u0031-\u0039][\u0030-\u0039]{0,2}$`
- **Min Length**: 1
- **Max Length**: 3

