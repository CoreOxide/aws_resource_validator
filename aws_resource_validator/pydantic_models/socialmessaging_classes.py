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
from aws_resource_validator.pydantic_models.socialmessaging_constants import *

class WhatsAppSignupCallback(BaseValidatorModel):
    accessToken: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteWhatsAppMessageMediaInput(BaseValidatorModel):
    mediaId: str
    originationPhoneNumberId: str


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
    headers: Mapping[str, str]


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
    tagKeys: Sequence[str]


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


class Blob(BaseValidatorModel):
    pass


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


class ListLinkedWhatsAppBusinessAccountsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    statusCode: int
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[Tag]


class WhatsAppSignupCallbackResult(BaseValidatorModel):
    associateInProgressToken: Optional[str] = None
    linkedAccountsWithIncompleteSetup: Optional[ Dict[str, LinkedWhatsAppBusinessAccountIdMetaData] ] = None


class LinkedWhatsAppBusinessAccountSummary(BaseValidatorModel):
    pass


class ListLinkedWhatsAppBusinessAccountsOutput(BaseValidatorModel):
    linkedAccounts: List[LinkedWhatsAppBusinessAccountSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class LinkedWhatsAppBusinessAccount(BaseValidatorModel):
    pass


class GetLinkedWhatsAppBusinessAccountOutput(BaseValidatorModel):
    account: LinkedWhatsAppBusinessAccount
    ResponseMetadata: ResponseMetadata


class WabaSetupFinalization(BaseValidatorModel):
    pass


class WabaPhoneNumberSetupFinalization(BaseValidatorModel):
    pass


class WhatsAppSetupFinalization(BaseValidatorModel):
    associateInProgressToken: str
    phoneNumbers: Sequence[WabaPhoneNumberSetupFinalization]
    phoneNumberParent: Optional[str] = None
    waba: Optional[WabaSetupFinalization] = None


class AssociateWhatsAppBusinessAccountOutput(BaseValidatorModel):
    signupCallbackResult: WhatsAppSignupCallbackResult
    statusCode: int
    ResponseMetadata: ResponseMetadata


class AssociateWhatsAppBusinessAccountInput(BaseValidatorModel):
    signupCallback: Optional[WhatsAppSignupCallback] = None
    setupFinalization: Optional[WhatsAppSetupFinalization] = None


