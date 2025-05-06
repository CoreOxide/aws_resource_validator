from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.securitylake.securitylake_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AwsIdentity(BaseValidatorModel):
    externalId: str
    principal: str


class AwsLogSourceConfiguration(BaseValidatorModel):
    regions: List[str]
    sourceName: AwsLogSourceNameType
    accounts: Optional[List[str]] = None
    sourceVersion: Optional[str] = None


class AwsLogSourceResource(BaseValidatorModel):
    sourceName: Optional[AwsLogSourceNameType] = None
    sourceVersion: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateDataLakeExceptionSubscriptionRequest(BaseValidatorModel):
    notificationEndpoint: str
    subscriptionProtocol: str
    exceptionTimeToLive: Optional[int] = None


class Tag(BaseValidatorModel):
    key: str
    value: str


class CustomLogSourceAttributes(BaseValidatorModel):
    crawlerArn: Optional[str] = None
    databaseArn: Optional[str] = None
    tableArn: Optional[str] = None


class CustomLogSourceCrawlerConfiguration(BaseValidatorModel):
    roleArn: str


class CustomLogSourceProvider(BaseValidatorModel):
    location: Optional[str] = None
    roleArn: Optional[str] = None


class DataLakeEncryptionConfiguration(BaseValidatorModel):
    kmsKeyId: Optional[str] = None


class DataLakeException(BaseValidatorModel):
    exception: Optional[str] = None
    region: Optional[str] = None
    remediation: Optional[str] = None
    timestamp: Optional[datetime] = None


class DataLakeLifecycleExpiration(BaseValidatorModel):
    days: Optional[int] = None


class DataLakeLifecycleTransition(BaseValidatorModel):
    days: Optional[int] = None
    storageClass: Optional[str] = None


class DataLakeReplicationConfigurationOutput(BaseValidatorModel):
    regions: Optional[List[str]] = None
    roleArn: Optional[str] = None


class DataLakeReplicationConfiguration(BaseValidatorModel):
    regions: Optional[List[str]] = None
    roleArn: Optional[str] = None


class DataLakeSourceStatus(BaseValidatorModel):
    resource: Optional[str] = None
    status: Optional[SourceCollectionStatusType] = None


class DataLakeUpdateException(BaseValidatorModel):
    code: Optional[str] = None
    reason: Optional[str] = None


class DeleteCustomLogSourceRequest(BaseValidatorModel):
    sourceName: str
    sourceVersion: Optional[str] = None


class DeleteDataLakeRequest(BaseValidatorModel):
    regions: List[str]


class DeleteSubscriberNotificationRequest(BaseValidatorModel):
    subscriberId: str


class DeleteSubscriberRequest(BaseValidatorModel):
    subscriberId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetDataLakeSourcesRequest(BaseValidatorModel):
    accounts: Optional[List[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetSubscriberRequest(BaseValidatorModel):
    subscriberId: str


class HttpsNotificationConfiguration(BaseValidatorModel):
    endpoint: str
    targetRoleArn: str
    authorizationApiKeyName: Optional[str] = None
    authorizationApiKeyValue: Optional[str] = None
    httpMethod: Optional[HttpMethodType] = None


class ListDataLakeExceptionsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regions: Optional[List[str]] = None


class ListDataLakesRequest(BaseValidatorModel):
    regions: Optional[List[str]] = None


class ListSubscribersRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class RegisterDataLakeDelegatedAdministratorRequest(BaseValidatorModel):
    accountId: str


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateDataLakeExceptionSubscriptionRequest(BaseValidatorModel):
    notificationEndpoint: str
    subscriptionProtocol: str
    exceptionTimeToLive: Optional[int] = None


class CreateAwsLogSourceRequest(BaseValidatorModel):
    sources: List[AwsLogSourceConfiguration]


class DeleteAwsLogSourceRequest(BaseValidatorModel):
    sources: List[AwsLogSourceConfiguration]


class DataLakeAutoEnableNewAccountConfigurationOutput(BaseValidatorModel):
    region: str
    sources: List[AwsLogSourceResource]


class DataLakeAutoEnableNewAccountConfiguration(BaseValidatorModel):
    region: str
    sources: List[AwsLogSourceResource]


class CreateAwsLogSourceResponse(BaseValidatorModel):
    failed: List[str]
    ResponseMetadata: ResponseMetadata


class CreateSubscriberNotificationResponse(BaseValidatorModel):
    subscriberEndpoint: str
    ResponseMetadata: ResponseMetadata


class DeleteAwsLogSourceResponse(BaseValidatorModel):
    failed: List[str]
    ResponseMetadata: ResponseMetadata


class GetDataLakeExceptionSubscriptionResponse(BaseValidatorModel):
    exceptionTimeToLive: int
    notificationEndpoint: str
    subscriptionProtocol: str
    ResponseMetadata: ResponseMetadata


class UpdateSubscriberNotificationResponse(BaseValidatorModel):
    subscriberEndpoint: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


class CustomLogSourceConfiguration(BaseValidatorModel):
    crawlerConfiguration: CustomLogSourceCrawlerConfiguration
    providerIdentity: AwsIdentity


class CustomLogSourceResource(BaseValidatorModel):
    attributes: Optional[CustomLogSourceAttributes] = None
    provider: Optional[CustomLogSourceProvider] = None
    sourceName: Optional[str] = None
    sourceVersion: Optional[str] = None


class ListDataLakeExceptionsResponse(BaseValidatorModel):
    exceptions: List[DataLakeException]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DataLakeLifecycleConfigurationOutput(BaseValidatorModel):
    expiration: Optional[DataLakeLifecycleExpiration] = None
    transitions: Optional[List[DataLakeLifecycleTransition]] = None


class DataLakeLifecycleConfiguration(BaseValidatorModel):
    expiration: Optional[DataLakeLifecycleExpiration] = None
    transitions: Optional[List[DataLakeLifecycleTransition]] = None

DataLakeReplicationConfigurationUnion = Union[DataLakeReplicationConfiguration, DataLakeReplicationConfigurationOutput]


class DataLakeSource(BaseValidatorModel):
    account: Optional[str] = None
    eventClasses: Optional[List[str]] = None
    sourceName: Optional[str] = None
    sourceStatuses: Optional[List[DataLakeSourceStatus]] = None


class DataLakeUpdateStatus(BaseValidatorModel):
    exception: Optional[DataLakeUpdateException] = None
    requestId: Optional[str] = None
    status: Optional[DataLakeStatusType] = None


class GetDataLakeSourcesRequestPaginate(BaseValidatorModel):
    accounts: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataLakeExceptionsRequestPaginate(BaseValidatorModel):
    regions: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubscribersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class NotificationConfiguration(BaseValidatorModel):
    httpsNotificationConfiguration: Optional[HttpsNotificationConfiguration] = None
    sqsNotificationConfiguration: Optional[Dict[str, Any]] = None


class GetDataLakeOrganizationConfigurationResponse(BaseValidatorModel):
    autoEnableNewAccount: List[DataLakeAutoEnableNewAccountConfigurationOutput]
    ResponseMetadata: ResponseMetadata

DataLakeAutoEnableNewAccountConfigurationUnion = Union[DataLakeAutoEnableNewAccountConfiguration, DataLakeAutoEnableNewAccountConfigurationOutput]


class CreateCustomLogSourceRequest(BaseValidatorModel):
    configuration: CustomLogSourceConfiguration
    sourceName: str
    eventClasses: Optional[List[str]] = None
    sourceVersion: Optional[str] = None


class CreateCustomLogSourceResponse(BaseValidatorModel):
    source: CustomLogSourceResource
    ResponseMetadata: ResponseMetadata


class LogSourceResource(BaseValidatorModel):
    awsLogSource: Optional[AwsLogSourceResource] = None
    customLogSource: Optional[CustomLogSourceResource] = None

DataLakeLifecycleConfigurationUnion = Union[DataLakeLifecycleConfiguration, DataLakeLifecycleConfigurationOutput]


class GetDataLakeSourcesResponse(BaseValidatorModel):
    dataLakeArn: str
    dataLakeSources: List[DataLakeSource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DataLakeResource(BaseValidatorModel):
    dataLakeArn: str
    region: str
    createStatus: Optional[DataLakeStatusType] = None
    encryptionConfiguration: Optional[DataLakeEncryptionConfiguration] = None
    lifecycleConfiguration: Optional[DataLakeLifecycleConfigurationOutput] = None
    replicationConfiguration: Optional[DataLakeReplicationConfigurationOutput] = None
    s3BucketArn: Optional[str] = None
    updateStatus: Optional[DataLakeUpdateStatus] = None


class CreateSubscriberNotificationRequest(BaseValidatorModel):
    configuration: NotificationConfiguration
    subscriberId: str


class UpdateSubscriberNotificationRequest(BaseValidatorModel):
    configuration: NotificationConfiguration
    subscriberId: str


class CreateDataLakeOrganizationConfigurationRequest(BaseValidatorModel):
    autoEnableNewAccount: Optional[List[DataLakeAutoEnableNewAccountConfigurationUnion]] = None


class DeleteDataLakeOrganizationConfigurationRequest(BaseValidatorModel):
    autoEnableNewAccount: Optional[List[DataLakeAutoEnableNewAccountConfigurationUnion]] = None


class CreateSubscriberRequest(BaseValidatorModel):
    sources: List[LogSourceResource]
    subscriberIdentity: AwsIdentity
    subscriberName: str
    accessTypes: Optional[List[AccessTypeType]] = None
    subscriberDescription: Optional[str] = None
    tags: Optional[List[Tag]] = None


class ListLogSourcesRequestPaginate(BaseValidatorModel):
    accounts: Optional[List[str]] = None
    regions: Optional[List[str]] = None
    sources: Optional[List[LogSourceResource]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLogSourcesRequest(BaseValidatorModel):
    accounts: Optional[List[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regions: Optional[List[str]] = None
    sources: Optional[List[LogSourceResource]] = None


class LogSource(BaseValidatorModel):
    account: Optional[str] = None
    region: Optional[str] = None
    sources: Optional[List[LogSourceResource]] = None


class SubscriberResource(BaseValidatorModel):
    sources: List[LogSourceResource]
    subscriberArn: str
    subscriberId: str
    subscriberIdentity: AwsIdentity
    subscriberName: str
    accessTypes: Optional[List[AccessTypeType]] = None
    createdAt: Optional[datetime] = None
    resourceShareArn: Optional[str] = None
    resourceShareName: Optional[str] = None
    roleArn: Optional[str] = None
    s3BucketArn: Optional[str] = None
    subscriberDescription: Optional[str] = None
    subscriberEndpoint: Optional[str] = None
    subscriberStatus: Optional[SubscriberStatusType] = None
    updatedAt: Optional[datetime] = None


class UpdateSubscriberRequest(BaseValidatorModel):
    subscriberId: str
    sources: Optional[List[LogSourceResource]] = None
    subscriberDescription: Optional[str] = None
    subscriberIdentity: Optional[AwsIdentity] = None
    subscriberName: Optional[str] = None


class DataLakeConfiguration(BaseValidatorModel):
    region: str
    encryptionConfiguration: Optional[DataLakeEncryptionConfiguration] = None
    lifecycleConfiguration: Optional[DataLakeLifecycleConfigurationUnion] = None
    replicationConfiguration: Optional[DataLakeReplicationConfigurationUnion] = None


class CreateDataLakeResponse(BaseValidatorModel):
    dataLakes: List[DataLakeResource]
    ResponseMetadata: ResponseMetadata


class ListDataLakesResponse(BaseValidatorModel):
    dataLakes: List[DataLakeResource]
    ResponseMetadata: ResponseMetadata


class UpdateDataLakeResponse(BaseValidatorModel):
    dataLakes: List[DataLakeResource]
    ResponseMetadata: ResponseMetadata


class ListLogSourcesResponse(BaseValidatorModel):
    sources: List[LogSource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateSubscriberResponse(BaseValidatorModel):
    subscriber: SubscriberResource
    ResponseMetadata: ResponseMetadata


class GetSubscriberResponse(BaseValidatorModel):
    subscriber: SubscriberResource
    ResponseMetadata: ResponseMetadata


class ListSubscribersResponse(BaseValidatorModel):
    subscribers: List[SubscriberResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateSubscriberResponse(BaseValidatorModel):
    subscriber: SubscriberResource
    ResponseMetadata: ResponseMetadata


class CreateDataLakeRequest(BaseValidatorModel):
    configurations: List[DataLakeConfiguration]
    metaStoreManagerRoleArn: str
    tags: Optional[List[Tag]] = None


class UpdateDataLakeRequest(BaseValidatorModel):
    configurations: List[DataLakeConfiguration]
    metaStoreManagerRoleArn: Optional[str] = None