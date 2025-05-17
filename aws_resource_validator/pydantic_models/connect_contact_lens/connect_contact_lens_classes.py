from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.connect_contact_lens.connect_contact_lens_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class PointOfInterest(BaseValidatorModel):
    BeginOffsetMillis: int
    EndOffsetMillis: int


class CharacterOffsets(BaseValidatorModel):
    BeginOffsetChar: int
    EndOffsetChar: int


# This class is the input for the 'list_realtime_contact_analysis_segments' function.
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


# This class is the output for the 'list_realtime_contact_analysis_segments' function.
class ListRealtimeContactAnalysisSegmentsResponse(BaseValidatorModel):
    Segments: List[RealtimeContactAnalysisSegment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None