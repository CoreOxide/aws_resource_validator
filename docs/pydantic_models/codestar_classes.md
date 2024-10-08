# Pydantic Models in codestar_classes

# AssociateTeamMemberRequestRequestTypeDef

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


# AssociateTeamMemberResultTypeDef

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodeCommitCodeDestinationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# CodeDestinationTypeDef

### codeCommit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_classes.CodeCommitCodeDestinationTypeDef]

### gitHub
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_classes.GitHubCodeDestinationTypeDef]


# CodeSourceTypeDef

### s3
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.S3LocationTypeDef'>
- **Required**: Yes


# CodeTypeDef

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.CodeSourceTypeDef'>
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.CodeDestinationTypeDef'>
- **Required**: Yes


# CreateProjectRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codestar_classes.CodeTypeDef]]

### toolchain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_classes.ToolchainTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProjectResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserProfileRequestRequestTypeDef

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


# CreateUserProfileResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProjectRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### deleteStack
- **Type**: typing.Optional[bool]


# DeleteProjectResultTypeDef

### stackId
- **Type**: <class 'str'>
- **Required**: Yes

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteUserProfileRequestRequestTypeDef

### userArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserProfileResultTypeDef

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProjectRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProjectResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ProjectStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserProfileRequestRequestTypeDef

### userArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserProfileResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateTeamMemberRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### userArn
- **Type**: <class 'str'>
- **Required**: Yes


# GitHubCodeDestinationTypeDef

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


# ListProjectsRequestListProjectsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_classes.PaginatorConfigTypeDef]


# ListProjectsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListProjectsResultTypeDef

### projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_classes.ProjectSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourcesRequestListResourcesPaginateTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_classes.PaginatorConfigTypeDef]


# ListResourcesRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListResourcesResultTypeDef

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_classes.ResourceTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForProjectRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTagsForProjectResultTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTeamMembersRequestListTeamMembersPaginateTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_classes.PaginatorConfigTypeDef]


# ListTeamMembersRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTeamMembersResultTypeDef

### teamMembers
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_classes.TeamMemberTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUserProfilesRequestListUserProfilesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_classes.PaginatorConfigTypeDef]


# ListUserProfilesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListUserProfilesResultTypeDef

### userProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_classes.UserProfileSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProjectStatusTypeDef

### state
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]


# ProjectSummaryTypeDef

### projectId
- **Type**: typing.Optional[str]

### projectArn
- **Type**: typing.Optional[str]


# ResourceTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# ResponseMetadataTypeDef

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


# S3LocationTypeDef

### bucketName
- **Type**: typing.Optional[str]

### bucketKey
- **Type**: typing.Optional[str]


# TagProjectRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagProjectResultTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TeamMemberTypeDef

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### projectRole
- **Type**: <class 'str'>
- **Required**: Yes

### remoteAccessAllowed
- **Type**: typing.Optional[bool]


# ToolchainSourceTypeDef

### s3
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.S3LocationTypeDef'>
- **Required**: Yes


# ToolchainTypeDef

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ToolchainSourceTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### stackParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UntagProjectRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateProjectRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateTeamMemberRequestRequestTypeDef

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


# UpdateTeamMemberResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserProfileRequestRequestTypeDef

### userArn
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### emailAddress
- **Type**: typing.Optional[str]

### sshPublicKey
- **Type**: typing.Optional[str]


# UpdateUserProfileResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserProfileSummaryTypeDef

### userArn
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### emailAddress
- **Type**: typing.Optional[str]

### sshPublicKey
- **Type**: typing.Optional[str]


