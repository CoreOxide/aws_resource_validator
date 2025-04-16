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
from aws_resource_validator.pydantic_models.securitylake_constants import *

class AwsIdentity(BaseValidatorModel):
    externalId: str
    principal: str


class AwsLogSourceConfiguration(BaseValidatorModel):
    regions: Sequence[str]
    sourceName: AwsLogSourceNameType
    accounts: Optional[Sequence[str]] = None
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
    regions: Optional[Sequence[str]] = None
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
    regions: Sequence[str]


class DeleteSubscriberNotificationRequest(BaseValidatorModel):
    subscriberId: str


class DeleteSubscriberRequest(BaseValidatorModel):
    subscriberId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetDataLakeSourcesRequest(BaseValidatorModel):
    accounts: Optional[Sequence[str]] = None
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
    regions: Optional[Sequence[str]] = None


class ListDataLakesRequest(BaseValidatorModel):
    regions: Optional[Sequence[str]] = None


class ListSubscribersRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class RegisterDataLakeDelegatedAdministratorRequest(BaseValidatorModel):
    accountId: str


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateDataLakeExceptionSubscriptionRequest(BaseValidatorModel):
    notificationEndpoint: str
    subscriptionProtocol: str
    exceptionTimeToLive: Optional[int] = None


class CreateAwsLogSourceRequest(BaseValidatorModel):
    sources: Sequence[AwsLogSourceConfiguration]


class DeleteAwsLogSourceRequest(BaseValidatorModel):
    sources: Sequence[AwsLogSourceConfiguration]


class DataLakeAutoEnableNewAccountConfigurationOutput(BaseValidatorModel):
    region: str
    sources: List[AwsLogSourceResource]


class DataLakeAutoEnableNewAccountConfiguration(BaseValidatorModel):
    region: str
    sources: Sequence[AwsLogSourceResource]


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
    tags: Sequence[Tag]


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
    transitions: Optional[Sequence[DataLakeLifecycleTransition]] = None


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
    accounts: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataLakeExceptionsRequestPaginate(BaseValidatorModel):
    regions: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubscribersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class NotificationConfiguration(BaseValidatorModel):
    httpsNotificationConfiguration: Optional[HttpsNotificationConfiguration] = None
    sqsNotificationConfiguration: Optional[Mapping[str, Any]] = None


class GetDataLakeOrganizationConfigurationResponse(BaseValidatorModel):
    autoEnableNewAccount: List[DataLakeAutoEnableNewAccountConfigurationOutput]
    ResponseMetadata: ResponseMetadata


class CreateCustomLogSourceRequest(BaseValidatorModel):
    configuration: CustomLogSourceConfiguration
    sourceName: str
    eventClasses: Optional[Sequence[str]] = None
    sourceVersion: Optional[str] = None


class CreateCustomLogSourceResponse(BaseValidatorModel):
    source: CustomLogSourceResource
    ResponseMetadata: ResponseMetadata


class LogSourceResource(BaseValidatorModel):
    awsLogSource: Optional[AwsLogSourceResource] = None
    customLogSource: Optional[CustomLogSourceResource] = None


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


class DataLakeAutoEnableNewAccountConfigurationUnion(BaseValidatorModel):
    pass


class CreateDataLakeOrganizationConfigurationRequest(BaseValidatorModel):
    autoEnableNewAccount: Optional[ Sequence[DataLakeAutoEnableNewAccountConfigurationUnion] ] = None


class DeleteDataLakeOrganizationConfigurationRequest(BaseValidatorModel):
    autoEnableNewAccount: Optional[ Sequence[DataLakeAutoEnableNewAccountConfigurationUnion] ] = None


class CreateSubscriberRequest(BaseValidatorModel):
    sources: Sequence[LogSourceResource]
    subscriberIdentity: AwsIdentity
    subscriberName: str
    accessTypes: Optional[Sequence[AccessTypeType]] = None
    subscriberDescription: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class ListLogSourcesRequestPaginate(BaseValidatorModel):
    accounts: Optional[Sequence[str]] = None
    regions: Optional[Sequence[str]] = None
    sources: Optional[Sequence[LogSourceResource]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLogSourcesRequest(BaseValidatorModel):
    accounts: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regions: Optional[Sequence[str]] = None
    sources: Optional[Sequence[LogSourceResource]] = None


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
    sources: Optional[Sequence[LogSourceResource]] = None
    subscriberDescription: Optional[str] = None
    subscriberIdentity: Optional[AwsIdentity] = None
    subscriberName: Optional[str] = None


class DataLakeReplicationConfigurationUnion(BaseValidatorModel):
    pass


class DataLakeLifecycleConfigurationUnion(BaseValidatorModel):
    pass


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
    configurations: Sequence[DataLakeConfiguration]
    metaStoreManagerRoleArn: str
    tags: Optional[Sequence[Tag]] = None


class UpdateDataLakeRequest(BaseValidatorModel):
    configurations: Sequence[DataLakeConfiguration]
    metaStoreManagerRoleArn: Optional[str] = None


