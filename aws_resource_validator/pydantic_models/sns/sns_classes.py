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


# This class is the input for the 'add_permission' function.
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


# This class is the input for the 'check_if_phone_number_is_opted_out' function.
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


# This class is the input for the 'confirm_subscription' function.
class ConfirmSubscriptionInput(BaseValidatorModel):
    TopicArn: str
    Token: str
    AuthenticateOnUnsubscribe: Optional[str] = None


class CreatePlatformApplicationInputServiceResourceCreatePlatformApplication(BaseValidatorModel):
    Name: str
    Platform: str
    Attributes: Dict[str, str]


# This class is the input for the 'create_platform_application' function.
class CreatePlatformApplicationInput(BaseValidatorModel):
    Name: str
    Platform: str
    Attributes: Dict[str, str]


class CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpoint(BaseValidatorModel):
    Token: str
    CustomUserData: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


# This class is the input for the 'create_platform_endpoint' function.
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


# This class is the input for the 'delete_endpoint' function.
class DeleteEndpointInput(BaseValidatorModel):
    EndpointArn: str


# This class is the input for the 'delete_platform_application' function.
class DeletePlatformApplicationInput(BaseValidatorModel):
    PlatformApplicationArn: str


class DeleteSMSSandboxPhoneNumberInput(BaseValidatorModel):
    PhoneNumber: str


# This class is the input for the 'delete_topic' function.
class DeleteTopicInput(BaseValidatorModel):
    TopicArn: str


class Endpoint(BaseValidatorModel):
    EndpointArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


# This class is the input for the 'get_data_protection_policy' function.
class GetDataProtectionPolicyInput(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'get_endpoint_attributes' function.
class GetEndpointAttributesInput(BaseValidatorModel):
    EndpointArn: str


# This class is the input for the 'get_platform_application_attributes' function.
class GetPlatformApplicationAttributesInput(BaseValidatorModel):
    PlatformApplicationArn: str


# This class is the input for the 'get_sms_attributes' function.
class GetSMSAttributesInput(BaseValidatorModel):
    attributes: Optional[List[str]] = None


# This class is the input for the 'get_subscription_attributes' function.
class GetSubscriptionAttributesInput(BaseValidatorModel):
    SubscriptionArn: str


# This class is the input for the 'get_topic_attributes' function.
class GetTopicAttributesInput(BaseValidatorModel):
    TopicArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_endpoints_by_platform_application' function.
class ListEndpointsByPlatformApplicationInput(BaseValidatorModel):
    PlatformApplicationArn: str
    NextToken: Optional[str] = None


# This class is the input for the 'list_origination_numbers' function.
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


# This class is the input for the 'list_phone_numbers_opted_out' function.
class ListPhoneNumbersOptedOutInput(BaseValidatorModel):
    nextToken: Optional[str] = None


# This class is the input for the 'list_platform_applications' function.
class ListPlatformApplicationsInput(BaseValidatorModel):
    NextToken: Optional[str] = None


class PlatformApplication(BaseValidatorModel):
    PlatformApplicationArn: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


# This class is the input for the 'list_sms_sandbox_phone_numbers' function.
class ListSMSSandboxPhoneNumbersInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SMSSandboxPhoneNumber(BaseValidatorModel):
    PhoneNumber: Optional[str] = None
    Status: Optional[SMSSandboxPhoneNumberVerificationStatusType] = None


# This class is the input for the 'list_subscriptions_by_topic' function.
class ListSubscriptionsByTopicInput(BaseValidatorModel):
    TopicArn: str
    NextToken: Optional[str] = None


class Subscription(BaseValidatorModel):
    SubscriptionArn: Optional[str] = None
    Owner: Optional[str] = None
    Protocol: Optional[str] = None
    Endpoint: Optional[str] = None
    TopicArn: Optional[str] = None


# This class is the input for the 'list_subscriptions' function.
class ListSubscriptionsInput(BaseValidatorModel):
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'list_topics' function.
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


# This class is the input for the 'put_data_protection_policy' function.
class PutDataProtectionPolicyInput(BaseValidatorModel):
    ResourceArn: str
    DataProtectionPolicy: str


class RemovePermissionInputTopicRemovePermission(BaseValidatorModel):
    Label: str


# This class is the input for the 'remove_permission' function.
class RemovePermissionInput(BaseValidatorModel):
    TopicArn: str
    Label: str


class SetEndpointAttributesInputPlatformEndpointSetAttributes(BaseValidatorModel):
    Attributes: Dict[str, str]


# This class is the input for the 'set_endpoint_attributes' function.
class SetEndpointAttributesInput(BaseValidatorModel):
    EndpointArn: str
    Attributes: Dict[str, str]


class SetPlatformApplicationAttributesInputPlatformApplicationSetAttributes(BaseValidatorModel):
    Attributes: Dict[str, str]


# This class is the input for the 'set_platform_application_attributes' function.
class SetPlatformApplicationAttributesInput(BaseValidatorModel):
    PlatformApplicationArn: str
    Attributes: Dict[str, str]


class SetSMSAttributesInput(BaseValidatorModel):
    attributes: Dict[str, str]


class SetSubscriptionAttributesInputSubscriptionSetAttributes(BaseValidatorModel):
    AttributeName: str
    AttributeValue: Optional[str] = None


# This class is the input for the 'set_subscription_attributes' function.
class SetSubscriptionAttributesInput(BaseValidatorModel):
    SubscriptionArn: str
    AttributeName: str
    AttributeValue: Optional[str] = None


class SetTopicAttributesInputTopicSetAttributes(BaseValidatorModel):
    AttributeName: str
    AttributeValue: Optional[str] = None


# This class is the input for the 'set_topic_attributes' function.
class SetTopicAttributesInput(BaseValidatorModel):
    TopicArn: str
    AttributeName: str
    AttributeValue: Optional[str] = None


class SubscribeInputTopicSubscribe(BaseValidatorModel):
    Protocol: str
    Endpoint: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    ReturnSubscriptionArn: Optional[bool] = None


# This class is the input for the 'subscribe' function.
class SubscribeInput(BaseValidatorModel):
    TopicArn: str
    Protocol: str
    Endpoint: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    ReturnSubscriptionArn: Optional[bool] = None


# This class is the input for the 'unsubscribe' function.
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


# This class is the output for the 'check_if_phone_number_is_opted_out' function.
class CheckIfPhoneNumberIsOptedOutResponse(BaseValidatorModel):
    isOptedOut: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'confirm_subscription' function.
class ConfirmSubscriptionResponse(BaseValidatorModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_platform_endpoint' function.
class CreateEndpointResponse(BaseValidatorModel):
    EndpointArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_platform_application' function.
class CreatePlatformApplicationResponse(BaseValidatorModel):
    PlatformApplicationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_topic' function.
class CreateTopicResponse(BaseValidatorModel):
    TopicArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'unsubscribe' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_data_protection_policy' function.
class GetDataProtectionPolicyResponse(BaseValidatorModel):
    DataProtectionPolicy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_endpoint_attributes' function.
class GetEndpointAttributesResponse(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_platform_application_attributes' function.
class GetPlatformApplicationAttributesResponse(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sms_attributes' function.
class GetSMSAttributesResponse(BaseValidatorModel):
    attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetSMSSandboxAccountStatusResult(BaseValidatorModel):
    IsInSandbox: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_subscription_attributes' function.
class GetSubscriptionAttributesResponse(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_topic_attributes' function.
class GetTopicAttributesResponse(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_phone_numbers_opted_out' function.
class ListPhoneNumbersOptedOutResponse(BaseValidatorModel):
    phoneNumbers: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'publish' function.
class PublishResponse(BaseValidatorModel):
    MessageId: str
    SequenceNumber: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'subscribe' function.
class SubscribeResponse(BaseValidatorModel):
    SubscriptionArn: str
    ResponseMetadata: ResponseMetadata


class CreateTopicInputServiceResourceCreateTopic(BaseValidatorModel):
    Name: str
    Attributes: Optional[Dict[str, str]] = None
    Tags: Optional[List[Tag]] = None
    DataProtectionPolicy: Optional[str] = None


# This class is the input for the 'create_topic' function.
class CreateTopicInput(BaseValidatorModel):
    Name: str
    Attributes: Optional[Dict[str, str]] = None
    Tags: Optional[List[Tag]] = None
    DataProtectionPolicy: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


# This class is the output for the 'list_endpoints_by_platform_application' function.
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


# This class is the output for the 'list_origination_numbers' function.
class ListOriginationNumbersResult(BaseValidatorModel):
    PhoneNumbers: List[PhoneNumberInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_platform_applications' function.
class ListPlatformApplicationsResponse(BaseValidatorModel):
    PlatformApplications: List[PlatformApplication]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_sms_sandbox_phone_numbers' function.
class ListSMSSandboxPhoneNumbersResult(BaseValidatorModel):
    PhoneNumbers: List[SMSSandboxPhoneNumber]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_subscriptions_by_topic' function.
class ListSubscriptionsByTopicResponse(BaseValidatorModel):
    Subscriptions: List[Subscription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_subscriptions' function.
class ListSubscriptionsResponse(BaseValidatorModel):
    Subscriptions: List[Subscription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_topics' function.
class ListTopicsResponse(BaseValidatorModel):
    Topics: List[Topic]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'publish_batch' function.
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


# This class is the input for the 'publish' function.
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


# This class is the input for the 'publish_batch' function.
class PublishBatchInput(BaseValidatorModel):
    TopicArn: str
    PublishBatchRequestEntries: List[PublishBatchRequestEntry]