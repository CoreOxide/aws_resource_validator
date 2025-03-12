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

class AwsIdentityTypeDef(BaseValidatorModel):
    externalId: str
    principal: str


class AwsLogSourceConfigurationTypeDef(BaseValidatorModel):
    regions: Sequence[str]
    sourceName: AwsLogSourceNameType
    accounts: Optional[Sequence[str]] = None
    sourceVersion: Optional[str] = None


class AwsLogSourceResourceTypeDef(BaseValidatorModel):
    sourceName: Optional[AwsLogSourceNameType] = None
    sourceVersion: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateDataLakeExceptionSubscriptionRequestTypeDef(BaseValidatorModel):
    notificationEndpoint: str
    subscriptionProtocol: str
    exceptionTimeToLive: Optional[int] = None


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class CustomLogSourceAttributesTypeDef(BaseValidatorModel):
    crawlerArn: Optional[str] = None
    databaseArn: Optional[str] = None
    tableArn: Optional[str] = None


class CustomLogSourceCrawlerConfigurationTypeDef(BaseValidatorModel):
    roleArn: str


class CustomLogSourceProviderTypeDef(BaseValidatorModel):
    location: Optional[str] = None
    roleArn: Optional[str] = None


class DataLakeEncryptionConfigurationTypeDef(BaseValidatorModel):
    kmsKeyId: Optional[str] = None


class DataLakeExceptionTypeDef(BaseValidatorModel):
    exception: Optional[str] = None
    region: Optional[str] = None
    remediation: Optional[str] = None
    timestamp: Optional[datetime] = None


class DataLakeLifecycleExpirationTypeDef(BaseValidatorModel):
    days: Optional[int] = None


class DataLakeLifecycleTransitionTypeDef(BaseValidatorModel):
    days: Optional[int] = None
    storageClass: Optional[str] = None


class DataLakeReplicationConfigurationOutputTypeDef(BaseValidatorModel):
    regions: Optional[List[str]] = None
    roleArn: Optional[str] = None


class DataLakeReplicationConfigurationTypeDef(BaseValidatorModel):
    regions: Optional[Sequence[str]] = None
    roleArn: Optional[str] = None


class DataLakeSourceStatusTypeDef(BaseValidatorModel):
    resource: Optional[str] = None
    status: Optional[SourceCollectionStatusType] = None


class DataLakeUpdateExceptionTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    reason: Optional[str] = None


class DeleteCustomLogSourceRequestTypeDef(BaseValidatorModel):
    sourceName: str
    sourceVersion: Optional[str] = None


class DeleteDataLakeRequestTypeDef(BaseValidatorModel):
    regions: Sequence[str]


class DeleteSubscriberNotificationRequestTypeDef(BaseValidatorModel):
    subscriberId: str


class DeleteSubscriberRequestTypeDef(BaseValidatorModel):
    subscriberId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetDataLakeSourcesRequestTypeDef(BaseValidatorModel):
    accounts: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetSubscriberRequestTypeDef(BaseValidatorModel):
    subscriberId: str


class HttpsNotificationConfigurationTypeDef(BaseValidatorModel):
    endpoint: str
    targetRoleArn: str
    authorizationApiKeyName: Optional[str] = None
    authorizationApiKeyValue: Optional[str] = None
    httpMethod: Optional[HttpMethodType] = None


class ListDataLakeExceptionsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regions: Optional[Sequence[str]] = None


class ListDataLakesRequestTypeDef(BaseValidatorModel):
    regions: Optional[Sequence[str]] = None


class ListSubscribersRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class RegisterDataLakeDelegatedAdministratorRequestTypeDef(BaseValidatorModel):
    accountId: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateDataLakeExceptionSubscriptionRequestTypeDef(BaseValidatorModel):
    notificationEndpoint: str
    subscriptionProtocol: str
    exceptionTimeToLive: Optional[int] = None


class CreateAwsLogSourceRequestTypeDef(BaseValidatorModel):
    sources: Sequence[AwsLogSourceConfigurationTypeDef]


class DeleteAwsLogSourceRequestTypeDef(BaseValidatorModel):
    sources: Sequence[AwsLogSourceConfigurationTypeDef]


class DataLakeAutoEnableNewAccountConfigurationOutputTypeDef(BaseValidatorModel):
    region: str
    sources: List[AwsLogSourceResourceTypeDef]


class DataLakeAutoEnableNewAccountConfigurationTypeDef(BaseValidatorModel):
    region: str
    sources: Sequence[AwsLogSourceResourceTypeDef]


class CreateAwsLogSourceResponseTypeDef(BaseValidatorModel):
    failed: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSubscriberNotificationResponseTypeDef(BaseValidatorModel):
    subscriberEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAwsLogSourceResponseTypeDef(BaseValidatorModel):
    failed: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDataLakeExceptionSubscriptionResponseTypeDef(BaseValidatorModel):
    exceptionTimeToLive: int
    notificationEndpoint: str
    subscriptionProtocol: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSubscriberNotificationResponseTypeDef(BaseValidatorModel):
    subscriberEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class CustomLogSourceConfigurationTypeDef(BaseValidatorModel):
    crawlerConfiguration: CustomLogSourceCrawlerConfigurationTypeDef
    providerIdentity: AwsIdentityTypeDef


class CustomLogSourceResourceTypeDef(BaseValidatorModel):
    attributes: Optional[CustomLogSourceAttributesTypeDef] = None
    provider: Optional[CustomLogSourceProviderTypeDef] = None
    sourceName: Optional[str] = None
    sourceVersion: Optional[str] = None


class ListDataLakeExceptionsResponseTypeDef(BaseValidatorModel):
    exceptions: List[DataLakeExceptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DataLakeLifecycleConfigurationOutputTypeDef(BaseValidatorModel):
    expiration: Optional[DataLakeLifecycleExpirationTypeDef] = None
    transitions: Optional[List[DataLakeLifecycleTransitionTypeDef]] = None


class DataLakeLifecycleConfigurationTypeDef(BaseValidatorModel):
    expiration: Optional[DataLakeLifecycleExpirationTypeDef] = None
    transitions: Optional[Sequence[DataLakeLifecycleTransitionTypeDef]] = None


class DataLakeSourceTypeDef(BaseValidatorModel):
    account: Optional[str] = None
    eventClasses: Optional[List[str]] = None
    sourceName: Optional[str] = None
    sourceStatuses: Optional[List[DataLakeSourceStatusTypeDef]] = None


class DataLakeUpdateStatusTypeDef(BaseValidatorModel):
    exception: Optional[DataLakeUpdateExceptionTypeDef] = None
    requestId: Optional[str] = None
    status: Optional[DataLakeStatusType] = None


class GetDataLakeSourcesRequestPaginateTypeDef(BaseValidatorModel):
    accounts: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataLakeExceptionsRequestPaginateTypeDef(BaseValidatorModel):
    regions: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSubscribersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class NotificationConfigurationTypeDef(BaseValidatorModel):
    httpsNotificationConfiguration: Optional[HttpsNotificationConfigurationTypeDef] = None
    sqsNotificationConfiguration: Optional[Mapping[str, Any]] = None


class GetDataLakeOrganizationConfigurationResponseTypeDef(BaseValidatorModel):
    autoEnableNewAccount: List[DataLakeAutoEnableNewAccountConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCustomLogSourceRequestTypeDef(BaseValidatorModel):
    configuration: CustomLogSourceConfigurationTypeDef
    sourceName: str
    eventClasses: Optional[Sequence[str]] = None
    sourceVersion: Optional[str] = None


class CreateCustomLogSourceResponseTypeDef(BaseValidatorModel):
    source: CustomLogSourceResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LogSourceResourceTypeDef(BaseValidatorModel):
    awsLogSource: Optional[AwsLogSourceResourceTypeDef] = None
    customLogSource: Optional[CustomLogSourceResourceTypeDef] = None


class GetDataLakeSourcesResponseTypeDef(BaseValidatorModel):
    dataLakeArn: str
    dataLakeSources: List[DataLakeSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DataLakeResourceTypeDef(BaseValidatorModel):
    dataLakeArn: str
    region: str
    createStatus: Optional[DataLakeStatusType] = None
    encryptionConfiguration: Optional[DataLakeEncryptionConfigurationTypeDef] = None
    lifecycleConfiguration: Optional[DataLakeLifecycleConfigurationOutputTypeDef] = None
    replicationConfiguration: Optional[DataLakeReplicationConfigurationOutputTypeDef] = None
    s3BucketArn: Optional[str] = None
    updateStatus: Optional[DataLakeUpdateStatusTypeDef] = None


class CreateSubscriberNotificationRequestTypeDef(BaseValidatorModel):
    configuration: NotificationConfigurationTypeDef
    subscriberId: str


class UpdateSubscriberNotificationRequestTypeDef(BaseValidatorModel):
    configuration: NotificationConfigurationTypeDef
    subscriberId: str


class DataLakeAutoEnableNewAccountConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateDataLakeOrganizationConfigurationRequestTypeDef(BaseValidatorModel):
    autoEnableNewAccount: Optional[ Sequence[DataLakeAutoEnableNewAccountConfigurationUnionTypeDef] ] = None


class DeleteDataLakeOrganizationConfigurationRequestTypeDef(BaseValidatorModel):
    autoEnableNewAccount: Optional[ Sequence[DataLakeAutoEnableNewAccountConfigurationUnionTypeDef] ] = None


class CreateSubscriberRequestTypeDef(BaseValidatorModel):
    sources: Sequence[LogSourceResourceTypeDef]
    subscriberIdentity: AwsIdentityTypeDef
    subscriberName: str
    accessTypes: Optional[Sequence[AccessTypeType]] = None
    subscriberDescription: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class ListLogSourcesRequestPaginateTypeDef(BaseValidatorModel):
    accounts: Optional[Sequence[str]] = None
    regions: Optional[Sequence[str]] = None
    sources: Optional[Sequence[LogSourceResourceTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLogSourcesRequestTypeDef(BaseValidatorModel):
    accounts: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regions: Optional[Sequence[str]] = None
    sources: Optional[Sequence[LogSourceResourceTypeDef]] = None


class LogSourceTypeDef(BaseValidatorModel):
    account: Optional[str] = None
    region: Optional[str] = None
    sources: Optional[List[LogSourceResourceTypeDef]] = None


class SubscriberResourceTypeDef(BaseValidatorModel):
    sources: List[LogSourceResourceTypeDef]
    subscriberArn: str
    subscriberId: str
    subscriberIdentity: AwsIdentityTypeDef
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


class UpdateSubscriberRequestTypeDef(BaseValidatorModel):
    subscriberId: str
    sources: Optional[Sequence[LogSourceResourceTypeDef]] = None
    subscriberDescription: Optional[str] = None
    subscriberIdentity: Optional[AwsIdentityTypeDef] = None
    subscriberName: Optional[str] = None


class DataLakeReplicationConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class DataLakeLifecycleConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class DataLakeConfigurationTypeDef(BaseValidatorModel):
    region: str
    encryptionConfiguration: Optional[DataLakeEncryptionConfigurationTypeDef] = None
    lifecycleConfiguration: Optional[DataLakeLifecycleConfigurationUnionTypeDef] = None
    replicationConfiguration: Optional[DataLakeReplicationConfigurationUnionTypeDef] = None


class CreateDataLakeResponseTypeDef(BaseValidatorModel):
    dataLakes: List[DataLakeResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListDataLakesResponseTypeDef(BaseValidatorModel):
    dataLakes: List[DataLakeResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDataLakeResponseTypeDef(BaseValidatorModel):
    dataLakes: List[DataLakeResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListLogSourcesResponseTypeDef(BaseValidatorModel):
    sources: List[LogSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateSubscriberResponseTypeDef(BaseValidatorModel):
    subscriber: SubscriberResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSubscriberResponseTypeDef(BaseValidatorModel):
    subscriber: SubscriberResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListSubscribersResponseTypeDef(BaseValidatorModel):
    subscribers: List[SubscriberResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateSubscriberResponseTypeDef(BaseValidatorModel):
    subscriber: SubscriberResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataLakeRequestTypeDef(BaseValidatorModel):
    configurations: Sequence[DataLakeConfigurationTypeDef]
    metaStoreManagerRoleArn: str
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateDataLakeRequestTypeDef(BaseValidatorModel):
    configurations: Sequence[DataLakeConfigurationTypeDef]
    metaStoreManagerRoleArn: Optional[str] = None


