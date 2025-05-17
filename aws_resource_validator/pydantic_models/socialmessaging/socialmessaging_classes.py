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


# This class is the input for the 'delete_whatsapp_media_message' function.
class DeleteWhatsAppMessageMediaInput(BaseValidatorModel):
    mediaId: str
    originationPhoneNumberId: str


class DisassociateWhatsAppBusinessAccountInput(BaseValidatorModel):
    id: str


# This class is the input for the 'get_linked_whatsapp_business_account' function.
class GetLinkedWhatsAppBusinessAccountInput(BaseValidatorModel):
    id: str


# This class is the input for the 'get_linked_whatsapp_business_account_phone_number' function.
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


# This class is the input for the 'list_linked_whatsapp_business_accounts' function.
class ListLinkedWhatsAppBusinessAccountsInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class Tag(BaseValidatorModel):
    key: str
    value: Optional[str] = None


# This class is the input for the 'untag_resource' function.
class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the output for the 'delete_whatsapp_media_message' function.
class DeleteWhatsAppMessageMediaOutput(BaseValidatorModel):
    success: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_whatsapp_message_media' function.
class GetWhatsAppMessageMediaOutput(BaseValidatorModel):
    mimeType: str
    fileSize: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'post_whatsapp_message_media' function.
class PostWhatsAppMessageMediaOutput(BaseValidatorModel):
    mediaId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_whatsapp_message' function.
class SendWhatsAppMessageOutput(BaseValidatorModel):
    messageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'tag_resource' function.
class TagResourceOutput(BaseValidatorModel):
    statusCode: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class UntagResourceOutput(BaseValidatorModel):
    statusCode: int
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'send_whatsapp_message' function.
class SendWhatsAppMessageInput(BaseValidatorModel):
    originationPhoneNumberId: str
    message: Blob
    metaApiVersion: str


# This class is the output for the 'get_linked_whatsapp_business_account_phone_number' function.
class GetLinkedWhatsAppBusinessAccountPhoneNumberOutput(BaseValidatorModel):
    phoneNumber: WhatsAppPhoneNumberDetail
    linkedWhatsAppBusinessAccountId: str
    ResponseMetadata: ResponseMetadata


class LinkedWhatsAppBusinessAccountIdMetaData(BaseValidatorModel):
    accountName: Optional[str] = None
    registrationStatus: Optional[RegistrationStatusType] = None
    unregisteredWhatsAppPhoneNumbers: Optional[List[WhatsAppPhoneNumberDetail]] = None
    wabaId: Optional[str] = None


# This class is the input for the 'get_whatsapp_message_media' function.
class GetWhatsAppMessageMediaInput(BaseValidatorModel):
    mediaId: str
    originationPhoneNumberId: str
    metadataOnly: Optional[bool] = None
    destinationS3PresignedUrl: Optional[S3PresignedUrl] = None
    destinationS3File: Optional[S3File] = None


# This class is the input for the 'post_whatsapp_message_media' function.
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


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    statusCode: int
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'tag_resource' function.
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


# This class is the output for the 'list_linked_whatsapp_business_accounts' function.
class ListLinkedWhatsAppBusinessAccountsOutput(BaseValidatorModel):
    linkedAccounts: List[LinkedWhatsAppBusinessAccountSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_linked_whatsapp_business_account' function.
class GetLinkedWhatsAppBusinessAccountOutput(BaseValidatorModel):
    account: LinkedWhatsAppBusinessAccount
    ResponseMetadata: ResponseMetadata


class WhatsAppSetupFinalization(BaseValidatorModel):
    associateInProgressToken: str
    phoneNumbers: List[WabaPhoneNumberSetupFinalization]
    phoneNumberParent: Optional[str] = None
    waba: Optional[WabaSetupFinalization] = None


# This class is the output for the 'associate_whatsapp_business_account' function.
class AssociateWhatsAppBusinessAccountOutput(BaseValidatorModel):
    signupCallbackResult: WhatsAppSignupCallbackResult
    statusCode: int
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'associate_whatsapp_business_account' function.
class AssociateWhatsAppBusinessAccountInput(BaseValidatorModel):
    signupCallback: Optional[WhatsAppSignupCallback] = None
    setupFinalization: Optional[WhatsAppSetupFinalization] = None