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
from aws_resource_validator.pydantic_models.connect_contact_lens_constants import *

class PointOfInterestTypeDef(BaseValidatorModel):
    BeginOffsetMillis: int
    EndOffsetMillis: int


class CharacterOffsetsTypeDef(BaseValidatorModel):
    BeginOffsetChar: int
    EndOffsetChar: int


class ListRealtimeContactAnalysisSegmentsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class PostContactSummaryTypeDef(BaseValidatorModel):
    Status: PostContactSummaryStatusType
    Content: Optional[str] = None
    FailureCode: Optional[PostContactSummaryFailureCodeType] = None


class CategoryDetailsTypeDef(BaseValidatorModel):
    PointsOfInterest: List[PointOfInterestTypeDef]


class IssueDetectedTypeDef(BaseValidatorModel):
    CharacterOffsets: CharacterOffsetsTypeDef


class CategoriesTypeDef(BaseValidatorModel):
    MatchedCategories: List[str]
    MatchedDetails: Dict[str, CategoryDetailsTypeDef]


class TranscriptTypeDef(BaseValidatorModel):
    Id: str
    ParticipantId: str
    ParticipantRole: str
    Content: str
    BeginOffsetMillis: int
    EndOffsetMillis: int
    Sentiment: SentimentValueType
    IssuesDetected: Optional[List[IssueDetectedTypeDef]] = None


class RealtimeContactAnalysisSegmentTypeDef(BaseValidatorModel):
    Transcript: Optional[TranscriptTypeDef] = None
    Categories: Optional[CategoriesTypeDef] = None
    PostContactSummary: Optional[PostContactSummaryTypeDef] = None


class ListRealtimeContactAnalysisSegmentsResponseTypeDef(BaseValidatorModel):
    Segments: List[RealtimeContactAnalysisSegmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


