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

class ApprovalRuleEventMetadataTypeDef(BaseValidatorModel):
    approvalRuleName: Optional[str] = None
    approvalRuleId: Optional[str] = None
    approvalRuleContent: Optional[str] = None


class ApprovalRuleOverriddenEventMetadataTypeDef(BaseValidatorModel):
    revisionId: Optional[str] = None
    overrideStatus: Optional[OverrideStatusType] = None


class ApprovalRuleTemplateTypeDef(BaseValidatorModel):
    approvalRuleTemplateId: Optional[str] = None
    approvalRuleTemplateName: Optional[str] = None
    approvalRuleTemplateDescription: Optional[str] = None
    approvalRuleTemplateContent: Optional[str] = None
    ruleContentSha256: Optional[str] = None
    lastModifiedDate: Optional[datetime] = None
    creationDate: Optional[datetime] = None
    lastModifiedUser: Optional[str] = None


class OriginApprovalRuleTemplateTypeDef(BaseValidatorModel):
    approvalRuleTemplateId: Optional[str] = None
    approvalRuleTemplateName: Optional[str] = None


class ApprovalStateChangedEventMetadataTypeDef(BaseValidatorModel):
    revisionId: Optional[str] = None
    approvalStatus: Optional[ApprovalStateType] = None


class ApprovalTypeDef(BaseValidatorModel):
    userArn: Optional[str] = None
    approvalState: Optional[ApprovalStateType] = None


class AssociateApprovalRuleTemplateWithRepositoryInputTypeDef(BaseValidatorModel):
    approvalRuleTemplateName: str
    repositoryName: str


class BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class BatchAssociateApprovalRuleTemplateWithRepositoriesInputTypeDef(BaseValidatorModel):
    approvalRuleTemplateName: str
    repositoryNames: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDescribeMergeConflictsErrorTypeDef(BaseValidatorModel):
    filePath: str
    exceptionName: str
    message: str


class BatchDescribeMergeConflictsInputTypeDef(BaseValidatorModel):
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


class BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class BatchDisassociateApprovalRuleTemplateFromRepositoriesInputTypeDef(BaseValidatorModel):
    approvalRuleTemplateName: str
    repositoryNames: Sequence[str]


class BatchGetCommitsErrorTypeDef(BaseValidatorModel):
    commitId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


class BatchGetCommitsInputTypeDef(BaseValidatorModel):
    commitIds: Sequence[str]
    repositoryName: str


class BatchGetRepositoriesErrorTypeDef(BaseValidatorModel):
    repositoryId: Optional[str] = None
    repositoryName: Optional[str] = None
    errorCode: Optional[BatchGetRepositoriesErrorCodeEnumType] = None
    errorMessage: Optional[str] = None


class BatchGetRepositoriesInputTypeDef(BaseValidatorModel):
    repositoryNames: Sequence[str]


class RepositoryMetadataTypeDef(BaseValidatorModel):
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


class BlobMetadataTypeDef(BaseValidatorModel):
    blobId: Optional[str] = None
    path: Optional[str] = None
    mode: Optional[str] = None


class BranchInfoTypeDef(BaseValidatorModel):
    branchName: Optional[str] = None
    commitId: Optional[str] = None


class CommentTypeDef(BaseValidatorModel):
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


class LocationTypeDef(BaseValidatorModel):
    filePath: Optional[str] = None
    filePosition: Optional[int] = None
    relativeFileVersion: Optional[RelativeFileVersionEnumType] = None


class UserInfoTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    email: Optional[str] = None
    date: Optional[str] = None


class FileModesTypeDef(BaseValidatorModel):
    source: Optional[FileModeTypeEnumType] = None
    destination: Optional[FileModeTypeEnumType] = None
    base: Optional[FileModeTypeEnumType] = None


class FileSizesTypeDef(BaseValidatorModel):
    source: Optional[int] = None
    destination: Optional[int] = None
    base: Optional[int] = None


class IsBinaryFileTypeDef(BaseValidatorModel):
    source: Optional[bool] = None
    destination: Optional[bool] = None
    base: Optional[bool] = None


class MergeOperationsTypeDef(BaseValidatorModel):
    source: Optional[ChangeTypeEnumType] = None
    destination: Optional[ChangeTypeEnumType] = None


class ObjectTypesTypeDef(BaseValidatorModel):
    source: Optional[ObjectTypeEnumType] = None
    destination: Optional[ObjectTypeEnumType] = None
    base: Optional[ObjectTypeEnumType] = None


class DeleteFileEntryTypeDef(BaseValidatorModel):
    filePath: str


class SetFileModeEntryTypeDef(BaseValidatorModel):
    filePath: str
    fileMode: FileModeTypeEnumType


class CreateApprovalRuleTemplateInputTypeDef(BaseValidatorModel):
    approvalRuleTemplateName: str
    approvalRuleTemplateContent: str
    approvalRuleTemplateDescription: Optional[str] = None


class CreateBranchInputTypeDef(BaseValidatorModel):
    repositoryName: str
    branchName: str
    commitId: str


class FileMetadataTypeDef(BaseValidatorModel):
    absolutePath: Optional[str] = None
    blobId: Optional[str] = None
    fileMode: Optional[FileModeTypeEnumType] = None


class CreatePullRequestApprovalRuleInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    approvalRuleName: str
    approvalRuleContent: str


class TargetTypeDef(BaseValidatorModel):
    repositoryName: str
    sourceReference: str
    destinationReference: Optional[str] = None


class CreateRepositoryInputTypeDef(BaseValidatorModel):
    repositoryName: str
    repositoryDescription: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    kmsKeyId: Optional[str] = None


class DeleteApprovalRuleTemplateInputTypeDef(BaseValidatorModel):
    approvalRuleTemplateName: str


class DeleteBranchInputTypeDef(BaseValidatorModel):
    repositoryName: str
    branchName: str


class DeleteCommentContentInputTypeDef(BaseValidatorModel):
    commentId: str


class DeleteFileInputTypeDef(BaseValidatorModel):
    repositoryName: str
    branchName: str
    filePath: str
    parentCommitId: str
    keepEmptyFolders: Optional[bool] = None
    commitMessage: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None


class DeletePullRequestApprovalRuleInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    approvalRuleName: str


class DeleteRepositoryInputTypeDef(BaseValidatorModel):
    repositoryName: str


class DescribeMergeConflictsInputTypeDef(BaseValidatorModel):
    repositoryName: str
    destinationCommitSpecifier: str
    sourceCommitSpecifier: str
    mergeOption: MergeOptionTypeEnumType
    filePath: str
    maxMergeHunks: Optional[int] = None
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    nextToken: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribePullRequestEventsInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    pullRequestEventType: Optional[PullRequestEventTypeType] = None
    actorArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DisassociateApprovalRuleTemplateFromRepositoryInputTypeDef(BaseValidatorModel):
    approvalRuleTemplateName: str
    repositoryName: str


class EvaluatePullRequestApprovalRulesInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    revisionId: str


class EvaluationTypeDef(BaseValidatorModel):
    approved: Optional[bool] = None
    overridden: Optional[bool] = None
    approvalRulesSatisfied: Optional[List[str]] = None
    approvalRulesNotSatisfied: Optional[List[str]] = None


class FileTypeDef(BaseValidatorModel):
    blobId: Optional[str] = None
    absolutePath: Optional[str] = None
    relativePath: Optional[str] = None
    fileMode: Optional[FileModeTypeEnumType] = None


class FolderTypeDef(BaseValidatorModel):
    treeId: Optional[str] = None
    absolutePath: Optional[str] = None
    relativePath: Optional[str] = None


class GetApprovalRuleTemplateInputTypeDef(BaseValidatorModel):
    approvalRuleTemplateName: str


class GetBlobInputTypeDef(BaseValidatorModel):
    repositoryName: str
    blobId: str


class GetBranchInputTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    branchName: Optional[str] = None


class GetCommentInputTypeDef(BaseValidatorModel):
    commentId: str


class GetCommentReactionsInputTypeDef(BaseValidatorModel):
    commentId: str
    reactionUserArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetCommentsForComparedCommitInputTypeDef(BaseValidatorModel):
    repositoryName: str
    afterCommitId: str
    beforeCommitId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetCommentsForPullRequestInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetCommitInputTypeDef(BaseValidatorModel):
    repositoryName: str
    commitId: str


class GetDifferencesInputTypeDef(BaseValidatorModel):
    repositoryName: str
    afterCommitSpecifier: str
    beforeCommitSpecifier: Optional[str] = None
    beforePath: Optional[str] = None
    afterPath: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetFileInputTypeDef(BaseValidatorModel):
    repositoryName: str
    filePath: str
    commitSpecifier: Optional[str] = None


class GetFolderInputTypeDef(BaseValidatorModel):
    repositoryName: str
    folderPath: str
    commitSpecifier: Optional[str] = None


class SubModuleTypeDef(BaseValidatorModel):
    commitId: Optional[str] = None
    absolutePath: Optional[str] = None
    relativePath: Optional[str] = None


class SymbolicLinkTypeDef(BaseValidatorModel):
    blobId: Optional[str] = None
    absolutePath: Optional[str] = None
    relativePath: Optional[str] = None
    fileMode: Optional[FileModeTypeEnumType] = None


class GetMergeCommitInputTypeDef(BaseValidatorModel):
    repositoryName: str
    sourceCommitSpecifier: str
    destinationCommitSpecifier: str
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None


class GetMergeConflictsInputTypeDef(BaseValidatorModel):
    repositoryName: str
    destinationCommitSpecifier: str
    sourceCommitSpecifier: str
    mergeOption: MergeOptionTypeEnumType
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    maxConflictFiles: Optional[int] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    nextToken: Optional[str] = None


class GetMergeOptionsInputTypeDef(BaseValidatorModel):
    repositoryName: str
    sourceCommitSpecifier: str
    destinationCommitSpecifier: str
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None


class GetPullRequestApprovalStatesInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    revisionId: str


class GetPullRequestInputTypeDef(BaseValidatorModel):
    pullRequestId: str


class GetPullRequestOverrideStateInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    revisionId: str


class GetRepositoryInputTypeDef(BaseValidatorModel):
    repositoryName: str


class GetRepositoryTriggersInputTypeDef(BaseValidatorModel):
    repositoryName: str


class RepositoryTriggerOutputTypeDef(BaseValidatorModel):
    name: str
    destinationArn: str
    events: List[RepositoryTriggerEventEnumType]
    customData: Optional[str] = None
    branches: Optional[List[str]] = None


class ListApprovalRuleTemplatesInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssociatedApprovalRuleTemplatesForRepositoryInputTypeDef(BaseValidatorModel):
    repositoryName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBranchesInputTypeDef(BaseValidatorModel):
    repositoryName: str
    nextToken: Optional[str] = None


class ListFileCommitHistoryRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    filePath: str
    commitSpecifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListPullRequestsInputTypeDef(BaseValidatorModel):
    repositoryName: str
    authorArn: Optional[str] = None
    pullRequestStatus: Optional[PullRequestStatusEnumType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListRepositoriesForApprovalRuleTemplateInputTypeDef(BaseValidatorModel):
    approvalRuleTemplateName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListRepositoriesInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    sortBy: Optional[SortByEnumType] = None
    order: Optional[OrderEnumType] = None


class RepositoryNameIdPairTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    repositoryId: Optional[str] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None


class MergeBranchesByFastForwardInputTypeDef(BaseValidatorModel):
    repositoryName: str
    sourceCommitSpecifier: str
    destinationCommitSpecifier: str
    targetBranch: Optional[str] = None


class MergeHunkDetailTypeDef(BaseValidatorModel):
    startLine: Optional[int] = None
    endLine: Optional[int] = None
    hunkContent: Optional[str] = None


class MergeMetadataTypeDef(BaseValidatorModel):
    isMerged: Optional[bool] = None
    mergedBy: Optional[str] = None
    mergeCommitId: Optional[str] = None
    mergeOption: Optional[MergeOptionTypeEnumType] = None


class MergePullRequestByFastForwardInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    repositoryName: str
    sourceCommitId: Optional[str] = None


class OverridePullRequestApprovalRulesInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    revisionId: str
    overrideStatus: OverrideStatusType


class PostCommentReplyInputTypeDef(BaseValidatorModel):
    inReplyTo: str
    content: str
    clientRequestToken: Optional[str] = None


class PullRequestCreatedEventMetadataTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    sourceCommitId: Optional[str] = None
    destinationCommitId: Optional[str] = None
    mergeBase: Optional[str] = None


class PullRequestSourceReferenceUpdatedEventMetadataTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    mergeBase: Optional[str] = None


class PullRequestStatusChangedEventMetadataTypeDef(BaseValidatorModel):
    pullRequestStatus: Optional[PullRequestStatusEnumType] = None


class PutCommentReactionInputTypeDef(BaseValidatorModel):
    commentId: str
    reactionValue: str


class SourceFileSpecifierTypeDef(BaseValidatorModel):
    filePath: str
    isMove: Optional[bool] = None


class ReactionValueFormatsTypeDef(BaseValidatorModel):
    emoji: Optional[str] = None
    shortCode: Optional[str] = None
    unicode: Optional[str] = None


class RepositoryTriggerExecutionFailureTypeDef(BaseValidatorModel):
    trigger: Optional[str] = None
    failureMessage: Optional[str] = None


class RepositoryTriggerTypeDef(BaseValidatorModel):
    name: str
    destinationArn: str
    events: Sequence[RepositoryTriggerEventEnumType]
    customData: Optional[str] = None
    branches: Optional[Sequence[str]] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateApprovalRuleTemplateContentInputTypeDef(BaseValidatorModel):
    approvalRuleTemplateName: str
    newRuleContent: str
    existingRuleContentSha256: Optional[str] = None


class UpdateApprovalRuleTemplateDescriptionInputTypeDef(BaseValidatorModel):
    approvalRuleTemplateName: str
    approvalRuleTemplateDescription: str


class UpdateApprovalRuleTemplateNameInputTypeDef(BaseValidatorModel):
    oldApprovalRuleTemplateName: str
    newApprovalRuleTemplateName: str


class UpdateCommentInputTypeDef(BaseValidatorModel):
    commentId: str
    content: str


class UpdateDefaultBranchInputTypeDef(BaseValidatorModel):
    repositoryName: str
    defaultBranchName: str


class UpdatePullRequestApprovalRuleContentInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    approvalRuleName: str
    newRuleContent: str
    existingRuleContentSha256: Optional[str] = None


class UpdatePullRequestApprovalStateInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    revisionId: str
    approvalState: ApprovalStateType


class UpdatePullRequestDescriptionInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    description: str


class UpdatePullRequestStatusInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    pullRequestStatus: PullRequestStatusEnumType


class UpdatePullRequestTitleInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    title: str


class UpdateRepositoryDescriptionInputTypeDef(BaseValidatorModel):
    repositoryName: str
    repositoryDescription: Optional[str] = None


class UpdateRepositoryEncryptionKeyInputTypeDef(BaseValidatorModel):
    repositoryName: str
    kmsKeyId: str


class UpdateRepositoryNameInputTypeDef(BaseValidatorModel):
    oldName: str
    newName: str


class ApprovalRuleTypeDef(BaseValidatorModel):
    approvalRuleId: Optional[str] = None
    approvalRuleName: Optional[str] = None
    approvalRuleContent: Optional[str] = None
    ruleContentSha256: Optional[str] = None
    lastModifiedDate: Optional[datetime] = None
    creationDate: Optional[datetime] = None
    lastModifiedUser: Optional[str] = None
    originApprovalRuleTemplate: Optional[OriginApprovalRuleTemplateTypeDef] = None


class BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef(BaseValidatorModel):
    associatedRepositoryNames: List[str]
    errors: List[BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateApprovalRuleTemplateOutputTypeDef(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUnreferencedMergeCommitOutputTypeDef(BaseValidatorModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteApprovalRuleTemplateOutputTypeDef(BaseValidatorModel):
    approvalRuleTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteFileOutputTypeDef(BaseValidatorModel):
    commitId: str
    blobId: str
    treeId: str
    filePath: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePullRequestApprovalRuleOutputTypeDef(BaseValidatorModel):
    approvalRuleId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRepositoryOutputTypeDef(BaseValidatorModel):
    repositoryId: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetApprovalRuleTemplateOutputTypeDef(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetBlobOutputTypeDef(BaseValidatorModel):
    content: bytes
    ResponseMetadata: ResponseMetadataTypeDef


class GetFileOutputTypeDef(BaseValidatorModel):
    commitId: str
    blobId: str
    filePath: str
    fileMode: FileModeTypeEnumType
    fileSize: int
    fileContent: bytes
    ResponseMetadata: ResponseMetadataTypeDef


class GetMergeCommitOutputTypeDef(BaseValidatorModel):
    sourceCommitId: str
    destinationCommitId: str
    baseCommitId: str
    mergedCommitId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetMergeOptionsOutputTypeDef(BaseValidatorModel):
    mergeOptions: List[MergeOptionTypeEnumType]
    sourceCommitId: str
    destinationCommitId: str
    baseCommitId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetPullRequestApprovalStatesOutputTypeDef(BaseValidatorModel):
    approvals: List[ApprovalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetPullRequestOverrideStateOutputTypeDef(BaseValidatorModel):
    overridden: bool
    overrider: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListApprovalRuleTemplatesOutputTypeDef(BaseValidatorModel):
    approvalRuleTemplateNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef(BaseValidatorModel):
    approvalRuleTemplateNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListBranchesOutputTypeDef(BaseValidatorModel):
    branches: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListPullRequestsOutputTypeDef(BaseValidatorModel):
    pullRequestIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListRepositoriesForApprovalRuleTemplateOutputTypeDef(BaseValidatorModel):
    repositoryNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MergeBranchesByFastForwardOutputTypeDef(BaseValidatorModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadataTypeDef


class MergeBranchesBySquashOutputTypeDef(BaseValidatorModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadataTypeDef


class MergeBranchesByThreeWayOutputTypeDef(BaseValidatorModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutFileOutputTypeDef(BaseValidatorModel):
    commitId: str
    blobId: str
    treeId: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutRepositoryTriggersOutputTypeDef(BaseValidatorModel):
    configurationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateApprovalRuleTemplateContentOutputTypeDef(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateApprovalRuleTemplateDescriptionOutputTypeDef(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateApprovalRuleTemplateNameOutputTypeDef(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRepositoryEncryptionKeyOutputTypeDef(BaseValidatorModel):
    repositoryId: str
    kmsKeyId: str
    originalKmsKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef(BaseValidatorModel):
    disassociatedRepositoryNames: List[str]
    errors: List[BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetRepositoriesOutputTypeDef(BaseValidatorModel):
    repositories: List[RepositoryMetadataTypeDef]
    repositoriesNotFound: List[str]
    errors: List[BatchGetRepositoriesErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRepositoryOutputTypeDef(BaseValidatorModel):
    repositoryMetadata: RepositoryMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetRepositoryOutputTypeDef(BaseValidatorModel):
    repositoryMetadata: RepositoryMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DifferenceTypeDef(BaseValidatorModel):
    beforeBlob: Optional[BlobMetadataTypeDef] = None
    afterBlob: Optional[BlobMetadataTypeDef] = None
    changeType: Optional[ChangeTypeEnumType] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class PutFileInputTypeDef(BaseValidatorModel):
    repositoryName: str
    branchName: str
    fileContent: BlobTypeDef
    filePath: str
    fileMode: Optional[FileModeTypeEnumType] = None
    parentCommitId: Optional[str] = None
    commitMessage: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None


class ReplaceContentEntryTypeDef(BaseValidatorModel):
    filePath: str
    replacementType: ReplacementTypeEnumType
    content: Optional[BlobTypeDef] = None
    fileMode: Optional[FileModeTypeEnumType] = None


class DeleteBranchOutputTypeDef(BaseValidatorModel):
    deletedBranch: BranchInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetBranchOutputTypeDef(BaseValidatorModel):
    branch: BranchInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCommentContentOutputTypeDef(BaseValidatorModel):
    comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCommentOutputTypeDef(BaseValidatorModel):
    comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PostCommentReplyOutputTypeDef(BaseValidatorModel):
    comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCommentOutputTypeDef(BaseValidatorModel):
    comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CommentsForComparedCommitTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    beforeBlobId: Optional[str] = None
    afterBlobId: Optional[str] = None
    location: Optional[LocationTypeDef] = None
    comments: Optional[List[CommentTypeDef]] = None


class CommentsForPullRequestTypeDef(BaseValidatorModel):
    pullRequestId: Optional[str] = None
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    beforeBlobId: Optional[str] = None
    afterBlobId: Optional[str] = None
    location: Optional[LocationTypeDef] = None
    comments: Optional[List[CommentTypeDef]] = None


class PostCommentForComparedCommitInputTypeDef(BaseValidatorModel):
    repositoryName: str
    afterCommitId: str
    content: str
    beforeCommitId: Optional[str] = None
    location: Optional[LocationTypeDef] = None
    clientRequestToken: Optional[str] = None


class PostCommentForComparedCommitOutputTypeDef(BaseValidatorModel):
    repositoryName: str
    beforeCommitId: str
    afterCommitId: str
    beforeBlobId: str
    afterBlobId: str
    location: LocationTypeDef
    comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PostCommentForPullRequestInputTypeDef(BaseValidatorModel):
    pullRequestId: str
    repositoryName: str
    beforeCommitId: str
    afterCommitId: str
    content: str
    location: Optional[LocationTypeDef] = None
    clientRequestToken: Optional[str] = None


class PostCommentForPullRequestOutputTypeDef(BaseValidatorModel):
    repositoryName: str
    pullRequestId: str
    beforeCommitId: str
    afterCommitId: str
    beforeBlobId: str
    afterBlobId: str
    location: LocationTypeDef
    comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CommitTypeDef(BaseValidatorModel):
    commitId: Optional[str] = None
    treeId: Optional[str] = None
    parents: Optional[List[str]] = None
    message: Optional[str] = None
    author: Optional[UserInfoTypeDef] = None
    committer: Optional[UserInfoTypeDef] = None
    additionalData: Optional[str] = None


class ConflictMetadataTypeDef(BaseValidatorModel):
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


class CreateCommitOutputTypeDef(BaseValidatorModel):
    commitId: str
    treeId: str
    filesAdded: List[FileMetadataTypeDef]
    filesUpdated: List[FileMetadataTypeDef]
    filesDeleted: List[FileMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePullRequestInputTypeDef(BaseValidatorModel):
    title: str
    targets: Sequence[TargetTypeDef]
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None


class DescribePullRequestEventsInputPaginateTypeDef(BaseValidatorModel):
    pullRequestId: str
    pullRequestEventType: Optional[PullRequestEventTypeType] = None
    actorArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetCommentsForComparedCommitInputPaginateTypeDef(BaseValidatorModel):
    repositoryName: str
    afterCommitId: str
    beforeCommitId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetCommentsForPullRequestInputPaginateTypeDef(BaseValidatorModel):
    pullRequestId: str
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetDifferencesInputPaginateTypeDef(BaseValidatorModel):
    repositoryName: str
    afterCommitSpecifier: str
    beforeCommitSpecifier: Optional[str] = None
    beforePath: Optional[str] = None
    afterPath: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBranchesInputPaginateTypeDef(BaseValidatorModel):
    repositoryName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPullRequestsInputPaginateTypeDef(BaseValidatorModel):
    repositoryName: str
    authorArn: Optional[str] = None
    pullRequestStatus: Optional[PullRequestStatusEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRepositoriesInputPaginateTypeDef(BaseValidatorModel):
    sortBy: Optional[SortByEnumType] = None
    order: Optional[OrderEnumType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class EvaluatePullRequestApprovalRulesOutputTypeDef(BaseValidatorModel):
    evaluation: EvaluationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetFolderOutputTypeDef(BaseValidatorModel):
    commitId: str
    folderPath: str
    treeId: str
    subFolders: List[FolderTypeDef]
    files: List[FileTypeDef]
    symbolicLinks: List[SymbolicLinkTypeDef]
    subModules: List[SubModuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetRepositoryTriggersOutputTypeDef(BaseValidatorModel):
    configurationId: str
    triggers: List[RepositoryTriggerOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListRepositoriesOutputTypeDef(BaseValidatorModel):
    repositories: List[RepositoryNameIdPairTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MergeHunkTypeDef(BaseValidatorModel):
    isConflict: Optional[bool] = None
    source: Optional[MergeHunkDetailTypeDef] = None
    destination: Optional[MergeHunkDetailTypeDef] = None
    base: Optional[MergeHunkDetailTypeDef] = None


class PullRequestMergedStateChangedEventMetadataTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    destinationReference: Optional[str] = None
    mergeMetadata: Optional[MergeMetadataTypeDef] = None


class PullRequestTargetTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    sourceReference: Optional[str] = None
    destinationReference: Optional[str] = None
    destinationCommit: Optional[str] = None
    sourceCommit: Optional[str] = None
    mergeBase: Optional[str] = None
    mergeMetadata: Optional[MergeMetadataTypeDef] = None


class PutFileEntryTypeDef(BaseValidatorModel):
    filePath: str
    fileMode: Optional[FileModeTypeEnumType] = None
    fileContent: Optional[BlobTypeDef] = None
    sourceFile: Optional[SourceFileSpecifierTypeDef] = None


class ReactionForCommentTypeDef(BaseValidatorModel):
    reaction: Optional[ReactionValueFormatsTypeDef] = None
    reactionUsers: Optional[List[str]] = None
    reactionsFromDeletedUsersCount: Optional[int] = None


class TestRepositoryTriggersOutputTypeDef(BaseValidatorModel):
    successfulExecutions: List[str]
    failedExecutions: List[RepositoryTriggerExecutionFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePullRequestApprovalRuleOutputTypeDef(BaseValidatorModel):
    approvalRule: ApprovalRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePullRequestApprovalRuleContentOutputTypeDef(BaseValidatorModel):
    approvalRule: ApprovalRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDifferencesOutputTypeDef(BaseValidatorModel):
    differences: List[DifferenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ConflictResolutionTypeDef(BaseValidatorModel):
    replaceContents: Optional[Sequence[ReplaceContentEntryTypeDef]] = None
    deleteFiles: Optional[Sequence[DeleteFileEntryTypeDef]] = None
    setFileModes: Optional[Sequence[SetFileModeEntryTypeDef]] = None


class GetCommentsForComparedCommitOutputTypeDef(BaseValidatorModel):
    commentsForComparedCommitData: List[CommentsForComparedCommitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetCommentsForPullRequestOutputTypeDef(BaseValidatorModel):
    commentsForPullRequestData: List[CommentsForPullRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchGetCommitsOutputTypeDef(BaseValidatorModel):
    commits: List[CommitTypeDef]
    errors: List[BatchGetCommitsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class FileVersionTypeDef(BaseValidatorModel):
    commit: Optional[CommitTypeDef] = None
    blobId: Optional[str] = None
    path: Optional[str] = None
    revisionChildren: Optional[List[str]] = None


class GetCommitOutputTypeDef(BaseValidatorModel):
    commit: CommitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetMergeConflictsOutputTypeDef(BaseValidatorModel):
    mergeable: bool
    destinationCommitId: str
    sourceCommitId: str
    baseCommitId: str
    conflictMetadataList: List[ConflictMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ConflictTypeDef(BaseValidatorModel):
    conflictMetadata: Optional[ConflictMetadataTypeDef] = None
    mergeHunks: Optional[List[MergeHunkTypeDef]] = None


class DescribeMergeConflictsOutputTypeDef(BaseValidatorModel):
    conflictMetadata: ConflictMetadataTypeDef
    mergeHunks: List[MergeHunkTypeDef]
    destinationCommitId: str
    sourceCommitId: str
    baseCommitId: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PullRequestEventTypeDef(BaseValidatorModel):
    pullRequestId: Optional[str] = None
    eventDate: Optional[datetime] = None
    pullRequestEventType: Optional[PullRequestEventTypeType] = None
    actorArn: Optional[str] = None
    pullRequestCreatedEventMetadata: Optional[PullRequestCreatedEventMetadataTypeDef] = None
    pullRequestStatusChangedEventMetadata: Optional[PullRequestStatusChangedEventMetadataTypeDef] = None
    pullRequestSourceReferenceUpdatedEventMetadata: Optional[ PullRequestSourceReferenceUpdatedEventMetadataTypeDef ] = None
    pullRequestMergedStateChangedEventMetadata: Optional[ PullRequestMergedStateChangedEventMetadataTypeDef ] = None
    approvalRuleEventMetadata: Optional[ApprovalRuleEventMetadataTypeDef] = None
    approvalStateChangedEventMetadata: Optional[ApprovalStateChangedEventMetadataTypeDef] = None
    approvalRuleOverriddenEventMetadata: Optional[ApprovalRuleOverriddenEventMetadataTypeDef] = None


class PullRequestTypeDef(BaseValidatorModel):
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


class CreateCommitInputTypeDef(BaseValidatorModel):
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


class GetCommentReactionsOutputTypeDef(BaseValidatorModel):
    reactionsForComment: List[ReactionForCommentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RepositoryTriggerUnionTypeDef(BaseValidatorModel):
    pass


class PutRepositoryTriggersInputTypeDef(BaseValidatorModel):
    repositoryName: str
    triggers: Sequence[RepositoryTriggerUnionTypeDef]


class TestRepositoryTriggersInputTypeDef(BaseValidatorModel):
    repositoryName: str
    triggers: Sequence[RepositoryTriggerUnionTypeDef]


class CreateUnreferencedMergeCommitInputTypeDef(BaseValidatorModel):
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


class MergeBranchesBySquashInputTypeDef(BaseValidatorModel):
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


class MergeBranchesByThreeWayInputTypeDef(BaseValidatorModel):
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


class MergePullRequestBySquashInputTypeDef(BaseValidatorModel):
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


class MergePullRequestByThreeWayInputTypeDef(BaseValidatorModel):
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


class ListFileCommitHistoryResponseTypeDef(BaseValidatorModel):
    revisionDag: List[FileVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchDescribeMergeConflictsOutputTypeDef(BaseValidatorModel):
    conflicts: List[ConflictTypeDef]
    errors: List[BatchDescribeMergeConflictsErrorTypeDef]
    destinationCommitId: str
    sourceCommitId: str
    baseCommitId: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribePullRequestEventsOutputTypeDef(BaseValidatorModel):
    pullRequestEvents: List[PullRequestEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreatePullRequestOutputTypeDef(BaseValidatorModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPullRequestOutputTypeDef(BaseValidatorModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class MergePullRequestByFastForwardOutputTypeDef(BaseValidatorModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class MergePullRequestBySquashOutputTypeDef(BaseValidatorModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class MergePullRequestByThreeWayOutputTypeDef(BaseValidatorModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePullRequestDescriptionOutputTypeDef(BaseValidatorModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePullRequestStatusOutputTypeDef(BaseValidatorModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePullRequestTitleOutputTypeDef(BaseValidatorModel):
    pullRequest: PullRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


