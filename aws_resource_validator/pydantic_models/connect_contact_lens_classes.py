from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class ListRealtimeContactAnalysisSegmentsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

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

class ListRealtimeContactAnalysisSegmentsResponseTypeDef(BaseValidatorModel):
    Segments: List[RealtimeContactAnalysisSegmentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

