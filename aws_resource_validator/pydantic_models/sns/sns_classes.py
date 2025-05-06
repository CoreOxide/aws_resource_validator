from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.sns.sns_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AddPermissionInputTopicAddPermission(BaseValidatorModel):
    Label: str
    AWSAccountId: List[str]
    ActionName: List[str]


class AddPermissionInput(BaseValidatorModel):
    TopicArn: str
    Label: str
    AWSAccountId: List[str]
    ActionName: List[str]


class BatchResultErrorEntry(BaseValidatorModel):
    Id: str
    Code: str
    SenderFault: bool
    Message: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CheckIfPhoneNumberIsOptedOutInput(BaseValidatorModel):
    phoneNumber: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ConfirmSubscriptionInputTopicConfirmSubscription(BaseValidatorModel):
    Token: str
    AuthenticateOnUnsubscribe: Optional[str] = None


class ConfirmSubscriptionInput(BaseValidatorModel):
    TopicArn: str
    Token: str
    AuthenticateOnUnsubscribe: Optional[str] = None


class CreatePlatformApplicationInputServiceResourceCreatePlatformApplication(BaseValidatorModel):
    Name: str
    Platform: str
    Attributes: Dict[str, str]


class CreatePlatformApplicationInput(BaseValidatorModel):
    Name: str
    Platform: str
    Attributes: Dict[str, str]


class CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpoint(BaseValidatorModel):
    Token: str
    CustomUserData: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class CreatePlatformEndpointInput(BaseValidatorModel):
    PlatformApplicationArn: str
    Token: str
    CustomUserData: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class CreateSMSSandboxPhoneNumberInput(BaseValidatorModel):
    PhoneNumber: str
    LanguageCode: Optional[LanguageCodeStringType] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class DeleteEndpointInput(BaseValidatorModel):
    EndpointArn: str


class DeletePlatformApplicationInput(BaseValidatorModel):
    PlatformApplicationArn: str


class DeleteSMSSandboxPhoneNumberInput(BaseValidatorModel):
    PhoneNumber: str


class DeleteTopicInput(BaseValidatorModel):
    TopicArn: str


class Endpoint(BaseValidatorModel):
    EndpointArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class GetDataProtectionPolicyInput(BaseValidatorModel):
    ResourceArn: str


class GetEndpointAttributesInput(BaseValidatorModel):
    EndpointArn: str


class GetPlatformApplicationAttributesInput(BaseValidatorModel):
    PlatformApplicationArn: str


class GetSMSAttributesInput(BaseValidatorModel):
    attributes: Optional[List[str]] = None


class GetSubscriptionAttributesInput(BaseValidatorModel):
    SubscriptionArn: str


class GetTopicAttributesInput(BaseValidatorModel):
    TopicArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListEndpointsByPlatformApplicationInput(BaseValidatorModel):
    PlatformApplicationArn: str
    NextToken: Optional[str] = None


class ListOriginationNumbersRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PhoneNumberInformation(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    PhoneNumber: Optional[str] = None
    Status: Optional[str] = None
    Iso2CountryCode: Optional[str] = None
    RouteType: Optional[RouteTypeType] = None
    NumberCapabilities: Optional[List[NumberCapabilityType]] = None


class ListPhoneNumbersOptedOutInput(BaseValidatorModel):
    nextToken: Optional[str] = None


class ListPlatformApplicationsInput(BaseValidatorModel):
    NextToken: Optional[str] = None


class PlatformApplication(BaseValidatorModel):
    PlatformApplicationArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class ListSMSSandboxPhoneNumbersInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SMSSandboxPhoneNumber(BaseValidatorModel):
    PhoneNumber: Optional[str] = None
    Status: Optional[SMSSandboxPhoneNumberVerificationStatusType] = None


class ListSubscriptionsByTopicInput(BaseValidatorModel):
    TopicArn: str
    NextToken: Optional[str] = None


class Subscription(BaseValidatorModel):
    SubscriptionArn: Optional[str] = None
    Owner: Optional[str] = None
    Protocol: Optional[str] = None
    Endpoint: Optional[str] = None
    TopicArn: Optional[str] = None


class ListSubscriptionsInput(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ListTopicsInput(BaseValidatorModel):
    NextToken: Optional[str] = None


class Topic(BaseValidatorModel):
    TopicArn: Optional[str] = None


class OptInPhoneNumberInput(BaseValidatorModel):
    phoneNumber: str


class PublishBatchResultEntry(BaseValidatorModel):
    Id: Optional[str] = None
    MessageId: Optional[str] = None
    SequenceNumber: Optional[str] = None


class PutDataProtectionPolicyInput(BaseValidatorModel):
    ResourceArn: str
    DataProtectionPolicy: str


class RemovePermissionInputTopicRemovePermission(BaseValidatorModel):
    Label: str


class RemovePermissionInput(BaseValidatorModel):
    TopicArn: str
    Label: str


class SetEndpointAttributesInputPlatformEndpointSetAttributes(BaseValidatorModel):
    Attributes: Dict[str, str]


class SetEndpointAttributesInput(BaseValidatorModel):
    EndpointArn: str
    Attributes: Dict[str, str]


class SetPlatformApplicationAttributesInputPlatformApplicationSetAttributes(BaseValidatorModel):
    Attributes: Dict[str, str]


class SetPlatformApplicationAttributesInput(BaseValidatorModel):
    PlatformApplicationArn: str
    Attributes: Dict[str, str]


class SetSMSAttributesInput(BaseValidatorModel):
    attributes: Dict[str, str]


class SetSubscriptionAttributesInputSubscriptionSetAttributes(BaseValidatorModel):
    AttributeName: str
    AttributeValue: Optional[str] = None


class SetSubscriptionAttributesInput(BaseValidatorModel):
    SubscriptionArn: str
    AttributeName: str
    AttributeValue: Optional[str] = None


class SetTopicAttributesInputTopicSetAttributes(BaseValidatorModel):
    AttributeName: str
    AttributeValue: Optional[str] = None


class SetTopicAttributesInput(BaseValidatorModel):
    TopicArn: str
    AttributeName: str
    AttributeValue: Optional[str] = None


class SubscribeInputTopicSubscribe(BaseValidatorModel):
    Protocol: str
    Endpoint: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    ReturnSubscriptionArn: Optional[bool] = None


class SubscribeInput(BaseValidatorModel):
    TopicArn: str
    Protocol: str
    Endpoint: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    ReturnSubscriptionArn: Optional[bool] = None


class UnsubscribeInput(BaseValidatorModel):
    SubscriptionArn: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class VerifySMSSandboxPhoneNumberInput(BaseValidatorModel):
    PhoneNumber: str
    OneTimePassword: str


class MessageAttributeValue(BaseValidatorModel):
    DataType: str
    StringValue: Optional[str] = None
    BinaryValue: Optional[Blob] = None


class CheckIfPhoneNumberIsOptedOutResponse(BaseValidatorModel):
    isOptedOut: bool
    ResponseMetadata: ResponseMetadata


class ConfirmSubscriptionResponse(BaseValidatorModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadata


class CreateEndpointResponse(BaseValidatorModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadata


class CreatePlatformApplicationResponse(BaseValidatorModel):
    PlatformApplicationArn: str
    ResponseMetadata: ResponseMetadata


class CreateTopicResponse(BaseValidatorModel):
    TopicArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetDataProtectionPolicyResponse(BaseValidatorModel):
    DataProtectionPolicy: str
    ResponseMetadata: ResponseMetadata


class GetEndpointAttributesResponse(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetPlatformApplicationAttributesResponse(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetSMSAttributesResponse(BaseValidatorModel):
    attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetSMSSandboxAccountStatusResult(BaseValidatorModel):
    IsInSandbox: bool
    ResponseMetadata: ResponseMetadata


class GetSubscriptionAttributesResponse(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetTopicAttributesResponse(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListPhoneNumbersOptedOutResponse(BaseValidatorModel):
    phoneNumbers: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PublishResponse(BaseValidatorModel):
    MessageId: str
    SequenceNumber: str
    ResponseMetadata: ResponseMetadata


class SubscribeResponse(BaseValidatorModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadata


class CreateTopicInputServiceResourceCreateTopic(BaseValidatorModel):
    Name: str
    Attributes: Optional[Dict[str, str]] = None
    Tags: Optional[List[Tag]] = None
    DataProtectionPolicy: Optional[str] = None


class CreateTopicInput(BaseValidatorModel):
    Name: str
    Attributes: Optional[Dict[str, str]] = None
    Tags: Optional[List[Tag]] = None
    DataProtectionPolicy: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class ListEndpointsByPlatformApplicationResponse(BaseValidatorModel):
    Endpoints: List[Endpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEndpointsByPlatformApplicationInputPaginate(BaseValidatorModel):
    PlatformApplicationArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOriginationNumbersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPhoneNumbersOptedOutInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPlatformApplicationsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSMSSandboxPhoneNumbersInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubscriptionsByTopicInputPaginate(BaseValidatorModel):
    TopicArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubscriptionsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTopicsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOriginationNumbersResult(BaseValidatorModel):
    PhoneNumbers: List[PhoneNumberInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPlatformApplicationsResponse(BaseValidatorModel):
    PlatformApplications: List[PlatformApplication]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSMSSandboxPhoneNumbersResult(BaseValidatorModel):
    PhoneNumbers: List[SMSSandboxPhoneNumber]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSubscriptionsByTopicResponse(BaseValidatorModel):
    Subscriptions: List[Subscription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSubscriptionsResponse(BaseValidatorModel):
    Subscriptions: List[Subscription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTopicsResponse(BaseValidatorModel):
    Topics: List[Topic]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PublishBatchResponse(BaseValidatorModel):
    Successful: List[PublishBatchResultEntry]
    Failed: List[BatchResultErrorEntry]
    ResponseMetadata: ResponseMetadata


class PublishBatchRequestEntry(BaseValidatorModel):
    Id: str
    Message: str
    Subject: Optional[str] = None
    MessageStructure: Optional[str] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValue]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None


class PublishInputPlatformEndpointPublish(BaseValidatorModel):
    Message: str
    TopicArn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Subject: Optional[str] = None
    MessageStructure: Optional[str] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValue]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None


class PublishInputTopicPublish(BaseValidatorModel):
    Message: str
    TargetArn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Subject: Optional[str] = None
    MessageStructure: Optional[str] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValue]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None


class PublishInput(BaseValidatorModel):
    Message: str
    TopicArn: Optional[str] = None
    TargetArn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Subject: Optional[str] = None
    MessageStructure: Optional[str] = None
    MessageAttributes: Optional[Dict[str, MessageAttributeValue]] = None
    MessageDeduplicationId: Optional[str] = None
    MessageGroupId: Optional[str] = None


class PublishBatchInput(BaseValidatorModel):
    TopicArn: str
    PublishBatchRequestEntries: List[PublishBatchRequestEntry]