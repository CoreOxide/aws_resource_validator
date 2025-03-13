# Imagebuilder Service

### AccountId
- **Type**: string
- **Pattern**: `^[0-9]{12}$`

### AmiNameString
- **Type**: string
- **Pattern**: `^[-_A-Za-z0-9{][-_A-Za-z0-9\s:{}\.]+[-_A-Za-z0-9}]$`
- **Min Length**: 1
- **Max Length**: 127

### ComponentBuildVersionArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):component/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

### ComponentParameterDescription
- **Type**: string
- **Pattern**: `[^\x00]+`
- **Min Length**: 1
- **Max Length**: 1024

### ComponentParameterName
- **Type**: string
- **Pattern**: `[^\x00]+`
- **Min Length**: 1
- **Max Length**: 256

### ComponentParameterType
- **Type**: string
- **Pattern**: `^String|Integer|Boolean|StringList$`
- **Min Length**: 1
- **Max Length**: 20

### ComponentParameterValue
- **Type**: string
- **Pattern**: `[^\x00]*`
- **Min Length**: 0

### ComponentVersionArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):component/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+$`

### ComponentVersionArnOrBuildVersionArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):component/[a-z0-9-_]+/(?:(?:([0-9]+|x)\.([0-9]+|x)\.([0-9]+|x))|(?:[0-9]+\.[0-9]+\.[0-9]+/[0-9]+))$`

### ContainerRecipeArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):container-recipe/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+$`

### DistributionConfigurationArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):distribution-configuration/[a-z0-9-_]+$`

### FilterName
- **Type**: string
- **Pattern**: `^[a-zA-Z]{1,1024}$`

### FilterValue
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z./_ :,{}"-]{1,1024}$`

### HttpTokens
- **Type**: string
- **Pattern**: `optional|required`

### ImageBuildVersionArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

### ImageBuilderArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`

### ImagePipelineArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-pipeline/[a-z0-9-_]+$`

### ImageRecipeArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-recipe/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+$`

### ImageVersionArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+$`

### ImageVersionArnOrBuildVersionArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/(?:(?:([0-9]+|x)\.([0-9]+|x)\.([0-9]+|x))|(?:[0-9]+\.[0-9]+\.[0-9]+/[0-9]+))$`

### InfrastructureConfigurationArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`

### InlineComponentData
- **Type**: string
- **Pattern**: `[^\x00]+`
- **Min Length**: 1
- **Max Length**: 16000

### InlineDockerFileTemplate
- **Type**: string
- **Pattern**: `[^\x00]+`
- **Min Length**: 1
- **Max Length**: 16000

### InlineWorkflowData
- **Type**: string
- **Pattern**: `[^\x00]+`
- **Min Length**: 1
- **Max Length**: 16000

### InstanceProfileNameType
- **Type**: string
- **Pattern**: `^[\w+=,.@-]+$`
- **Min Length**: 1
- **Max Length**: 256

### LaunchTemplateId
- **Type**: string
- **Pattern**: `^lt-[a-z0-9-_]{17}$`

### LicenseConfigurationArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:license-manager:[^:]+:[0-9]{12}:license-configuration:lic-[a-z0-9-_]{32}$`

### LifecycleExecutionId
- **Type**: string
- **Pattern**: `^lce-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

### LifecyclePolicyArn
- **Type**: string
- **Pattern**: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws):lifecycle-policy/[a-z0-9-_]+$`
- **Max Length**: 1024

### MarketplaceResourceLocation
- **Type**: string
- **Pattern**: `^s3://[^/]+/.+[^/]$`
- **Max Length**: 1024

### OrganizationArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:organizations::[0-9]{12}:organization/o-[a-z0-9]{10,32}$`

### OrganizationalUnitArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:organizations::[0-9]{12}:ou/o-[a-z0-9]{10,32}/ou-[0-9a-z]{4,32}-[0-9a-z]{8,32}`

### ParallelGroup
- **Type**: string
- **Pattern**: `^[A-Za-z0-9][A-Za-z0-9-_+#]{0,99}$`
- **Min Length**: 1
- **Max Length**: 100

### ProductCodeId
- **Type**: string
- **Pattern**: `^[A-Za-z0-9]{1,25}$`

### ResourceName
- **Type**: string
- **Pattern**: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`

### RoleNameOrArn
- **Type**: string
- **Pattern**: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
- **Min Length**: 1
- **Max Length**: 2048

### SnsTopicArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:sns:[^:]+:[0-9]{12}:[a-zA-Z0-9-_]{1,256}$`

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### Timezone
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]{2,}(?:\/[a-zA-z0-9-_+]+)*`
- **Min Length**: 3
- **Max Length**: 100

### UserDataOverride
- **Type**: string
- **Pattern**: `^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$`
- **Min Length**: 1
- **Max Length**: 21847

### VersionNumber
- **Type**: string
- **Pattern**: `^[0-9]+\.[0-9]+\.[0-9]+$`

### WorkflowBuildVersionArn
- **Type**: string
- **Pattern**: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
- **Max Length**: 1024

### WorkflowExecutionId
- **Type**: string
- **Pattern**: `^wf-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

### WorkflowNameArn
- **Type**: string
- **Pattern**: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/x\.x\.x$`

### WorkflowParameterDescription
- **Type**: string
- **Pattern**: `[^\x00]+`
- **Min Length**: 0
- **Max Length**: 1024

### WorkflowParameterName
- **Type**: string
- **Pattern**: `[^\x00]+`
- **Min Length**: 1
- **Max Length**: 128

### WorkflowParameterType
- **Type**: string
- **Pattern**: `^string|integer|boolean|stringList$`
- **Min Length**: 1
- **Max Length**: 20

### WorkflowParameterValue
- **Type**: string
- **Pattern**: `[^\x00]*`
- **Min Length**: 0

### WorkflowStepAction
- **Type**: string
- **Pattern**: `^[A-Za-z][A-Za-z0-9-_]{1,99}$`

### WorkflowStepExecutionId
- **Type**: string
- **Pattern**: `^step-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

### WorkflowStepName
- **Type**: string
- **Pattern**: `^[A-Za-z][A-Za-z0-9-_]{1,99}$`

### WorkflowVersionArn
- **Type**: string
- **Pattern**: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+$`

### WorkflowVersionArnOrBuildVersionArn
- **Type**: string
- **Pattern**: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/(?:(?:([0-9]+|x)\.([0-9]+|x)\.([0-9]+|x))|(?:[0-9]+\.[0-9]+\.[0-9]+/[0-9]+))$`

### WorkflowWildcardVersionArn
- **Type**: string
- **Pattern**: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`

