# Codecommit Classes

# Approval

### userArn
- **Type**: typing.Optional[str]

### approvalState
- **Type**: typing.Optional[typing.Literal['APPROVE', 'REVOKE']]


# ApprovalRule

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.OriginApprovalRuleTemplate]


# ApprovalRuleEventMetadata

### approvalRuleName
- **Type**: typing.Optional[str]

### approvalRuleId
- **Type**: typing.Optional[str]

### approvalRuleContent
- **Type**: typing.Optional[str]


# ApprovalRuleOverriddenEventMetadata

### revisionId
- **Type**: typing.Optional[str]

### overrideStatus
- **Type**: typing.Optional[typing.Literal['OVERRIDE', 'REVOKE']]


# ApprovalRuleTemplate

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


# ApprovalStateChangedEventMetadata

### revisionId
- **Type**: typing.Optional[str]

### approvalStatus
- **Type**: typing.Optional[typing.Literal['APPROVE', 'REVOKE']]


# AssociateApprovalRuleTemplateWithRepositoryInput

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateApprovalRuleTemplateWithRepositoriesError

### repositoryName
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# BatchAssociateApprovalRuleTemplateWithRepositoriesInput

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryNames
- **Type**: typing.List[str]
- **Required**: Yes


# BatchAssociateApprovalRuleTemplateWithRepositoriesOutput

### associatedRepositoryNames
- **Type**: typing.List[str]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.BatchAssociateApprovalRuleTemplateWithRepositoriesError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDescribeMergeConflictsError

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### exceptionName
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDescribeMergeConflictsInput

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
- **Type**: typing.Optional[typing.List[str]]

### conflictDetailLevel
- **Type**: typing.Optional[typing.Literal['FILE_LEVEL', 'LINE_LEVEL']]

### conflictResolutionStrategy
- **Type**: typing.Optional[typing.Literal['ACCEPT_DESTINATION', 'ACCEPT_SOURCE', 'AUTOMERGE', 'NONE']]

### nextToken
- **Type**: typing.Optional[str]


# BatchDescribeMergeConflictsOutput

### conflicts
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Conflict]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.BatchDescribeMergeConflictsError]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# BatchDisassociateApprovalRuleTemplateFromRepositoriesError

### repositoryName
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# BatchDisassociateApprovalRuleTemplateFromRepositoriesInput

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryNames
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput

### disassociatedRepositoryNames
- **Type**: typing.List[str]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.BatchDisassociateApprovalRuleTemplateFromRepositoriesError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetCommitsError

### commitId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# BatchGetCommitsInput

### commitIds
- **Type**: typing.List[str]
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetCommitsOutput

### commits
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Commit]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.BatchGetCommitsError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetRepositoriesError

### repositoryId
- **Type**: typing.Optional[str]

### repositoryName
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['EncryptionIntegrityChecksFailedException', 'EncryptionKeyAccessDeniedException', 'EncryptionKeyDisabledException', 'EncryptionKeyNotFoundException', 'EncryptionKeyUnavailableException', 'RepositoryDoesNotExistException']]

### errorMessage
- **Type**: typing.Optional[str]


# BatchGetRepositoriesInput

### repositoryNames
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetRepositoriesOutput

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.RepositoryMetadata]
- **Required**: Yes

### repositoriesNotFound
- **Type**: typing.List[str]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.BatchGetRepositoriesError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# BlobMetadata

### blobId
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### mode
- **Type**: typing.Optional[str]


# BranchInfo

### branchName
- **Type**: typing.Optional[str]

### commitId
- **Type**: typing.Optional[str]


# Comment

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


# CommentsForComparedCommit

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Location]

### comments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Comment]]


# CommentsForPullRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Location]

### comments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Comment]]


# Commit

### commitId
- **Type**: typing.Optional[str]

### treeId
- **Type**: typing.Optional[str]

### parents
- **Type**: typing.Optional[typing.List[str]]

### message
- **Type**: typing.Optional[str]

### author
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.UserInfo]

### committer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.UserInfo]

### additionalData
- **Type**: typing.Optional[str]


# Conflict

### conflictMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ConflictMetadata]

### mergeHunks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.MergeHunk]]


# ConflictMetadata

### filePath
- **Type**: typing.Optional[str]

### fileSizes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.FileSizes]

### fileModes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.FileModes]

### objectTypes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ObjectTypes]

### numberOfConflicts
- **Type**: typing.Optional[int]

### isBinaryFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.IsBinaryFile]

### contentConflict
- **Type**: typing.Optional[bool]

### fileModeConflict
- **Type**: typing.Optional[bool]

### objectTypeConflict
- **Type**: typing.Optional[bool]

### mergeOperations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.MergeOperations]


# ConflictResolution

### replaceContents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ReplaceContentEntry]]

### deleteFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.DeleteFileEntry]]

### setFileModes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.SetFileModeEntry]]


# CreateApprovalRuleTemplateInput

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### approvalRuleTemplateContent
- **Type**: <class 'str'>
- **Required**: Yes

### approvalRuleTemplateDescription
- **Type**: typing.Optional[str]


# CreateApprovalRuleTemplateOutput

### approvalRuleTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ApprovalRuleTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBranchInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### commitId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCommitInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PutFileEntry]]

### deleteFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.DeleteFileEntry]]

### setFileModes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.SetFileModeEntry]]


# CreateCommitOutput

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### treeId
- **Type**: <class 'str'>
- **Required**: Yes

### filesAdded
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.FileMetadata]
- **Required**: Yes

### filesUpdated
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.FileMetadata]
- **Required**: Yes

### filesDeleted
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.FileMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePullRequestApprovalRuleInput

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### approvalRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### approvalRuleContent
- **Type**: <class 'str'>
- **Required**: Yes


# CreatePullRequestApprovalRuleOutput

### approvalRule
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ApprovalRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePullRequestInput

### title
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Target]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### clientRequestToken
- **Type**: typing.Optional[str]


# CreatePullRequestOutput

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PullRequest'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRepositoryInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryDescription
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### kmsKeyId
- **Type**: typing.Optional[str]


# CreateRepositoryOutput

### repositoryMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.RepositoryMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUnreferencedMergeCommitInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ConflictResolution]


# CreateUnreferencedMergeCommitOutput

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### treeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApprovalRuleTemplateInput

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApprovalRuleTemplateOutput

### approvalRuleTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBranchInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBranchOutput

### deletedBranch
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.BranchInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCommentContentInput

### commentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCommentContentOutput

### comment
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Comment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFileEntry

### filePath
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFileInput

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


# DeleteFileOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePullRequestApprovalRuleInput

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### approvalRuleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePullRequestApprovalRuleOutput

### approvalRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRepositoryInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRepositoryOutput

### repositoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMergeConflictsInput

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


# DescribeMergeConflictsOutput

### conflictMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ConflictMetadata'>
- **Required**: Yes

### mergeHunks
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.MergeHunk]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribePullRequestEventsInput

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


# DescribePullRequestEventsInputPaginate

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### pullRequestEventType
- **Type**: typing.Optional[typing.Literal['PULL_REQUEST_APPROVAL_RULE_CREATED', 'PULL_REQUEST_APPROVAL_RULE_DELETED', 'PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN', 'PULL_REQUEST_APPROVAL_RULE_UPDATED', 'PULL_REQUEST_APPROVAL_STATE_CHANGED', 'PULL_REQUEST_CREATED', 'PULL_REQUEST_MERGE_STATE_CHANGED', 'PULL_REQUEST_SOURCE_REFERENCE_UPDATED', 'PULL_REQUEST_STATUS_CHANGED']]

### actorArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PaginatorConfig]


# DescribePullRequestEventsOutput

### pullRequestEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PullRequestEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Difference

### beforeBlob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.BlobMetadata]

### afterBlob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.BlobMetadata]

### changeType
- **Type**: typing.Optional[typing.Literal['A', 'D', 'M']]


# DisassociateApprovalRuleTemplateFromRepositoryInput

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# EvaluatePullRequestApprovalRulesInput

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluatePullRequestApprovalRulesOutput

### evaluation
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Evaluation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# Evaluation

### approved
- **Type**: typing.Optional[bool]

### overridden
- **Type**: typing.Optional[bool]

### approvalRulesSatisfied
- **Type**: typing.Optional[typing.List[str]]

### approvalRulesNotSatisfied
- **Type**: typing.Optional[typing.List[str]]


# File

### blobId
- **Type**: typing.Optional[str]

### absolutePath
- **Type**: typing.Optional[str]

### relativePath
- **Type**: typing.Optional[str]

### fileMode
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]


# FileMetadata

### absolutePath
- **Type**: typing.Optional[str]

### blobId
- **Type**: typing.Optional[str]

### fileMode
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]


# FileModes

### source
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]

### destination
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]

### base
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]


# FileSizes

### source
- **Type**: typing.Optional[int]

### destination
- **Type**: typing.Optional[int]

### base
- **Type**: typing.Optional[int]


# FileVersion

### commit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Commit]

### blobId
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### revisionChildren
- **Type**: typing.Optional[typing.List[str]]


# Folder

### treeId
- **Type**: typing.Optional[str]

### absolutePath
- **Type**: typing.Optional[str]

### relativePath
- **Type**: typing.Optional[str]


# GetApprovalRuleTemplateInput

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetApprovalRuleTemplateOutput

### approvalRuleTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ApprovalRuleTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# GetBlobInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### blobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBlobOutput

### content
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# GetBranchInput

### repositoryName
- **Type**: typing.Optional[str]

### branchName
- **Type**: typing.Optional[str]


# GetBranchOutput

### branch
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.BranchInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# GetCommentInput

### commentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCommentOutput

### comment
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Comment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# GetCommentReactionsInput

### commentId
- **Type**: <class 'str'>
- **Required**: Yes

### reactionUserArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetCommentReactionsOutput

### reactionsForComment
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ReactionForComment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetCommentsForComparedCommitInput

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


# GetCommentsForComparedCommitInputPaginate

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### afterCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### beforeCommitId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PaginatorConfig]


# GetCommentsForComparedCommitOutput

### commentsForComparedCommitData
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.CommentsForComparedCommit]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetCommentsForPullRequestInput

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


# GetCommentsForPullRequestInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PaginatorConfig]


# GetCommentsForPullRequestOutput

### commentsForPullRequestData
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.CommentsForPullRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetCommitInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### commitId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCommitOutput

### commit
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Commit'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# GetDifferencesInput

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


# GetDifferencesInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PaginatorConfig]


# GetDifferencesOutput

### differences
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Difference]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetFileInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### commitSpecifier
- **Type**: typing.Optional[str]


# GetFileOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# GetFolderInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### folderPath
- **Type**: <class 'str'>
- **Required**: Yes

### commitSpecifier
- **Type**: typing.Optional[str]


# GetFolderOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Folder]
- **Required**: Yes

### files
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.File]
- **Required**: Yes

### symbolicLinks
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.SymbolicLink]
- **Required**: Yes

### subModules
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.SubModule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# GetMergeCommitInput

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


# GetMergeCommitOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# GetMergeConflictsInput

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


# GetMergeConflictsOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ConflictMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetMergeOptionsInput

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


# GetMergeOptionsOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# GetPullRequestApprovalStatesInput

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPullRequestApprovalStatesOutput

### approvals
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Approval]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# GetPullRequestInput

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPullRequestOutput

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PullRequest'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# GetPullRequestOverrideStateInput

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPullRequestOverrideStateOutput

### overridden
- **Type**: <class 'bool'>
- **Required**: Yes

### overrider
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# GetRepositoryInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRepositoryOutput

### repositoryMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.RepositoryMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# GetRepositoryTriggersInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRepositoryTriggersOutput

### configurationId
- **Type**: <class 'str'>
- **Required**: Yes

### triggers
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.RepositoryTriggerOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# IsBinaryFile

### source
- **Type**: typing.Optional[bool]

### destination
- **Type**: typing.Optional[bool]

### base
- **Type**: typing.Optional[bool]


# ListApprovalRuleTemplatesInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListApprovalRuleTemplatesOutput

### approvalRuleTemplateNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssociatedApprovalRuleTemplatesForRepositoryInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssociatedApprovalRuleTemplatesForRepositoryOutput

### approvalRuleTemplateNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBranchesInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBranchesInputPaginate

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PaginatorConfig]


# ListBranchesOutput

### branches
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFileCommitHistoryRequest

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


# ListFileCommitHistoryResponse

### revisionDag
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.FileVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPullRequestsInput

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


# ListPullRequestsInputPaginate

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### authorArn
- **Type**: typing.Optional[str]

### pullRequestStatus
- **Type**: typing.Optional[typing.Literal['CLOSED', 'OPEN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PaginatorConfig]


# ListPullRequestsOutput

### pullRequestIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesForApprovalRuleTemplateInput

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRepositoriesForApprovalRuleTemplateOutput

### repositoryNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesInput

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['lastModifiedDate', 'repositoryName']]

### order
- **Type**: typing.Optional[typing.Literal['ascending', 'descending']]


# ListRepositoriesInputPaginate

### sortBy
- **Type**: typing.Optional[typing.Literal['lastModifiedDate', 'repositoryName']]

### order
- **Type**: typing.Optional[typing.Literal['ascending', 'descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PaginatorConfig]


# ListRepositoriesOutput

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.RepositoryNameIdPair]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceOutput

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Location

### filePath
- **Type**: typing.Optional[str]

### filePosition
- **Type**: typing.Optional[int]

### relativeFileVersion
- **Type**: typing.Optional[typing.Literal['AFTER', 'BEFORE']]


# MergeBranchesByFastForwardInput

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


# MergeBranchesByFastForwardOutput

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### treeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# MergeBranchesBySquashInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ConflictResolution]


# MergeBranchesBySquashOutput

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### treeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# MergeBranchesByThreeWayInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ConflictResolution]


# MergeBranchesByThreeWayOutput

### commitId
- **Type**: <class 'str'>
- **Required**: Yes

### treeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# MergeHunk

### isConflict
- **Type**: typing.Optional[bool]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.MergeHunkDetail]

### destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.MergeHunkDetail]

### base
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.MergeHunkDetail]


# MergeHunkDetail

### startLine
- **Type**: typing.Optional[int]

### endLine
- **Type**: typing.Optional[int]

### hunkContent
- **Type**: typing.Optional[str]


# MergeMetadata

### isMerged
- **Type**: typing.Optional[bool]

### mergedBy
- **Type**: typing.Optional[str]

### mergeCommitId
- **Type**: typing.Optional[str]

### mergeOption
- **Type**: typing.Optional[typing.Literal['FAST_FORWARD_MERGE', 'SQUASH_MERGE', 'THREE_WAY_MERGE']]


# MergeOperations

### source
- **Type**: typing.Optional[typing.Literal['A', 'D', 'M']]

### destination
- **Type**: typing.Optional[typing.Literal['A', 'D', 'M']]


# MergePullRequestByFastForwardInput

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCommitId
- **Type**: typing.Optional[str]


# MergePullRequestByFastForwardOutput

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PullRequest'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# MergePullRequestBySquashInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ConflictResolution]


# MergePullRequestBySquashOutput

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PullRequest'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# MergePullRequestByThreeWayInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ConflictResolution]


# MergePullRequestByThreeWayOutput

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PullRequest'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# ObjectTypes

### source
- **Type**: typing.Optional[typing.Literal['DIRECTORY', 'FILE', 'GIT_LINK', 'SYMBOLIC_LINK']]

### destination
- **Type**: typing.Optional[typing.Literal['DIRECTORY', 'FILE', 'GIT_LINK', 'SYMBOLIC_LINK']]

### base
- **Type**: typing.Optional[typing.Literal['DIRECTORY', 'FILE', 'GIT_LINK', 'SYMBOLIC_LINK']]


# OriginApprovalRuleTemplate

### approvalRuleTemplateId
- **Type**: typing.Optional[str]

### approvalRuleTemplateName
- **Type**: typing.Optional[str]


# OverridePullRequestApprovalRulesInput

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### overrideStatus
- **Type**: typing.Literal['OVERRIDE', 'REVOKE']
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PostCommentForComparedCommitInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Location]

### clientRequestToken
- **Type**: typing.Optional[str]


# PostCommentForComparedCommitOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Location'>
- **Required**: Yes

### comment
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Comment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# PostCommentForPullRequestInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Location]

### clientRequestToken
- **Type**: typing.Optional[str]


# PostCommentForPullRequestOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Location'>
- **Required**: Yes

### comment
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Comment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# PostCommentReplyInput

### inReplyTo
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]


# PostCommentReplyOutput

### comment
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Comment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# PullRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PullRequestTarget]]

### clientRequestToken
- **Type**: typing.Optional[str]

### revisionId
- **Type**: typing.Optional[str]

### approvalRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ApprovalRule]]


# PullRequestCreatedEventMetadata

### repositoryName
- **Type**: typing.Optional[str]

### sourceCommitId
- **Type**: typing.Optional[str]

### destinationCommitId
- **Type**: typing.Optional[str]

### mergeBase
- **Type**: typing.Optional[str]


# PullRequestEvent

### pullRequestId
- **Type**: typing.Optional[str]

### eventDate
- **Type**: typing.Optional[datetime.datetime]

### pullRequestEventType
- **Type**: typing.Optional[typing.Literal['PULL_REQUEST_APPROVAL_RULE_CREATED', 'PULL_REQUEST_APPROVAL_RULE_DELETED', 'PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN', 'PULL_REQUEST_APPROVAL_RULE_UPDATED', 'PULL_REQUEST_APPROVAL_STATE_CHANGED', 'PULL_REQUEST_CREATED', 'PULL_REQUEST_MERGE_STATE_CHANGED', 'PULL_REQUEST_SOURCE_REFERENCE_UPDATED', 'PULL_REQUEST_STATUS_CHANGED']]

### actorArn
- **Type**: typing.Optional[str]

### pullRequestCreatedEventMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PullRequestCreatedEventMetadata]

### pullRequestStatusChangedEventMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PullRequestStatusChangedEventMetadata]

### pullRequestSourceReferenceUpdatedEventMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PullRequestSourceReferenceUpdatedEventMetadata]

### pullRequestMergedStateChangedEventMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PullRequestMergedStateChangedEventMetadata]

### approvalRuleEventMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ApprovalRuleEventMetadata]

### approvalStateChangedEventMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ApprovalStateChangedEventMetadata]

### approvalRuleOverriddenEventMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ApprovalRuleOverriddenEventMetadata]


# PullRequestMergedStateChangedEventMetadata

### repositoryName
- **Type**: typing.Optional[str]

### destinationReference
- **Type**: typing.Optional[str]

### mergeMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.MergeMetadata]


# PullRequestSourceReferenceUpdatedEventMetadata

### repositoryName
- **Type**: typing.Optional[str]

### beforeCommitId
- **Type**: typing.Optional[str]

### afterCommitId
- **Type**: typing.Optional[str]

### mergeBase
- **Type**: typing.Optional[str]


# PullRequestStatusChangedEventMetadata

### pullRequestStatus
- **Type**: typing.Optional[typing.Literal['CLOSED', 'OPEN']]


# PullRequestTarget

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.MergeMetadata]


# PutCommentReactionInput

### commentId
- **Type**: <class 'str'>
- **Required**: Yes

### reactionValue
- **Type**: <class 'str'>
- **Required**: Yes


# PutFileEntry

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### fileMode
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]

### fileContent
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### sourceFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.SourceFileSpecifier]


# PutFileInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: <class 'str'>
- **Required**: Yes

### fileContent
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
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


# PutFileOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# PutRepositoryTriggersInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### triggers
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.RepositoryTrigger, aws_resource_validator.pydantic_models.codecommit.codecommit_classes.RepositoryTriggerOutput]]
- **Required**: Yes


# PutRepositoryTriggersOutput

### configurationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# ReactionForComment

### reaction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ReactionValueFormats]

### reactionUsers
- **Type**: typing.Optional[typing.List[str]]

### reactionsFromDeletedUsersCount
- **Type**: typing.Optional[int]


# ReactionValueFormats

### emoji
- **Type**: typing.Optional[str]

### shortCode
- **Type**: typing.Optional[str]

### unicode
- **Type**: typing.Optional[str]


# ReplaceContentEntry

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### replacementType
- **Type**: typing.Literal['KEEP_BASE', 'KEEP_DESTINATION', 'KEEP_SOURCE', 'USE_NEW_CONTENT']
- **Required**: Yes

### content
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### fileMode
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]


# RepositoryMetadata

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


# RepositoryNameIdPair

### repositoryName
- **Type**: typing.Optional[str]

### repositoryId
- **Type**: typing.Optional[str]


# RepositoryTrigger

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


# RepositoryTriggerExecutionFailure

### trigger
- **Type**: typing.Optional[str]

### failureMessage
- **Type**: typing.Optional[str]


# RepositoryTriggerOutput

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


# ResponseMetadata

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


# SetFileModeEntry

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### fileMode
- **Type**: typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']
- **Required**: Yes


# SourceFileSpecifier

### filePath
- **Type**: <class 'str'>
- **Required**: Yes

### isMove
- **Type**: typing.Optional[bool]


# SubModule

### commitId
- **Type**: typing.Optional[str]

### absolutePath
- **Type**: typing.Optional[str]

### relativePath
- **Type**: typing.Optional[str]


# SymbolicLink

### blobId
- **Type**: typing.Optional[str]

### absolutePath
- **Type**: typing.Optional[str]

### relativePath
- **Type**: typing.Optional[str]

### fileMode
- **Type**: typing.Optional[typing.Literal['EXECUTABLE', 'NORMAL', 'SYMLINK']]


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# Target

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceReference
- **Type**: <class 'str'>
- **Required**: Yes

### destinationReference
- **Type**: typing.Optional[str]


# TestRepositoryTriggersInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### triggers
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.RepositoryTrigger, aws_resource_validator.pydantic_models.codecommit.codecommit_classes.RepositoryTriggerOutput]]
- **Required**: Yes


# TestRepositoryTriggersOutput

### successfulExecutions
- **Type**: typing.List[str]
- **Required**: Yes

### failedExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecommit.codecommit_classes.RepositoryTriggerExecutionFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateApprovalRuleTemplateContentInput

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### newRuleContent
- **Type**: <class 'str'>
- **Required**: Yes

### existingRuleContentSha256
- **Type**: typing.Optional[str]


# UpdateApprovalRuleTemplateContentOutput

### approvalRuleTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ApprovalRuleTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateApprovalRuleTemplateDescriptionInput

### approvalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### approvalRuleTemplateDescription
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApprovalRuleTemplateDescriptionOutput

### approvalRuleTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ApprovalRuleTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateApprovalRuleTemplateNameInput

### oldApprovalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### newApprovalRuleTemplateName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApprovalRuleTemplateNameOutput

### approvalRuleTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ApprovalRuleTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCommentInput

### commentId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateCommentOutput

### comment
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.Comment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDefaultBranchInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### defaultBranchName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePullRequestApprovalRuleContentInput

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


# UpdatePullRequestApprovalRuleContentOutput

### approvalRule
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ApprovalRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePullRequestApprovalStateInput

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### approvalState
- **Type**: typing.Literal['APPROVE', 'REVOKE']
- **Required**: Yes


# UpdatePullRequestDescriptionInput

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePullRequestDescriptionOutput

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PullRequest'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePullRequestStatusInput

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### pullRequestStatus
- **Type**: typing.Literal['CLOSED', 'OPEN']
- **Required**: Yes


# UpdatePullRequestStatusOutput

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PullRequest'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePullRequestTitleInput

### pullRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePullRequestTitleOutput

### pullRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.PullRequest'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRepositoryDescriptionInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryDescription
- **Type**: typing.Optional[str]


# UpdateRepositoryEncryptionKeyInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRepositoryEncryptionKeyOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecommit.codecommit_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRepositoryNameInput

### oldName
- **Type**: <class 'str'>
- **Required**: Yes

### newName
- **Type**: <class 'str'>
- **Required**: Yes


# UserInfo

### name
- **Type**: typing.Optional[str]

### email
- **Type**: typing.Optional[str]

### date
- **Type**: typing.Optional[str]


