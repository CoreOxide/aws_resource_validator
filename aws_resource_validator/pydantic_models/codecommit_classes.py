from datetime import datetime
from pydantic import BaseModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.codecommit_constants import *

class ApprovalRuleEventMetadataTypeDef(BaseModel):
    approvalRuleName: Optional[str] = None
    approvalRuleId: Optional[str] = None
    approvalRuleContent: Optional[str] = None

class ApprovalRuleOverriddenEventMetadataTypeDef(BaseModel):
    revisionId: Optional[str] = None
    overrideStatus: Optional[OverrideStatusType] = None

class ApprovalRuleTemplateTypeDef(BaseModel):
    approvalRuleTemplateId: Optional[str] = None
    approvalRuleTemplateName: Optional[str] = None
    approvalRuleTemplateDescription: Optional[str] = None
    approvalRuleTemplateContent: Optional[str] = None
    ruleContentSha256: Optional[str] = None
    lastModifiedDate: Optional[datetime] = None
    creationDate: Optional[datetime] = None
    lastModifiedUser: Optional[str] = None

class OriginApprovalRuleTemplateTypeDef(BaseModel):
    approvalRuleTemplateId: Optional[str] = None
    approvalRuleTemplateName: Optional[str] = None

class ApprovalStateChangedEventMetadataTypeDef(BaseModel):
    revisionId: Optional[str] = None
    approvalStatus: Optional[ApprovalStateType] = None

class ApprovalTypeDef(BaseModel):
    userArn: Optional[str] = None
    approvalState: Optional[ApprovalStateType] = None

class AssociateApprovalRuleTemplateWithRepositoryInputRequestTypeDef(BaseModel):
    approvalRuleTemplateName: str
    repositoryName: str

class BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef(BaseModel):
    repositoryName: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class BatchAssociateApprovalRuleTemplateWithRepositoriesInputRequestTypeDef(BaseModel):
    approvalRuleTemplateName: str
    repositoryNames: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchDescribeMergeConflictsErrorTypeDef(BaseModel):
    filePath: str
    exceptionName: str
    message: str

class BatchDescribeMergeConflictsInputRequestTypeDef(BaseModel):
    repositoryName: str
    destinationCommitSpecifier: str
    sourceCommitSpecifier: str
    mergeOption: MergeOptionTypeEnumType
    maxMergeHunks: Optional[int] = None
    maxConflictFiles: Optional[int] = None
    filePaths: Optional[Sequence[str]] = None
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    nextToken: Optional[str] = None

class BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef(BaseModel):
    repositoryName: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class BatchDisassociateApprovalRuleTemplateFromRepositoriesInputRequestTypeDef(BaseModel):
    approvalRuleTemplateName: str
    repositoryNames: Sequence[str]

class BatchGetCommitsErrorTypeDef(BaseModel):
    commitId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None

class BatchGetCommitsInputRequestTypeDef(BaseModel):
    commitIds: Sequence[str]
    repositoryName: str

class BatchGetRepositoriesErrorTypeDef(BaseModel):
    repositoryId: Optional[str] = None
    repositoryName: Optional[str] = None
    errorCode: Optional[BatchGetRepositoriesErrorCodeEnumType] = None
    errorMessage: Optional[str] = None

class BatchGetRepositoriesInputRequestTypeDef(BaseModel):
    repositoryNames: Sequence[str]

class RepositoryMetadataTypeDef(BaseModel):
    accountId: Optional[str] = None
    repositoryId: Optional[str] = None
    repositoryName: Optional[str] = None
    repositoryDescription: Optional[str] = None
    defaultBranch: Optional[str] = None
    lastModifiedDate: Optional[datetime] = None
    creationDate: Optional[datetime] = None
    cloneUrlHttp: Optional[str] = None
    cloneUrlSsh: Optional[str] = None
    Arn: Optional[str] = None
    kmsKeyId: Optional[str] = None

class BlobMetadataTypeDef(BaseModel):
    blobId: Optional[str] = None
    path: Optional[str] = None
    mode: Optional[str] = None

class BranchInfoTypeDef(BaseModel):
    branchName: Optional[str] = None
    commitId: Optional[str] = None

class CommentTypeDef(BaseModel):
    commentId: Optional[str] = None
    content: Optional[str] = None
    inReplyTo: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None
    authorArn: Optional[str] = None
    deleted: Optional[bool] = None
    clientRequestToken: Optional[str] = None
    callerReactions: Optional[List[str]] = None
    reactionCounts: Optional[Dict[str, int]] = None

class LocationTypeDef(BaseModel):
    filePath: Optional[str] = None
    filePosition: Optional[int] = None
    relativeFileVersion: Optional[RelativeFileVersionEnumType] = None

class UserInfoTypeDef(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    date: Optional[str] = None

class FileModesTypeDef(BaseModel):
    source: Optional[FileModeTypeEnumType] = None
    destination: Optional[FileModeTypeEnumType] = None
    base: Optional[FileModeTypeEnumType] = None

class FileSizesTypeDef(BaseModel):
    source: Optional[int] = None
    destination: Optional[int] = None
    base: Optional[int] = None

class IsBinaryFileTypeDef(BaseModel):
    source: Optional[bool] = None
    destination: Optional[bool] = None
    base: Optional[bool] = None

class MergeOperationsTypeDef(BaseModel):
    source: Optional[ChangeTypeEnumType] = None
    destination: Optional[ChangeTypeEnumType] = None

class ObjectTypesTypeDef(BaseModel):
    source: Optional[ObjectTypeEnumType] = None
    destination: Optional[ObjectTypeEnumType] = None
    base: Optional[ObjectTypeEnumType] = None

class DeleteFileEntryTypeDef(BaseModel):
    filePath: str

class SetFileModeEntryTypeDef(BaseModel):
    filePath: str
    fileMode: FileModeTypeEnumType

class CreateApprovalRuleTemplateInputRequestTypeDef(BaseModel):
    approvalRuleTemplateName: str
    approvalRuleTemplateContent: str
    approvalRuleTemplateDescription: Optional[str] = None

class CreateBranchInputRequestTypeDef(BaseModel):
    repositoryName: str
    branchName: str
    commitId: str

class FileMetadataTypeDef(BaseModel):
    absolutePath: Optional[str] = None
    blobId: Optional[str] = None
    fileMode: Optional[FileModeTypeEnumType] = None

class CreatePullRequestApprovalRuleInputRequestTypeDef(BaseModel):
    pullRequestId: str
    approvalRuleName: str
    approvalRuleContent: str

class TargetTypeDef(BaseModel):
    repositoryName: str
    sourceReference: str
    destinationReference: Optional[str] = None

class CreateRepositoryInputRequestTypeDef(BaseModel):
    repositoryName: str
    repositoryDescription: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    kmsKeyId: Optional[str] = None

class DeleteApprovalRuleTemplateInputRequestTypeDef(BaseModel):
    approvalRuleTemplateName: str

class DeleteBranchInputRequestTypeDef(BaseModel):
    repositoryName: str
    branchName: str

class DeleteCommentContentInputRequestTypeDef(BaseModel):
    commentId: str

class DeleteFileInputRequestTypeDef(BaseModel):
    repositoryName: str
    branchName: str
    filePath: str
    parentCommitId: str
    keepEmptyFolders: Optional[bool] = None
    commitMessage: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None

class DeletePullRequestApprovalRuleInputRequestTypeDef(BaseModel):
    pullRequestId: str
    approvalRuleName: str

class DeleteRepositoryInputRequestTypeDef(BaseModel):
    repositoryName: str

class DescribeMergeConflictsInputRequestTypeDef(BaseModel):
    repositoryName: str
    destinationCommitSpecifier: str
    sourceCommitSpecifier: str
    mergeOption: MergeOptionTypeEnumType
    filePath: str
    maxMergeHunks: Optional[int] = None
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    nextToken: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribePullRequestEventsInputRequestTypeDef(BaseModel):
    pullRequestId: str
    pullRequestEventType: Optional[PullRequestEventTypeType] = None
    actorArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DisassociateApprovalRuleTemplateFromRepositoryInputRequestTypeDef(BaseModel):
    approvalRuleTemplateName: str
    repositoryName: str

class EvaluatePullRequestApprovalRulesInputRequestTypeDef(BaseModel):
    pullRequestId: str
    revisionId: str

class EvaluationTypeDef(BaseModel):
    approved: Optional[bool] = None
    overridden: Optional[bool] = None
    approvalRulesSatisfied: Optional[List[str]] = None
    approvalRulesNotSatisfied: Optional[List[str]] = None

class FileTypeDef(BaseModel):
    blobId: Optional[str] = None
    absolutePath: Optional[str] = None
    relativePath: Optional[str] = None
    fileMode: Optional[FileModeTypeEnumType] = None

class FolderTypeDef(BaseModel):
    treeId: Optional[str] = None
    absolutePath: Optional[str] = None
    relativePath: Optional[str] = None

class GetApprovalRuleTemplateInputRequestTypeDef(BaseModel):
    approvalRuleTemplateName: str

class GetBlobInputRequestTypeDef(BaseModel):
    repositoryName: str
    blobId: str

class GetBranchInputRequestTypeDef(BaseModel):
    repositoryName: Optional[str] = None
    branchName: Optional[str] = None

class GetCommentInputRequestTypeDef(BaseModel):
    commentId: str

class GetCommentReactionsInputRequestTypeDef(BaseModel):
    commentId: str
    reactionUserArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetCommentsForComparedCommitInputRequestTypeDef(BaseModel):
    repositoryName: str
    afterCommitId: str
    beforeCommitId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetCommentsForPullRequestInputRequestTypeDef(BaseModel):
    pullRequestId: str
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetCommitInputRequestTypeDef(BaseModel):
    repositoryName: str
    commitId: str

class GetDifferencesInputRequestTypeDef(BaseModel):
    repositoryName: str
    afterCommitSpecifier: str
    beforeCommitSpecifier: Optional[str] = None
    beforePath: Optional[str] = None
    afterPath: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetFileInputRequestTypeDef(BaseModel):
    repositoryName: str
    filePath: str
    commitSpecifier: Optional[str] = None

class GetFolderInputRequestTypeDef(BaseModel):
    repositoryName: str
    folderPath: str
    commitSpecifier: Optional[str] = None

class SubModuleTypeDef(BaseModel):
    commitId: Optional[str] = None
    absolutePath: Optional[str] = None
    relativePath: Optional[str] = None

class SymbolicLinkTypeDef(BaseModel):
    blobId: Optional[str] = None
    absolutePath: Optional[str] = None
    relativePath: Optional[str] = None
    fileMode: Optional[FileModeTypeEnumType] = None

class GetMergeCommitInputRequestTypeDef(BaseModel):
    repositoryName: str
    sourceCommitSpecifier: str
    destinationCommitSpecifier: str
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None

class GetMergeConflictsInputRequestTypeDef(BaseModel):
    repositoryName: str
    destinationCommitSpecifier: str
    sourceCommitSpecifier: str
    mergeOption: MergeOptionTypeEnumType
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    maxConflictFiles: Optional[int] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    nextToken: Optional[str] = None

class GetMergeOptionsInputRequestTypeDef(BaseModel):
    repositoryName: str
    sourceCommitSpecifier: str
    destinationCommitSpecifier: str
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None

class GetPullRequestApprovalStatesInputRequestTypeDef(BaseModel):
    pullRequestId: str
    revisionId: str

class GetPullRequestInputRequestTypeDef(BaseModel):
    pullRequestId: str

class GetPullRequestOverrideStateInputRequestTypeDef(BaseModel):
    pullRequestId: str
    revisionId: str

class GetRepositoryInputRequestTypeDef(BaseModel):
    repositoryName: str

class GetRepositoryTriggersInputRequestTypeDef(BaseModel):
    repositoryName: str

class RepositoryTriggerTypeDef(BaseModel):
    name: str
    destinationArn: str
    events: List[RepositoryTriggerEventEnumType]
    customData: Optional[str] = None
    branches: Optional[List[str]] = None

class ListApprovalRuleTemplatesInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef(BaseModel):
    repositoryName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListBranchesInputRequestTypeDef(BaseModel):
    repositoryName: str
    nextToken: Optional[str] = None

class ListFileCommitHistoryRequestRequestTypeDef(BaseModel):
    repositoryName: str
    filePath: str
    commitSpecifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListPullRequestsInputRequestTypeDef(BaseModel):
    repositoryName: str
    authorArn: Optional[str] = None
    pullRequestStatus: Optional[PullRequestStatusEnumType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListRepositoriesForApprovalRuleTemplateInputRequestTypeDef(BaseModel):
    approvalRuleTemplateName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListRepositoriesInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    sortBy: Optional[SortByEnumType] = None
    order: Optional[OrderEnumType] = None

class RepositoryNameIdPairTypeDef(BaseModel):
    repositoryName: Optional[str] = None
    repositoryId: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    nextToken: Optional[str] = None

class MergeBranchesByFastForwardInputRequestTypeDef(BaseModel):
    repositoryName: str
    sourceCommitSpecifier: str
    destinationCommitSpecifier: str
    targetBranch: Optional[str] = None

class MergeHunkDetailTypeDef(BaseModel):
    startLine: Optional[int] = None
    endLine: Optional[int] = None
    hunkContent: Optional[str] = None

class MergeMetadataTypeDef(BaseModel):
    isMerged: Optional[bool] = None
    mergedBy: Optional[str] = None
    mergeCommitId: Optional[str] = None
    mergeOption: Optional[MergeOptionTypeEnumType] = None

class MergePullRequestByFastForwardInputRequestTypeDef(BaseModel):
    pullRequestId: str
    repositoryName: str
    sourceCommitId: Optional[str] = None

class OverridePullRequestApprovalRulesInputRequestTypeDef(BaseModel):
    pullRequestId: str
    revisionId: str
    overrideStatus: OverrideStatusType

class PostCommentReplyInputRequestTypeDef(BaseModel):
    inReplyTo: str
    content: str
    clientRequestToken: Optional[str] = None

class PullRequestCreatedEventMetadataTypeDef(BaseModel):
    repositoryName: Optional[str] = None
    sourceCommitId: Optional[str] = None
    destinationCommitId: Optional[str] = None
    mergeBase: Optional[str] = None

class PullRequestSourceReferenceUpdatedEventMetadataTypeDef(BaseModel):
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    mergeBase: Optional[str] = None

class PullRequestStatusChangedEventMetadataTypeDef(BaseModel):
    pullRequestStatus: Optional[PullRequestStatusEnumType] = None

class PutCommentReactionInputRequestTypeDef(BaseModel):
    commentId: str
    reactionValue: str

class SourceFileSpecifierTypeDef(BaseModel):
    filePath: str
    isMove: Optional[bool] = None

class ReactionValueFormatsTypeDef(BaseModel):
    emoji: Optional[str] = None
    shortCode: Optional[str] = None
    unicode: Optional[str] = None

class RepositoryTriggerExecutionFailureTypeDef(BaseModel):
    trigger: Optional[str] = None
    failureMessage: Optional[str] = None

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateApprovalRuleTemplateContentInputRequestTypeDef(BaseModel):
    approvalRuleTemplateName: str
    newRuleContent: str
    existingRuleContentSha256: Optional[str] = None

class UpdateApprovalRuleTemplateDescriptionInputRequestTypeDef(BaseModel):
    approvalRuleTemplateName: str
    approvalRuleTemplateDescription: str

class UpdateApprovalRuleTemplateNameInputRequestTypeDef(BaseModel):
    oldApprovalRuleTemplateName: str
    newApprovalRuleTemplateName: str

class UpdateCommentInputRequestTypeDef(BaseModel):
    commentId: str
    content: str

class UpdateDefaultBranchInputRequestTypeDef(BaseModel):
    repositoryName: str
    defaultBranchName: str

class UpdatePullRequestApprovalRuleContentInputRequestTypeDef(BaseModel):
    pullRequestId: str
    approvalRuleName: str
    newRuleContent: str
    existingRuleContentSha256: Optional[str] = None

class UpdatePullRequestApprovalStateInputRequestTypeDef(BaseModel):
    pullRequestId: str
    revisionId: str
    approvalState: ApprovalStateType

class UpdatePullRequestDescriptionInputRequestTypeDef(BaseModel):
    pullRequestId: str
    description: str

class UpdatePullRequestStatusInputRequestTypeDef(BaseModel):
    pullRequestId: str
    pullRequestStatus: PullRequestStatusEnumType

class UpdatePullRequestTitleInputRequestTypeDef(BaseModel):
    pullRequestId: str
    title: str

class UpdateRepositoryDescriptionInputRequestTypeDef(BaseModel):
    repositoryName: str
    repositoryDescription: Optional[str] = None

class UpdateRepositoryEncryptionKeyInputRequestTypeDef(BaseModel):
    repositoryName: str
    kmsKeyId: str

class UpdateRepositoryNameInputRequestTypeDef(BaseModel):
    oldName: str
    newName: str

class ApprovalRuleTypeDef(BaseModel):
    approvalRuleId: Optional[str] = None
    approvalRuleName: Optional[str] = None
    approvalRuleContent: Optional[str] = None
    ruleContentSha256: Optional[str] = None
    lastModifiedDate: Optional[datetime] = None
    creationDate: Optional[datetime] = None
    lastModifiedUser: Optional[str] = None
    originApprovalRuleTemplate: Optional[OriginApprovalRuleTemplateTypeDef] = None

class BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef(BaseModel):
    associatedRepositoryNames: List[str]
    errors: List[BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApprovalRuleTemplateOutputTypeDef(BaseModel):
    approvalRuleTemplate: ApprovalRuleTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUnreferencedMergeCommitOutputTypeDef(BaseModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApprovalRuleTemplateOutputTypeDef(BaseModel):
    approvalRuleTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFileOutputTypeDef(BaseModel):
    commitId: str
    blobId: str
    treeId: str
    filePath: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePullRequestApprovalRuleOutputTypeDef(BaseModel):
    approvalRuleId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRepositoryOutputTypeDef(BaseModel):
    repositoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetApprovalRuleTemplateOutputTypeDef(BaseModel):
    approvalRuleTemplate: ApprovalRuleTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBlobOutputTypeDef(BaseModel):
    content: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class GetFileOutputTypeDef(BaseModel):
    commitId: str
    blobId: str
    filePath: str
    fileMode: FileModeTypeEnumType
    fileSize: int
    fileContent: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class GetMergeCommitOutputTypeDef(BaseModel):
    sourceCommitId: str
    destinationCommitId: str
    baseCommitId: str
    mergedCommitId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMergeOptionsOutputTypeDef(BaseModel):
    mergeOptions: List[MergeOptionTypeEnumType]
    sourceCommitId: str
    destinationCommitId: str
    baseCommitId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPullRequestApprovalStatesOutputTypeDef(BaseModel):
    approvals: List[ApprovalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPullRequestOverrideStateOutputTypeDef(BaseModel):
    overridden: bool
    overrider: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApprovalRuleTemplatesOutputTypeDef(BaseModel):
    approvalRuleTemplateNames: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef(BaseModel):
    approvalRuleTemplateNames: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBranchesOutputTypeDef(BaseModel):
    branches: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPullRequestsOutputTypeDef(BaseModel):
    pullRequestIds: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositoriesForApprovalRuleTemplateOutputTypeDef(BaseModel):
    repositoryNames: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    tags: Dict[str, str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MergeBranchesByFastForwardOutputTypeDef(BaseModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class MergeBranchesBySquashOutputTypeDef(BaseModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class MergeBranchesByThreeWayOutputTypeDef(BaseModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutFileOutputTypeDef(BaseModel):
    commitId: str
    blobId: str
    treeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutRepositoryTriggersOutputTypeDef(BaseModel):
    configurationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApprovalRuleTemplateContentOutputTypeDef(BaseModel):
    approvalRuleTemplate: ApprovalRuleTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApprovalRuleTemplateDescriptionOutputTypeDef(BaseModel):
    approvalRuleTemplate: ApprovalRuleTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApprovalRuleTemplateNameOutputTypeDef(BaseModel):
    approvalRuleTemplate: ApprovalRuleTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRepositoryEncryptionKeyOutputTypeDef(BaseModel):
    repositoryId: str
    kmsKeyId: str
    originalKmsKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef(BaseModel):
    disassociatedRepositoryNames: List[str]
    errors: List[BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetRepositoriesOutputTypeDef(BaseModel):
    repositories: List[RepositoryMetadataTypeDef]
    repositoriesNotFound: List[str]
    errors: List[BatchGetRepositoriesErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRepositoryOutputTypeDef(BaseModel):
    repositoryMetadata: RepositoryMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositoryOutputTypeDef(BaseModel):
    repositoryMetadata: RepositoryMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DifferenceTypeDef(BaseModel):
    beforeBlob: Optional[BlobMetadataTypeDef] = None
    afterBlob: Optional[BlobMetadataTypeDef] = None
    changeType: Optional[ChangeTypeEnumType] = None

class PutFileInputRequestTypeDef(BaseModel):
    repositoryName: str
    branchName: str
    fileContent: BlobTypeDef
    filePath: str
    fileMode: Optional[FileModeTypeEnumType] = None
    parentCommitId: Optional[str] = None
    commitMessage: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None

class ReplaceContentEntryTypeDef(BaseModel):
    filePath: str
    replacementType: ReplacementTypeEnumType
    content: Optional[BlobTypeDef] = None
    fileMode: Optional[FileModeTypeEnumType] = None

class DeleteBranchOutputTypeDef(BaseModel):
    deletedBranch: BranchInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBranchOutputTypeDef(BaseModel):
    branch: BranchInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCommentContentOutputTypeDef(BaseModel):
    comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCommentOutputTypeDef(BaseModel):
    comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PostCommentReplyOutputTypeDef(BaseModel):
    comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCommentOutputTypeDef(BaseModel):
    comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CommentsForComparedCommitTypeDef(BaseModel):
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    beforeBlobId: Optional[str] = None
    afterBlobId: Optional[str] = None
    location: Optional[LocationTypeDef] = None
    comments: Optional[List[CommentTypeDef]] = None

class CommentsForPullRequestTypeDef(BaseModel):
    pullRequestId: Optional[str] = None
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    beforeBlobId: Optional[str] = None
    afterBlobId: Optional[str] = None
    location: Optional[LocationTypeDef] = None
    comments: Optional[List[CommentTypeDef]] = None

class PostCommentForComparedCommitInputRequestTypeDef(BaseModel):
    repositoryName: str
    afterCommitId: str
    content: str
    beforeCommitId: Optional[str] = None
    location: Optional[LocationTypeDef] = None
    clientRequestToken: Optional[str] = None

class PostCommentForComparedCommitOutputTypeDef(BaseModel):
    repositoryName: str
    beforeCommitId: str
    afterCommitId: str
    beforeBlobId: str
    afterBlobId: str
    location: LocationTypeDef
    comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PostCommentForPullRequestInputRequestTypeDef(BaseModel):
    pullRequestId: str
    repositoryName: str
    beforeCommitId: str
    afterCommitId: str
    content: str
    location: Optional[LocationTypeDef] = None
    clientRequestToken: Optional[str] = None

class PostCommentForPullRequestOutputTypeDef(BaseModel):
    repositoryName: str
    pullRequestId: str
    beforeCommitId: str
    afterCommitId: str
    beforeBlobId: str
    afterBlobId: str
    location: LocationTypeDef
    comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CommitTypeDef(BaseModel):
    commitId: Optional[str] = None
    treeId: Optional[str] = None
    parents: Optional[List[str]] = None
    message: Optional[str] = None
    author: Optional[UserInfoTypeDef] = None
    committer: Optional[UserInfoTypeDef] = None
    additionalData: Optional[str] = None

class ConflictMetadataTypeDef(BaseModel):
    filePath: Optional[str] = None
    fileSizes: Optional[FileSizesTypeDef] = None
    fileModes: Optional[FileModesTypeDef] = None
    objectTypes: Optional[ObjectTypesTypeDef] = None
    numberOfConflicts: Optional[int] = None
    isBinaryFile: Optional[IsBinaryFileTypeDef] = None
    contentConflict: Optional[bool] = None
    fileModeConflict: Optional[bool] = None
    objectTypeConflict: Optional[bool] = None
    mergeOperations: Optional[MergeOperationsTypeDef] = None

class CreateCommitOutputTypeDef(BaseModel):
    commitId: str
    treeId: str
    filesAdded: List[FileMetadataTypeDef]
    filesUpdated: List[FileMetadataTypeDef]
    filesDeleted: List[FileMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePullRequestInputRequestTypeDef(BaseModel):
    title: str
    targets: Sequence[TargetTypeDef]
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None

class DescribePullRequestEventsInputDescribePullRequestEventsPaginateTypeDef(BaseModel):
    pullRequestId: str
    pullRequestEventType: Optional[PullRequestEventTypeType] = None
    actorArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCommentsForComparedCommitInputGetCommentsForComparedCommitPaginateTypeDef(BaseModel):
    repositoryName: str
    afterCommitId: str
    beforeCommitId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCommentsForPullRequestInputGetCommentsForPullRequestPaginateTypeDef(BaseModel):
    pullRequestId: str
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDifferencesInputGetDifferencesPaginateTypeDef(BaseModel):
    repositoryName: str
    afterCommitSpecifier: str
    beforeCommitSpecifier: Optional[str] = None
    beforePath: Optional[str] = None
    afterPath: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBranchesInputListBranchesPaginateTypeDef(BaseModel):
    repositoryName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPullRequestsInputListPullRequestsPaginateTypeDef(BaseModel):
    repositoryName: str
    authorArn: Optional[str] = None
    pullRequestStatus: Optional[PullRequestStatusEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRepositoriesInputListRepositoriesPaginateTypeDef(BaseModel):
    sortBy: Optional[SortByEnumType] = None
    order: Optional[OrderEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class EvaluatePullRequestApprovalRulesOutputTypeDef(BaseModel):
    evaluation: EvaluationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFolderOutputTypeDef(BaseModel):
    commitId: str
    folderPath: str
    treeId: str
    subFolders: List[FolderTypeDef]
    files: List[FileTypeDef]
    symbolicLinks: List[SymbolicLinkTypeDef]
    subModules: List[SubModuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositoryTriggersOutputTypeDef(BaseModel):
    configurationId: str
    triggers: List[RepositoryTriggerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRepositoryTriggersInputRequestTypeDef(BaseModel):
    repositoryName: str
    triggers: Sequence[RepositoryTriggerTypeDef]

class TestRepositoryTriggersInputRequestTypeDef(BaseModel):
    repositoryName: str
    triggers: Sequence[RepositoryTriggerTypeDef]

class ListRepositoriesOutputTypeDef(BaseModel):
    repositories: List[RepositoryNameIdPairTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MergeHunkTypeDef(BaseModel):
    isConflict: Optional[bool] = None
    source: Optional[MergeHunkDetailTypeDef] = None
    destination: Optional[MergeHunkDetailTypeDef] = None
    base: Optional[MergeHunkDetailTypeDef] = None

class PullRequestMergedStateChangedEventMetadataTypeDef(BaseModel):
    repositoryName: Optional[str] = None
    destinationReference: Optional[str] = None
    mergeMetadata: Optional[MergeMetadataTypeDef] = None

class PullRequestTargetTypeDef(BaseModel):
    repositoryName: Optional[str] = None
    sourceReference: Optional[str] = None
    destinationReference: Optional[str] = None
    destinationCommit: Optional[str] = None
    sourceCommit: Optional[str] = None
    mergeBase: Optional[str] = None
    mergeMetadata: Optional[MergeMetadataTypeDef] = None

class PutFileEntryTypeDef(BaseModel):
    filePath: str
    fileMode: Optional[FileModeTypeEnumType] = None
    fileContent: Optional[BlobTypeDef] = None
    sourceFile: Optional[SourceFileSpecifierTypeDef] = None

class ReactionForCommentTypeDef(BaseModel):
    reaction: Optional[ReactionValueFormatsTypeDef] = None
    reactionUsers: Optional[List[str]] = None
    reactionsFromDeletedUsersCount: Optional[int] = None

class TestRepositoryTriggersOutputTypeDef(BaseModel):
    successfulExecutions: List[str]
    failedExecutions: List[RepositoryTriggerExecutionFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePullRequestApprovalRuleOutputTypeDef(BaseModel):
    approvalRule: ApprovalRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePullRequestApprovalRuleContentOutputTypeDef(BaseModel):
    approvalRule: ApprovalRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDifferencesOutputTypeDef(BaseModel):
    differences: List[DifferenceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConflictResolutionTypeDef(BaseModel):
    replaceContents: Optional[Sequence[ReplaceContentEntryTypeDef]] = None
    deleteFiles: Optional[Sequence[DeleteFileEntryTypeDef]] = None
    setFileModes: Optional[Sequence[SetFileModeEntryTypeDef]] = None

class GetCommentsForComparedCommitOutputTypeDef(BaseModel):
    commentsForComparedCommitData: List[CommentsForComparedCommitTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCommentsForPullRequestOutputTypeDef(BaseModel):
    commentsForPullRequestData: List[CommentsForPullRequestTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetCommitsOutputTypeDef(BaseModel):
    commits: List[CommitTypeDef]
    errors: List[BatchGetCommitsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FileVersionTypeDef(BaseModel):
    commit: Optional[CommitTypeDef] = None
    blobId: Optional[str] = None
    path: Optional[str] = None
    revisionChildren: Optional[List[str]] = None

class GetCommitOutputTypeDef(BaseModel):
    commit: CommitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMergeConflictsOutputTypeDef(BaseModel):
    mergeable: bool
    destinationCommitId: str
    sourceCommitId: str
    baseCommitId: str
    conflictMetadataList: List[ConflictMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConflictTypeDef(BaseModel):
    conflictMetadata: Optional[ConflictMetadataTypeDef] = None
    mergeHunks: Optional[List[MergeHunkTypeDef]] = None

class DescribeMergeConflictsOutputTypeDef(BaseModel):
    conflictMetadata: ConflictMetadataTypeDef
    mergeHunks: List[MergeHunkTypeDef]
    nextToken: str
    destinationCommitId: str
    sourceCommitId: str
    baseCommitId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PullRequestEventTypeDef(BaseModel):
    pullRequestId: Optional[str] = None
    eventDate: Optional[datetime] = None
    pullRequestEventType: Optional[PullRequestEventTypeType] = None
    actorArn: Optional[str] = None
    pullRequestCreatedEventMetadata: Optional[PullRequestCreatedEventMetadataTypeDef] = None
    pullRequestStatusChangedEventMetadata: Optional[       PullRequestStatusChangedEventMetadataTypeDef     ] = None
    pullRequestSourceReferenceUpdatedEventMetadata: Optional[       PullRequestSourceReferenceUpdatedEventMetadataTypeDef     ] = None
    pullRequestMergedStateChangedEventMetadata: Optional[       PullRequestMergedStateChangedEventMetadataTypeDef     ] = None
    approvalRuleEventMetadata: Optional[ApprovalRuleEventMetadataTypeDef] = None
    approvalStateChangedEventMetadata: Optional[ApprovalStateChangedEventMetadataTypeDef] = None
    approvalRuleOverriddenEventMetadata: Optional[       ApprovalRuleOverriddenEventMetadataTypeDef     ] = None

class PullRequestTypeDef(BaseModel):
    pullRequestId: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    lastActivityDate: Optional[datetime] = None
    creationDate: Optional[datetime] = None
    pullRequestStatus: Optional[PullRequestStatusEnumType] = None
    authorArn: Optional[str] = None
    pullRequestTargets: Optional[List[PullRequestTargetTypeDef]] = None
    clientRequestToken: Optional[str] = None
    revisionId: Optional[str] = None
    approvalRules: Optional[List[ApprovalRuleTypeDef]] = None

class CreateCommitInputRequestTypeDef(BaseModel):
    repositoryName: str
    branchName: str
    parentCommitId: Optional[str] = None
    authorName: Optional[str] = None
    email: Optional[str] = None
    commitMessage: Optional[str] = None
    keepEmptyFolders: Optional[bool] = None
    putFiles: Optional[Sequence[PutFileEntryTypeDef]] = None
    deleteFiles: Optional[Sequence[DeleteFileEntryTypeDef]] = None
    setFileModes: Optional[Sequence[SetFileModeEntryTypeDef]] = None

class GetCommentReactionsOutputTypeDef(BaseModel):
    reactionsForComment: List[ReactionForCommentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUnreferencedMergeCommitInputRequestTypeDef(BaseModel):
    repositoryName: str
    sourceCommitSpecifier: str
    destinationCommitSpecifier: str
    mergeOption: MergeOptionTypeEnumType
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    authorName: Optional[str] = None
    email: Optional[str] = None
    commitMessage: Optional[str] = None
    keepEmptyFolders: Optional[bool] = None
    conflictResolution: Optional[ConflictResolutionTypeDef] = None

class MergeBranchesBySquashInputRequestTypeDef(BaseModel):
    repositoryName: str
    sourceCommitSpecifier: str
    destinationCommitSpecifier: str
    targetBranch: Optional[str] = None
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    authorName: Optional[str] = None
    email: Optional[str] = None
    commitMessage: Optional[str] = None
    keepEmptyFolders: Optional[bool] = None
    conflictResolution: Optional[ConflictResolutionTypeDef] = None

class MergeBranchesByThreeWayInputRequestTypeDef(BaseModel):
    repositoryName: str
    sourceCommitSpecifier: str
    destinationCommitSpecifier: str
    targetBranch: Optional[str] = None
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    authorName: Optional[str] = None
    email: Optional[str] = None
    commitMessage: Optional[str] = None
    keepEmptyFolders: Optional[bool] = None
    conflictResolution: Optional[ConflictResolutionTypeDef] = None

class MergePullRequestBySquashInputRequestTypeDef(BaseModel):
    pullRequestId: str
    repositoryName: str
    sourceCommitId: Optional[str] = None
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    commitMessage: Optional[str] = None
    authorName: Optional[str] = None
    email: Optional[str] = None
    keepEmptyFolders: Optional[bool] = None
    conflictResolution: Optional[ConflictResolutionTypeDef] = None

class MergePullRequestByThreeWayInputRequestTypeDef(BaseModel):
    pullRequestId: str
    repositoryName: str
    sourceCommitId: Optional[str] = None
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    commitMessage: Optional[str] = None
    authorName: Optional[str] = None
    email: Optional[str] = None
    keepEmptyFolders: Optional[bool] = None
    conflictResolution: Optional[ConflictResolutionTypeDef] = None

class ListFileCommitHistoryResponseTypeDef(BaseModel):
    revisionDag: List[FileVersionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDescribeMergeConflictsOutputTypeDef(BaseModel):
    conflicts: List[ConflictTypeDef]
    nextToken: str
    errors: List[BatchDescribeMergeConflictsErrorTypeDef]
    destinationCommitId: str
    sourceCommitId: str
    baseCommitId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePullRequestEventsOutputTypeDef(BaseModel):
    pullRequestEvents: List[PullRequestEventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePullRequestOutputTypeDef(BaseModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPullRequestOutputTypeDef(BaseModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MergePullRequestByFastForwardOutputTypeDef(BaseModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MergePullRequestBySquashOutputTypeDef(BaseModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MergePullRequestByThreeWayOutputTypeDef(BaseModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePullRequestDescriptionOutputTypeDef(BaseModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePullRequestStatusOutputTypeDef(BaseModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePullRequestTitleOutputTypeDef(BaseModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

