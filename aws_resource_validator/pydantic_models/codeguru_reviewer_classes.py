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
from aws_resource_validator.pydantic_models.codeguru_reviewer_constants import *

class KMSKeyDetailsTypeDef(BaseModel):
    KMSKeyId: Optional[str] = None
    EncryptionOption: Optional[EncryptionOptionType] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BranchDiffSourceCodeTypeTypeDef(BaseModel):
    SourceBranchName: str
    DestinationBranchName: str

class CodeArtifactsTypeDef(BaseModel):
    SourceCodeArtifactsObjectKey: str
    BuildArtifactsObjectKey: Optional[str] = None

class CodeCommitRepositoryTypeDef(BaseModel):
    Name: str

class MetricsSummaryTypeDef(BaseModel):
    MeteredLinesOfCodeCount: Optional[int] = None
    SuppressedLinesOfCodeCount: Optional[int] = None
    FindingsCount: Optional[int] = None

class MetricsTypeDef(BaseModel):
    MeteredLinesOfCodeCount: Optional[int] = None
    SuppressedLinesOfCodeCount: Optional[int] = None
    FindingsCount: Optional[int] = None

class CommitDiffSourceCodeTypeTypeDef(BaseModel):
    SourceCommit: Optional[str] = None
    DestinationCommit: Optional[str] = None
    MergeBaseCommit: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeCodeReviewRequestRequestTypeDef(BaseModel):
    CodeReviewArn: str

class DescribeRecommendationFeedbackRequestRequestTypeDef(BaseModel):
    CodeReviewArn: str
    RecommendationId: str
    UserId: Optional[str] = None

class RecommendationFeedbackTypeDef(BaseModel):
    CodeReviewArn: Optional[str] = None
    RecommendationId: Optional[str] = None
    Reactions: Optional[List[ReactionType]] = None
    UserId: Optional[str] = None
    CreatedTimeStamp: Optional[datetime] = None
    LastUpdatedTimeStamp: Optional[datetime] = None

class DescribeRepositoryAssociationRequestRequestTypeDef(BaseModel):
    AssociationArn: str

class DisassociateRepositoryRequestRequestTypeDef(BaseModel):
    AssociationArn: str

class EventInfoTypeDef(BaseModel):
    Name: Optional[str] = None
    State: Optional[str] = None

class ListCodeReviewsRequestRequestTypeDef(BaseModel):
    Type: TypeType
    ProviderTypes: Optional[Sequence[ProviderTypeType]] = None
    States: Optional[Sequence[JobStateType]] = None
    RepositoryNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRecommendationFeedbackRequestRequestTypeDef(BaseModel):
    CodeReviewArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    UserIds: Optional[Sequence[str]] = None
    RecommendationIds: Optional[Sequence[str]] = None

class RecommendationFeedbackSummaryTypeDef(BaseModel):
    RecommendationId: Optional[str] = None
    Reactions: Optional[List[ReactionType]] = None
    UserId: Optional[str] = None

class ListRecommendationsRequestRequestTypeDef(BaseModel):
    CodeReviewArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListRepositoryAssociationsRequestRequestTypeDef(BaseModel):
    ProviderTypes: Optional[Sequence[ProviderTypeType]] = None
    States: Optional[Sequence[RepositoryAssociationStateType]] = None
    Names: Optional[Sequence[str]] = None
    Owners: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RepositoryAssociationSummaryTypeDef(BaseModel):
    AssociationArn: Optional[str] = None
    ConnectionArn: Optional[str] = None
    LastUpdatedTimeStamp: Optional[datetime] = None
    AssociationId: Optional[str] = None
    Name: Optional[str] = None
    Owner: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    State: Optional[RepositoryAssociationStateType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class PutRecommendationFeedbackRequestRequestTypeDef(BaseModel):
    CodeReviewArn: str
    RecommendationId: str
    Reactions: Sequence[ReactionType]

class RuleMetadataTypeDef(BaseModel):
    RuleId: Optional[str] = None
    RuleName: Optional[str] = None
    ShortDescription: Optional[str] = None
    LongDescription: Optional[str] = None
    RuleTags: Optional[List[str]] = None

class RepositoryHeadSourceCodeTypeTypeDef(BaseModel):
    BranchName: str

class S3RepositoryTypeDef(BaseModel):
    Name: str
    BucketName: str

class ThirdPartySourceRepositoryTypeDef(BaseModel):
    Name: str
    ConnectionArn: str
    Owner: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    TagKeys: Sequence[str]

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class S3RepositoryDetailsTypeDef(BaseModel):
    BucketName: Optional[str] = None
    CodeArtifacts: Optional[CodeArtifactsTypeDef] = None

class DescribeCodeReviewRequestCodeReviewCompletedWaitTypeDef(BaseModel):
    CodeReviewArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeRepositoryAssociationRequestRepositoryAssociationSucceededWaitTypeDef(BaseModel):
    AssociationArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeRecommendationFeedbackResponseTypeDef(BaseModel):
    RecommendationFeedback: RecommendationFeedbackTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RequestMetadataTypeDef(BaseModel):
    RequestId: Optional[str] = None
    Requester: Optional[str] = None
    EventInfo: Optional[EventInfoTypeDef] = None
    VendorName: Optional[VendorNameType] = None

class ListRecommendationFeedbackResponseTypeDef(BaseModel):
    RecommendationFeedbackSummaries: List[RecommendationFeedbackSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositoryAssociationsRequestListRepositoryAssociationsPaginateTypeDef(BaseModel):
    ProviderTypes: Optional[Sequence[ProviderTypeType]] = None
    States: Optional[Sequence[RepositoryAssociationStateType]] = None
    Names: Optional[Sequence[str]] = None
    Owners: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRepositoryAssociationsResponseTypeDef(BaseModel):
    RepositoryAssociationSummaries: List[RepositoryAssociationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecommendationSummaryTypeDef(BaseModel):
    FilePath: Optional[str] = None
    RecommendationId: Optional[str] = None
    StartLine: Optional[int] = None
    EndLine: Optional[int] = None
    Description: Optional[str] = None
    RecommendationCategory: Optional[RecommendationCategoryType] = None
    RuleMetadata: Optional[RuleMetadataTypeDef] = None
    Severity: Optional[SeverityType] = None

class RepositoryTypeDef(BaseModel):
    CodeCommit: Optional[CodeCommitRepositoryTypeDef] = None
    Bitbucket: Optional[ThirdPartySourceRepositoryTypeDef] = None
    GitHubEnterpriseServer: Optional[ThirdPartySourceRepositoryTypeDef] = None
    S3Bucket: Optional[S3RepositoryTypeDef] = None

class RepositoryAssociationTypeDef(BaseModel):
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

class S3BucketRepositoryTypeDef(BaseModel):
    Name: str
    Details: Optional[S3RepositoryDetailsTypeDef] = None

class ListRecommendationsResponseTypeDef(BaseModel):
    RecommendationSummaries: List[RecommendationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateRepositoryRequestRequestTypeDef(BaseModel):
    Repository: RepositoryTypeDef
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    KMSKeyDetails: Optional[KMSKeyDetailsTypeDef] = None

class AssociateRepositoryResponseTypeDef(BaseModel):
    RepositoryAssociation: RepositoryAssociationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRepositoryAssociationResponseTypeDef(BaseModel):
    RepositoryAssociation: RepositoryAssociationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateRepositoryResponseTypeDef(BaseModel):
    RepositoryAssociation: RepositoryAssociationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SourceCodeTypeTypeDef(BaseModel):
    CommitDiff: Optional[CommitDiffSourceCodeTypeTypeDef] = None
    RepositoryHead: Optional[RepositoryHeadSourceCodeTypeTypeDef] = None
    BranchDiff: Optional[BranchDiffSourceCodeTypeTypeDef] = None
    S3BucketRepository: Optional[S3BucketRepositoryTypeDef] = None
    RequestMetadata: Optional[RequestMetadataTypeDef] = None

class CodeReviewSummaryTypeDef(BaseModel):
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
    MetricsSummary: Optional[MetricsSummaryTypeDef] = None
    SourceCodeType: Optional[SourceCodeTypeTypeDef] = None

class CodeReviewTypeDef(BaseModel):
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
    SourceCodeType: Optional[SourceCodeTypeTypeDef] = None
    AssociationArn: Optional[str] = None
    Metrics: Optional[MetricsTypeDef] = None
    AnalysisTypes: Optional[List[AnalysisTypeType]] = None
    ConfigFileState: Optional[ConfigFileStateType] = None

class RepositoryAnalysisTypeDef(BaseModel):
    RepositoryHead: Optional[RepositoryHeadSourceCodeTypeTypeDef] = None
    SourceCodeType: Optional[SourceCodeTypeTypeDef] = None

class ListCodeReviewsResponseTypeDef(BaseModel):
    CodeReviewSummaries: List[CodeReviewSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCodeReviewResponseTypeDef(BaseModel):
    CodeReview: CodeReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCodeReviewResponseTypeDef(BaseModel):
    CodeReview: CodeReviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CodeReviewTypeTypeDef(BaseModel):
    RepositoryAnalysis: RepositoryAnalysisTypeDef
    AnalysisTypes: Optional[Sequence[AnalysisTypeType]] = None

class CreateCodeReviewRequestRequestTypeDef(BaseModel):
    Name: str
    RepositoryAssociationArn: str
    Type: CodeReviewTypeTypeDef
    ClientRequestToken: Optional[str] = None

