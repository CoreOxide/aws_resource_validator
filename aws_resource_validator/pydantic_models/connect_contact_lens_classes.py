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
from aws_resource_validator.pydantic_models.connect_contact_lens_constants import *

class PointOfInterestTypeDef(BaseModel):
    BeginOffsetMillis: int
    EndOffsetMillis: int

class CharacterOffsetsTypeDef(BaseModel):
    BeginOffsetChar: int
    EndOffsetChar: int

class ListRealtimeContactAnalysisSegmentsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CategoryDetailsTypeDef(BaseModel):
    PointsOfInterest: List[PointOfInterestTypeDef]

class IssueDetectedTypeDef(BaseModel):
    CharacterOffsets: CharacterOffsetsTypeDef

class CategoriesTypeDef(BaseModel):
    MatchedCategories: List[str]
    MatchedDetails: Dict[str, CategoryDetailsTypeDef]

class TranscriptTypeDef(BaseModel):
    Id: str
    ParticipantId: str
    ParticipantRole: str
    Content: str
    BeginOffsetMillis: int
    EndOffsetMillis: int
    Sentiment: SentimentValueType
    IssuesDetected: Optional[List[IssueDetectedTypeDef]] = None

class RealtimeContactAnalysisSegmentTypeDef(BaseModel):
    Transcript: Optional[TranscriptTypeDef] = None
    Categories: Optional[CategoriesTypeDef] = None

class ListRealtimeContactAnalysisSegmentsResponseTypeDef(BaseModel):
    Segments: List[RealtimeContactAnalysisSegmentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

