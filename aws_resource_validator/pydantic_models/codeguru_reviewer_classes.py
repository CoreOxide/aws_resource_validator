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
from aws_resource_validator.pydantic_models.codeguru_reviewer_constants import *

class KMSKeyDetailsTypeDef(BaseValidatorModel):
    KMSKeyId: Optional[str] = None
    EncryptionOption: Optional[EncryptionOptionType] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BranchDiffSourceCodeTypeTypeDef(BaseValidatorModel):
    SourceBranchName: str
    DestinationBranchName: str


class CodeArtifactsTypeDef(BaseValidatorModel):
    SourceCodeArtifactsObjectKey: str
    BuildArtifactsObjectKey: Optional[str] = None


class CodeCommitRepositoryTypeDef(BaseValidatorModel):
    Name: str


class MetricsSummaryTypeDef(BaseValidatorModel):
    MeteredLinesOfCodeCount: Optional[int] = None
    SuppressedLinesOfCodeCount: Optional[int] = None
    FindingsCount: Optional[int] = None


class MetricsTypeDef(BaseValidatorModel):
    MeteredLinesOfCodeCount: Optional[int] = None
    SuppressedLinesOfCodeCount: Optional[int] = None
    FindingsCount: Optional[int] = None


class CommitDiffSourceCodeTypeTypeDef(BaseValidatorModel):
    SourceCommit: Optional[str] = None
    DestinationCommit: Optional[str] = None
    MergeBaseCommit: Optional[str] = None


class DescribeCodeReviewRequestTypeDef(BaseValidatorModel):
    CodeReviewArn: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeRecommendationFeedbackRequestTypeDef(BaseValidatorModel):
    CodeReviewArn: str
    RecommendationId: str
    UserId: Optional[str] = None


class RecommendationFeedbackTypeDef(BaseValidatorModel):
    CodeReviewArn: Optional[str] = None
    RecommendationId: Optional[str] = None
    Reactions: Optional[List[ReactionType]] = None
    UserId: Optional[str] = None
    CreatedTimeStamp: Optional[datetime] = None
    LastUpdatedTimeStamp: Optional[datetime] = None


class DescribeRepositoryAssociationRequestTypeDef(BaseValidatorModel):
    AssociationArn: str


class DisassociateRepositoryRequestTypeDef(BaseValidatorModel):
    AssociationArn: str


class EventInfoTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    State: Optional[str] = None


class ListRecommendationFeedbackRequestTypeDef(BaseValidatorModel):
    CodeReviewArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    UserIds: Optional[Sequence[str]] = None
    RecommendationIds: Optional[Sequence[str]] = None


class RecommendationFeedbackSummaryTypeDef(BaseValidatorModel):
    RecommendationId: Optional[str] = None
    Reactions: Optional[List[ReactionType]] = None
    UserId: Optional[str] = None


class ListRecommendationsRequestTypeDef(BaseValidatorModel):
    CodeReviewArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListRepositoryAssociationsRequestTypeDef(BaseValidatorModel):
    ProviderTypes: Optional[Sequence[ProviderTypeType]] = None
    States: Optional[Sequence[RepositoryAssociationStateType]] = None
    Names: Optional[Sequence[str]] = None
    Owners: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RepositoryAssociationSummaryTypeDef(BaseValidatorModel):
    AssociationArn: Optional[str] = None
    ConnectionArn: Optional[str] = None
    LastUpdatedTimeStamp: Optional[datetime] = None
    AssociationId: Optional[str] = None
    Name: Optional[str] = None
    Owner: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    State: Optional[RepositoryAssociationStateType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class PutRecommendationFeedbackRequestTypeDef(BaseValidatorModel):
    CodeReviewArn: str
    RecommendationId: str
    Reactions: Sequence[ReactionType]


class RuleMetadataTypeDef(BaseValidatorModel):
    RuleId: Optional[str] = None
    RuleName: Optional[str] = None
    ShortDescription: Optional[str] = None
    LongDescription: Optional[str] = None
    RuleTags: Optional[List[str]] = None


class RepositoryHeadSourceCodeTypeTypeDef(BaseValidatorModel):
    BranchName: str


class S3RepositoryTypeDef(BaseValidatorModel):
    Name: str
    BucketName: str


class ThirdPartySourceRepositoryTypeDef(BaseValidatorModel):
    Name: str
    ConnectionArn: str
    Owner: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    TagKeys: Sequence[str]


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class S3RepositoryDetailsTypeDef(BaseValidatorModel):
    BucketName: Optional[str] = None
    CodeArtifacts: Optional[CodeArtifactsTypeDef] = None


class DescribeCodeReviewRequestWaitTypeDef(BaseValidatorModel):
    CodeReviewArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeRepositoryAssociationRequestWaitTypeDef(BaseValidatorModel):
    AssociationArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeRecommendationFeedbackResponseTypeDef(BaseValidatorModel):
    RecommendationFeedback: RecommendationFeedbackTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RequestMetadataTypeDef(BaseValidatorModel):
    RequestId: Optional[str] = None
    Requester: Optional[str] = None
    EventInfo: Optional[EventInfoTypeDef] = None
    VendorName: Optional[VendorNameType] = None


class ListRecommendationFeedbackResponseTypeDef(BaseValidatorModel):
    RecommendationFeedbackSummaries: List[RecommendationFeedbackSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRepositoryAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    ProviderTypes: Optional[Sequence[ProviderTypeType]] = None
    States: Optional[Sequence[RepositoryAssociationStateType]] = None
    Names: Optional[Sequence[str]] = None
    Owners: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRepositoryAssociationsResponseTypeDef(BaseValidatorModel):
    RepositoryAssociationSummaries: List[RepositoryAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RecommendationSummaryTypeDef(BaseValidatorModel):
    FilePath: Optional[str] = None
    RecommendationId: Optional[str] = None
    StartLine: Optional[int] = None
    EndLine: Optional[int] = None
    Description: Optional[str] = None
    RecommendationCategory: Optional[RecommendationCategoryType] = None
    RuleMetadata: Optional[RuleMetadataTypeDef] = None
    Severity: Optional[SeverityType] = None


class RepositoryTypeDef(BaseValidatorModel):
    CodeCommit: Optional[CodeCommitRepositoryTypeDef] = None
    Bitbucket: Optional[ThirdPartySourceRepositoryTypeDef] = None
    GitHubEnterpriseServer: Optional[ThirdPartySourceRepositoryTypeDef] = None
    S3Bucket: Optional[S3RepositoryTypeDef] = None


class RepositoryAssociationTypeDef(BaseValidatorModel):
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
    KMSKeyDetails: Optional[KMSKeyDetailsTypeDef] = None
    S3RepositoryDetails: Optional[S3RepositoryDetailsTypeDef] = None


class S3BucketRepositoryTypeDef(BaseValidatorModel):
    Name: str
    Details: Optional[S3RepositoryDetailsTypeDef] = None


class ListRecommendationsResponseTypeDef(BaseValidatorModel):
    RecommendationSummaries: List[RecommendationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AssociateRepositoryRequestTypeDef(BaseValidatorModel):
    Repository: RepositoryTypeDef
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    KMSKeyDetails: Optional[KMSKeyDetailsTypeDef] = None


class AssociateRepositoryResponseTypeDef(BaseValidatorModel):
    RepositoryAssociation: RepositoryAssociationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRepositoryAssociationResponseTypeDef(BaseValidatorModel):
    RepositoryAssociation: RepositoryAssociationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateRepositoryResponseTypeDef(BaseValidatorModel):
    RepositoryAssociation: RepositoryAssociationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class SourceCodeTypeTypeDef(BaseValidatorModel):
    CommitDiff: Optional[CommitDiffSourceCodeTypeTypeDef] = None
    RepositoryHead: Optional[RepositoryHeadSourceCodeTypeTypeDef] = None
    BranchDiff: Optional[BranchDiffSourceCodeTypeTypeDef] = None
    S3BucketRepository: Optional[S3BucketRepositoryTypeDef] = None
    RequestMetadata: Optional[RequestMetadataTypeDef] = None


class RepositoryAnalysisTypeDef(BaseValidatorModel):
    RepositoryHead: Optional[RepositoryHeadSourceCodeTypeTypeDef] = None
    SourceCodeType: Optional[SourceCodeTypeTypeDef] = None


class CodeReviewSummaryTypeDef(BaseValidatorModel):
    pass


class ListCodeReviewsResponseTypeDef(BaseValidatorModel):
    CodeReviewSummaries: List[CodeReviewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CodeReviewTypeDef(BaseValidatorModel):
    pass


class CreateCodeReviewResponseTypeDef(BaseValidatorModel):
    CodeReview: CodeReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCodeReviewResponseTypeDef(BaseValidatorModel):
    CodeReview: CodeReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CodeReviewTypeTypeDef(BaseValidatorModel):
    RepositoryAnalysis: RepositoryAnalysisTypeDef
    AnalysisTypes: Optional[Sequence[AnalysisTypeType]] = None


