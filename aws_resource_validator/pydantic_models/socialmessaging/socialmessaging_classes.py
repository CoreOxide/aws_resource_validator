from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.socialmessaging.socialmessaging_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class WhatsAppSignupCallback(BaseValidatorModel):
    accessToken: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class DeleteWhatsAppMessageMediaInput(BaseValidatorModel):
    mediaId: str
    originationPhoneNumberId: str


class DisassociateWhatsAppBusinessAccountInput(BaseValidatorModel):
    id: str


class GetLinkedWhatsAppBusinessAccountInput(BaseValidatorModel):
    id: str


class GetLinkedWhatsAppBusinessAccountPhoneNumberInput(BaseValidatorModel):
    id: str


class WhatsAppPhoneNumberDetail(BaseValidatorModel):
    arn: str
    phoneNumber: str
    phoneNumberId: str
    metaPhoneNumberId: str
    displayPhoneNumberName: str
    displayPhoneNumber: str
    qualityRating: str


class S3File(BaseValidatorModel):
    bucketName: str
    key: str


class S3PresignedUrl(BaseValidatorModel):
    url: str
    headers: Dict[str, str]


class WhatsAppBusinessAccountEventDestination(BaseValidatorModel):
    eventDestinationArn: str
    roleArn: Optional[str] = None


class WhatsAppPhoneNumberSummary(BaseValidatorModel):
    arn: str
    phoneNumber: str
    phoneNumberId: str
    metaPhoneNumberId: str
    displayPhoneNumberName: str
    displayPhoneNumber: str
    qualityRating: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListLinkedWhatsAppBusinessAccountsInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class Tag(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class DeleteWhatsAppMessageMediaOutput(BaseValidatorModel):
    success: bool
    ResponseMetadata: ResponseMetadata


class GetWhatsAppMessageMediaOutput(BaseValidatorModel):
    mimeType: str
    fileSize: int
    ResponseMetadata: ResponseMetadata


class PostWhatsAppMessageMediaOutput(BaseValidatorModel):
    mediaId: str
    ResponseMetadata: ResponseMetadata


class SendWhatsAppMessageOutput(BaseValidatorModel):
    messageId: str
    ResponseMetadata: ResponseMetadata


class TagResourceOutput(BaseValidatorModel):
    statusCode: int
    ResponseMetadata: ResponseMetadata


class UntagResourceOutput(BaseValidatorModel):
    statusCode: int
    ResponseMetadata: ResponseMetadata


class SendWhatsAppMessageInput(BaseValidatorModel):
    originationPhoneNumberId: str
    message: Blob
    metaApiVersion: str


class GetLinkedWhatsAppBusinessAccountPhoneNumberOutput(BaseValidatorModel):
    phoneNumber: WhatsAppPhoneNumberDetail
    linkedWhatsAppBusinessAccountId: str
    ResponseMetadata: ResponseMetadata


class LinkedWhatsAppBusinessAccountIdMetaData(BaseValidatorModel):
    accountName: Optional[str] = None
    registrationStatus: Optional[RegistrationStatusType] = None
    unregisteredWhatsAppPhoneNumbers: Optional[List[WhatsAppPhoneNumberDetail]] = None
    wabaId: Optional[str] = None


class GetWhatsAppMessageMediaInput(BaseValidatorModel):
    mediaId: str
    originationPhoneNumberId: str
    metadataOnly: Optional[bool] = None
    destinationS3PresignedUrl: Optional[S3PresignedUrl] = None
    destinationS3File: Optional[S3File] = None


class PostWhatsAppMessageMediaInput(BaseValidatorModel):
    originationPhoneNumberId: str
    sourceS3PresignedUrl: Optional[S3PresignedUrl] = None
    sourceS3File: Optional[S3File] = None


class LinkedWhatsAppBusinessAccountSummary(BaseValidatorModel):
    arn: str
    id: str
    wabaId: str
    registrationStatus: RegistrationStatusType
    linkDate: datetime
    wabaName: str
    eventDestinations: List[WhatsAppBusinessAccountEventDestination]


class PutWhatsAppBusinessAccountEventDestinationsInput(BaseValidatorModel):
    id: str
    eventDestinations: List[WhatsAppBusinessAccountEventDestination]


class LinkedWhatsAppBusinessAccount(BaseValidatorModel):
    arn: str
    id: str
    wabaId: str
    registrationStatus: RegistrationStatusType
    linkDate: datetime
    wabaName: str
    eventDestinations: List[WhatsAppBusinessAccountEventDestination]
    phoneNumbers: List[WhatsAppPhoneNumberSummary]


class ListLinkedWhatsAppBusinessAccountsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    statusCode: int
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


class WabaPhoneNumberSetupFinalization(BaseValidatorModel):
    id: str
    twoFactorPin: str
    dataLocalizationRegion: Optional[str] = None
    tags: Optional[List[Tag]] = None


class WabaSetupFinalization(BaseValidatorModel):
    id: Optional[str] = None
    eventDestinations: Optional[List[WhatsAppBusinessAccountEventDestination]] = None
    tags: Optional[List[Tag]] = None


class WhatsAppSignupCallbackResult(BaseValidatorModel):
    associateInProgressToken: Optional[str] = None
    linkedAccountsWithIncompleteSetup: Optional[Dict[str, LinkedWhatsAppBusinessAccountIdMetaData]] = None


class ListLinkedWhatsAppBusinessAccountsOutput(BaseValidatorModel):
    linkedAccounts: List[LinkedWhatsAppBusinessAccountSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetLinkedWhatsAppBusinessAccountOutput(BaseValidatorModel):
    account: LinkedWhatsAppBusinessAccount
    ResponseMetadata: ResponseMetadata


class WhatsAppSetupFinalization(BaseValidatorModel):
    associateInProgressToken: str
    phoneNumbers: List[WabaPhoneNumberSetupFinalization]
    phoneNumberParent: Optional[str] = None
    waba: Optional[WabaSetupFinalization] = None


class AssociateWhatsAppBusinessAccountOutput(BaseValidatorModel):
    signupCallbackResult: WhatsAppSignupCallbackResult
    statusCode: int
    ResponseMetadata: ResponseMetadata


class AssociateWhatsAppBusinessAccountInput(BaseValidatorModel):
    signupCallback: Optional[WhatsAppSignupCallback] = None
    setupFinalization: Optional[WhatsAppSetupFinalization] = None