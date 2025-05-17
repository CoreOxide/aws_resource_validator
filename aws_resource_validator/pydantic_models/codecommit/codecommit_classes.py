from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.codecommit.codecommit_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


# This class is the input for the 'associate_approval_rule_template_with_repository' function.
class AssociateApprovalRuleTemplateWithRepositoryInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    repositoryName: str


class BatchAssociateApprovalRuleTemplateWithRepositoriesError(BaseValidatorModel):
    repositoryName: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


# This class is the input for the 'batch_associate_approval_rule_template_with_repositories' function.
class BatchAssociateApprovalRuleTemplateWithRepositoriesInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    repositoryNames: List[str]


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


# This class is the input for the 'batch_describe_merge_conflicts' function.
class BatchDescribeMergeConflictsInput(BaseValidatorModel):
    repositoryName: str
    destinationCommitSpecifier: str
    sourceCommitSpecifier: str
    mergeOption: MergeOptionTypeEnumType
    maxMergeHunks: Optional[int] = None
    maxConflictFiles: Optional[int] = None
    filePaths: Optional[List[str]] = None
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    nextToken: Optional[str] = None


class BatchDisassociateApprovalRuleTemplateFromRepositoriesError(BaseValidatorModel):
    repositoryName: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


# This class is the input for the 'batch_disassociate_approval_rule_template_from_repositories' function.
class BatchDisassociateApprovalRuleTemplateFromRepositoriesInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    repositoryNames: List[str]


class BatchGetCommitsError(BaseValidatorModel):
    commitId: Optional[str] = None
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None


# This class is the input for the 'batch_get_commits' function.
class BatchGetCommitsInput(BaseValidatorModel):
    commitIds: List[str]
    repositoryName: str


class BatchGetRepositoriesError(BaseValidatorModel):
    repositoryId: Optional[str] = None
    repositoryName: Optional[str] = None
    errorCode: Optional[BatchGetRepositoriesErrorCodeEnumType] = None
    errorMessage: Optional[str] = None


# This class is the input for the 'batch_get_repositories' function.
class BatchGetRepositoriesInput(BaseValidatorModel):
    repositoryNames: List[str]


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

Blob = Union[str, bytes, IO[Any], StreamingBody]


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


# This class is the input for the 'create_approval_rule_template' function.
class CreateApprovalRuleTemplateInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    approvalRuleTemplateContent: str
    approvalRuleTemplateDescription: Optional[str] = None


# This class is the input for the 'create_branch' function.
class CreateBranchInput(BaseValidatorModel):
    repositoryName: str
    branchName: str
    commitId: str


class FileMetadata(BaseValidatorModel):
    absolutePath: Optional[str] = None
    blobId: Optional[str] = None
    fileMode: Optional[FileModeTypeEnumType] = None


# This class is the input for the 'create_pull_request_approval_rule' function.
class CreatePullRequestApprovalRuleInput(BaseValidatorModel):
    pullRequestId: str
    approvalRuleName: str
    approvalRuleContent: str


class Target(BaseValidatorModel):
    repositoryName: str
    sourceReference: str
    destinationReference: Optional[str] = None


# This class is the input for the 'create_repository' function.
class CreateRepositoryInput(BaseValidatorModel):
    repositoryName: str
    repositoryDescription: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    kmsKeyId: Optional[str] = None


# This class is the input for the 'delete_approval_rule_template' function.
class DeleteApprovalRuleTemplateInput(BaseValidatorModel):
    approvalRuleTemplateName: str


# This class is the input for the 'delete_branch' function.
class DeleteBranchInput(BaseValidatorModel):
    repositoryName: str
    branchName: str


# This class is the input for the 'delete_comment_content' function.
class DeleteCommentContentInput(BaseValidatorModel):
    commentId: str


# This class is the input for the 'delete_file' function.
class DeleteFileInput(BaseValidatorModel):
    repositoryName: str
    branchName: str
    filePath: str
    parentCommitId: str
    keepEmptyFolders: Optional[bool] = None
    commitMessage: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None


# This class is the input for the 'delete_pull_request_approval_rule' function.
class DeletePullRequestApprovalRuleInput(BaseValidatorModel):
    pullRequestId: str
    approvalRuleName: str


# This class is the input for the 'delete_repository' function.
class DeleteRepositoryInput(BaseValidatorModel):
    repositoryName: str


# This class is the input for the 'describe_merge_conflicts' function.
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


# This class is the input for the 'describe_pull_request_events' function.
class DescribePullRequestEventsInput(BaseValidatorModel):
    pullRequestId: str
    pullRequestEventType: Optional[PullRequestEventTypeType] = None
    actorArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'disassociate_approval_rule_template_from_repository' function.
class DisassociateApprovalRuleTemplateFromRepositoryInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    repositoryName: str


# This class is the input for the 'evaluate_pull_request_approval_rules' function.
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


# This class is the input for the 'get_approval_rule_template' function.
class GetApprovalRuleTemplateInput(BaseValidatorModel):
    approvalRuleTemplateName: str


# This class is the input for the 'get_blob' function.
class GetBlobInput(BaseValidatorModel):
    repositoryName: str
    blobId: str


# This class is the input for the 'get_branch' function.
class GetBranchInput(BaseValidatorModel):
    repositoryName: Optional[str] = None
    branchName: Optional[str] = None


# This class is the input for the 'get_comment' function.
class GetCommentInput(BaseValidatorModel):
    commentId: str


# This class is the input for the 'get_comment_reactions' function.
class GetCommentReactionsInput(BaseValidatorModel):
    commentId: str
    reactionUserArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_comments_for_compared_commit' function.
class GetCommentsForComparedCommitInput(BaseValidatorModel):
    repositoryName: str
    afterCommitId: str
    beforeCommitId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_comments_for_pull_request' function.
class GetCommentsForPullRequestInput(BaseValidatorModel):
    pullRequestId: str
    repositoryName: Optional[str] = None
    beforeCommitId: Optional[str] = None
    afterCommitId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_commit' function.
class GetCommitInput(BaseValidatorModel):
    repositoryName: str
    commitId: str


# This class is the input for the 'get_differences' function.
class GetDifferencesInput(BaseValidatorModel):
    repositoryName: str
    afterCommitSpecifier: str
    beforeCommitSpecifier: Optional[str] = None
    beforePath: Optional[str] = None
    afterPath: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_file' function.
class GetFileInput(BaseValidatorModel):
    repositoryName: str
    filePath: str
    commitSpecifier: Optional[str] = None


# This class is the input for the 'get_folder' function.
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


# This class is the input for the 'get_merge_commit' function.
class GetMergeCommitInput(BaseValidatorModel):
    repositoryName: str
    sourceCommitSpecifier: str
    destinationCommitSpecifier: str
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None


# This class is the input for the 'get_merge_conflicts' function.
class GetMergeConflictsInput(BaseValidatorModel):
    repositoryName: str
    destinationCommitSpecifier: str
    sourceCommitSpecifier: str
    mergeOption: MergeOptionTypeEnumType
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    maxConflictFiles: Optional[int] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None
    nextToken: Optional[str] = None


# This class is the input for the 'get_merge_options' function.
class GetMergeOptionsInput(BaseValidatorModel):
    repositoryName: str
    sourceCommitSpecifier: str
    destinationCommitSpecifier: str
    conflictDetailLevel: Optional[ConflictDetailLevelTypeEnumType] = None
    conflictResolutionStrategy: Optional[ConflictResolutionStrategyTypeEnumType] = None


# This class is the input for the 'get_pull_request_approval_states' function.
class GetPullRequestApprovalStatesInput(BaseValidatorModel):
    pullRequestId: str
    revisionId: str


# This class is the input for the 'get_pull_request' function.
class GetPullRequestInput(BaseValidatorModel):
    pullRequestId: str


# This class is the input for the 'get_pull_request_override_state' function.
class GetPullRequestOverrideStateInput(BaseValidatorModel):
    pullRequestId: str
    revisionId: str


# This class is the input for the 'get_repository' function.
class GetRepositoryInput(BaseValidatorModel):
    repositoryName: str


# This class is the input for the 'get_repository_triggers' function.
class GetRepositoryTriggersInput(BaseValidatorModel):
    repositoryName: str


class RepositoryTriggerOutput(BaseValidatorModel):
    name: str
    destinationArn: str
    events: List[RepositoryTriggerEventEnumType]
    customData: Optional[str] = None
    branches: Optional[List[str]] = None


# This class is the input for the 'list_approval_rule_templates' function.
class ListApprovalRuleTemplatesInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_associated_approval_rule_templates_for_repository' function.
class ListAssociatedApprovalRuleTemplatesForRepositoryInput(BaseValidatorModel):
    repositoryName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_branches' function.
class ListBranchesInput(BaseValidatorModel):
    repositoryName: str
    nextToken: Optional[str] = None


# This class is the input for the 'list_file_commit_history' function.
class ListFileCommitHistoryRequest(BaseValidatorModel):
    repositoryName: str
    filePath: str
    commitSpecifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_pull_requests' function.
class ListPullRequestsInput(BaseValidatorModel):
    repositoryName: str
    authorArn: Optional[str] = None
    pullRequestStatus: Optional[PullRequestStatusEnumType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_repositories_for_approval_rule_template' function.
class ListRepositoriesForApprovalRuleTemplateInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_repositories' function.
class ListRepositoriesInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    sortBy: Optional[SortByEnumType] = None
    order: Optional[OrderEnumType] = None


class RepositoryNameIdPair(BaseValidatorModel):
    repositoryName: Optional[str] = None
    repositoryId: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None


# This class is the input for the 'merge_branches_by_fast_forward' function.
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


# This class is the input for the 'merge_pull_request_by_fast_forward' function.
class MergePullRequestByFastForwardInput(BaseValidatorModel):
    pullRequestId: str
    repositoryName: str
    sourceCommitId: Optional[str] = None


# This class is the input for the 'override_pull_request_approval_rules' function.
class OverridePullRequestApprovalRulesInput(BaseValidatorModel):
    pullRequestId: str
    revisionId: str
    overrideStatus: OverrideStatusType


# This class is the input for the 'post_comment_reply' function.
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


# This class is the input for the 'put_comment_reaction' function.
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
    events: List[RepositoryTriggerEventEnumType]
    customData: Optional[str] = None
    branches: Optional[List[str]] = None


# This class is the input for the 'tag_resource' function.
class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


# This class is the input for the 'untag_resource' function.
class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_approval_rule_template_content' function.
class UpdateApprovalRuleTemplateContentInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    newRuleContent: str
    existingRuleContentSha256: Optional[str] = None


# This class is the input for the 'update_approval_rule_template_description' function.
class UpdateApprovalRuleTemplateDescriptionInput(BaseValidatorModel):
    approvalRuleTemplateName: str
    approvalRuleTemplateDescription: str


# This class is the input for the 'update_approval_rule_template_name' function.
class UpdateApprovalRuleTemplateNameInput(BaseValidatorModel):
    oldApprovalRuleTemplateName: str
    newApprovalRuleTemplateName: str


# This class is the input for the 'update_comment' function.
class UpdateCommentInput(BaseValidatorModel):
    commentId: str
    content: str


# This class is the input for the 'update_default_branch' function.
class UpdateDefaultBranchInput(BaseValidatorModel):
    repositoryName: str
    defaultBranchName: str


# This class is the input for the 'update_pull_request_approval_rule_content' function.
class UpdatePullRequestApprovalRuleContentInput(BaseValidatorModel):
    pullRequestId: str
    approvalRuleName: str
    newRuleContent: str
    existingRuleContentSha256: Optional[str] = None


# This class is the input for the 'update_pull_request_approval_state' function.
class UpdatePullRequestApprovalStateInput(BaseValidatorModel):
    pullRequestId: str
    revisionId: str
    approvalState: ApprovalStateType


# This class is the input for the 'update_pull_request_description' function.
class UpdatePullRequestDescriptionInput(BaseValidatorModel):
    pullRequestId: str
    description: str


# This class is the input for the 'update_pull_request_status' function.
class UpdatePullRequestStatusInput(BaseValidatorModel):
    pullRequestId: str
    pullRequestStatus: PullRequestStatusEnumType


# This class is the input for the 'update_pull_request_title' function.
class UpdatePullRequestTitleInput(BaseValidatorModel):
    pullRequestId: str
    title: str


# This class is the input for the 'update_repository_description' function.
class UpdateRepositoryDescriptionInput(BaseValidatorModel):
    repositoryName: str
    repositoryDescription: Optional[str] = None


# This class is the input for the 'update_repository_encryption_key' function.
class UpdateRepositoryEncryptionKeyInput(BaseValidatorModel):
    repositoryName: str
    kmsKeyId: str


# This class is the input for the 'update_repository_name' function.
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


# This class is the output for the 'batch_associate_approval_rule_template_with_repositories' function.
class BatchAssociateApprovalRuleTemplateWithRepositoriesOutput(BaseValidatorModel):
    associatedRepositoryNames: List[str]
    errors: List[BatchAssociateApprovalRuleTemplateWithRepositoriesError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_approval_rule_template' function.
class CreateApprovalRuleTemplateOutput(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_unreferenced_merge_commit' function.
class CreateUnreferencedMergeCommitOutput(BaseValidatorModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_approval_rule_template' function.
class DeleteApprovalRuleTemplateOutput(BaseValidatorModel):
    approvalRuleTemplateId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_file' function.
class DeleteFileOutput(BaseValidatorModel):
    commitId: str
    blobId: str
    treeId: str
    filePath: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_pull_request_approval_rule' function.
class DeletePullRequestApprovalRuleOutput(BaseValidatorModel):
    approvalRuleId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_repository' function.
class DeleteRepositoryOutput(BaseValidatorModel):
    repositoryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_repository_name' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_approval_rule_template' function.
class GetApprovalRuleTemplateOutput(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_blob' function.
class GetBlobOutput(BaseValidatorModel):
    content: bytes
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_file' function.
class GetFileOutput(BaseValidatorModel):
    commitId: str
    blobId: str
    filePath: str
    fileMode: FileModeTypeEnumType
    fileSize: int
    fileContent: bytes
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_merge_commit' function.
class GetMergeCommitOutput(BaseValidatorModel):
    sourceCommitId: str
    destinationCommitId: str
    baseCommitId: str
    mergedCommitId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_merge_options' function.
class GetMergeOptionsOutput(BaseValidatorModel):
    mergeOptions: List[MergeOptionTypeEnumType]
    sourceCommitId: str
    destinationCommitId: str
    baseCommitId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_pull_request_approval_states' function.
class GetPullRequestApprovalStatesOutput(BaseValidatorModel):
    approvals: List[Approval]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_pull_request_override_state' function.
class GetPullRequestOverrideStateOutput(BaseValidatorModel):
    overridden: bool
    overrider: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_approval_rule_templates' function.
class ListApprovalRuleTemplatesOutput(BaseValidatorModel):
    approvalRuleTemplateNames: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_associated_approval_rule_templates_for_repository' function.
class ListAssociatedApprovalRuleTemplatesForRepositoryOutput(BaseValidatorModel):
    approvalRuleTemplateNames: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_branches' function.
class ListBranchesOutput(BaseValidatorModel):
    branches: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_pull_requests' function.
class ListPullRequestsOutput(BaseValidatorModel):
    pullRequestIds: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_repositories_for_approval_rule_template' function.
class ListRepositoriesForApprovalRuleTemplateOutput(BaseValidatorModel):
    repositoryNames: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'merge_branches_by_fast_forward' function.
class MergeBranchesByFastForwardOutput(BaseValidatorModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'merge_branches_by_squash' function.
class MergeBranchesBySquashOutput(BaseValidatorModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'merge_branches_by_three_way' function.
class MergeBranchesByThreeWayOutput(BaseValidatorModel):
    commitId: str
    treeId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_file' function.
class PutFileOutput(BaseValidatorModel):
    commitId: str
    blobId: str
    treeId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_repository_triggers' function.
class PutRepositoryTriggersOutput(BaseValidatorModel):
    configurationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_approval_rule_template_content' function.
class UpdateApprovalRuleTemplateContentOutput(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_approval_rule_template_description' function.
class UpdateApprovalRuleTemplateDescriptionOutput(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_approval_rule_template_name' function.
class UpdateApprovalRuleTemplateNameOutput(BaseValidatorModel):
    approvalRuleTemplate: ApprovalRuleTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_repository_encryption_key' function.
class UpdateRepositoryEncryptionKeyOutput(BaseValidatorModel):
    repositoryId: str
    kmsKeyId: str
    originalKmsKeyId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_disassociate_approval_rule_template_from_repositories' function.
class BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput(BaseValidatorModel):
    disassociatedRepositoryNames: List[str]
    errors: List[BatchDisassociateApprovalRuleTemplateFromRepositoriesError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_get_repositories' function.
class BatchGetRepositoriesOutput(BaseValidatorModel):
    repositories: List[RepositoryMetadata]
    repositoriesNotFound: List[str]
    errors: List[BatchGetRepositoriesError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_repository' function.
class CreateRepositoryOutput(BaseValidatorModel):
    repositoryMetadata: RepositoryMetadata
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_repository' function.
class GetRepositoryOutput(BaseValidatorModel):
    repositoryMetadata: RepositoryMetadata
    ResponseMetadata: ResponseMetadata


class Difference(BaseValidatorModel):
    beforeBlob: Optional[BlobMetadata] = None
    afterBlob: Optional[BlobMetadata] = None
    changeType: Optional[ChangeTypeEnumType] = None


# This class is the input for the 'put_file' function.
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


# This class is the output for the 'delete_branch' function.
class DeleteBranchOutput(BaseValidatorModel):
    deletedBranch: BranchInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_branch' function.
class GetBranchOutput(BaseValidatorModel):
    branch: BranchInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_comment_content' function.
class DeleteCommentContentOutput(BaseValidatorModel):
    comment: Comment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_comment' function.
class GetCommentOutput(BaseValidatorModel):
    comment: Comment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'post_comment_reply' function.
class PostCommentReplyOutput(BaseValidatorModel):
    comment: Comment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_comment' function.
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


# This class is the input for the 'post_comment_for_compared_commit' function.
class PostCommentForComparedCommitInput(BaseValidatorModel):
    repositoryName: str
    afterCommitId: str
    content: str
    beforeCommitId: Optional[str] = None
    location: Optional[Location] = None
    clientRequestToken: Optional[str] = None


# This class is the output for the 'post_comment_for_compared_commit' function.
class PostCommentForComparedCommitOutput(BaseValidatorModel):
    repositoryName: str
    beforeCommitId: str
    afterCommitId: str
    beforeBlobId: str
    afterBlobId: str
    location: Location
    comment: Comment
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'post_comment_for_pull_request' function.
class PostCommentForPullRequestInput(BaseValidatorModel):
    pullRequestId: str
    repositoryName: str
    beforeCommitId: str
    afterCommitId: str
    content: str
    location: Optional[Location] = None
    clientRequestToken: Optional[str] = None


# This class is the output for the 'post_comment_for_pull_request' function.
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


# This class is the output for the 'create_commit' function.
class CreateCommitOutput(BaseValidatorModel):
    commitId: str
    treeId: str
    filesAdded: List[FileMetadata]
    filesUpdated: List[FileMetadata]
    filesDeleted: List[FileMetadata]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_pull_request' function.
class CreatePullRequestInput(BaseValidatorModel):
    title: str
    targets: List[Target]
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


# This class is the output for the 'evaluate_pull_request_approval_rules' function.
class EvaluatePullRequestApprovalRulesOutput(BaseValidatorModel):
    evaluation: Evaluation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_folder' function.
class GetFolderOutput(BaseValidatorModel):
    commitId: str
    folderPath: str
    treeId: str
    subFolders: List[Folder]
    files: List[File]
    symbolicLinks: List[SymbolicLink]
    subModules: List[SubModule]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_repository_triggers' function.
class GetRepositoryTriggersOutput(BaseValidatorModel):
    configurationId: str
    triggers: List[RepositoryTriggerOutput]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_repositories' function.
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


# This class is the output for the 'test_repository_triggers' function.
class TestRepositoryTriggersOutput(BaseValidatorModel):
    successfulExecutions: List[str]
    failedExecutions: List[RepositoryTriggerExecutionFailure]
    ResponseMetadata: ResponseMetadata

RepositoryTriggerUnion = Union[RepositoryTrigger, RepositoryTriggerOutput]


# This class is the output for the 'create_pull_request_approval_rule' function.
class CreatePullRequestApprovalRuleOutput(BaseValidatorModel):
    approvalRule: ApprovalRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_pull_request_approval_rule_content' function.
class UpdatePullRequestApprovalRuleContentOutput(BaseValidatorModel):
    approvalRule: ApprovalRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_differences' function.
class GetDifferencesOutput(BaseValidatorModel):
    differences: List[Difference]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ConflictResolution(BaseValidatorModel):
    replaceContents: Optional[List[ReplaceContentEntry]] = None
    deleteFiles: Optional[List[DeleteFileEntry]] = None
    setFileModes: Optional[List[SetFileModeEntry]] = None


# This class is the output for the 'get_comments_for_compared_commit' function.
class GetCommentsForComparedCommitOutput(BaseValidatorModel):
    commentsForComparedCommitData: List[CommentsForComparedCommit]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_comments_for_pull_request' function.
class GetCommentsForPullRequestOutput(BaseValidatorModel):
    commentsForPullRequestData: List[CommentsForPullRequest]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'batch_get_commits' function.
class BatchGetCommitsOutput(BaseValidatorModel):
    commits: List[Commit]
    errors: List[BatchGetCommitsError]
    ResponseMetadata: ResponseMetadata


class FileVersion(BaseValidatorModel):
    commit: Optional[Commit] = None
    blobId: Optional[str] = None
    path: Optional[str] = None
    revisionChildren: Optional[List[str]] = None


# This class is the output for the 'get_commit' function.
class GetCommitOutput(BaseValidatorModel):
    commit: Commit
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_merge_conflicts' function.
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


# This class is the output for the 'describe_merge_conflicts' function.
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
    pullRequestSourceReferenceUpdatedEventMetadata: Optional[PullRequestSourceReferenceUpdatedEventMetadata] = None
    pullRequestMergedStateChangedEventMetadata: Optional[PullRequestMergedStateChangedEventMetadata] = None
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


# This class is the input for the 'create_commit' function.
class CreateCommitInput(BaseValidatorModel):
    repositoryName: str
    branchName: str
    parentCommitId: Optional[str] = None
    authorName: Optional[str] = None
    email: Optional[str] = None
    commitMessage: Optional[str] = None
    keepEmptyFolders: Optional[bool] = None
    putFiles: Optional[List[PutFileEntry]] = None
    deleteFiles: Optional[List[DeleteFileEntry]] = None
    setFileModes: Optional[List[SetFileModeEntry]] = None


# This class is the output for the 'get_comment_reactions' function.
class GetCommentReactionsOutput(BaseValidatorModel):
    reactionsForComment: List[ReactionForComment]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'put_repository_triggers' function.
class PutRepositoryTriggersInput(BaseValidatorModel):
    repositoryName: str
    triggers: List[RepositoryTriggerUnion]


# This class is the input for the 'test_repository_triggers' function.
class TestRepositoryTriggersInput(BaseValidatorModel):
    repositoryName: str
    triggers: List[RepositoryTriggerUnion]


# This class is the input for the 'create_unreferenced_merge_commit' function.
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


# This class is the input for the 'merge_branches_by_squash' function.
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


# This class is the input for the 'merge_branches_by_three_way' function.
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


# This class is the input for the 'merge_pull_request_by_squash' function.
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


# This class is the input for the 'merge_pull_request_by_three_way' function.
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


# This class is the output for the 'list_file_commit_history' function.
class ListFileCommitHistoryResponse(BaseValidatorModel):
    revisionDag: List[FileVersion]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'batch_describe_merge_conflicts' function.
class BatchDescribeMergeConflictsOutput(BaseValidatorModel):
    conflicts: List[Conflict]
    errors: List[BatchDescribeMergeConflictsError]
    destinationCommitId: str
    sourceCommitId: str
    baseCommitId: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_pull_request_events' function.
class DescribePullRequestEventsOutput(BaseValidatorModel):
    pullRequestEvents: List[PullRequestEvent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_pull_request' function.
class CreatePullRequestOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_pull_request' function.
class GetPullRequestOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'merge_pull_request_by_fast_forward' function.
class MergePullRequestByFastForwardOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'merge_pull_request_by_squash' function.
class MergePullRequestBySquashOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'merge_pull_request_by_three_way' function.
class MergePullRequestByThreeWayOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_pull_request_description' function.
class UpdatePullRequestDescriptionOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_pull_request_status' function.
class UpdatePullRequestStatusOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_pull_request_title' function.
class UpdatePullRequestTitleOutput(BaseValidatorModel):
    pullRequest: PullRequest
    ResponseMetadata: ResponseMetadata