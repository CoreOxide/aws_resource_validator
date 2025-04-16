from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
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

class ApprovalRuleEventMetadata(BaseValidatorModel):
    approvalRuleName: Optional[str] = None
    approvalRuleId: Optional[str] = None
    approvalRuleContent: Optional[str] = None


class ApprovalRuleOverriddenEventMetadata(BaseValidatorModel):
    revisionId: Optional[str] = None
    overrideStatus: Optional[OverrideStatusType] = None


class ApprovalRuleTemplate(BaseValidatorModel):
    approvalRuleTemplateId: Optional[str] = None
    approvalRuleTemplateName: Optional[str] = None
    approvalRuleTemplateDescription: Optional[str] = None
    approvalRuleTemplateContent: Optional[str] = None
    ruleContentSha256: Optional[str] = None
    lastModifiedDate: Optional[datetime] = None
    creationDate: Optional[datetime] = None
    lastModifiedUser: Optional[str] = None


class OriginApprovalRuleTemplate(BaseValidatorModel):
    approvalRuleTemplateId: Optional[str] = None
    approvalRuleTemplateName: Optional[str] = None


class ApprovalStateChangedEventMetadata(BaseValidatorModel):
    revisionId: Optional[str] = None
    approvalStatus: Optional[ApprovalStateType] = None


class Approval(BaseValidatorModel):
    userArn: Optional[str] = None
    approvalState: Optional[ApprovalStateType] = None


class AssociateApprovalRuleTemplateWithRepositoryInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    repositoryName: str


class BatchAssociateApprovalRuleTemplateWithRepositoriesError(BaseValidatorModel):
    repositoryName: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class BatchAssociateApprovalRuleTemplateWithRepositoriesInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    repositoryNames: Sequence[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDescribeMergeConflictsError(BaseValidatorModel):
    filePath: str
    exceptionName: str
    message: str


class BatchDescribeMergeConflictsInput(BaseValidatorModel):
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


class BatchDisassociateApprovalRuleTemplateFromRepositoriesError(BaseValidatorModel):
    repositoryName: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class BatchDisassociateApprovalRuleTemplateFromRepositoriesInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    repositoryNames: Sequence[str]


class BatchGetCommitsError(BaseValidatorModel):
    commitId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class BatchGetCommitsInput(BaseValidatorModel):
    commitIds: Sequence[str]
    repositoryName: str


class BatchGetRepositoriesError(BaseValidatorModel):
    repositoryId: Optional[str] = None
    repositoryName: Optional[str] = None
    errorCode: Optional[BatchGetRepositoriesErrorCodeEnumType] = None
    errorMessage: Optional[str] = None


class BatchGetRepositoriesInput(BaseValidatorModel):
    repositoryNames: Sequence[str]


class RepositoryMetadata(BaseValidatorModel):
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


class BlobMetadata(BaseValidatorModel):
    blobId: Optional[str] = None
    path: Optional[str] = None
    mode: Optional[str] = None


class BranchInfo(BaseValidatorModel):
    branchName: Optional[str] = None
    commitId: Optional[str] = None


class Comment(BaseValidatorModel):
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


class Location(BaseValidatorModel):
    filePath: Optional[str] = None
    filePosition: Optional[int] = None
    relativeFileVersion: Optional[RelativeFileVersionEnumType] = None


class UserInfo(BaseValidatorModel):
    name: Optional[str] = None
    email: Optional[str] = None
    date: Optional[str] = None


class FileModes(BaseValidatorModel):
    source: Optional[FileModeTypeEnumType] = None
    destination: Optional[FileModeTypeEnumType] = None
    base: Optional[FileModeTypeEnumType] = None


class FileSizes(BaseValidatorModel):
    source: Optional[int] = None
    destination: Optional[int] = None
    base: Optional[int] = None


class IsBinaryFile(BaseValidatorModel):
    source: Optional[bool] = None
    destination: Optional[bool] = None
    base: Optional[bool] = None


class MergeOperations(BaseValidatorModel):
    source: Optional[ChangeTypeEnumType] = None
    destination: Optional[ChangeTypeEnumType] = None


class ObjectTypes(BaseValidatorModel):
    source: Optional[ObjectTypeEnumType] = None
    destination: Optional[ObjectTypeEnumType] = None
    base: Optional[ObjectTypeEnumType] = None


class DeleteFileEntry(BaseValidatorModel):
    filePath: str


class SetFileModeEntry(BaseValidatorModel):
    filePath: str
    fileMode: FileModeTypeEnumType


class CreateApprovalRuleTemplateInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    approvalRuleTemplateContent: str
    approvalRuleTemplateDescription: Optional[str] = None


class CreateBranchInput(BaseValidatorModel):
    repositoryName: str
    branchName: str
    commitId: str


class FileMetadata(BaseValidatorModel):
    absolutePath: Optional[str] = None
    blobId: Optional[str] = None
    fileMode: Optional[FileModeTypeEnumType] = None


class CreatePullRequestApprovalRuleInput(BaseValidatorModel):
    pullRequestId: str
    approvalRuleName: str
    approvalRuleContent: str


class Target(BaseValidatorModel):
    repositoryName: str
    sourceReference: str
    destinationReference: Optional[str] = None


class CreateRepositoryInput(BaseValidatorModel):
    repositoryName: str
    repositoryDescription: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    kmsKeyId: Optional[str] = None


class DeleteApprovalRuleTemplateInput(BaseValidatorModel):
    approvalRuleTemplateName: str


class DeleteBranchInput(BaseValidatorModel):
    repositoryName: str
    branchName: str


class DeleteCommentContentInput(BaseValidatorModel):
    commentId: str


class DeleteFileInput(BaseValidatorModel):
    repositoryName: str
    branchName: str
    filePath: str
    parentCommitId: str
    keepEmptyFolders: Optional[bool] = None
    commitMessage: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None


class DeletePullRequestApprovalRuleInput(BaseValidatorModel):
    pullRequestId: str
    approvalRuleName: str


class DeleteRepositoryInput(BaseValidatorModel):
    repositoryName: str


class DescribeMergeConflictsInput(BaseValidatorModel):
    repositoryName: str
    destinationCommitSpecifier: str
    sourceCommitSpecifier: str
    mergeOption: MergeOptionTypeEnumType
    filePath: str
    maxMergeHunks: Optional[int] = None
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    nextToken: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribePullRequestEventsInput(BaseValidatorModel):
    pullRequestId: str
    pullRequestEventType: Optional[PullRequestEventTypeType] = None
    actorArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DisassociateApprovalRuleTemplateFromRepositoryInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    repositoryName: str


class EvaluatePullRequestApprovalRulesInput(BaseValidatorModel):
    pullRequestId: str
    revisionId: str


class Evaluation(BaseValidatorModel):
    approved: Optional[bool] = None
    overridden: Optional[bool] = None
    approvalRulesSatisfied: Optional[List[str]] = None
    approvalRulesNotSatisfied: Optional[List[str]] = None


class File(BaseValidatorModel):
    blobId: Optional[str] = None
    absolutePath: Optional[str] = None
    relativePath: Optional[str] = None
    fileMode: Optional[FileModeTypeEnumType] = None


class Folder(BaseValidatorModel):
    treeId: Optional[str] = None
    absolutePath: Optional[str] = None
    relativePath: Optional[str] = None


class GetApprovalRuleTemplateInput(BaseValidatorModel):
    approvalRuleTemplateName: str


class GetBlobInput(BaseValidatorModel):
    repositoryName: str
    blobId: str


class GetBranchInput(BaseValidatorModel):
    repositoryName: Optional[str] = None
    branchName: Optional[str] = None


class GetCommentInput(BaseValidatorModel):
    commentId: str


class GetCommentReactionsInput(BaseValidatorModel):
    commentId: str
    reactionUserArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetCommentsForComparedCommitInput(BaseValidatorModel):
    repositoryName: str
    afterCommitId: str
    beforeCommitId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetCommentsForPullRequestInput(BaseValidatorModel):
    pullRequestId: str
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetCommitInput(BaseValidatorModel):
    repositoryName: str
    commitId: str


class GetDifferencesInput(BaseValidatorModel):
    repositoryName: str
    afterCommitSpecifier: str
    beforeCommitSpecifier: Optional[str] = None
    beforePath: Optional[str] = None
    afterPath: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetFileInput(BaseValidatorModel):
    repositoryName: str
    filePath: str
    commitSpecifier: Optional[str] = None


class GetFolderInput(BaseValidatorModel):
    repositoryName: str
    folderPath: str
    commitSpecifier: Optional[str] = None


class SubModule(BaseValidatorModel):
    commitId: Optional[str] = None
    absolutePath: Optional[str] = None
    relativePath: Optional[str] = None


class SymbolicLink(BaseValidatorModel):
    blobId: Optional[str] = None
    absolutePath: Optional[str] = None
    relativePath: Optional[str] = None
    fileMode: Optional[FileModeTypeEnumType] = None


class GetMergeCommitInput(BaseValidatorModel):
    repositoryName: str
    sourceCommitSpecifier: str
    destinationCommitSpecifier: str
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None


class GetMergeConflictsInput(BaseValidatorModel):
    repositoryName: str
    destinationCommitSpecifier: str
    sourceCommitSpecifier: str
    mergeOption: MergeOptionTypeEnumType
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    maxConflictFiles: Optional[int] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    nextToken: Optional[str] = None


class GetMergeOptionsInput(BaseValidatorModel):
    repositoryName: str
    sourceCommitSpecifier: str
    destinationCommitSpecifier: str
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None


class GetPullRequestApprovalStatesInput(BaseValidatorModel):
    pullRequestId: str
    revisionId: str


class GetPullRequestInput(BaseValidatorModel):
    pullRequestId: str


class GetPullRequestOverrideStateInput(BaseValidatorModel):
    pullRequestId: str
    revisionId: str


class GetRepositoryInput(BaseValidatorModel):
    repositoryName: str


class GetRepositoryTriggersInput(BaseValidatorModel):
    repositoryName: str


class RepositoryTriggerOutput(BaseValidatorModel):
    name: str
    destinationArn: str
    events: List[RepositoryTriggerEventEnumType]
    customData: Optional[str] = None
    branches: Optional[List[str]] = None


class ListApprovalRuleTemplatesInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssociatedApprovalRuleTemplatesForRepositoryInput(BaseValidatorModel):
    repositoryName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBranchesInput(BaseValidatorModel):
    repositoryName: str
    nextToken: Optional[str] = None


class ListFileCommitHistoryRequest(BaseValidatorModel):
    repositoryName: str
    filePath: str
    commitSpecifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListPullRequestsInput(BaseValidatorModel):
    repositoryName: str
    authorArn: Optional[str] = None
    pullRequestStatus: Optional[PullRequestStatusEnumType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListRepositoriesForApprovalRuleTemplateInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListRepositoriesInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    sortBy: Optional[SortByEnumType] = None
    order: Optional[OrderEnumType] = None


class RepositoryNameIdPair(BaseValidatorModel):
    repositoryName: Optional[str] = None
    repositoryId: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None


class MergeBranchesByFastForwardInput(BaseValidatorModel):
    repositoryName: str
    sourceCommitSpecifier: str
    destinationCommitSpecifier: str
    targetBranch: Optional[str] = None


class MergeHunkDetail(BaseValidatorModel):
    startLine: Optional[int] = None
    endLine: Optional[int] = None
    hunkContent: Optional[str] = None


class MergeMetadata(BaseValidatorModel):
    isMerged: Optional[bool] = None
    mergedBy: Optional[str] = None
    mergeCommitId: Optional[str] = None
    mergeOption: Optional[MergeOptionTypeEnumType] = None


class MergePullRequestByFastForwardInput(BaseValidatorModel):
    pullRequestId: str
    repositoryName: str
    sourceCommitId: Optional[str] = None


class OverridePullRequestApprovalRulesInput(BaseValidatorModel):
    pullRequestId: str
    revisionId: str
    overrideStatus: OverrideStatusType


class PostCommentReplyInput(BaseValidatorModel):
    inReplyTo: str
    content: str
    clientRequestToken: Optional[str] = None


class PullRequestCreatedEventMetadata(BaseValidatorModel):
    repositoryName: Optional[str] = None
    sourceCommitId: Optional[str] = None
    destinationCommitId: Optional[str] = None
    mergeBase: Optional[str] = None


class PullRequestSourceReferenceUpdatedEventMetadata(BaseValidatorModel):
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    mergeBase: Optional[str] = None


class PullRequestStatusChangedEventMetadata(BaseValidatorModel):
    pullRequestStatus: Optional[PullRequestStatusEnumType] = None


class PutCommentReactionInput(BaseValidatorModel):
    commentId: str
    reactionValue: str


class SourceFileSpecifier(BaseValidatorModel):
    filePath: str
    isMove: Optional[bool] = None


class ReactionValueFormats(BaseValidatorModel):
    emoji: Optional[str] = None
    shortCode: Optional[str] = None
    unicode: Optional[str] = None


class RepositoryTriggerExecutionFailure(BaseValidatorModel):
    trigger: Optional[str] = None
    failureMessage: Optional[str] = None


class RepositoryTrigger(BaseValidatorModel):
    name: str
    destinationArn: str
    events: Sequence[RepositoryTriggerEventEnumType]
    customData: Optional[str] = None
    branches: Optional[Sequence[str]] = None


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateApprovalRuleTemplateContentInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    newRuleContent: str
    existingRuleContentSha256: Optional[str] = None


class UpdateApprovalRuleTemplateDescriptionInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    approvalRuleTemplateDescription: str


class UpdateApprovalRuleTemplateNameInput(BaseValidatorModel):
    oldApprovalRuleTemplateName: str
    newApprovalRuleTemplateName: str


class UpdateCommentInput(BaseValidatorModel):
    commentId: str
    content: str


class UpdateDefaultBranchInput(BaseValidatorModel):
    repositoryName: str
    defaultBranchName: str


class UpdatePullRequestApprovalRuleContentInput(BaseValidatorModel):
    pullRequestId: str
    approvalRuleName: str
    newRuleContent: str
    existingRuleContentSha256: Optional[str] = None


class UpdatePullRequestApprovalStateInput(BaseValidatorModel):
    pullRequestId: str
    revisionId: str
    approvalState: ApprovalStateType


class UpdatePullRequestDescriptionInput(BaseValidatorModel):
    pullRequestId: str
    description: str


class UpdatePullRequestStatusInput(BaseValidatorModel):
    pullRequestId: str
    pullRequestStatus: PullRequestStatusEnumType


class UpdatePullRequestTitleInput(BaseValidatorModel):
    pullRequestId: str
    title: str


class UpdateRepositoryDescriptionInput(BaseValidatorModel):
    repositoryName: str
    repositoryDescription: Optional[str] = None


class UpdateRepositoryEncryptionKeyInput(BaseValidatorModel):
    repositoryName: str
    kmsKeyId: str


class UpdateRepositoryNameInput(BaseValidatorModel):
    oldName: str
    newName: str


class ApprovalRule(BaseValidatorModel):
    approvalRuleId: Optional[str] = None
    approvalRuleName: Optional[str] = None
    approvalRuleContent: Optional[str] = None
    ruleContentSha256: Optional[str] = None
    lastModifiedDate: Optional[datetime] = None
    creationDate: Optional[datetime] = None
    lastModifiedUser: Optional[str] = None
    originApprovalRuleTemplate: Optional[OriginApprovalRuleTemplate] = None


class BatchAssociateApprovalRuleTemplateWithRepositoriesOutput(BaseValidatorModel):
    associatedRepositoryNames: List[str]
    errors: List[BatchAssociateApprovalRuleTemplateWithRepositoriesError]
    ResponseMetadata: ResponseMetadata


class CreateApprovalRuleTemplateOutput(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplate
    ResponseMetadata: ResponseMetadata


class CreateUnreferencedMergeCommitOutput(BaseValidatorModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadata


class DeleteApprovalRuleTemplateOutput(BaseValidatorModel):
    approvalRuleTemplateId: str
    ResponseMetadata: ResponseMetadata


class DeleteFileOutput(BaseValidatorModel):
    commitId: str
    blobId: str
    treeId: str
    filePath: str
    ResponseMetadata: ResponseMetadata


class DeletePullRequestApprovalRuleOutput(BaseValidatorModel):
    approvalRuleId: str
    ResponseMetadata: ResponseMetadata


class DeleteRepositoryOutput(BaseValidatorModel):
    repositoryId: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetApprovalRuleTemplateOutput(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplate
    ResponseMetadata: ResponseMetadata


class GetBlobOutput(BaseValidatorModel):
    content: bytes
    ResponseMetadata: ResponseMetadata


class GetFileOutput(BaseValidatorModel):
    commitId: str
    blobId: str
    filePath: str
    fileMode: FileModeTypeEnumType
    fileSize: int
    fileContent: bytes
    ResponseMetadata: ResponseMetadata


class GetMergeCommitOutput(BaseValidatorModel):
    sourceCommitId: str
    destinationCommitId: str
    baseCommitId: str
    mergedCommitId: str
    ResponseMetadata: ResponseMetadata


class GetMergeOptionsOutput(BaseValidatorModel):
    mergeOptions: List[MergeOptionTypeEnumType]
    sourceCommitId: str
    destinationCommitId: str
    baseCommitId: str
    ResponseMetadata: ResponseMetadata


class GetPullRequestApprovalStatesOutput(BaseValidatorModel):
    approvals: List[Approval]
    ResponseMetadata: ResponseMetadata


class GetPullRequestOverrideStateOutput(BaseValidatorModel):
    overridden: bool
    overrider: str
    ResponseMetadata: ResponseMetadata


class ListApprovalRuleTemplatesOutput(BaseValidatorModel):
    approvalRuleTemplateNames: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAssociatedApprovalRuleTemplatesForRepositoryOutput(BaseValidatorModel):
    approvalRuleTemplateNames: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListBranchesOutput(BaseValidatorModel):
    branches: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListPullRequestsOutput(BaseValidatorModel):
    pullRequestIds: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListRepositoriesForApprovalRuleTemplateOutput(BaseValidatorModel):
    repositoryNames: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MergeBranchesByFastForwardOutput(BaseValidatorModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadata


class MergeBranchesBySquashOutput(BaseValidatorModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadata


class MergeBranchesByThreeWayOutput(BaseValidatorModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadata


class PutFileOutput(BaseValidatorModel):
    commitId: str
    blobId: str
    treeId: str
    ResponseMetadata: ResponseMetadata


class PutRepositoryTriggersOutput(BaseValidatorModel):
    configurationId: str
    ResponseMetadata: ResponseMetadata


class UpdateApprovalRuleTemplateContentOutput(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplate
    ResponseMetadata: ResponseMetadata


class UpdateApprovalRuleTemplateDescriptionOutput(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplate
    ResponseMetadata: ResponseMetadata


class UpdateApprovalRuleTemplateNameOutput(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplate
    ResponseMetadata: ResponseMetadata


class UpdateRepositoryEncryptionKeyOutput(BaseValidatorModel):
    repositoryId: str
    kmsKeyId: str
    originalKmsKeyId: str
    ResponseMetadata: ResponseMetadata


class BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput(BaseValidatorModel):
    disassociatedRepositoryNames: List[str]
    errors: List[BatchDisassociateApprovalRuleTemplateFromRepositoriesError]
    ResponseMetadata: ResponseMetadata


class BatchGetRepositoriesOutput(BaseValidatorModel):
    repositories: List[RepositoryMetadata]
    repositoriesNotFound: List[str]
    errors: List[BatchGetRepositoriesError]
    ResponseMetadata: ResponseMetadata


class CreateRepositoryOutput(BaseValidatorModel):
    repositoryMetadata: RepositoryMetadata
    ResponseMetadata: ResponseMetadata


class GetRepositoryOutput(BaseValidatorModel):
    repositoryMetadata: RepositoryMetadata
    ResponseMetadata: ResponseMetadata


class Difference(BaseValidatorModel):
    beforeBlob: Optional[BlobMetadata] = None
    afterBlob: Optional[BlobMetadata] = None
    changeType: Optional[ChangeTypeEnumType] = None


class Blob(BaseValidatorModel):
    pass


class PutFileInput(BaseValidatorModel):
    repositoryName: str
    branchName: str
    fileContent: Blob
    filePath: str
    fileMode: Optional[FileModeTypeEnumType] = None
    parentCommitId: Optional[str] = None
    commitMessage: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None


class ReplaceContentEntry(BaseValidatorModel):
    filePath: str
    replacementType: ReplacementTypeEnumType
    content: Optional[Blob] = None
    fileMode: Optional[FileModeTypeEnumType] = None


class DeleteBranchOutput(BaseValidatorModel):
    deletedBranch: BranchInfo
    ResponseMetadata: ResponseMetadata


class GetBranchOutput(BaseValidatorModel):
    branch: BranchInfo
    ResponseMetadata: ResponseMetadata


class DeleteCommentContentOutput(BaseValidatorModel):
    comment: Comment
    ResponseMetadata: ResponseMetadata


class GetCommentOutput(BaseValidatorModel):
    comment: Comment
    ResponseMetadata: ResponseMetadata


class PostCommentReplyOutput(BaseValidatorModel):
    comment: Comment
    ResponseMetadata: ResponseMetadata


class UpdateCommentOutput(BaseValidatorModel):
    comment: Comment
    ResponseMetadata: ResponseMetadata


class CommentsForComparedCommit(BaseValidatorModel):
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    beforeBlobId: Optional[str] = None
    afterBlobId: Optional[str] = None
    location: Optional[Location] = None
    comments: Optional[List[Comment]] = None


class CommentsForPullRequest(BaseValidatorModel):
    pullRequestId: Optional[str] = None
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    beforeBlobId: Optional[str] = None
    afterBlobId: Optional[str] = None
    location: Optional[Location] = None
    comments: Optional[List[Comment]] = None


class PostCommentForComparedCommitInput(BaseValidatorModel):
    repositoryName: str
    afterCommitId: str
    content: str
    beforeCommitId: Optional[str] = None
    location: Optional[Location] = None
    clientRequestToken: Optional[str] = None


class PostCommentForComparedCommitOutput(BaseValidatorModel):
    repositoryName: str
    beforeCommitId: str
    afterCommitId: str
    beforeBlobId: str
    afterBlobId: str
    location: Location
    comment: Comment
    ResponseMetadata: ResponseMetadata


class PostCommentForPullRequestInput(BaseValidatorModel):
    pullRequestId: str
    repositoryName: str
    beforeCommitId: str
    afterCommitId: str
    content: str
    location: Optional[Location] = None
    clientRequestToken: Optional[str] = None


class PostCommentForPullRequestOutput(BaseValidatorModel):
    repositoryName: str
    pullRequestId: str
    beforeCommitId: str
    afterCommitId: str
    beforeBlobId: str
    afterBlobId: str
    location: Location
    comment: Comment
    ResponseMetadata: ResponseMetadata


class Commit(BaseValidatorModel):
    commitId: Optional[str] = None
    treeId: Optional[str] = None
    parents: Optional[List[str]] = None
    message: Optional[str] = None
    author: Optional[UserInfo] = None
    committer: Optional[UserInfo] = None
    additionalData: Optional[str] = None


class ConflictMetadata(BaseValidatorModel):
    filePath: Optional[str] = None
    fileSizes: Optional[FileSizes] = None
    fileModes: Optional[FileModes] = None
    objectTypes: Optional[ObjectTypes] = None
    numberOfConflicts: Optional[int] = None
    isBinaryFile: Optional[IsBinaryFile] = None
    contentConflict: Optional[bool] = None
    fileModeConflict: Optional[bool] = None
    objectTypeConflict: Optional[bool] = None
    mergeOperations: Optional[MergeOperations] = None


class CreateCommitOutput(BaseValidatorModel):
    commitId: str
    treeId: str
    filesAdded: List[FileMetadata]
    filesUpdated: List[FileMetadata]
    filesDeleted: List[FileMetadata]
    ResponseMetadata: ResponseMetadata


class CreatePullRequestInput(BaseValidatorModel):
    title: str
    targets: Sequence[Target]
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None


class DescribePullRequestEventsInputPaginate(BaseValidatorModel):
    pullRequestId: str
    pullRequestEventType: Optional[PullRequestEventTypeType] = None
    actorArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetCommentsForComparedCommitInputPaginate(BaseValidatorModel):
    repositoryName: str
    afterCommitId: str
    beforeCommitId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetCommentsForPullRequestInputPaginate(BaseValidatorModel):
    pullRequestId: str
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetDifferencesInputPaginate(BaseValidatorModel):
    repositoryName: str
    afterCommitSpecifier: str
    beforeCommitSpecifier: Optional[str] = None
    beforePath: Optional[str] = None
    afterPath: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBranchesInputPaginate(BaseValidatorModel):
    repositoryName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPullRequestsInputPaginate(BaseValidatorModel):
    repositoryName: str
    authorArn: Optional[str] = None
    pullRequestStatus: Optional[PullRequestStatusEnumType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRepositoriesInputPaginate(BaseValidatorModel):
    sortBy: Optional[SortByEnumType] = None
    order: Optional[OrderEnumType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class EvaluatePullRequestApprovalRulesOutput(BaseValidatorModel):
    evaluation: Evaluation
    ResponseMetadata: ResponseMetadata


class GetFolderOutput(BaseValidatorModel):
    commitId: str
    folderPath: str
    treeId: str
    subFolders: List[Folder]
    files: List[File]
    symbolicLinks: List[SymbolicLink]
    subModules: List[SubModule]
    ResponseMetadata: ResponseMetadata


class GetRepositoryTriggersOutput(BaseValidatorModel):
    configurationId: str
    triggers: List[RepositoryTriggerOutput]
    ResponseMetadata: ResponseMetadata


class ListRepositoriesOutput(BaseValidatorModel):
    repositories: List[RepositoryNameIdPair]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MergeHunk(BaseValidatorModel):
    isConflict: Optional[bool] = None
    source: Optional[MergeHunkDetail] = None
    destination: Optional[MergeHunkDetail] = None
    base: Optional[MergeHunkDetail] = None


class PullRequestMergedStateChangedEventMetadata(BaseValidatorModel):
    repositoryName: Optional[str] = None
    destinationReference: Optional[str] = None
    mergeMetadata: Optional[MergeMetadata] = None


class PullRequestTarget(BaseValidatorModel):
    repositoryName: Optional[str] = None
    sourceReference: Optional[str] = None
    destinationReference: Optional[str] = None
    destinationCommit: Optional[str] = None
    sourceCommit: Optional[str] = None
    mergeBase: Optional[str] = None
    mergeMetadata: Optional[MergeMetadata] = None


class PutFileEntry(BaseValidatorModel):
    filePath: str
    fileMode: Optional[FileModeTypeEnumType] = None
    fileContent: Optional[Blob] = None
    sourceFile: Optional[SourceFileSpecifier] = None


class ReactionForComment(BaseValidatorModel):
    reaction: Optional[ReactionValueFormats] = None
    reactionUsers: Optional[List[str]] = None
    reactionsFromDeletedUsersCount: Optional[int] = None


class TestRepositoryTriggersOutput(BaseValidatorModel):
    successfulExecutions: List[str]
    failedExecutions: List[RepositoryTriggerExecutionFailure]
    ResponseMetadata: ResponseMetadata


class CreatePullRequestApprovalRuleOutput(BaseValidatorModel):
    approvalRule: ApprovalRule
    ResponseMetadata: ResponseMetadata


class UpdatePullRequestApprovalRuleContentOutput(BaseValidatorModel):
    approvalRule: ApprovalRule
    ResponseMetadata: ResponseMetadata


class GetDifferencesOutput(BaseValidatorModel):
    differences: List[Difference]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ConflictResolution(BaseValidatorModel):
    replaceContents: Optional[Sequence[ReplaceContentEntry]] = None
    deleteFiles: Optional[Sequence[DeleteFileEntry]] = None
    setFileModes: Optional[Sequence[SetFileModeEntry]] = None


class GetCommentsForComparedCommitOutput(BaseValidatorModel):
    commentsForComparedCommitData: List[CommentsForComparedCommit]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetCommentsForPullRequestOutput(BaseValidatorModel):
    commentsForPullRequestData: List[CommentsForPullRequest]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchGetCommitsOutput(BaseValidatorModel):
    commits: List[Commit]
    errors: List[BatchGetCommitsError]
    ResponseMetadata: ResponseMetadata


class FileVersion(BaseValidatorModel):
    commit: Optional[Commit] = None
    blobId: Optional[str] = None
    path: Optional[str] = None
    revisionChildren: Optional[List[str]] = None


class GetCommitOutput(BaseValidatorModel):
    commit: Commit
    ResponseMetadata: ResponseMetadata


class GetMergeConflictsOutput(BaseValidatorModel):
    mergeable: bool
    destinationCommitId: str
    sourceCommitId: str
    baseCommitId: str
    conflictMetadataList: List[ConflictMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Conflict(BaseValidatorModel):
    conflictMetadata: Optional[ConflictMetadata] = None
    mergeHunks: Optional[List[MergeHunk]] = None


class DescribeMergeConflictsOutput(BaseValidatorModel):
    conflictMetadata: ConflictMetadata
    mergeHunks: List[MergeHunk]
    destinationCommitId: str
    sourceCommitId: str
    baseCommitId: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PullRequestEvent(BaseValidatorModel):
    pullRequestId: Optional[str] = None
    eventDate: Optional[datetime] = None
    pullRequestEventType: Optional[PullRequestEventTypeType] = None
    actorArn: Optional[str] = None
    pullRequestCreatedEventMetadata: Optional[PullRequestCreatedEventMetadata] = None
    pullRequestStatusChangedEventMetadata: Optional[PullRequestStatusChangedEventMetadata] = None
    pullRequestSourceReferenceUpdatedEventMetadata: Optional[ PullRequestSourceReferenceUpdatedEventMetadata ] = None
    pullRequestMergedStateChangedEventMetadata: Optional[ PullRequestMergedStateChangedEventMetadata ] = None
    approvalRuleEventMetadata: Optional[ApprovalRuleEventMetadata] = None
    approvalStateChangedEventMetadata: Optional[ApprovalStateChangedEventMetadata] = None
    approvalRuleOverriddenEventMetadata: Optional[ApprovalRuleOverriddenEventMetadata] = None


class PullRequest(BaseValidatorModel):
    pullRequestId: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    lastActivityDate: Optional[datetime] = None
    creationDate: Optional[datetime] = None
    pullRequestStatus: Optional[PullRequestStatusEnumType] = None
    authorArn: Optional[str] = None
    pullRequestTargets: Optional[List[PullRequestTarget]] = None
    clientRequestToken: Optional[str] = None
    revisionId: Optional[str] = None
    approvalRules: Optional[List[ApprovalRule]] = None


class CreateCommitInput(BaseValidatorModel):
    repositoryName: str
    branchName: str
    parentCommitId: Optional[str] = None
    authorName: Optional[str] = None
    email: Optional[str] = None
    commitMessage: Optional[str] = None
    keepEmptyFolders: Optional[bool] = None
    putFiles: Optional[Sequence[PutFileEntry]] = None
    deleteFiles: Optional[Sequence[DeleteFileEntry]] = None
    setFileModes: Optional[Sequence[SetFileModeEntry]] = None


class GetCommentReactionsOutput(BaseValidatorModel):
    reactionsForComment: List[ReactionForComment]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RepositoryTriggerUnion(BaseValidatorModel):
    pass


class PutRepositoryTriggersInput(BaseValidatorModel):
    repositoryName: str
    triggers: Sequence[RepositoryTriggerUnion]


class TestRepositoryTriggersInput(BaseValidatorModel):
    repositoryName: str
    triggers: Sequence[RepositoryTriggerUnion]


class CreateUnreferencedMergeCommitInput(BaseValidatorModel):
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
    conflictResolution: Optional[ConflictResolution] = None


class MergeBranchesBySquashInput(BaseValidatorModel):
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
    conflictResolution: Optional[ConflictResolution] = None


class MergeBranchesByThreeWayInput(BaseValidatorModel):
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
    conflictResolution: Optional[ConflictResolution] = None


class MergePullRequestBySquashInput(BaseValidatorModel):
    pullRequestId: str
    repositoryName: str
    sourceCommitId: Optional[str] = None
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    commitMessage: Optional[str] = None
    authorName: Optional[str] = None
    email: Optional[str] = None
    keepEmptyFolders: Optional[bool] = None
    conflictResolution: Optional[ConflictResolution] = None


class MergePullRequestByThreeWayInput(BaseValidatorModel):
    pullRequestId: str
    repositoryName: str
    sourceCommitId: Optional[str] = None
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    commitMessage: Optional[str] = None
    authorName: Optional[str] = None
    email: Optional[str] = None
    keepEmptyFolders: Optional[bool] = None
    conflictResolution: Optional[ConflictResolution] = None


class ListFileCommitHistoryResponse(BaseValidatorModel):
    revisionDag: List[FileVersion]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchDescribeMergeConflictsOutput(BaseValidatorModel):
    conflicts: List[Conflict]
    errors: List[BatchDescribeMergeConflictsError]
    destinationCommitId: str
    sourceCommitId: str
    baseCommitId: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribePullRequestEventsOutput(BaseValidatorModel):
    pullRequestEvents: List[PullRequestEvent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreatePullRequestOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


class GetPullRequestOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


class MergePullRequestByFastForwardOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


class MergePullRequestBySquashOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


class MergePullRequestByThreeWayOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


class UpdatePullRequestDescriptionOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


class UpdatePullRequestStatusOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


class UpdatePullRequestTitleOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


