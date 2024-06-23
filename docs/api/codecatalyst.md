# Codecatalyst Service

### CreateDevEnvironmentRequestAliasString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
- **Min Length**: 1
- **Max Length**: 128

### GetUserDetailsRequestUserNameString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.-]{3,100}`
- **Min Length**: 3
- **Max Length**: 100

### GetWorkflowRequestProjectNameString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
- **Min Length**: 1

### GetWorkflowRunRequestProjectNameString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
- **Min Length**: 1

### ListWorkflowRunsRequestProjectNameString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
- **Min Length**: 1

### ListWorkflowsRequestSpaceNameString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
- **Min Length**: 1

### NameString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
- **Min Length**: 3
- **Max Length**: 63

### ProjectDescription
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+(?:[-_a-zA-Z0-9.,;:/\+=?&$%    ])*`
- **Min Length**: 0
- **Max Length**: 200

### ProjectDisplayName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+(?:[-_\. ][a-zA-Z0-9]+)*`
- **Min Length**: 3
- **Max Length**: 63

### RegionString
- **Type**: string
- **Pattern**: `(us(?:-gov)?|af|ap|ca|cn|eu|sa)-(central|(?:north|south)?(?:east|west)?)-(\d+)`
- **Min Length**: 3
- **Max Length**: 16

### SourceRepositoryIdString
- **Type**: string
- **Pattern**: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

### SourceRepositoryNameString
- **Type**: string
- **Pattern**: `(?!.*[.]git$)[\w\-.]*`
- **Min Length**: 1
- **Max Length**: 100

### SpaceDescription
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+(?:[-_a-zA-Z0-9.,;:/\+=?&$%    ])*`
- **Min Length**: 0
- **Max Length**: 200

### StartWorkflowRunRequestClientTokenString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
- **Min Length**: 1
- **Max Length**: 64

### StartWorkflowRunRequestProjectNameString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
- **Min Length**: 1

### StartWorkflowRunRequestSpaceNameString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
- **Min Length**: 1

### UpdateDevEnvironmentRequestAliasString
- **Type**: string
- **Pattern**: `$|^[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
- **Min Length**: 0
- **Max Length**: 128

### UpdateDevEnvironmentResponseAliasString
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
- **Min Length**: 1
- **Max Length**: 128

### Uuid
- **Type**: string
- **Pattern**: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

