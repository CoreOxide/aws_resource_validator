from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.codeguru_reviewer.codeguru_reviewer_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class KMSKeyDetails(BaseValidatorModel):
    KMSKeyId: Optional[str] = None
    EncryptionOption: Optional[EncryptionOptionType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BranchDiffSourceCodeType(BaseValidatorModel):
    SourceBranchName: str
    DestinationBranchName: str


class CodeArtifacts(BaseValidatorModel):
    SourceCodeArtifactsObjectKey: str
    BuildArtifactsObjectKey: Optional[str] = None


class CodeCommitRepository(BaseValidatorModel):
    Name: str


class MetricsSummary(BaseValidatorModel):
    MeteredLinesOfCodeCount: Optional[int] = None
    SuppressedLinesOfCodeCount: Optional[int] = None
    FindingsCount: Optional[int] = None


class Metrics(BaseValidatorModel):
    MeteredLinesOfCodeCount: Optional[int] = None
    SuppressedLinesOfCodeCount: Optional[int] = None
    FindingsCount: Optional[int] = None


class CommitDiffSourceCodeType(BaseValidatorModel):
    SourceCommit: Optional[str] = None
    DestinationCommit: Optional[str] = None
    MergeBaseCommit: Optional[str] = None


# This class is the input for the 'describe_code_review' function.
class DescribeCodeReviewRequest(BaseValidatorModel):
    CodeReviewArn: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_recommendation_feedback' function.
class DescribeRecommendationFeedbackRequest(BaseValidatorModel):
    CodeReviewArn: str
    RecommendationId: str
    UserId: Optional[str] = None


class RecommendationFeedback(BaseValidatorModel):
    CodeReviewArn: Optional[str] = None
    RecommendationId: Optional[str] = None
    Reactions: Optional[List[ReactionType]] = None
    UserId: Optional[str] = None
    CreatedTimeStamp: Optional[datetime] = None
    LastUpdatedTimeStamp: Optional[datetime] = None


# This class is the input for the 'describe_repository_association' function.
class DescribeRepositoryAssociationRequest(BaseValidatorModel):
    AssociationArn: str


# This class is the input for the 'disassociate_repository' function.
class DisassociateRepositoryRequest(BaseValidatorModel):
    AssociationArn: str


class EventInfo(BaseValidatorModel):
    Name: Optional[str] = None
    State: Optional[str] = None


# This class is the input for the 'list_code_reviews' function.
class ListCodeReviewsRequest(BaseValidatorModel):
    Type: TypeType
    ProviderTypes: Optional[List[ProviderTypeType]] = None
    States: Optional[List[JobStateType]] = None
    RepositoryNames: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_recommendation_feedback' function.
class ListRecommendationFeedbackRequest(BaseValidatorModel):
    CodeReviewArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    UserIds: Optional[List[str]] = None
    RecommendationIds: Optional[List[str]] = None


class RecommendationFeedbackSummary(BaseValidatorModel):
    RecommendationId: Optional[str] = None
    Reactions: Optional[List[ReactionType]] = None
    UserId: Optional[str] = None


# This class is the input for the 'list_recommendations' function.
class ListRecommendationsRequest(BaseValidatorModel):
    CodeReviewArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_repository_associations' function.
class ListRepositoryAssociationsRequest(BaseValidatorModel):
    ProviderTypes: Optional[List[ProviderTypeType]] = None
    States: Optional[List[RepositoryAssociationStateType]] = None
    Names: Optional[List[str]] = None
    Owners: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RepositoryAssociationSummary(BaseValidatorModel):
    AssociationArn: Optional[str] = None
    ConnectionArn: Optional[str] = None
    LastUpdatedTimeStamp: Optional[datetime] = None
    AssociationId: Optional[str] = None
    Name: Optional[str] = None
    Owner: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    State: Optional[RepositoryAssociationStateType] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class PutRecommendationFeedbackRequest(BaseValidatorModel):
    CodeReviewArn: str
    RecommendationId: str
    Reactions: List[ReactionType]


class RuleMetadata(BaseValidatorModel):
    RuleId: Optional[str] = None
    RuleName: Optional[str] = None
    ShortDescription: Optional[str] = None
    LongDescription: Optional[str] = None
    RuleTags: Optional[List[str]] = None


class RepositoryHeadSourceCodeType(BaseValidatorModel):
    BranchName: str


class S3Repository(BaseValidatorModel):
    Name: str
    BucketName: str


class ThirdPartySourceRepository(BaseValidatorModel):
    Name: str
    ConnectionArn: str
    Owner: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    TagKeys: List[str]


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class S3RepositoryDetails(BaseValidatorModel):
    BucketName: Optional[str] = None
    CodeArtifacts: Optional[CodeArtifacts] = None


class DescribeCodeReviewRequestWait(BaseValidatorModel):
    CodeReviewArn: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeRepositoryAssociationRequestWait(BaseValidatorModel):
    AssociationArn: str
    WaiterConfig: Optional[WaiterConfig] = None


# This class is the output for the 'describe_recommendation_feedback' function.
class DescribeRecommendationFeedbackResponse(BaseValidatorModel):
    RecommendationFeedback: RecommendationFeedback
    ResponseMetadata: ResponseMetadata


class RequestMetadata(BaseValidatorModel):
    RequestId: Optional[str] = None
    Requester: Optional[str] = None
    EventInfo: Optional[EventInfo] = None
    VendorName: Optional[VendorNameType] = None


# This class is the output for the 'list_recommendation_feedback' function.
class ListRecommendationFeedbackResponse(BaseValidatorModel):
    RecommendationFeedbackSummaries: List[RecommendationFeedbackSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRepositoryAssociationsRequestPaginate(BaseValidatorModel):
    ProviderTypes: Optional[List[ProviderTypeType]] = None
    States: Optional[List[RepositoryAssociationStateType]] = None
    Names: Optional[List[str]] = None
    Owners: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_repository_associations' function.
class ListRepositoryAssociationsResponse(BaseValidatorModel):
    RepositoryAssociationSummaries: List[RepositoryAssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RecommendationSummary(BaseValidatorModel):
    FilePath: Optional[str] = None
    RecommendationId: Optional[str] = None
    StartLine: Optional[int] = None
    EndLine: Optional[int] = None
    Description: Optional[str] = None
    RecommendationCategory: Optional[RecommendationCategoryType] = None
    RuleMetadata: Optional[RuleMetadata] = None
    Severity: Optional[SeverityType] = None


class Repository(BaseValidatorModel):
    CodeCommit: Optional[CodeCommitRepository] = None
    Bitbucket: Optional[ThirdPartySourceRepository] = None
    GitHubEnterpriseServer: Optional[ThirdPartySourceRepository] = None
    S3Bucket: Optional[S3Repository] = None


class RepositoryAssociation(BaseValidatorModel):
    AssociationId: Optional[str] = None
    AssociationArn: Optional[str] = None
    ConnectionArn: Optional[str] = None
    Name: Optional[str] = None
    Owner: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    State: Optional[RepositoryAssociationStateType] = None
    StateReason: Optional[str] = None
    LastUpdatedTimeStamp: Optional[datetime] = None
    CreatedTimeStamp: Optional[datetime] = None
    KMSKeyDetails: Optional[KMSKeyDetails] = None
    S3RepositoryDetails: Optional[S3RepositoryDetails] = None


class S3BucketRepository(BaseValidatorModel):
    Name: str
    Details: Optional[S3RepositoryDetails] = None


# This class is the output for the 'list_recommendations' function.
class ListRecommendationsResponse(BaseValidatorModel):
    RecommendationSummaries: List[RecommendationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'associate_repository' function.
class AssociateRepositoryRequest(BaseValidatorModel):
    Repository: Repository
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    KMSKeyDetails: Optional[KMSKeyDetails] = None


# This class is the output for the 'associate_repository' function.
class AssociateRepositoryResponse(BaseValidatorModel):
    RepositoryAssociation: RepositoryAssociation
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_repository_association' function.
class DescribeRepositoryAssociationResponse(BaseValidatorModel):
    RepositoryAssociation: RepositoryAssociation
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_repository' function.
class DisassociateRepositoryResponse(BaseValidatorModel):
    RepositoryAssociation: RepositoryAssociation
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class SourceCodeType(BaseValidatorModel):
    CommitDiff: Optional[CommitDiffSourceCodeType] = None
    RepositoryHead: Optional[RepositoryHeadSourceCodeType] = None
    BranchDiff: Optional[BranchDiffSourceCodeType] = None
    S3BucketRepository: Optional[S3BucketRepository] = None
    RequestMetadata: Optional[RequestMetadata] = None


class CodeReviewSummary(BaseValidatorModel):
    Name: Optional[str] = None
    CodeReviewArn: Optional[str] = None
    RepositoryName: Optional[str] = None
    Owner: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    State: Optional[JobStateType] = None
    CreatedTimeStamp: Optional[datetime] = None
    LastUpdatedTimeStamp: Optional[datetime] = None
    Type: Optional[TypeType] = None
    PullRequestId: Optional[str] = None
    MetricsSummary: Optional[MetricsSummary] = None
    SourceCodeType: Optional[SourceCodeType] = None


class CodeReview(BaseValidatorModel):
    Name: Optional[str] = None
    CodeReviewArn: Optional[str] = None
    RepositoryName: Optional[str] = None
    Owner: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    State: Optional[JobStateType] = None
    StateReason: Optional[str] = None
    CreatedTimeStamp: Optional[datetime] = None
    LastUpdatedTimeStamp: Optional[datetime] = None
    Type: Optional[TypeType] = None
    PullRequestId: Optional[str] = None
    SourceCodeType: Optional[SourceCodeType] = None
    AssociationArn: Optional[str] = None
    Metrics: Optional[Metrics] = None
    AnalysisTypes: Optional[List[AnalysisTypeType]] = None
    ConfigFileState: Optional[ConfigFileStateType] = None


class RepositoryAnalysis(BaseValidatorModel):
    RepositoryHead: Optional[RepositoryHeadSourceCodeType] = None
    SourceCodeType: Optional[SourceCodeType] = None


# This class is the output for the 'list_code_reviews' function.
class ListCodeReviewsResponse(BaseValidatorModel):
    CodeReviewSummaries: List[CodeReviewSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_code_review' function.
class CreateCodeReviewResponse(BaseValidatorModel):
    CodeReview: CodeReview
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_code_review' function.
class DescribeCodeReviewResponse(BaseValidatorModel):
    CodeReview: CodeReview
    ResponseMetadata: ResponseMetadata


class CodeReviewType(BaseValidatorModel):
    RepositoryAnalysis: RepositoryAnalysis
    AnalysisTypes: Optional[List[AnalysisTypeType]] = None


# This class is the input for the 'create_code_review' function.
class CreateCodeReviewRequest(BaseValidatorModel):
    Name: str
    RepositoryAssociationArn: str
    Type: CodeReviewType
    ClientRequestToken: Optional[str] = None