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
from aws_resource_validator.pydantic_models.sns_constants import *

class AddPermissionInputTopicAddPermissionTypeDef(BaseValidatorModel):
    Label: str
    AWSAccountId: Sequence[str]
    ActionName: Sequence[str]


class AddPermissionInputTypeDef(BaseValidatorModel):
    TopicArn: str
    Label: str
    AWSAccountId: Sequence[str]
    ActionName: Sequence[str]


class BatchResultErrorEntryTypeDef(BaseValidatorModel):
    Id: str
    Code: str
    SenderFault: bool
    Message: Optional[str] = None


class CheckIfPhoneNumberIsOptedOutInputTypeDef(BaseValidatorModel):
    phoneNumber: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ConfirmSubscriptionInputTopicConfirmSubscriptionTypeDef(BaseValidatorModel):
    Token: str
    AuthenticateOnUnsubscribe: Optional[str] = None


class ConfirmSubscriptionInputTypeDef(BaseValidatorModel):
    TopicArn: str
    Token: str
    AuthenticateOnUnsubscribe: Optional[str] = None


class CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationTypeDef(BaseValidatorModel):
    Name: str
    Platform: str
    Attributes: Mapping[str, str]


class CreatePlatformApplicationInputTypeDef(BaseValidatorModel):
    Name: str
    Platform: str
    Attributes: Mapping[str, str]


class CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointTypeDef(BaseValidatorModel):
    Token: str
    CustomUserData: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None


class CreatePlatformEndpointInputTypeDef(BaseValidatorModel):
    PlatformApplicationArn: str
    Token: str
    CustomUserData: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None


class CreateSMSSandboxPhoneNumberInputTypeDef(BaseValidatorModel):
    PhoneNumber: str
    LanguageCode: Optional[LanguageCodeStringType] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class DeleteEndpointInputTypeDef(BaseValidatorModel):
    EndpointArn: str


class DeletePlatformApplicationInputTypeDef(BaseValidatorModel):
    PlatformApplicationArn: str


class DeleteSMSSandboxPhoneNumberInputTypeDef(BaseValidatorModel):
    PhoneNumber: str


class DeleteTopicInputTypeDef(BaseValidatorModel):
    TopicArn: str


class EndpointTypeDef(BaseValidatorModel):
    EndpointArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class GetDataProtectionPolicyInputTypeDef(BaseValidatorModel):
    ResourceArn: str


class GetEndpointAttributesInputTypeDef(BaseValidatorModel):
    EndpointArn: str


class GetPlatformApplicationAttributesInputTypeDef(BaseValidatorModel):
    PlatformApplicationArn: str


class GetSMSAttributesInputTypeDef(BaseValidatorModel):
    attributes: Optional[Sequence[str]] = None


class GetSubscriptionAttributesInputTypeDef(BaseValidatorModel):
    SubscriptionArn: str


class GetTopicAttributesInputTypeDef(BaseValidatorModel):
    TopicArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListEndpointsByPlatformApplicationInputTypeDef(BaseValidatorModel):
    PlatformApplicationArn: str
    NextToken: Optional[str] = None


class ListOriginationNumbersRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PhoneNumberInformationTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    PhoneNumber: Optional[str] = None
    Status: Optional[str] = None
    Iso2CountryCode: Optional[str] = None
    RouteType: Optional[RouteTypeType] = None
    NumberCapabilities: Optional[List[NumberCapabilityType]] = None


class ListPhoneNumbersOptedOutInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None


class ListPlatformApplicationsInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class PlatformApplicationTypeDef(BaseValidatorModel):
    PlatformApplicationArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class ListSMSSandboxPhoneNumbersInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SMSSandboxPhoneNumberTypeDef(BaseValidatorModel):
    PhoneNumber: Optional[str] = None
    Status: Optional[SMSSandboxPhoneNumberVerificationStatusType] = None


class ListSubscriptionsByTopicInputTypeDef(BaseValidatorModel):
    TopicArn: str
    NextToken: Optional[str] = None


class ListSubscriptionsInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListTopicsInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class TopicTypeDef(BaseValidatorModel):
    TopicArn: Optional[str] = None


class OptInPhoneNumberInputTypeDef(BaseValidatorModel):
    phoneNumber: str


class PublishBatchResultEntryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    MessageId: Optional[str] = None
    SequenceNumber: Optional[str] = None


class PutDataProtectionPolicyInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    DataProtectionPolicy: str


class RemovePermissionInputTopicRemovePermissionTypeDef(BaseValidatorModel):
    Label: str


class RemovePermissionInputTypeDef(BaseValidatorModel):
    TopicArn: str
    Label: str


class SetEndpointAttributesInputPlatformEndpointSetAttributesTypeDef(BaseValidatorModel):
    Attributes: Mapping[str, str]


class SetEndpointAttributesInputTypeDef(BaseValidatorModel):
    EndpointArn: str
    Attributes: Mapping[str, str]


class SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesTypeDef(BaseValidatorModel):
    Attributes: Mapping[str, str]


class SetPlatformApplicationAttributesInputTypeDef(BaseValidatorModel):
    PlatformApplicationArn: str
    Attributes: Mapping[str, str]


class SetSMSAttributesInputTypeDef(BaseValidatorModel):
    attributes: Mapping[str, str]


class SetSubscriptionAttributesInputSubscriptionSetAttributesTypeDef(BaseValidatorModel):
    AttributeName: str
    AttributeValue: Optional[str] = None


class SetSubscriptionAttributesInputTypeDef(BaseValidatorModel):
    SubscriptionArn: str
    AttributeName: str
    AttributeValue: Optional[str] = None


class SetTopicAttributesInputTopicSetAttributesTypeDef(BaseValidatorModel):
    AttributeName: str
    AttributeValue: Optional[str] = None


class SetTopicAttributesInputTypeDef(BaseValidatorModel):
    TopicArn: str
    AttributeName: str
    AttributeValue: Optional[str] = None


class UnsubscribeInputTypeDef(BaseValidatorModel):
    SubscriptionArn: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class VerifySMSSandboxPhoneNumberInputTypeDef(BaseValidatorModel):
    PhoneNumber: str
    OneTimePassword: str


class BlobTypeDef(BaseValidatorModel):
    pass


class MessageAttributeValueTypeDef(BaseValidatorModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[BlobTypeDef] = None


class CheckIfPhoneNumberIsOptedOutResponseTypeDef(BaseValidatorModel):
    isOptedOut: bool
    ResponseMetadata: ResponseMetadataTypeDef


class ConfirmSubscriptionResponseTypeDef(BaseValidatorModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEndpointResponseTypeDef(BaseValidatorModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePlatformApplicationResponseTypeDef(BaseValidatorModel):
    PlatformApplicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTopicResponseTypeDef(BaseValidatorModel):
    TopicArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetDataProtectionPolicyResponseTypeDef(BaseValidatorModel):
    DataProtectionPolicy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetEndpointAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetPlatformApplicationAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetSMSAttributesResponseTypeDef(BaseValidatorModel):
    attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetSMSSandboxAccountStatusResultTypeDef(BaseValidatorModel):
    IsInSandbox: bool
    ResponseMetadata: ResponseMetadataTypeDef


class GetSubscriptionAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetTopicAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListPhoneNumbersOptedOutResponseTypeDef(BaseValidatorModel):
    phoneNumbers: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PublishResponseTypeDef(BaseValidatorModel):
    MessageId: str
    SequenceNumber: str
    ResponseMetadata: ResponseMetadataTypeDef


class SubscribeResponseTypeDef(BaseValidatorModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTopicInputServiceResourceCreateTopicTypeDef(BaseValidatorModel):
    Name: str
    Attributes: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataProtectionPolicy: Optional[str] = None


class CreateTopicInputTypeDef(BaseValidatorModel):
    Name: str
    Attributes: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataProtectionPolicy: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class ListEndpointsByPlatformApplicationResponseTypeDef(BaseValidatorModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListEndpointsByPlatformApplicationInputPaginateTypeDef(BaseValidatorModel):
    PlatformApplicationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOriginationNumbersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPhoneNumbersOptedOutInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPlatformApplicationsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSMSSandboxPhoneNumbersInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSubscriptionsByTopicInputPaginateTypeDef(BaseValidatorModel):
    TopicArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSubscriptionsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTopicsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOriginationNumbersResultTypeDef(BaseValidatorModel):
    PhoneNumbers: List[PhoneNumberInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPlatformApplicationsResponseTypeDef(BaseValidatorModel):
    PlatformApplications: List[PlatformApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSMSSandboxPhoneNumbersResultTypeDef(BaseValidatorModel):
    PhoneNumbers: List[SMSSandboxPhoneNumberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SubscriptionTypeDef(BaseValidatorModel):
    pass


class ListSubscriptionsByTopicResponseTypeDef(BaseValidatorModel):
    Subscriptions: List[SubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSubscriptionsResponseTypeDef(BaseValidatorModel):
    Subscriptions: List[SubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTopicsResponseTypeDef(BaseValidatorModel):
    Topics: List[TopicTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PublishBatchResponseTypeDef(BaseValidatorModel):
    Successful: List[PublishBatchResultEntryTypeDef]
    Failed: List[BatchResultErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PublishBatchRequestEntryTypeDef(BaseValidatorModel):
    Id: str
    Message: str
    Subject: Optional[str] = None
    MessageStructure: Optional[str] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None


class PublishInputPlatformEndpointPublishTypeDef(BaseValidatorModel):
    Message: str
    TopicArn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Subject: Optional[str] = None
    MessageStructure: Optional[str] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None


class PublishInputTopicPublishTypeDef(BaseValidatorModel):
    Message: str
    TargetArn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Subject: Optional[str] = None
    MessageStructure: Optional[str] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None


class PublishInputTypeDef(BaseValidatorModel):
    Message: str
    TopicArn: Optional[str] = None
    TargetArn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Subject: Optional[str] = None
    MessageStructure: Optional[str] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None


class PublishBatchInputTypeDef(BaseValidatorModel):
    TopicArn: str
    PublishBatchRequestEntries: Sequence[PublishBatchRequestEntryTypeDef]


