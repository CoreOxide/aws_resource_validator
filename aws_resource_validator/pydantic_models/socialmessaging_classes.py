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

class WhatsAppSignupCallbackTypeDef(BaseValidatorModel):
    accessToken: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteWhatsAppMessageMediaInputTypeDef(BaseValidatorModel):
    mediaId: str
    originationPhoneNumberId: str


class WhatsAppPhoneNumberDetailTypeDef(BaseValidatorModel):
    arn: str
    phoneNumber: str
    phoneNumberId: str
    metaPhoneNumberId: str
    displayPhoneNumberName: str
    displayPhoneNumber: str
    qualityRating: str


class S3FileTypeDef(BaseValidatorModel):
    bucketName: str
    key: str


class S3PresignedUrlTypeDef(BaseValidatorModel):
    url: str
    headers: Mapping[str, str]


class WhatsAppBusinessAccountEventDestinationTypeDef(BaseValidatorModel):
    eventDestinationArn: str
    roleArn: Optional[str] = None


class WhatsAppPhoneNumberSummaryTypeDef(BaseValidatorModel):
    arn: str
    phoneNumber: str
    phoneNumberId: str
    metaPhoneNumberId: str
    displayPhoneNumberName: str
    displayPhoneNumber: str
    qualityRating: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListLinkedWhatsAppBusinessAccountsInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str


class TagTypeDef(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class DeleteWhatsAppMessageMediaOutputTypeDef(BaseValidatorModel):
    success: bool
    ResponseMetadata: ResponseMetadataTypeDef


class GetWhatsAppMessageMediaOutputTypeDef(BaseValidatorModel):
    mimeType: str
    fileSize: int
    ResponseMetadata: ResponseMetadataTypeDef


class PostWhatsAppMessageMediaOutputTypeDef(BaseValidatorModel):
    mediaId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SendWhatsAppMessageOutputTypeDef(BaseValidatorModel):
    messageId: str
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceOutputTypeDef(BaseValidatorModel):
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef


class UntagResourceOutputTypeDef(BaseValidatorModel):
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class SendWhatsAppMessageInputTypeDef(BaseValidatorModel):
    originationPhoneNumberId: str
    message: BlobTypeDef
    metaApiVersion: str


class GetLinkedWhatsAppBusinessAccountPhoneNumberOutputTypeDef(BaseValidatorModel):
    phoneNumber: WhatsAppPhoneNumberDetailTypeDef
    linkedWhatsAppBusinessAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef


class LinkedWhatsAppBusinessAccountIdMetaDataTypeDef(BaseValidatorModel):
    accountName: Optional[str] = None
    registrationStatus: Optional[RegistrationStatusType] = None
    unregisteredWhatsAppPhoneNumbers: Optional[List[WhatsAppPhoneNumberDetailTypeDef]] = None
    wabaId: Optional[str] = None


class GetWhatsAppMessageMediaInputTypeDef(BaseValidatorModel):
    mediaId: str
    originationPhoneNumberId: str
    metadataOnly: Optional[bool] = None
    destinationS3PresignedUrl: Optional[S3PresignedUrlTypeDef] = None
    destinationS3File: Optional[S3FileTypeDef] = None


class PostWhatsAppMessageMediaInputTypeDef(BaseValidatorModel):
    originationPhoneNumberId: str
    sourceS3PresignedUrl: Optional[S3PresignedUrlTypeDef] = None
    sourceS3File: Optional[S3FileTypeDef] = None


class ListLinkedWhatsAppBusinessAccountsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    statusCode: int
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class WhatsAppSignupCallbackResultTypeDef(BaseValidatorModel):
    associateInProgressToken: Optional[str] = None
    linkedAccountsWithIncompleteSetup: Optional[ Dict[str, LinkedWhatsAppBusinessAccountIdMetaDataTypeDef] ] = None


class LinkedWhatsAppBusinessAccountSummaryTypeDef(BaseValidatorModel):
    pass


class ListLinkedWhatsAppBusinessAccountsOutputTypeDef(BaseValidatorModel):
    linkedAccounts: List[LinkedWhatsAppBusinessAccountSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class LinkedWhatsAppBusinessAccountTypeDef(BaseValidatorModel):
    pass


class GetLinkedWhatsAppBusinessAccountOutputTypeDef(BaseValidatorModel):
    account: LinkedWhatsAppBusinessAccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class WabaSetupFinalizationTypeDef(BaseValidatorModel):
    pass


class WabaPhoneNumberSetupFinalizationTypeDef(BaseValidatorModel):
    pass


class WhatsAppSetupFinalizationTypeDef(BaseValidatorModel):
    associateInProgressToken: str
    phoneNumbers: Sequence[WabaPhoneNumberSetupFinalizationTypeDef]
    phoneNumberParent: Optional[str] = None
    waba: Optional[WabaSetupFinalizationTypeDef] = None


class AssociateWhatsAppBusinessAccountOutputTypeDef(BaseValidatorModel):
    signupCallbackResult: WhatsAppSignupCallbackResultTypeDef
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateWhatsAppBusinessAccountInputTypeDef(BaseValidatorModel):
    signupCallback: Optional[WhatsAppSignupCallbackTypeDef] = None
    setupFinalization: Optional[WhatsAppSetupFinalizationTypeDef] = None


