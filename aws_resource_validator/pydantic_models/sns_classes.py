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
from aws_resource_validator.pydantic_models.sns_constants import *

class AddPermissionInputRequestTypeDef(BaseValidatorModel):
    TopicArn: str
    Label: str
    AWSAccountId: Sequence[str]
    ActionName: Sequence[str]

class AddPermissionInputTopicAddPermissionTypeDef(BaseValidatorModel):
    Label: str
    AWSAccountId: Sequence[str]
    ActionName: Sequence[str]

class BatchResultErrorEntryTypeDef(BaseValidatorModel):
    Id: str
    Code: str
    SenderFault: bool
    Message: Optional[str] = None

class CheckIfPhoneNumberIsOptedOutInputRequestTypeDef(BaseValidatorModel):
    phoneNumber: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ConfirmSubscriptionInputRequestTypeDef(BaseValidatorModel):
    TopicArn: str
    Token: str
    AuthenticateOnUnsubscribe: Optional[str] = None

class ConfirmSubscriptionInputTopicConfirmSubscriptionTypeDef(BaseValidatorModel):
    Token: str
    AuthenticateOnUnsubscribe: Optional[str] = None

class CreatePlatformApplicationInputRequestTypeDef(BaseValidatorModel):
    Name: str
    Platform: str
    Attributes: Mapping[str, str]

class CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationTypeDef(BaseValidatorModel):
    Name: str
    Platform: str
    Attributes: Mapping[str, str]

class CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointTypeDef(BaseValidatorModel):
    Token: str
    CustomUserData: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None

class CreatePlatformEndpointInputRequestTypeDef(BaseValidatorModel):
    PlatformApplicationArn: str
    Token: str
    CustomUserData: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None

class CreateSMSSandboxPhoneNumberInputRequestTypeDef(BaseValidatorModel):
    PhoneNumber: str
    LanguageCode: Optional[LanguageCodeStringType] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class DeleteEndpointInputRequestTypeDef(BaseValidatorModel):
    EndpointArn: str

class DeletePlatformApplicationInputRequestTypeDef(BaseValidatorModel):
    PlatformApplicationArn: str

class DeleteSMSSandboxPhoneNumberInputRequestTypeDef(BaseValidatorModel):
    PhoneNumber: str

class DeleteTopicInputRequestTypeDef(BaseValidatorModel):
    TopicArn: str

class EndpointTypeDef(BaseValidatorModel):
    EndpointArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None

class GetDataProtectionPolicyInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class GetEndpointAttributesInputRequestTypeDef(BaseValidatorModel):
    EndpointArn: str

class GetPlatformApplicationAttributesInputRequestTypeDef(BaseValidatorModel):
    PlatformApplicationArn: str

class GetSMSAttributesInputRequestTypeDef(BaseValidatorModel):
    attributes: Optional[Sequence[str]] = None

class GetSubscriptionAttributesInputRequestTypeDef(BaseValidatorModel):
    SubscriptionArn: str

class GetTopicAttributesInputRequestTypeDef(BaseValidatorModel):
    TopicArn: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListEndpointsByPlatformApplicationInputRequestTypeDef(BaseValidatorModel):
    PlatformApplicationArn: str
    NextToken: Optional[str] = None

class ListOriginationNumbersRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PhoneNumberInformationTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    PhoneNumber: Optional[str] = None
    Status: Optional[str] = None
    Iso2CountryCode: Optional[str] = None
    RouteType: Optional[RouteTypeType] = None
    NumberCapabilities: Optional[List[NumberCapabilityType]] = None

class ListPhoneNumbersOptedOutInputRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None

class ListPlatformApplicationsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None

class PlatformApplicationTypeDef(BaseValidatorModel):
    PlatformApplicationArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None

class ListSMSSandboxPhoneNumbersInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SMSSandboxPhoneNumberTypeDef(BaseValidatorModel):
    PhoneNumber: Optional[str] = None
    Status: Optional[SMSSandboxPhoneNumberVerificationStatusType] = None

class ListSubscriptionsByTopicInputRequestTypeDef(BaseValidatorModel):
    TopicArn: str
    NextToken: Optional[str] = None

class SubscriptionTypeDef(BaseValidatorModel):
    SubscriptionArn: Optional[str] = None
    Owner: Optional[str] = None
    Protocol: Optional[str] = None
    Endpoint: Optional[str] = None
    TopicArn: Optional[str] = None

class ListSubscriptionsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ListTopicsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None

class TopicTypeDef(BaseValidatorModel):
    TopicArn: Optional[str] = None

class OptInPhoneNumberInputRequestTypeDef(BaseValidatorModel):
    phoneNumber: str

class PublishBatchResultEntryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    MessageId: Optional[str] = None
    SequenceNumber: Optional[str] = None

class PutDataProtectionPolicyInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    DataProtectionPolicy: str

class RemovePermissionInputRequestTypeDef(BaseValidatorModel):
    TopicArn: str
    Label: str

class RemovePermissionInputTopicRemovePermissionTypeDef(BaseValidatorModel):
    Label: str

class SetEndpointAttributesInputPlatformEndpointSetAttributesTypeDef(BaseValidatorModel):
    Attributes: Mapping[str, str]

class SetEndpointAttributesInputRequestTypeDef(BaseValidatorModel):
    EndpointArn: str
    Attributes: Mapping[str, str]

class SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesTypeDef(BaseValidatorModel):
    Attributes: Mapping[str, str]

class SetPlatformApplicationAttributesInputRequestTypeDef(BaseValidatorModel):
    PlatformApplicationArn: str
    Attributes: Mapping[str, str]

class SetSMSAttributesInputRequestTypeDef(BaseValidatorModel):
    attributes: Mapping[str, str]

class SetSubscriptionAttributesInputRequestTypeDef(BaseValidatorModel):
    SubscriptionArn: str
    AttributeName: str
    AttributeValue: Optional[str] = None

class SetSubscriptionAttributesInputSubscriptionSetAttributesTypeDef(BaseValidatorModel):
    AttributeName: str
    AttributeValue: Optional[str] = None

class SetTopicAttributesInputRequestTypeDef(BaseValidatorModel):
    TopicArn: str
    AttributeName: str
    AttributeValue: Optional[str] = None

class SetTopicAttributesInputTopicSetAttributesTypeDef(BaseValidatorModel):
    AttributeName: str
    AttributeValue: Optional[str] = None

class SubscribeInputRequestTypeDef(BaseValidatorModel):
    TopicArn: str
    Protocol: str
    Endpoint: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    ReturnSubscriptionArn: Optional[bool] = None

class SubscribeInputTopicSubscribeTypeDef(BaseValidatorModel):
    Protocol: str
    Endpoint: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    ReturnSubscriptionArn: Optional[bool] = None

class UnsubscribeInputRequestTypeDef(BaseValidatorModel):
    SubscriptionArn: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class VerifySMSSandboxPhoneNumberInputRequestTypeDef(BaseValidatorModel):
    PhoneNumber: str
    OneTimePassword: str

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PublishResponseTypeDef(BaseValidatorModel):
    MessageId: str
    SequenceNumber: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubscribeResponseTypeDef(BaseValidatorModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicInputRequestTypeDef(BaseValidatorModel):
    Name: str
    Attributes: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataProtectionPolicy: Optional[str] = None

class CreateTopicInputServiceResourceCreateTopicTypeDef(BaseValidatorModel):
    Name: str
    Attributes: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataProtectionPolicy: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class ListEndpointsByPlatformApplicationResponseTypeDef(BaseValidatorModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListOriginationNumbersRequestListOriginationNumbersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPhoneNumbersOptedOutInputListPhoneNumbersOptedOutPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPlatformApplicationsInputListPlatformApplicationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSMSSandboxPhoneNumbersInputListSMSSandboxPhoneNumbersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionsByTopicInputListSubscriptionsByTopicPaginateTypeDef(BaseValidatorModel):
    TopicArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionsInputListSubscriptionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTopicsInputListTopicsPaginateTypeDef(BaseValidatorModel):
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

class PublishInputRequestTypeDef(BaseValidatorModel):
    Message: str
    TopicArn: Optional[str] = None
    TargetArn: Optional[str] = None
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

class PublishBatchInputRequestTypeDef(BaseValidatorModel):
    TopicArn: str
    PublishBatchRequestEntries: Sequence[PublishBatchRequestEntryTypeDef]

