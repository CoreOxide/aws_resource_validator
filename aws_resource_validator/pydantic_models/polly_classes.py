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
from aws_resource_validator.pydantic_models.polly_constants import *

class DeleteLexiconInput(BaseValidatorModel):
    Name: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeVoicesInput(BaseValidatorModel):
    Engine: Optional[EngineType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    IncludeAdditionalLanguageCodes: Optional[bool] = None
    NextToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Voice(BaseValidatorModel):
    Gender: Optional[GenderType] = None
    Id: Optional[VoiceIdType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageName: Optional[str] = None
    Name: Optional[str] = None
    AdditionalLanguageCodes: Optional[List[LanguageCodeType]] = None
    SupportedEngines: Optional[List[EngineType]] = None


class GetLexiconInput(BaseValidatorModel):
    Name: str


class LexiconAttributes(BaseValidatorModel):
    Alphabet: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LastModified: Optional[datetime] = None
    LexiconArn: Optional[str] = None
    LexemesCount: Optional[int] = None
    Size: Optional[int] = None


class Lexicon(BaseValidatorModel):
    Content: Optional[str] = None
    Name: Optional[str] = None


class GetSpeechSynthesisTaskInput(BaseValidatorModel):
    TaskId: str


class SynthesisTask(BaseValidatorModel):
    Engine: Optional[EngineType] = None
    TaskId: Optional[str] = None
    TaskStatus: Optional[TaskStatusType] = None
    TaskStatusReason: Optional[str] = None
    OutputUri: Optional[str] = None
    CreationTime: Optional[datetime] = None
    RequestCharacters: Optional[int] = None
    SnsTopicArn: Optional[str] = None
    LexiconNames: Optional[List[str]] = None
    OutputFormat: Optional[OutputFormatType] = None
    SampleRate: Optional[str] = None
    SpeechMarkTypes: Optional[List[SpeechMarkTypeType]] = None
    TextType: Optional[TextTypeType] = None
    VoiceId: Optional[VoiceIdType] = None
    LanguageCode: Optional[LanguageCodeType] = None


class ListLexiconsInput(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListSpeechSynthesisTasksInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Status: Optional[TaskStatusType] = None


class PutLexiconInput(BaseValidatorModel):
    Name: str
    Content: str


class DescribeVoicesInputPaginate(BaseValidatorModel):
    Engine: Optional[EngineType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    IncludeAdditionalLanguageCodes: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLexiconsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSpeechSynthesisTasksInputPaginate(BaseValidatorModel):
    Status: Optional[TaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SynthesizeSpeechOutput(BaseValidatorModel):
    AudioStream: StreamingBody
    ContentType: str
    RequestCharacters: int
    ResponseMetadata: ResponseMetadata


class DescribeVoicesOutput(BaseValidatorModel):
    Voices: List[Voice]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LexiconDescription(BaseValidatorModel):
    Name: Optional[str] = None
    Attributes: Optional[LexiconAttributes] = None


class GetLexiconOutput(BaseValidatorModel):
    Lexicon: Lexicon
    LexiconAttributes: LexiconAttributes
    ResponseMetadata: ResponseMetadata


class GetSpeechSynthesisTaskOutput(BaseValidatorModel):
    SynthesisTask: SynthesisTask
    ResponseMetadata: ResponseMetadata


class ListSpeechSynthesisTasksOutput(BaseValidatorModel):
    SynthesisTasks: List[SynthesisTask]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartSpeechSynthesisTaskOutput(BaseValidatorModel):
    SynthesisTask: SynthesisTask
    ResponseMetadata: ResponseMetadata


class ListLexiconsOutput(BaseValidatorModel):
    Lexicons: List[LexiconDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


