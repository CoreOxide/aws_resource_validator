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
from aws_resource_validator.pydantic_models.connectparticipant_constants import *

class AttachmentItemTypeDef(BaseValidatorModel):
    ContentType: Optional[str] = None
    AttachmentId: Optional[str] = None
    AttachmentName: Optional[str] = None
    Status: Optional[ArtifactStatusType] = None


class CancelParticipantAuthenticationRequestTypeDef(BaseValidatorModel):
    SessionId: str
    ConnectionToken: str


class CompleteAttachmentUploadRequestTypeDef(BaseValidatorModel):
    AttachmentIds: Sequence[str]
    ClientToken: str
    ConnectionToken: str


class ConnectionCredentialsTypeDef(BaseValidatorModel):
    ConnectionToken: Optional[str] = None
    Expiry: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class WebsocketTypeDef(BaseValidatorModel):
    Url: Optional[str] = None
    ConnectionExpiry: Optional[str] = None


class DescribeViewRequestTypeDef(BaseValidatorModel):
    ViewToken: str
    ConnectionToken: str


class DisconnectParticipantRequestTypeDef(BaseValidatorModel):
    ConnectionToken: str
    ClientToken: Optional[str] = None


class GetAttachmentRequestTypeDef(BaseValidatorModel):
    AttachmentId: str
    ConnectionToken: str
    UrlExpiryInSeconds: Optional[int] = None


class GetAuthenticationUrlRequestTypeDef(BaseValidatorModel):
    SessionId: str
    RedirectUri: str
    ConnectionToken: str


class StartPositionTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    AbsoluteTime: Optional[str] = None
    MostRecent: Optional[int] = None


class ReceiptTypeDef(BaseValidatorModel):
    DeliveredTimestamp: Optional[str] = None
    ReadTimestamp: Optional[str] = None
    RecipientParticipantId: Optional[str] = None


class SendEventRequestTypeDef(BaseValidatorModel):
    ContentType: str
    ConnectionToken: str
    Content: Optional[str] = None
    ClientToken: Optional[str] = None


class SendMessageRequestTypeDef(BaseValidatorModel):
    ContentType: str
    Content: str
    ConnectionToken: str
    ClientToken: Optional[str] = None


class StartAttachmentUploadRequestTypeDef(BaseValidatorModel):
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
    AttachmentSizeInBytes: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetAuthenticationUrlResponseTypeDef(BaseValidatorModel):
    AuthenticationUrl: str
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


class GetTranscriptRequestTypeDef(BaseValidatorModel):
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


class DescribeViewResponseTypeDef(BaseValidatorModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ItemTypeDef(BaseValidatorModel):
    pass


class GetTranscriptResponseTypeDef(BaseValidatorModel):
    InitialContactId: str
    Transcript: List[ItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


