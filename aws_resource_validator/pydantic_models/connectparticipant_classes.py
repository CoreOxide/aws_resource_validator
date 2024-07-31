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
from aws_resource_validator.pydantic_models.connectparticipant_constants import *

class AttachmentItemTypeDef(BaseModel):
    ContentType: Optional[str] = None
    AttachmentId: Optional[str] = None
    AttachmentName: Optional[str] = None
    Status: Optional[ArtifactStatusType] = None

class CompleteAttachmentUploadRequestRequestTypeDef(BaseModel):
    AttachmentIds: Sequence[str]
    ClientToken: str
    ConnectionToken: str

class ConnectionCredentialsTypeDef(BaseModel):
    ConnectionToken: Optional[str] = None
    Expiry: Optional[str] = None

class CreateParticipantConnectionRequestRequestTypeDef(BaseModel):
    ParticipantToken: str
    Type: Optional[Sequence[ConnectionTypeType]] = None
    ConnectParticipant: Optional[bool] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class WebsocketTypeDef(BaseModel):
    Url: Optional[str] = None
    ConnectionExpiry: Optional[str] = None

class DescribeViewRequestRequestTypeDef(BaseModel):
    ViewToken: str
    ConnectionToken: str

class DisconnectParticipantRequestRequestTypeDef(BaseModel):
    ConnectionToken: str
    ClientToken: Optional[str] = None

class GetAttachmentRequestRequestTypeDef(BaseModel):
    AttachmentId: str
    ConnectionToken: str

class StartPositionTypeDef(BaseModel):
    Id: Optional[str] = None
    AbsoluteTime: Optional[str] = None
    MostRecent: Optional[int] = None

class ReceiptTypeDef(BaseModel):
    DeliveredTimestamp: Optional[str] = None
    ReadTimestamp: Optional[str] = None
    RecipientParticipantId: Optional[str] = None

class SendEventRequestRequestTypeDef(BaseModel):
    ContentType: str
    ConnectionToken: str
    Content: Optional[str] = None
    ClientToken: Optional[str] = None

class SendMessageRequestRequestTypeDef(BaseModel):
    ContentType: str
    Content: str
    ConnectionToken: str
    ClientToken: Optional[str] = None

class StartAttachmentUploadRequestRequestTypeDef(BaseModel):
    ContentType: str
    AttachmentSizeInBytes: int
    AttachmentName: str
    ClientToken: str
    ConnectionToken: str

class UploadMetadataTypeDef(BaseModel):
    Url: Optional[str] = None
    UrlExpiry: Optional[str] = None
    HeadersToInclude: Optional[Dict[str, str]] = None

class ViewContentTypeDef(BaseModel):
    InputSchema: Optional[str] = None
    Template: Optional[str] = None
    Actions: Optional[List[str]] = None

class GetAttachmentResponseTypeDef(BaseModel):
    Url: str
    UrlExpiry: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendEventResponseTypeDef(BaseModel):
    Id: str
    AbsoluteTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendMessageResponseTypeDef(BaseModel):
    Id: str
    AbsoluteTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateParticipantConnectionResponseTypeDef(BaseModel):
    Websocket: WebsocketTypeDef
    ConnectionCredentials: ConnectionCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTranscriptRequestRequestTypeDef(BaseModel):
    ConnectionToken: str
    ContactId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ScanDirection: Optional[ScanDirectionType] = None
    SortOrder: Optional[SortKeyType] = None
    StartPosition: Optional[StartPositionTypeDef] = None

class MessageMetadataTypeDef(BaseModel):
    MessageId: Optional[str] = None
    Receipts: Optional[List[ReceiptTypeDef]] = None

class StartAttachmentUploadResponseTypeDef(BaseModel):
    AttachmentId: str
    UploadMetadata: UploadMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ViewTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[int] = None
    Content: Optional[ViewContentTypeDef] = None

class ItemTypeDef(BaseModel):
    AbsoluteTime: Optional[str] = None
    Content: Optional[str] = None
    ContentType: Optional[str] = None
    Id: Optional[str] = None
    Type: Optional[ChatItemTypeType] = None
    ParticipantId: Optional[str] = None
    DisplayName: Optional[str] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    Attachments: Optional[List[AttachmentItemTypeDef]] = None
    MessageMetadata: Optional[MessageMetadataTypeDef] = None
    RelatedContactId: Optional[str] = None
    ContactId: Optional[str] = None

class DescribeViewResponseTypeDef(BaseModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTranscriptResponseTypeDef(BaseModel):
    InitialContactId: str
    Transcript: List[ItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

