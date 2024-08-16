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
from aws_resource_validator.pydantic_models.connectparticipant_constants import *

class AttachmentItemTypeDef(BaseValidatorModel):
    ContentType: Optional[str] = None
    AttachmentId: Optional[str] = None
    AttachmentName: Optional[str] = None
    Status: Optional[ArtifactStatusType] = None

class CompleteAttachmentUploadRequestRequestTypeDef(BaseValidatorModel):
    AttachmentIds: Sequence[str]
    ClientToken: str
    ConnectionToken: str

class ConnectionCredentialsTypeDef(BaseValidatorModel):
    ConnectionToken: Optional[str] = None
    Expiry: Optional[str] = None

class CreateParticipantConnectionRequestRequestTypeDef(BaseValidatorModel):
    ParticipantToken: str
    Type: Optional[Sequence[ConnectionTypeType]] = None
    ConnectParticipant: Optional[bool] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class WebsocketTypeDef(BaseValidatorModel):
    Url: Optional[str] = None
    ConnectionExpiry: Optional[str] = None

class DescribeViewRequestRequestTypeDef(BaseValidatorModel):
    ViewToken: str
    ConnectionToken: str

class DisconnectParticipantRequestRequestTypeDef(BaseValidatorModel):
    ConnectionToken: str
    ClientToken: Optional[str] = None

class GetAttachmentRequestRequestTypeDef(BaseValidatorModel):
    AttachmentId: str
    ConnectionToken: str

class StartPositionTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    AbsoluteTime: Optional[str] = None
    MostRecent: Optional[int] = None

class ReceiptTypeDef(BaseValidatorModel):
    DeliveredTimestamp: Optional[str] = None
    ReadTimestamp: Optional[str] = None
    RecipientParticipantId: Optional[str] = None

class SendEventRequestRequestTypeDef(BaseValidatorModel):
    ContentType: str
    ConnectionToken: str
    Content: Optional[str] = None
    ClientToken: Optional[str] = None

class SendMessageRequestRequestTypeDef(BaseValidatorModel):
    ContentType: str
    Content: str
    ConnectionToken: str
    ClientToken: Optional[str] = None

class StartAttachmentUploadRequestRequestTypeDef(BaseValidatorModel):
    ContentType: str
    AttachmentSizeInBytes: int
    AttachmentName: str
    ClientToken: str
    ConnectionToken: str

class UploadMetadataTypeDef(BaseValidatorModel):
    Url: Optional[str] = None
    UrlExpiry: Optional[str] = None
    HeadersToInclude: Optional[Dict[str, str]] = None

class ViewContentTypeDef(BaseValidatorModel):
    InputSchema: Optional[str] = None
    Template: Optional[str] = None
    Actions: Optional[List[str]] = None

class GetAttachmentResponseTypeDef(BaseValidatorModel):
    Url: str
    UrlExpiry: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendEventResponseTypeDef(BaseValidatorModel):
    Id: str
    AbsoluteTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendMessageResponseTypeDef(BaseValidatorModel):
    Id: str
    AbsoluteTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateParticipantConnectionResponseTypeDef(BaseValidatorModel):
    Websocket: WebsocketTypeDef
    ConnectionCredentials: ConnectionCredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTranscriptRequestRequestTypeDef(BaseValidatorModel):
    ConnectionToken: str
    ContactId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ScanDirection: Optional[ScanDirectionType] = None
    SortOrder: Optional[SortKeyType] = None
    StartPosition: Optional[StartPositionTypeDef] = None

class MessageMetadataTypeDef(BaseValidatorModel):
    MessageId: Optional[str] = None
    Receipts: Optional[List[ReceiptTypeDef]] = None

class StartAttachmentUploadResponseTypeDef(BaseValidatorModel):
    AttachmentId: str
    UploadMetadata: UploadMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ViewTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[int] = None
    Content: Optional[ViewContentTypeDef] = None

class ItemTypeDef(BaseValidatorModel):
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

class DescribeViewResponseTypeDef(BaseValidatorModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTranscriptResponseTypeDef(BaseValidatorModel):
    InitialContactId: str
    Transcript: List[ItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

