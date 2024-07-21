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
from aws_resource_validator.pydantic_models.polly_constants import *

class DeleteLexiconInputRequestTypeDef(BaseModel):
    Name: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeVoicesInputRequestTypeDef(BaseModel):
    Engine: Optional[EngineType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    IncludeAdditionalLanguageCodes: Optional[bool] = None
    NextToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class VoiceTypeDef(BaseModel):
    Gender: Optional[GenderType] = None
    Id: Optional[VoiceIdType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LanguageName: Optional[str] = None
    Name: Optional[str] = None
    AdditionalLanguageCodes: Optional[List[LanguageCodeType]] = None
    SupportedEngines: Optional[List[EngineType]] = None

class GetLexiconInputRequestTypeDef(BaseModel):
    Name: str

class LexiconAttributesTypeDef(BaseModel):
    Alphabet: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LastModified: Optional[datetime] = None
    LexiconArn: Optional[str] = None
    LexemesCount: Optional[int] = None
    Size: Optional[int] = None

class LexiconTypeDef(BaseModel):
    Content: Optional[str] = None
    Name: Optional[str] = None

class GetSpeechSynthesisTaskInputRequestTypeDef(BaseModel):
    TaskId: str

class SynthesisTaskTypeDef(BaseModel):
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

class ListLexiconsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class ListSpeechSynthesisTasksInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Status: Optional[TaskStatusType] = None

class PutLexiconInputRequestTypeDef(BaseModel):
    Name: str
    Content: str

class StartSpeechSynthesisTaskInputRequestTypeDef(BaseModel):
    OutputFormat: OutputFormatType
    OutputS3BucketName: str
    Text: str
    VoiceId: VoiceIdType
    Engine: Optional[EngineType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LexiconNames: Optional[Sequence[str]] = None
    OutputS3KeyPrefix: Optional[str] = None
    SampleRate: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    SpeechMarkTypes: Optional[Sequence[SpeechMarkTypeType]] = None
    TextType: Optional[TextTypeType] = None

class SynthesizeSpeechInputRequestTypeDef(BaseModel):
    OutputFormat: OutputFormatType
    Text: str
    VoiceId: VoiceIdType
    Engine: Optional[EngineType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LexiconNames: Optional[Sequence[str]] = None
    SampleRate: Optional[str] = None
    SpeechMarkTypes: Optional[Sequence[SpeechMarkTypeType]] = None
    TextType: Optional[TextTypeType] = None

class DescribeVoicesInputDescribeVoicesPaginateTypeDef(BaseModel):
    Engine: Optional[EngineType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    IncludeAdditionalLanguageCodes: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLexiconsInputListLexiconsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSpeechSynthesisTasksInputListSpeechSynthesisTasksPaginateTypeDef(BaseModel):
    Status: Optional[TaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SynthesizeSpeechOutputTypeDef(BaseModel):
    AudioStream: StreamingBody
    ContentType: str
    RequestCharacters: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVoicesOutputTypeDef(BaseModel):
    Voices: List[VoiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LexiconDescriptionTypeDef(BaseModel):
    Name: Optional[str] = None
    Attributes: Optional[LexiconAttributesTypeDef] = None

class GetLexiconOutputTypeDef(BaseModel):
    Lexicon: LexiconTypeDef
    LexiconAttributes: LexiconAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSpeechSynthesisTaskOutputTypeDef(BaseModel):
    SynthesisTask: SynthesisTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSpeechSynthesisTasksOutputTypeDef(BaseModel):
    SynthesisTasks: List[SynthesisTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartSpeechSynthesisTaskOutputTypeDef(BaseModel):
    SynthesisTask: SynthesisTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLexiconsOutputTypeDef(BaseModel):
    Lexicons: List[LexiconDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

