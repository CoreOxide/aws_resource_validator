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

class DeleteLexiconInputTypeDef(BaseValidatorModel):
    Name: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeVoicesInputTypeDef(BaseValidatorModel):
    Engine: Optional[EngineType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    IncludeAdditionalLanguageCodes: Optional[bool] = None
    NextToken: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class VoiceTypeDef(BaseValidatorModel):
    Gender: Optional[GenderType] = None
    Id: Optional[VoiceIdType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageName: Optional[str] = None
    Name: Optional[str] = None
    AdditionalLanguageCodes: Optional[List[LanguageCodeType]] = None
    SupportedEngines: Optional[List[EngineType]] = None


class GetLexiconInputTypeDef(BaseValidatorModel):
    Name: str


class LexiconAttributesTypeDef(BaseValidatorModel):
    Alphabet: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LastModified: Optional[datetime] = None
    LexiconArn: Optional[str] = None
    LexemesCount: Optional[int] = None
    Size: Optional[int] = None


class LexiconTypeDef(BaseValidatorModel):
    Content: Optional[str] = None
    Name: Optional[str] = None


class GetSpeechSynthesisTaskInputTypeDef(BaseValidatorModel):
    TaskId: str


class SynthesisTaskTypeDef(BaseValidatorModel):
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


class ListLexiconsInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListSpeechSynthesisTasksInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Status: Optional[TaskStatusType] = None


class PutLexiconInputTypeDef(BaseValidatorModel):
    Name: str
    Content: str


class DescribeVoicesInputPaginateTypeDef(BaseValidatorModel):
    Engine: Optional[EngineType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    IncludeAdditionalLanguageCodes: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLexiconsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSpeechSynthesisTasksInputPaginateTypeDef(BaseValidatorModel):
    Status: Optional[TaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SynthesizeSpeechOutputTypeDef(BaseValidatorModel):
    AudioStream: StreamingBody
    ContentType: str
    RequestCharacters: int
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeVoicesOutputTypeDef(BaseValidatorModel):
    Voices: List[VoiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LexiconDescriptionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Attributes: Optional[LexiconAttributesTypeDef] = None


class GetLexiconOutputTypeDef(BaseValidatorModel):
    Lexicon: LexiconTypeDef
    LexiconAttributes: LexiconAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSpeechSynthesisTaskOutputTypeDef(BaseValidatorModel):
    SynthesisTask: SynthesisTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListSpeechSynthesisTasksOutputTypeDef(BaseValidatorModel):
    SynthesisTasks: List[SynthesisTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StartSpeechSynthesisTaskOutputTypeDef(BaseValidatorModel):
    SynthesisTask: SynthesisTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListLexiconsOutputTypeDef(BaseValidatorModel):
    Lexicons: List[LexiconDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


