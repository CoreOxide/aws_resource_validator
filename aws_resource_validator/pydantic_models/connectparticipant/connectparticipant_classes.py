from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.connectparticipant.connectparticipant_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AttachmentItem(BaseValidatorModel):
    ContentType: Optional[str] = None
    AttachmentId: Optional[str] = None
    AttachmentName: Optional[str] = None
    Status: Optional[ArtifactStatusType] = None


class CancelParticipantAuthenticationRequest(BaseValidatorModel):
    SessionId: str
    ConnectionToken: str


class CompleteAttachmentUploadRequest(BaseValidatorModel):
    AttachmentIds: List[str]
    ClientToken: str
    ConnectionToken: str


class ConnectionCredentials(BaseValidatorModel):
    ConnectionToken: Optional[str] = None
    Expiry: Optional[str] = None


class CreateParticipantConnectionRequest(BaseValidatorModel):
    ParticipantToken: str
    Type: Optional[List[ConnectionTypeType]] = None
    ConnectParticipant: Optional[bool] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Websocket(BaseValidatorModel):
    Url: Optional[str] = None
    ConnectionExpiry: Optional[str] = None


class DescribeViewRequest(BaseValidatorModel):
    ViewToken: str
    ConnectionToken: str


class DisconnectParticipantRequest(BaseValidatorModel):
    ConnectionToken: str
    ClientToken: Optional[str] = None


class GetAttachmentRequest(BaseValidatorModel):
    AttachmentId: str
    ConnectionToken: str
    UrlExpiryInSeconds: Optional[int] = None


class GetAuthenticationUrlRequest(BaseValidatorModel):
    SessionId: str
    RedirectUri: str
    ConnectionToken: str


class StartPosition(BaseValidatorModel):
    Id: Optional[str] = None
    AbsoluteTime: Optional[str] = None
    MostRecent: Optional[int] = None


class Receipt(BaseValidatorModel):
    DeliveredTimestamp: Optional[str] = None
    ReadTimestamp: Optional[str] = None
    RecipientParticipantId: Optional[str] = None


class SendEventRequest(BaseValidatorModel):
    ContentType: str
    ConnectionToken: str
    Content: Optional[str] = None
    ClientToken: Optional[str] = None


class SendMessageRequest(BaseValidatorModel):
    ContentType: str
    Content: str
    ConnectionToken: str
    ClientToken: Optional[str] = None


class StartAttachmentUploadRequest(BaseValidatorModel):
    ContentType: str
    AttachmentSizeInBytes: int
    AttachmentName: str
    ClientToken: str
    ConnectionToken: str


class UploadMetadata(BaseValidatorModel):
    Url: Optional[str] = None
    UrlExpiry: Optional[str] = None
    HeadersToInclude: Optional[Dict[str, str]] = None


class ViewContent(BaseValidatorModel):
    InputSchema: Optional[str] = None
    Template: Optional[str] = None
    Actions: Optional[List[str]] = None


class GetAttachmentResponse(BaseValidatorModel):
    Url: str
    UrlExpiry: str
    AttachmentSizeInBytes: int
    ResponseMetadata: ResponseMetadata


class GetAuthenticationUrlResponse(BaseValidatorModel):
    AuthenticationUrl: str
    ResponseMetadata: ResponseMetadata


class SendEventResponse(BaseValidatorModel):
    Id: str
    AbsoluteTime: str
    ResponseMetadata: ResponseMetadata


class SendMessageResponse(BaseValidatorModel):
    Id: str
    AbsoluteTime: str
    ResponseMetadata: ResponseMetadata


class CreateParticipantConnectionResponse(BaseValidatorModel):
    Websocket: Websocket
    ConnectionCredentials: ConnectionCredentials
    ResponseMetadata: ResponseMetadata


class GetTranscriptRequest(BaseValidatorModel):
    ConnectionToken: str
    ContactId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ScanDirection: Optional[ScanDirectionType] = None
    SortOrder: Optional[SortKeyType] = None
    StartPosition: Optional[StartPosition] = None


class MessageMetadata(BaseValidatorModel):
    MessageId: Optional[str] = None
    Receipts: Optional[List[Receipt]] = None


class StartAttachmentUploadResponse(BaseValidatorModel):
    AttachmentId: str
    UploadMetadata: UploadMetadata
    ResponseMetadata: ResponseMetadata


class View(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[int] = None
    Content: Optional[ViewContent] = None


class Item(BaseValidatorModel):
    AbsoluteTime: Optional[str] = None
    Content: Optional[str] = None
    ContentType: Optional[str] = None
    Id: Optional[str] = None
    Type: Optional[ChatItemTypeType] = None
    ParticipantId: Optional[str] = None
    DisplayName: Optional[str] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    Attachments: Optional[List[AttachmentItem]] = None
    MessageMetadata: Optional[MessageMetadata] = None
    RelatedContactId: Optional[str] = None
    ContactId: Optional[str] = None


class DescribeViewResponse(BaseValidatorModel):
    View: View
    ResponseMetadata: ResponseMetadata


class GetTranscriptResponse(BaseValidatorModel):
    InitialContactId: str
    Transcript: List[Item]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None