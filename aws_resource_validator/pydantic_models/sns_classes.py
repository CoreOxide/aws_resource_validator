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
from aws_resource_validator.pydantic_models.sns_constants import *

class AddPermissionInputRequestTypeDef(BaseModel):
    TopicArn: str
    Label: str
    AWSAccountId: Sequence[str]
    ActionName: Sequence[str]

class AddPermissionInputTopicAddPermissionTypeDef(BaseModel):
    Label: str
    AWSAccountId: Sequence[str]
    ActionName: Sequence[str]

class BatchResultErrorEntryTypeDef(BaseModel):
    Id: str
    Code: str
    SenderFault: bool
    Message: Optional[str] = None

class CheckIfPhoneNumberIsOptedOutInputRequestTypeDef(BaseModel):
    phoneNumber: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ConfirmSubscriptionInputRequestTypeDef(BaseModel):
    TopicArn: str
    Token: str
    AuthenticateOnUnsubscribe: Optional[str] = None

class ConfirmSubscriptionInputTopicConfirmSubscriptionTypeDef(BaseModel):
    Token: str
    AuthenticateOnUnsubscribe: Optional[str] = None

class CreatePlatformApplicationInputRequestTypeDef(BaseModel):
    Name: str
    Platform: str
    Attributes: Mapping[str, str]

class CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationTypeDef(BaseModel):
    Name: str
    Platform: str
    Attributes: Mapping[str, str]

class CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointTypeDef(BaseModel):
    Token: str
    CustomUserData: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None

class CreatePlatformEndpointInputRequestTypeDef(BaseModel):
    PlatformApplicationArn: str
    Token: str
    CustomUserData: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None

class CreateSMSSandboxPhoneNumberInputRequestTypeDef(BaseModel):
    PhoneNumber: str
    LanguageCode: Optional[LanguageCodeStringType] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class DeleteEndpointInputRequestTypeDef(BaseModel):
    EndpointArn: str

class DeletePlatformApplicationInputRequestTypeDef(BaseModel):
    PlatformApplicationArn: str

class DeleteSMSSandboxPhoneNumberInputRequestTypeDef(BaseModel):
    PhoneNumber: str

class DeleteTopicInputRequestTypeDef(BaseModel):
    TopicArn: str

class EndpointTypeDef(BaseModel):
    EndpointArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None

class GetDataProtectionPolicyInputRequestTypeDef(BaseModel):
    ResourceArn: str

class GetEndpointAttributesInputRequestTypeDef(BaseModel):
    EndpointArn: str

class GetPlatformApplicationAttributesInputRequestTypeDef(BaseModel):
    PlatformApplicationArn: str

class GetSMSAttributesInputRequestTypeDef(BaseModel):
    attributes: Optional[Sequence[str]] = None

class GetSubscriptionAttributesInputRequestTypeDef(BaseModel):
    SubscriptionArn: str

class GetTopicAttributesInputRequestTypeDef(BaseModel):
    TopicArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListEndpointsByPlatformApplicationInputRequestTypeDef(BaseModel):
    PlatformApplicationArn: str
    NextToken: Optional[str] = None

class ListOriginationNumbersRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PhoneNumberInformationTypeDef(BaseModel):
    CreatedAt: Optional[datetime] = None
    PhoneNumber: Optional[str] = None
    Status: Optional[str] = None
    Iso2CountryCode: Optional[str] = None
    RouteType: Optional[RouteTypeType] = None
    NumberCapabilities: Optional[List[NumberCapabilityType]] = None

class ListPhoneNumbersOptedOutInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None

class ListPlatformApplicationsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class PlatformApplicationTypeDef(BaseModel):
    PlatformApplicationArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None

class ListSMSSandboxPhoneNumbersInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SMSSandboxPhoneNumberTypeDef(BaseModel):
    PhoneNumber: Optional[str] = None
    Status: Optional[SMSSandboxPhoneNumberVerificationStatusType] = None

class ListSubscriptionsByTopicInputRequestTypeDef(BaseModel):
    TopicArn: str
    NextToken: Optional[str] = None

class SubscriptionTypeDef(BaseModel):
    SubscriptionArn: Optional[str] = None
    Owner: Optional[str] = None
    Protocol: Optional[str] = None
    Endpoint: Optional[str] = None
    TopicArn: Optional[str] = None

class ListSubscriptionsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListTopicsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class TopicTypeDef(BaseModel):
    TopicArn: Optional[str] = None

class OptInPhoneNumberInputRequestTypeDef(BaseModel):
    phoneNumber: str

class PublishBatchResultEntryTypeDef(BaseModel):
    Id: Optional[str] = None
    MessageId: Optional[str] = None
    SequenceNumber: Optional[str] = None

class PutDataProtectionPolicyInputRequestTypeDef(BaseModel):
    ResourceArn: str
    DataProtectionPolicy: str

class RemovePermissionInputRequestTypeDef(BaseModel):
    TopicArn: str
    Label: str

class RemovePermissionInputTopicRemovePermissionTypeDef(BaseModel):
    Label: str

class SetEndpointAttributesInputPlatformEndpointSetAttributesTypeDef(BaseModel):
    Attributes: Mapping[str, str]

class SetEndpointAttributesInputRequestTypeDef(BaseModel):
    EndpointArn: str
    Attributes: Mapping[str, str]

class SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesTypeDef(BaseModel):
    Attributes: Mapping[str, str]

class SetPlatformApplicationAttributesInputRequestTypeDef(BaseModel):
    PlatformApplicationArn: str
    Attributes: Mapping[str, str]

class SetSMSAttributesInputRequestTypeDef(BaseModel):
    attributes: Mapping[str, str]

class SetSubscriptionAttributesInputRequestTypeDef(BaseModel):
    SubscriptionArn: str
    AttributeName: str
    AttributeValue: Optional[str] = None

class SetSubscriptionAttributesInputSubscriptionSetAttributesTypeDef(BaseModel):
    AttributeName: str
    AttributeValue: Optional[str] = None

class SetTopicAttributesInputRequestTypeDef(BaseModel):
    TopicArn: str
    AttributeName: str
    AttributeValue: Optional[str] = None

class SetTopicAttributesInputTopicSetAttributesTypeDef(BaseModel):
    AttributeName: str
    AttributeValue: Optional[str] = None

class SubscribeInputRequestTypeDef(BaseModel):
    TopicArn: str
    Protocol: str
    Endpoint: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    ReturnSubscriptionArn: Optional[bool] = None

class SubscribeInputTopicSubscribeTypeDef(BaseModel):
    Protocol: str
    Endpoint: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    ReturnSubscriptionArn: Optional[bool] = None

class UnsubscribeInputRequestTypeDef(BaseModel):
    SubscriptionArn: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class VerifySMSSandboxPhoneNumberInputRequestTypeDef(BaseModel):
    PhoneNumber: str
    OneTimePassword: str

class MessageAttributeValueTypeDef(BaseModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[BlobTypeDef] = None

class CheckIfPhoneNumberIsOptedOutResponseTypeDef(BaseModel):
    isOptedOut: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ConfirmSubscriptionResponseTypeDef(BaseModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointResponseTypeDef(BaseModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePlatformApplicationResponseTypeDef(BaseModel):
    PlatformApplicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicResponseTypeDef(BaseModel):
    TopicArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataProtectionPolicyResponseTypeDef(BaseModel):
    DataProtectionPolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEndpointAttributesResponseTypeDef(BaseModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPlatformApplicationAttributesResponseTypeDef(BaseModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSMSAttributesResponseTypeDef(BaseModel):
    attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSMSSandboxAccountStatusResultTypeDef(BaseModel):
    IsInSandbox: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriptionAttributesResponseTypeDef(BaseModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTopicAttributesResponseTypeDef(BaseModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPhoneNumbersOptedOutResponseTypeDef(BaseModel):
    phoneNumbers: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PublishResponseTypeDef(BaseModel):
    MessageId: str
    SequenceNumber: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubscribeResponseTypeDef(BaseModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicInputRequestTypeDef(BaseModel):
    Name: str
    Attributes: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataProtectionPolicy: Optional[str] = None

class CreateTopicInputServiceResourceCreateTopicTypeDef(BaseModel):
    Name: str
    Attributes: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataProtectionPolicy: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class ListEndpointsByPlatformApplicationResponseTypeDef(BaseModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListOriginationNumbersRequestListOriginationNumbersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPhoneNumbersOptedOutInputListPhoneNumbersOptedOutPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPlatformApplicationsInputListPlatformApplicationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSMSSandboxPhoneNumbersInputListSMSSandboxPhoneNumbersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionsByTopicInputListSubscriptionsByTopicPaginateTypeDef(BaseModel):
    TopicArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionsInputListSubscriptionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTopicsInputListTopicsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOriginationNumbersResultTypeDef(BaseModel):
    PhoneNumbers: List[PhoneNumberInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPlatformApplicationsResponseTypeDef(BaseModel):
    PlatformApplications: List[PlatformApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSMSSandboxPhoneNumbersResultTypeDef(BaseModel):
    PhoneNumbers: List[SMSSandboxPhoneNumberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSubscriptionsByTopicResponseTypeDef(BaseModel):
    Subscriptions: List[SubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSubscriptionsResponseTypeDef(BaseModel):
    Subscriptions: List[SubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTopicsResponseTypeDef(BaseModel):
    Topics: List[TopicTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PublishBatchResponseTypeDef(BaseModel):
    Successful: List[PublishBatchResultEntryTypeDef]
    Failed: List[BatchResultErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PublishBatchRequestEntryTypeDef(BaseModel):
    Id: str
    Message: str
    Subject: Optional[str] = None
    MessageStructure: Optional[str] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None

class PublishInputPlatformEndpointPublishTypeDef(BaseModel):
    Message: str
    TopicArn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Subject: Optional[str] = None
    MessageStructure: Optional[str] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None

class PublishInputRequestTypeDef(BaseModel):
    Message: str
    TopicArn: Optional[str] = None
    TargetArn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Subject: Optional[str] = None
    MessageStructure: Optional[str] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None

class PublishInputTopicPublishTypeDef(BaseModel):
    Message: str
    TargetArn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Subject: Optional[str] = None
    MessageStructure: Optional[str] = None
    MessageAttributes: Optional[Mapping[str, MessageAttributeValueTypeDef]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None

class PublishBatchInputRequestTypeDef(BaseModel):
    TopicArn: str
    PublishBatchRequestEntries: Sequence[PublishBatchRequestEntryTypeDef]

