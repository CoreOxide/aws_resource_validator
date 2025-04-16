# Codestar Classes

# AssociateTeamMemberRequestRequest

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### projectRole
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### remoteAccessAllowed
- **Type**: typing.Optional[bool]


# AssociateTeamMemberResult

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Code

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.CodeSource'>
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.CodeDestination'>
- **Required**: Yes


# CodeCommitCodeDestination

### name
- **Type**: <class 'str'>
- **Required**: Yes


# CodeDestination

### codeCommit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_classes.CodeCommitCodeDestination]

### gitHub
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_classes.GitHubCodeDestination]


# CodeSource

### s3
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.S3Location'>
- **Required**: Yes


# CreateProjectRequestRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientRequestToken
- **Type**: typing.Optional[str]

### sourceCode
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codestar_classes.Code]]

### toolchain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_classes.Toolchain]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProjectResult

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### projectTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserProfileRequestRequest

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### emailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### sshPublicKey
- **Type**: typing.Optional[str]


# CreateUserProfileResult

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### emailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### sshPublicKey
- **Type**: <class 'str'>
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProjectRequestRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### deleteStack
- **Type**: typing.Optional[bool]


# DeleteProjectResult

### stackId
- **Type**: <class 'str'>
- **Required**: Yes

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteUserProfileRequestRequest

### userArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserProfileResult

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProjectRequestRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProjectResult

### name
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### createdTimeStamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stackId
- **Type**: <class 'str'>
- **Required**: Yes

### projectTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ProjectStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserProfileRequestRequest

### userArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserProfileResult

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### emailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### sshPublicKey
- **Type**: <class 'str'>
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateTeamMemberRequestRequest

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes


# GitHubCodeDestination

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### owner
- **Type**: <class 'str'>
- **Required**: Yes

### privateRepository
- **Type**: <class 'bool'>
- **Required**: Yes

### issuesEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### token
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ListProjectsRequestListProjectsPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_classes.PaginatorConfig]


# ListProjectsRequestRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListProjectsResult

### projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_classes.ProjectSummary]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# ListResourcesRequestListResourcesPaginate

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_classes.PaginatorConfig]


# ListResourcesRequestRequest

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListResourcesResult

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_classes.Resource]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForProjectRequestRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTagsForProjectResult

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# ListTeamMembersRequestListTeamMembersPaginate

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_classes.PaginatorConfig]


# ListTeamMembersRequestRequest

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTeamMembersResult

### teamMembers
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_classes.TeamMember]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# ListUserProfilesRequestListUserProfilesPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_classes.PaginatorConfig]


# ListUserProfilesRequestRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListUserProfilesResult

### userProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_classes.UserProfileSummary]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProjectStatus

### state
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]


# ProjectSummary

### projectId
- **Type**: typing.Optional[str]

### projectArn
- **Type**: typing.Optional[str]


# Resource

### id
- **Type**: <class 'str'>
- **Required**: Yes


# ResponseMetadata

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes


# S3Location

### bucketName
- **Type**: typing.Optional[str]

### bucketKey
- **Type**: typing.Optional[str]


# TagProjectRequestRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagProjectResult

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# TeamMember

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### projectRole
- **Type**: <class 'str'>
- **Required**: Yes

### remoteAccessAllowed
- **Type**: typing.Optional[bool]


# Toolchain

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ToolchainSource'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### stackParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ToolchainSource

### s3
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.S3Location'>
- **Required**: Yes


# UntagProjectRequestRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateProjectRequestRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateTeamMemberRequestRequest

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### projectRole
- **Type**: typing.Optional[str]

### remoteAccessAllowed
- **Type**: typing.Optional[bool]


# UpdateTeamMemberResult

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### projectRole
- **Type**: <class 'str'>
- **Required**: Yes

### remoteAccessAllowed
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserProfileRequestRequest

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### emailAddress
- **Type**: typing.Optional[str]

### sshPublicKey
- **Type**: typing.Optional[str]


# UpdateUserProfileResult

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### emailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### sshPublicKey
- **Type**: <class 'str'>
- **Required**: Yes

### createdTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadata'>
- **Required**: Yes


# UserProfileSummary

### userArn
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### emailAddress
- **Type**: typing.Optional[str]

### sshPublicKey
- **Type**: typing.Optional[str]


