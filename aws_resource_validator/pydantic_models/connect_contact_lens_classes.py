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

class PointOfInterest(BaseValidatorModel):
    BeginOffsetMillis: int
    EndOffsetMillis: int


class CharacterOffsets(BaseValidatorModel):
    BeginOffsetChar: int
    EndOffsetChar: int


class ListRealtimeContactAnalysisSegmentsRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class PostContactSummary(BaseValidatorModel):
    Status: PostContactSummaryStatusType
    Content: Optional[str] = None
    FailureCode: Optional[PostContactSummaryFailureCodeType] = None


class CategoryDetails(BaseValidatorModel):
    PointsOfInterest: List[PointOfInterest]


class IssueDetected(BaseValidatorModel):
    CharacterOffsets: CharacterOffsets


class Categories(BaseValidatorModel):
    MatchedCategories: List[str]
    MatchedDetails: Dict[str, CategoryDetails]


class Transcript(BaseValidatorModel):
    Id: str
    ParticipantId: str
    ParticipantRole: str
    Content: str
    BeginOffsetMillis: int
    EndOffsetMillis: int
    Sentiment: SentimentValueType
    IssuesDetected: Optional[List[IssueDetected]] = None


class RealtimeContactAnalysisSegment(BaseValidatorModel):
    Transcript: Optional[Transcript] = None
    Categories: Optional[Categories] = None
    PostContactSummary: Optional[PostContactSummary] = None


class ListRealtimeContactAnalysisSegmentsResponse(BaseValidatorModel):
    Segments: List[RealtimeContactAnalysisSegment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


