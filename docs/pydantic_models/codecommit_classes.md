# Codecommit Classes

# ApprovalRuleEventMetadataTypeDef

### approvalRuleName
- **Type**: typing.Optional[str]

### approvalRuleId
- **Type**: typing.Optional[str]

### approvalRuleContent
- **Type**: typing.Optional[str]


# ApprovalRuleOverriddenEventMetadataTypeDef

### revisionId
- **Type**: typing.Optional[str]

### overrideStatus
- **Type**: typing.Optional[typing.Literal['OVERRIDE', 'REVOKE']]


# ApprovalRuleTemplateTypeDef

### approvalRuleTemplateId
- **Type**: typing.Optional[str]

### approvalRuleTemplateName
- **Type**: typing.Optional[str]

### approvalRuleTemplateDescription
- **Type**: typing.Optional[str]

### approvalRuleTemplateContent
- **Type**: typing.Optional[str]

### ruleContentSha256
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedUser
- **Type**: typing.Optional[str]


# ApprovalRuleTypeDef

### approvalRuleId
- **Type**: typing.Optional[str]

### approvalRuleName
- **Type**: typing.Optional[str]

### approvalRuleContent
- **Type**: typing.Optional[str]

### ruleContentSha256
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedUser
- **Type**: typing.Optional[str]

### originApprovalRuleTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.OriginApprovalRuleTemplateTypeDef]


# ApprovalStateChangedEventMetadataTypeDef

### revisionId
- **Type**: typing.Optional[str]

### approvalStatus
- **Type**: typing.Optional[typing.Literal['APPROVE', 'REVOKE']]


# ApprovalTypeDef

### userArn
- **Type**: typing.Optional[str]

### approvalState
- **Type**: typing.Optional[typing.Literal['APPROVE', 'REVOKE']]


# AssociateApprovalRuleTemplateWithRepositoryInputTypeDef

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef

### repositoryName
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# BatchAssociateApprovalRuleTemplateWithRepositoriesInputTypeDef

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef

### associatedRepositoryNames
- **Type**: typing.List[str]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDescribeMergeConflictsErrorTypeDef

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### exceptionName
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDescribeMergeConflictsInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### destinationCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### mergeOption
- **Type**: typing.Literal['FAST_FORWARD_MERGE', 'SQUASH_MERGE', 'THREE_WAY_MERGE']
- **Required**: Yes

### maxMergeHunks
- **Type**: typing.Optional[int]

### maxConflictFiles
- **Type**: typing.Optional[int]

### filePaths
- **Type**: typing.Optional[typing.Sequence[str]]

### conflictDetailLevel
- **Type**: typing.Optional[typing.Literal['FILE_LEVEL', 'LINE_LEVEL']]

### conflictResolutionStrategy
- **Type**: typing.Optional[typing.Literal['ACCEPT_DESTINATION', 'ACCEPT_SOURCE', 'AUTOMERGE', 'NONE']]

### nextToken
- **Type**: typing.Optional[str]


# BatchDescribeMergeConflictsOutputTypeDef

### conflicts
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.ConflictTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.BatchDescribeMergeConflictsErrorTypeDef]
- **Required**: Yes

### destinationCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### baseCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef

### repositoryName
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# BatchDisassociateApprovalRuleTemplateFromRepositoriesInputTypeDef

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef

### disassociatedRepositoryNames
- **Type**: typing.List[str]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetCommitsErrorTypeDef

### commitId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# BatchGetCommitsInputTypeDef

### commitIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetCommitsOutputTypeDef

### commits
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.CommitTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.BatchGetCommitsErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetRepositoriesErrorTypeDef

### repositoryId
- **Type**: typing.Optional[str]

### repositoryName
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['EncryptionIntegrityChecksFailedException', 'EncryptionKeyAccessDeniedException', 'EncryptionKeyDisabledException', 'EncryptionKeyNotFoundException', 'EncryptionKeyUnavailableException', 'RepositoryDoesNotExistException']]

### errorMessage
- **Type**: typing.Optional[str]


# BatchGetRepositoriesInputTypeDef

### repositoryNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetRepositoriesOutputTypeDef

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.RepositoryMetadataTypeDef]
- **Required**: Yes

### repositoriesNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.BatchGetRepositoriesErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlobMetadataTypeDef

### blobId
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### mode
- **Type**: typing.Optional[str]


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BranchInfoTypeDef

### branchName
- **Type**: typing.Optional[str]

### commitId
- **Type**: typing.Optional[str]


# CommentTypeDef

### commentId
- **Type**: typing.Optional[str]

### content
- **Type**: typing.Optional[str]

### inReplyTo
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### authorArn
- **Type**: typing.Optional[str]

### deleted
- **Type**: typing.Optional[bool]

### clientRequestToken
- **Type**: typing.Optional[str]

### callerReactions
- **Type**: typing.Optional[typing.List[str]]

### reactionCounts
- **Type**: typing.Optional[typing.Dict[str, int]]


# CommentsForComparedCommitTypeDef

### repositoryName
- **Type**: typing.Optional[str]

### beforeCommitId
- **Type**: typing.Optional[str]

### afterCommitId
- **Type**: typing.Optional[str]

### beforeBlobId
- **Type**: typing.Optional[str]

### afterBlobId
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.LocationTypeDef]

### comments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit_classes.CommentTypeDef]]


# CommentsForPullRequestTypeDef

### pullRequestId
- **Type**: typing.Optional[str]

### repositoryName
- **Type**: typing.Optional[str]

### beforeCommitId
- **Type**: typing.Optional[str]

### afterCommitId
- **Type**: typing.Optional[str]

### beforeBlobId
- **Type**: typing.Optional[str]

### afterBlobId
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.LocationTypeDef]

### comments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit_classes.CommentTypeDef]]


# CommitTypeDef

### commitId
- **Type**: typing.Optional[str]

### treeId
- **Type**: typing.Optional[str]

### parents
- **Type**: typing.Optional[typing.List[str]]

### message
- **Type**: typing.Optional[str]

### author
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.UserInfoTypeDef]

### committer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.UserInfoTypeDef]

### additionalData
- **Type**: typing.Optional[str]


# ConflictMetadataTypeDef

### filePath
- **Type**: typing.Optional[str]

### fileSizes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.FileSizesTypeDef]

### fileModes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.FileModesTypeDef]

### objectTypes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.ObjectTypesTypeDef]

### numberOfConflicts
- **Type**: typing.Optional[int]

### isBinaryFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.IsBinaryFileTypeDef]

### contentConflict
- **Type**: typing.Optional[bool]

### fileModeConflict
- **Type**: typing.Optional[bool]

### objectTypeConflict
- **Type**: typing.Optional[bool]

### mergeOperations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.MergeOperationsTypeDef]


# ConflictResolutionTypeDef

### replaceContents
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecommit_classes.ReplaceContentEntryTypeDef]]

### deleteFiles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecommit_classes.DeleteFileEntryTypeDef]]

### setFileModes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecommit_classes.SetFileModeEntryTypeDef]]


# ConflictTypeDef

### conflictMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.ConflictMetadataTypeDef]

### mergeHunks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit_classes.MergeHunkTypeDef]]


# CreateApprovalRuleTemplateInputTypeDef

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### approvalRuleTemplateContent
- **Type**: <class 'str'>
- **Required**: Yes

### approvalRuleTemplateDescription
- **Type**: typing.Optional[str]


# CreateApprovalRuleTemplateOutputTypeDef

### approvalRuleTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ApprovalRuleTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBranchInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### commitId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCommitInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### parentCommitId
- **Type**: typing.Optional[str]

### authorName
- **Type**: typing.Optional[str]

### email
- **Type**: typing.Optional[str]

### commitMessage
- **Type**: typing.Optional[str]

### keepEmptyFolders
- **Type**: typing.Optional[bool]

### putFiles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecommit_classes.PutFileEntryTypeDef]]

### deleteFiles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecommit_classes.DeleteFileEntryTypeDef]]

### setFileModes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecommit_classes.SetFileModeEntryTypeDef]]


# CreateCommitOutputTypeDef

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### treeId
- **Type**: <class 'str'>
- **Required**: Yes

### filesAdded
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.FileMetadataTypeDef]
- **Required**: Yes

### filesUpdated
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.FileMetadataTypeDef]
- **Required**: Yes

### filesDeleted
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.FileMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePullRequestApprovalRuleInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### approvalRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### approvalRuleContent
- **Type**: <class 'str'>
- **Required**: Yes


# CreatePullRequestApprovalRuleOutputTypeDef

### approvalRule
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ApprovalRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePullRequestInputTypeDef

### title
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codecommit_classes.TargetTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientRequestToken
- **Type**: typing.Optional[str]


# CreatePullRequestOutputTypeDef

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.PullRequestTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRepositoryInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryDescription
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### kmsKeyId
- **Type**: typing.Optional[str]


# CreateRepositoryOutputTypeDef

### repositoryMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.RepositoryMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUnreferencedMergeCommitInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### destinationCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### mergeOption
- **Type**: typing.Literal['FAST_FORWARD_MERGE', 'SQUASH_MERGE', 'THREE_WAY_MERGE']
- **Required**: Yes

### conflictDetailLevel
- **Type**: typing.Optional[typing.Literal['FILE_LEVEL', 'LINE_LEVEL']]

### conflictResolutionStrategy
- **Type**: typing.Optional[typing.Literal['ACCEPT_DESTINATION', 'ACCEPT_SOURCE', 'AUTOMERGE', 'NONE']]

### authorName
- **Type**: typing.Optional[str]

### email
- **Type**: typing.Optional[str]

### commitMessage
- **Type**: typing.Optional[str]

### keepEmptyFolders
- **Type**: typing.Optional[bool]

### conflictResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.ConflictResolutionTypeDef]


# CreateUnreferencedMergeCommitOutputTypeDef

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### treeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApprovalRuleTemplateInputTypeDef

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApprovalRuleTemplateOutputTypeDef

### approvalRuleTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBranchInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBranchOutputTypeDef

### deletedBranch
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.BranchInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCommentContentInputTypeDef

### commentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCommentContentOutputTypeDef

### comment
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.CommentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFileEntryTypeDef

### filePath
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFileInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### parentCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### keepEmptyFolders
- **Type**: typing.Optional[bool]

### commitMessage
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### email
- **Type**: typing.Optional[str]


# DeleteFileOutputTypeDef

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### blobId
- **Type**: <class 'str'>
- **Required**: Yes

### treeId
- **Type**: <class 'str'>
- **Required**: Yes

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePullRequestApprovalRuleInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### approvalRuleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePullRequestApprovalRuleOutputTypeDef

### approvalRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRepositoryInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRepositoryOutputTypeDef

### repositoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMergeConflictsInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### destinationCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### mergeOption
- **Type**: typing.Literal['FAST_FORWARD_MERGE', 'SQUASH_MERGE', 'THREE_WAY_MERGE']
- **Required**: Yes

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### maxMergeHunks
- **Type**: typing.Optional[int]

### conflictDetailLevel
- **Type**: typing.Optional[typing.Literal['FILE_LEVEL', 'LINE_LEVEL']]

### conflictResolutionStrategy
- **Type**: typing.Optional[typing.Literal['ACCEPT_DESTINATION', 'ACCEPT_SOURCE', 'AUTOMERGE', 'NONE']]

### nextToken
- **Type**: typing.Optional[str]


# DescribeMergeConflictsOutputTypeDef

### conflictMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ConflictMetadataTypeDef'>
- **Required**: Yes

### mergeHunks
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.MergeHunkTypeDef]
- **Required**: Yes

### destinationCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### baseCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribePullRequestEventsInputPaginateTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### pullRequestEventType
- **Type**: typing.Optional[typing.Literal['PULL_REQUEST_APPROVAL_RULE_CREATED', 'PULL_REQUEST_APPROVAL_RULE_DELETED', 'PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN', 'PULL_REQUEST_APPROVAL_RULE_UPDATED', 'PULL_REQUEST_APPROVAL_STATE_CHANGED', 'PULL_REQUEST_CREATED', 'PULL_REQUEST_MERGE_STATE_CHANGED', 'PULL_REQUEST_SOURCE_REFERENCE_UPDATED', 'PULL_REQUEST_STATUS_CHANGED']]

### actorArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.PaginatorConfigTypeDef]


# DescribePullRequestEventsInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### pullRequestEventType
- **Type**: typing.Optional[typing.Literal['PULL_REQUEST_APPROVAL_RULE_CREATED', 'PULL_REQUEST_APPROVAL_RULE_DELETED', 'PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN', 'PULL_REQUEST_APPROVAL_RULE_UPDATED', 'PULL_REQUEST_APPROVAL_STATE_CHANGED', 'PULL_REQUEST_CREATED', 'PULL_REQUEST_MERGE_STATE_CHANGED', 'PULL_REQUEST_SOURCE_REFERENCE_UPDATED', 'PULL_REQUEST_STATUS_CHANGED']]

### actorArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribePullRequestEventsOutputTypeDef

### pullRequestEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.PullRequestEventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DifferenceTypeDef

### beforeBlob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.BlobMetadataTypeDef]

### afterBlob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.BlobMetadataTypeDef]

### changeType
- **Type**: typing.Optional[typing.Literal['A', 'D', 'M']]


# DisassociateApprovalRuleTemplateFromRepositoryInputTypeDef

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EvaluatePullRequestApprovalRulesInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluatePullRequestApprovalRulesOutputTypeDef

### evaluation
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.EvaluationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EvaluationTypeDef

### approved
- **Type**: typing.Optional[bool]

### overridden
- **Type**: typing.Optional[bool]

### approvalRulesSatisfied
- **Type**: typing.Optional[typing.List[str]]

### approvalRulesNotSatisfied
- **Type**: typing.Optional[typing.List[str]]


# FileMetadataTypeDef

### absolutePath
- **Type**: typing.Optional[str]

### blobId
- **Type**: typing.Optional[str]

### fileMode
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]


# FileModesTypeDef

### source
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]

### destination
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]

### base
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]


# FileSizesTypeDef

### source
- **Type**: typing.Optional[int]

### destination
- **Type**: typing.Optional[int]

### base
- **Type**: typing.Optional[int]


# FileTypeDef

### blobId
- **Type**: typing.Optional[str]

### absolutePath
- **Type**: typing.Optional[str]

### relativePath
- **Type**: typing.Optional[str]

### fileMode
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]


# FileVersionTypeDef

### commit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.CommitTypeDef]

### blobId
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### revisionChildren
- **Type**: typing.Optional[typing.List[str]]


# FolderTypeDef

### treeId
- **Type**: typing.Optional[str]

### absolutePath
- **Type**: typing.Optional[str]

### relativePath
- **Type**: typing.Optional[str]


# GetApprovalRuleTemplateInputTypeDef

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetApprovalRuleTemplateOutputTypeDef

### approvalRuleTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ApprovalRuleTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBlobInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### blobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBlobOutputTypeDef

### content
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBranchInputTypeDef

### repositoryName
- **Type**: typing.Optional[str]

### branchName
- **Type**: typing.Optional[str]


# GetBranchOutputTypeDef

### branch
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.BranchInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCommentInputTypeDef

### commentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCommentOutputTypeDef

### comment
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.CommentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCommentReactionsInputTypeDef

### commentId
- **Type**: <class 'str'>
- **Required**: Yes

### reactionUserArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetCommentReactionsOutputTypeDef

### reactionsForComment
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.ReactionForCommentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetCommentsForComparedCommitInputPaginateTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### afterCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### beforeCommitId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.PaginatorConfigTypeDef]


# GetCommentsForComparedCommitInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### afterCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### beforeCommitId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetCommentsForComparedCommitOutputTypeDef

### commentsForComparedCommitData
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.CommentsForComparedCommitTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetCommentsForPullRequestInputPaginateTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: typing.Optional[str]

### beforeCommitId
- **Type**: typing.Optional[str]

### afterCommitId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.PaginatorConfigTypeDef]


# GetCommentsForPullRequestInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: typing.Optional[str]

### beforeCommitId
- **Type**: typing.Optional[str]

### afterCommitId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetCommentsForPullRequestOutputTypeDef

### commentsForPullRequestData
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.CommentsForPullRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetCommitInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### commitId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCommitOutputTypeDef

### commit
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.CommitTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDifferencesInputPaginateTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### afterCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### beforeCommitSpecifier
- **Type**: typing.Optional[str]

### beforePath
- **Type**: typing.Optional[str]

### afterPath
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.PaginatorConfigTypeDef]


# GetDifferencesInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### afterCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### beforeCommitSpecifier
- **Type**: typing.Optional[str]

### beforePath
- **Type**: typing.Optional[str]

### afterPath
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetDifferencesOutputTypeDef

### differences
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.DifferenceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetFileInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### commitSpecifier
- **Type**: typing.Optional[str]


# GetFileOutputTypeDef

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### blobId
- **Type**: <class 'str'>
- **Required**: Yes

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### fileMode
- **Type**: typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']
- **Required**: Yes

### fileSize
- **Type**: <class 'int'>
- **Required**: Yes

### fileContent
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFolderInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### folderPath
- **Type**: <class 'str'>
- **Required**: Yes

### commitSpecifier
- **Type**: typing.Optional[str]


# GetFolderOutputTypeDef

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### folderPath
- **Type**: <class 'str'>
- **Required**: Yes

### treeId
- **Type**: <class 'str'>
- **Required**: Yes

### subFolders
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.FolderTypeDef]
- **Required**: Yes

### files
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.FileTypeDef]
- **Required**: Yes

### symbolicLinks
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.SymbolicLinkTypeDef]
- **Required**: Yes

### subModules
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.SubModuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMergeCommitInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### destinationCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### conflictDetailLevel
- **Type**: typing.Optional[typing.Literal['FILE_LEVEL', 'LINE_LEVEL']]

### conflictResolutionStrategy
- **Type**: typing.Optional[typing.Literal['ACCEPT_DESTINATION', 'ACCEPT_SOURCE', 'AUTOMERGE', 'NONE']]


# GetMergeCommitOutputTypeDef

### sourceCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### destinationCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### baseCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### mergedCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMergeConflictsInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### destinationCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### mergeOption
- **Type**: typing.Literal['FAST_FORWARD_MERGE', 'SQUASH_MERGE', 'THREE_WAY_MERGE']
- **Required**: Yes

### conflictDetailLevel
- **Type**: typing.Optional[typing.Literal['FILE_LEVEL', 'LINE_LEVEL']]

### maxConflictFiles
- **Type**: typing.Optional[int]

### conflictResolutionStrategy
- **Type**: typing.Optional[typing.Literal['ACCEPT_DESTINATION', 'ACCEPT_SOURCE', 'AUTOMERGE', 'NONE']]

### nextToken
- **Type**: typing.Optional[str]


# GetMergeConflictsOutputTypeDef

### mergeable
- **Type**: <class 'bool'>
- **Required**: Yes

### destinationCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### baseCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### conflictMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.ConflictMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetMergeOptionsInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### destinationCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### conflictDetailLevel
- **Type**: typing.Optional[typing.Literal['FILE_LEVEL', 'LINE_LEVEL']]

### conflictResolutionStrategy
- **Type**: typing.Optional[typing.Literal['ACCEPT_DESTINATION', 'ACCEPT_SOURCE', 'AUTOMERGE', 'NONE']]


# GetMergeOptionsOutputTypeDef

### mergeOptions
- **Type**: typing.List[typing.Literal['FAST_FORWARD_MERGE', 'SQUASH_MERGE', 'THREE_WAY_MERGE']]
- **Required**: Yes

### sourceCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### destinationCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### baseCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPullRequestApprovalStatesInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPullRequestApprovalStatesOutputTypeDef

### approvals
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.ApprovalTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPullRequestInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPullRequestOutputTypeDef

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.PullRequestTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPullRequestOverrideStateInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPullRequestOverrideStateOutputTypeDef

### overridden
- **Type**: <class 'bool'>
- **Required**: Yes

### overrider
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRepositoryInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRepositoryOutputTypeDef

### repositoryMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.RepositoryMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRepositoryTriggersInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRepositoryTriggersOutputTypeDef

### configurationId
- **Type**: <class 'str'>
- **Required**: Yes

### triggers
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.RepositoryTriggerOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IsBinaryFileTypeDef

### source
- **Type**: typing.Optional[bool]

### destination
- **Type**: typing.Optional[bool]

### base
- **Type**: typing.Optional[bool]


# ListApprovalRuleTemplatesInputTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListApprovalRuleTemplatesOutputTypeDef

### approvalRuleTemplateNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssociatedApprovalRuleTemplatesForRepositoryInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef

### approvalRuleTemplateNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBranchesInputPaginateTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.PaginatorConfigTypeDef]


# ListBranchesInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBranchesOutputTypeDef

### branches
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFileCommitHistoryRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### commitSpecifier
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFileCommitHistoryResponseTypeDef

### revisionDag
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.FileVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPullRequestsInputPaginateTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### authorArn
- **Type**: typing.Optional[str]

### pullRequestStatus
- **Type**: typing.Optional[typing.Literal['CLOSED', 'OPEN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.PaginatorConfigTypeDef]


# ListPullRequestsInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### authorArn
- **Type**: typing.Optional[str]

### pullRequestStatus
- **Type**: typing.Optional[typing.Literal['CLOSED', 'OPEN']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPullRequestsOutputTypeDef

### pullRequestIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesForApprovalRuleTemplateInputTypeDef

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRepositoriesForApprovalRuleTemplateOutputTypeDef

### repositoryNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesInputPaginateTypeDef

### sortBy
- **Type**: typing.Optional[typing.Literal['lastModifiedDate', 'repositoryName']]

### order
- **Type**: typing.Optional[typing.Literal['ascending', 'descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.PaginatorConfigTypeDef]


# ListRepositoriesInputTypeDef

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['lastModifiedDate', 'repositoryName']]

### order
- **Type**: typing.Optional[typing.Literal['ascending', 'descending']]


# ListRepositoriesOutputTypeDef

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.RepositoryNameIdPairTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LocationTypeDef

### filePath
- **Type**: typing.Optional[str]

### filePosition
- **Type**: typing.Optional[int]

### relativeFileVersion
- **Type**: typing.Optional[typing.Literal['AFTER', 'BEFORE']]


# MergeBranchesByFastForwardInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### destinationCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### targetBranch
- **Type**: typing.Optional[str]


# MergeBranchesByFastForwardOutputTypeDef

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### treeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MergeBranchesBySquashInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### destinationCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### targetBranch
- **Type**: typing.Optional[str]

### conflictDetailLevel
- **Type**: typing.Optional[typing.Literal['FILE_LEVEL', 'LINE_LEVEL']]

### conflictResolutionStrategy
- **Type**: typing.Optional[typing.Literal['ACCEPT_DESTINATION', 'ACCEPT_SOURCE', 'AUTOMERGE', 'NONE']]

### authorName
- **Type**: typing.Optional[str]

### email
- **Type**: typing.Optional[str]

### commitMessage
- **Type**: typing.Optional[str]

### keepEmptyFolders
- **Type**: typing.Optional[bool]

### conflictResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.ConflictResolutionTypeDef]


# MergeBranchesBySquashOutputTypeDef

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### treeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MergeBranchesByThreeWayInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### destinationCommitSpecifier
- **Type**: <class 'str'>
- **Required**: Yes

### targetBranch
- **Type**: typing.Optional[str]

### conflictDetailLevel
- **Type**: typing.Optional[typing.Literal['FILE_LEVEL', 'LINE_LEVEL']]

### conflictResolutionStrategy
- **Type**: typing.Optional[typing.Literal['ACCEPT_DESTINATION', 'ACCEPT_SOURCE', 'AUTOMERGE', 'NONE']]

### authorName
- **Type**: typing.Optional[str]

### email
- **Type**: typing.Optional[str]

### commitMessage
- **Type**: typing.Optional[str]

### keepEmptyFolders
- **Type**: typing.Optional[bool]

### conflictResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.ConflictResolutionTypeDef]


# MergeBranchesByThreeWayOutputTypeDef

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### treeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MergeHunkDetailTypeDef

### startLine
- **Type**: typing.Optional[int]

### endLine
- **Type**: typing.Optional[int]

### hunkContent
- **Type**: typing.Optional[str]


# MergeHunkTypeDef

### isConflict
- **Type**: typing.Optional[bool]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.MergeHunkDetailTypeDef]

### destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.MergeHunkDetailTypeDef]

### base
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.MergeHunkDetailTypeDef]


# MergeMetadataTypeDef

### isMerged
- **Type**: typing.Optional[bool]

### mergedBy
- **Type**: typing.Optional[str]

### mergeCommitId
- **Type**: typing.Optional[str]

### mergeOption
- **Type**: typing.Optional[typing.Literal['FAST_FORWARD_MERGE', 'SQUASH_MERGE', 'THREE_WAY_MERGE']]


# MergeOperationsTypeDef

### source
- **Type**: typing.Optional[typing.Literal['A', 'D', 'M']]

### destination
- **Type**: typing.Optional[typing.Literal['A', 'D', 'M']]


# MergePullRequestByFastForwardInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitId
- **Type**: typing.Optional[str]


# MergePullRequestByFastForwardOutputTypeDef

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.PullRequestTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MergePullRequestBySquashInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitId
- **Type**: typing.Optional[str]

### conflictDetailLevel
- **Type**: typing.Optional[typing.Literal['FILE_LEVEL', 'LINE_LEVEL']]

### conflictResolutionStrategy
- **Type**: typing.Optional[typing.Literal['ACCEPT_DESTINATION', 'ACCEPT_SOURCE', 'AUTOMERGE', 'NONE']]

### commitMessage
- **Type**: typing.Optional[str]

### authorName
- **Type**: typing.Optional[str]

### email
- **Type**: typing.Optional[str]

### keepEmptyFolders
- **Type**: typing.Optional[bool]

### conflictResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.ConflictResolutionTypeDef]


# MergePullRequestBySquashOutputTypeDef

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.PullRequestTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MergePullRequestByThreeWayInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitId
- **Type**: typing.Optional[str]

### conflictDetailLevel
- **Type**: typing.Optional[typing.Literal['FILE_LEVEL', 'LINE_LEVEL']]

### conflictResolutionStrategy
- **Type**: typing.Optional[typing.Literal['ACCEPT_DESTINATION', 'ACCEPT_SOURCE', 'AUTOMERGE', 'NONE']]

### commitMessage
- **Type**: typing.Optional[str]

### authorName
- **Type**: typing.Optional[str]

### email
- **Type**: typing.Optional[str]

### keepEmptyFolders
- **Type**: typing.Optional[bool]

### conflictResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.ConflictResolutionTypeDef]


# MergePullRequestByThreeWayOutputTypeDef

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.PullRequestTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ObjectTypesTypeDef

### source
- **Type**: typing.Optional[typing.Literal['DIRECTORY', 'FILE', 'GIT_LINK', 'SYMBOLIC_LINK']]

### destination
- **Type**: typing.Optional[typing.Literal['DIRECTORY', 'FILE', 'GIT_LINK', 'SYMBOLIC_LINK']]

### base
- **Type**: typing.Optional[typing.Literal['DIRECTORY', 'FILE', 'GIT_LINK', 'SYMBOLIC_LINK']]


# OriginApprovalRuleTemplateTypeDef

### approvalRuleTemplateId
- **Type**: typing.Optional[str]

### approvalRuleTemplateName
- **Type**: typing.Optional[str]


# OverridePullRequestApprovalRulesInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### overrideStatus
- **Type**: typing.Literal['OVERRIDE', 'REVOKE']
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PostCommentForComparedCommitInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### afterCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: <class 'str'>
- **Required**: Yes

### beforeCommitId
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.LocationTypeDef]

### clientRequestToken
- **Type**: typing.Optional[str]


# PostCommentForComparedCommitOutputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### beforeCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### afterCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### beforeBlobId
- **Type**: <class 'str'>
- **Required**: Yes

### afterBlobId
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.LocationTypeDef'>
- **Required**: Yes

### comment
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.CommentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PostCommentForPullRequestInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### beforeCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### afterCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.LocationTypeDef]

### clientRequestToken
- **Type**: typing.Optional[str]


# PostCommentForPullRequestOutputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### beforeCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### afterCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### beforeBlobId
- **Type**: <class 'str'>
- **Required**: Yes

### afterBlobId
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.LocationTypeDef'>
- **Required**: Yes

### comment
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.CommentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PostCommentReplyInputTypeDef

### inReplyTo
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]


# PostCommentReplyOutputTypeDef

### comment
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.CommentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PullRequestCreatedEventMetadataTypeDef

### repositoryName
- **Type**: typing.Optional[str]

### sourceCommitId
- **Type**: typing.Optional[str]

### destinationCommitId
- **Type**: typing.Optional[str]

### mergeBase
- **Type**: typing.Optional[str]


# PullRequestEventTypeDef

### pullRequestId
- **Type**: typing.Optional[str]

### eventDate
- **Type**: typing.Optional[datetime.datetime]

### pullRequestEventType
- **Type**: typing.Optional[typing.Literal['PULL_REQUEST_APPROVAL_RULE_CREATED', 'PULL_REQUEST_APPROVAL_RULE_DELETED', 'PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN', 'PULL_REQUEST_APPROVAL_RULE_UPDATED', 'PULL_REQUEST_APPROVAL_STATE_CHANGED', 'PULL_REQUEST_CREATED', 'PULL_REQUEST_MERGE_STATE_CHANGED', 'PULL_REQUEST_SOURCE_REFERENCE_UPDATED', 'PULL_REQUEST_STATUS_CHANGED']]

### actorArn
- **Type**: typing.Optional[str]

### pullRequestCreatedEventMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.PullRequestCreatedEventMetadataTypeDef]

### pullRequestStatusChangedEventMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.PullRequestStatusChangedEventMetadataTypeDef]

### pullRequestSourceReferenceUpdatedEventMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.PullRequestSourceReferenceUpdatedEventMetadataTypeDef]

### pullRequestMergedStateChangedEventMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.PullRequestMergedStateChangedEventMetadataTypeDef]

### approvalRuleEventMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.ApprovalRuleEventMetadataTypeDef]

### approvalStateChangedEventMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.ApprovalStateChangedEventMetadataTypeDef]

### approvalRuleOverriddenEventMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.ApprovalRuleOverriddenEventMetadataTypeDef]


# PullRequestMergedStateChangedEventMetadataTypeDef

### repositoryName
- **Type**: typing.Optional[str]

### destinationReference
- **Type**: typing.Optional[str]

### mergeMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.MergeMetadataTypeDef]


# PullRequestSourceReferenceUpdatedEventMetadataTypeDef

### repositoryName
- **Type**: typing.Optional[str]

### beforeCommitId
- **Type**: typing.Optional[str]

### afterCommitId
- **Type**: typing.Optional[str]

### mergeBase
- **Type**: typing.Optional[str]


# PullRequestStatusChangedEventMetadataTypeDef

### pullRequestStatus
- **Type**: typing.Optional[typing.Literal['CLOSED', 'OPEN']]


# PullRequestTargetTypeDef

### repositoryName
- **Type**: typing.Optional[str]

### sourceReference
- **Type**: typing.Optional[str]

### destinationReference
- **Type**: typing.Optional[str]

### destinationCommit
- **Type**: typing.Optional[str]

### sourceCommit
- **Type**: typing.Optional[str]

### mergeBase
- **Type**: typing.Optional[str]

### mergeMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.MergeMetadataTypeDef]


# PullRequestTypeDef

### pullRequestId
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### lastActivityDate
- **Type**: typing.Optional[datetime.datetime]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### pullRequestStatus
- **Type**: typing.Optional[typing.Literal['CLOSED', 'OPEN']]

### authorArn
- **Type**: typing.Optional[str]

### pullRequestTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit_classes.PullRequestTargetTypeDef]]

### clientRequestToken
- **Type**: typing.Optional[str]

### revisionId
- **Type**: typing.Optional[str]

### approvalRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit_classes.ApprovalRuleTypeDef]]


# PutCommentReactionInputTypeDef

### commentId
- **Type**: <class 'str'>
- **Required**: Yes

### reactionValue
- **Type**: <class 'str'>
- **Required**: Yes


# PutFileEntryTypeDef

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### fileMode
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]

### fileContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.BlobTypeDef]

### sourceFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.SourceFileSpecifierTypeDef]


# PutFileInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### fileContent
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.BlobTypeDef'>
- **Required**: Yes

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### fileMode
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]

### parentCommitId
- **Type**: typing.Optional[str]

### commitMessage
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### email
- **Type**: typing.Optional[str]


# PutFileOutputTypeDef

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### blobId
- **Type**: <class 'str'>
- **Required**: Yes

### treeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRepositoryTriggersInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### triggers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codecommit_classes.RepositoryTriggerUnionTypeDef]
- **Required**: Yes


# PutRepositoryTriggersOutputTypeDef

### configurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReactionForCommentTypeDef

### reaction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.ReactionValueFormatsTypeDef]

### reactionUsers
- **Type**: typing.Optional[typing.List[str]]

### reactionsFromDeletedUsersCount
- **Type**: typing.Optional[int]


# ReactionValueFormatsTypeDef

### emoji
- **Type**: typing.Optional[str]

### shortCode
- **Type**: typing.Optional[str]

### unicode
- **Type**: typing.Optional[str]


# ReplaceContentEntryTypeDef

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### replacementType
- **Type**: typing.Literal['KEEP_BASE', 'KEEP_DESTINATION', 'KEEP_SOURCE', 'USE_NEW_CONTENT']
- **Required**: Yes

### content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit_classes.BlobTypeDef]

### fileMode
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]


# RepositoryMetadataTypeDef

### accountId
- **Type**: typing.Optional[str]

### repositoryId
- **Type**: typing.Optional[str]

### repositoryName
- **Type**: typing.Optional[str]

### repositoryDescription
- **Type**: typing.Optional[str]

### defaultBranch
- **Type**: typing.Optional[str]

### lastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### cloneUrlHttp
- **Type**: typing.Optional[str]

### cloneUrlSsh
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### kmsKeyId
- **Type**: typing.Optional[str]


# RepositoryNameIdPairTypeDef

### repositoryName
- **Type**: typing.Optional[str]

### repositoryId
- **Type**: typing.Optional[str]


# RepositoryTriggerExecutionFailureTypeDef

### trigger
- **Type**: typing.Optional[str]

### failureMessage
- **Type**: typing.Optional[str]


# RepositoryTriggerOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### events
- **Type**: typing.List[typing.Literal['all', 'createReference', 'deleteReference', 'updateReference']]
- **Required**: Yes

### customData
- **Type**: typing.Optional[str]

### branches
- **Type**: typing.Optional[typing.List[str]]


# RepositoryTriggerTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### events
- **Type**: typing.Sequence[typing.Literal['all', 'createReference', 'deleteReference', 'updateReference']]
- **Required**: Yes

### customData
- **Type**: typing.Optional[str]

### branches
- **Type**: typing.Optional[typing.Sequence[str]]


# RepositoryTriggerUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseMetadataTypeDef

### RequestId
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

### HostId
- **Type**: typing.Optional[str]


# SetFileModeEntryTypeDef

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### fileMode
- **Type**: typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']
- **Required**: Yes


# SourceFileSpecifierTypeDef

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### isMove
- **Type**: typing.Optional[bool]


# SubModuleTypeDef

### commitId
- **Type**: typing.Optional[str]

### absolutePath
- **Type**: typing.Optional[str]

### relativePath
- **Type**: typing.Optional[str]


# SymbolicLinkTypeDef

### blobId
- **Type**: typing.Optional[str]

### absolutePath
- **Type**: typing.Optional[str]

### relativePath
- **Type**: typing.Optional[str]

### fileMode
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]


# TagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TargetTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceReference
- **Type**: <class 'str'>
- **Required**: Yes

### destinationReference
- **Type**: typing.Optional[str]


# TestRepositoryTriggersInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### triggers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codecommit_classes.RepositoryTriggerUnionTypeDef]
- **Required**: Yes


# TestRepositoryTriggersOutputTypeDef

### successfulExecutions
- **Type**: typing.List[str]
- **Required**: Yes

### failedExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit_classes.RepositoryTriggerExecutionFailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UntagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApprovalRuleTemplateContentInputTypeDef

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### newRuleContent
- **Type**: <class 'str'>
- **Required**: Yes

### existingRuleContentSha256
- **Type**: typing.Optional[str]


# UpdateApprovalRuleTemplateContentOutputTypeDef

### approvalRuleTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ApprovalRuleTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateApprovalRuleTemplateDescriptionInputTypeDef

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### approvalRuleTemplateDescription
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApprovalRuleTemplateDescriptionOutputTypeDef

### approvalRuleTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ApprovalRuleTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateApprovalRuleTemplateNameInputTypeDef

### oldApprovalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### newApprovalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApprovalRuleTemplateNameOutputTypeDef

### approvalRuleTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ApprovalRuleTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCommentInputTypeDef

### commentId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateCommentOutputTypeDef

### comment
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.CommentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDefaultBranchInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### defaultBranchName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePullRequestApprovalRuleContentInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### approvalRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### newRuleContent
- **Type**: <class 'str'>
- **Required**: Yes

### existingRuleContentSha256
- **Type**: typing.Optional[str]


# UpdatePullRequestApprovalRuleContentOutputTypeDef

### approvalRule
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ApprovalRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePullRequestApprovalStateInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### approvalState
- **Type**: typing.Literal['APPROVE', 'REVOKE']
- **Required**: Yes


# UpdatePullRequestDescriptionInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePullRequestDescriptionOutputTypeDef

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.PullRequestTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePullRequestStatusInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### pullRequestStatus
- **Type**: typing.Literal['CLOSED', 'OPEN']
- **Required**: Yes


# UpdatePullRequestStatusOutputTypeDef

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.PullRequestTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePullRequestTitleInputTypeDef

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePullRequestTitleOutputTypeDef

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.PullRequestTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRepositoryDescriptionInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryDescription
- **Type**: typing.Optional[str]


# UpdateRepositoryEncryptionKeyInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRepositoryEncryptionKeyOutputTypeDef

### repositoryId
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### originalKmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRepositoryNameInputTypeDef

### oldName
- **Type**: <class 'str'>
- **Required**: Yes

### newName
- **Type**: <class 'str'>
- **Required**: Yes


# UserInfoTypeDef

### name
- **Type**: typing.Optional[str]

### email
- **Type**: typing.Optional[str]

### date
- **Type**: typing.Optional[str]


