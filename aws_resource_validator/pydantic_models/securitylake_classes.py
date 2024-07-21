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
from aws_resource_validator.pydantic_models.securitylake_constants import *

class AwsIdentityTypeDef(BaseModel):
    externalId: str
    principal: str

class AwsLogSourceConfigurationTypeDef(BaseModel):
    regions: Sequence[str]
    sourceName: AwsLogSourceNameType
    accounts: Optional[Sequence[str]] = None
    sourceVersion: Optional[str] = None

class AwsLogSourceResourceTypeDef(BaseModel):
    sourceName: Optional[AwsLogSourceNameType] = None
    sourceVersion: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateDataLakeExceptionSubscriptionRequestRequestTypeDef(BaseModel):
    notificationEndpoint: str
    subscriptionProtocol: str
    exceptionTimeToLive: Optional[int] = None

class TagTypeDef(BaseModel):
    key: str
    value: str

class CustomLogSourceAttributesTypeDef(BaseModel):
    crawlerArn: Optional[str] = None
    databaseArn: Optional[str] = None
    tableArn: Optional[str] = None

class CustomLogSourceCrawlerConfigurationTypeDef(BaseModel):
    roleArn: str

class CustomLogSourceProviderTypeDef(BaseModel):
    location: Optional[str] = None
    roleArn: Optional[str] = None

class DataLakeEncryptionConfigurationTypeDef(BaseModel):
    kmsKeyId: Optional[str] = None

class DataLakeReplicationConfigurationTypeDef(BaseModel):
    regions: Optional[Sequence[str]] = None
    roleArn: Optional[str] = None

class DataLakeExceptionTypeDef(BaseModel):
    exception: Optional[str] = None
    region: Optional[str] = None
    remediation: Optional[str] = None
    timestamp: Optional[datetime] = None

class DataLakeLifecycleExpirationTypeDef(BaseModel):
    days: Optional[int] = None

class DataLakeLifecycleTransitionTypeDef(BaseModel):
    days: Optional[int] = None
    storageClass: Optional[str] = None

class DataLakeReplicationConfigurationOutputTypeDef(BaseModel):
    regions: Optional[List[str]] = None
    roleArn: Optional[str] = None

class DataLakeSourceStatusTypeDef(BaseModel):
    resource: Optional[str] = None
    status: Optional[SourceCollectionStatusType] = None

class DataLakeUpdateExceptionTypeDef(BaseModel):
    code: Optional[str] = None
    reason: Optional[str] = None

class DeleteCustomLogSourceRequestRequestTypeDef(BaseModel):
    sourceName: str
    sourceVersion: Optional[str] = None

class DeleteDataLakeRequestRequestTypeDef(BaseModel):
    regions: Sequence[str]

class DeleteSubscriberNotificationRequestRequestTypeDef(BaseModel):
    subscriberId: str

class DeleteSubscriberRequestRequestTypeDef(BaseModel):
    subscriberId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetDataLakeSourcesRequestRequestTypeDef(BaseModel):
    accounts: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetSubscriberRequestRequestTypeDef(BaseModel):
    subscriberId: str

class HttpsNotificationConfigurationTypeDef(BaseModel):
    endpoint: str
    targetRoleArn: str
    authorizationApiKeyName: Optional[str] = None
    authorizationApiKeyValue: Optional[str] = None
    httpMethod: Optional[HttpMethodType] = None

class ListDataLakeExceptionsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regions: Optional[Sequence[str]] = None

class ListDataLakesRequestRequestTypeDef(BaseModel):
    regions: Optional[Sequence[str]] = None

class ListSubscribersRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class RegisterDataLakeDelegatedAdministratorRequestRequestTypeDef(BaseModel):
    accountId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateDataLakeExceptionSubscriptionRequestRequestTypeDef(BaseModel):
    notificationEndpoint: str
    subscriptionProtocol: str
    exceptionTimeToLive: Optional[int] = None

class CreateAwsLogSourceRequestRequestTypeDef(BaseModel):
    sources: Sequence[AwsLogSourceConfigurationTypeDef]

class DeleteAwsLogSourceRequestRequestTypeDef(BaseModel):
    sources: Sequence[AwsLogSourceConfigurationTypeDef]

class DataLakeAutoEnableNewAccountConfigurationOutputTypeDef(BaseModel):
    region: str
    sources: List[AwsLogSourceResourceTypeDef]

class DataLakeAutoEnableNewAccountConfigurationTypeDef(BaseModel):
    region: str
    sources: Sequence[AwsLogSourceResourceTypeDef]

class CreateAwsLogSourceResponseTypeDef(BaseModel):
    failed: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubscriberNotificationResponseTypeDef(BaseModel):
    subscriberEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAwsLogSourceResponseTypeDef(BaseModel):
    failed: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataLakeExceptionSubscriptionResponseTypeDef(BaseModel):
    exceptionTimeToLive: int
    notificationEndpoint: str
    subscriptionProtocol: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSubscriberNotificationResponseTypeDef(BaseModel):
    subscriberEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CustomLogSourceConfigurationTypeDef(BaseModel):
    crawlerConfiguration: CustomLogSourceCrawlerConfigurationTypeDef
    providerIdentity: AwsIdentityTypeDef

class CustomLogSourceResourceTypeDef(BaseModel):
    attributes: Optional[CustomLogSourceAttributesTypeDef] = None
    provider: Optional[CustomLogSourceProviderTypeDef] = None
    sourceName: Optional[str] = None
    sourceVersion: Optional[str] = None

class ListDataLakeExceptionsResponseTypeDef(BaseModel):
    exceptions: List[DataLakeExceptionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataLakeLifecycleConfigurationOutputTypeDef(BaseModel):
    expiration: Optional[DataLakeLifecycleExpirationTypeDef] = None
    transitions: Optional[List[DataLakeLifecycleTransitionTypeDef]] = None

class DataLakeLifecycleConfigurationTypeDef(BaseModel):
    expiration: Optional[DataLakeLifecycleExpirationTypeDef] = None
    transitions: Optional[Sequence[DataLakeLifecycleTransitionTypeDef]] = None

class DataLakeSourceTypeDef(BaseModel):
    account: Optional[str] = None
    eventClasses: Optional[List[str]] = None
    sourceName: Optional[str] = None
    sourceStatuses: Optional[List[DataLakeSourceStatusTypeDef]] = None

class DataLakeUpdateStatusTypeDef(BaseModel):
    exception: Optional[DataLakeUpdateExceptionTypeDef] = None
    requestId: Optional[str] = None
    status: Optional[DataLakeStatusType] = None

class GetDataLakeSourcesRequestGetDataLakeSourcesPaginateTypeDef(BaseModel):
    accounts: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataLakeExceptionsRequestListDataLakeExceptionsPaginateTypeDef(BaseModel):
    regions: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscribersRequestListSubscribersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class NotificationConfigurationTypeDef(BaseModel):
    httpsNotificationConfiguration: Optional[HttpsNotificationConfigurationTypeDef] = None
    sqsNotificationConfiguration: Optional[Mapping[str, Any]] = None

class GetDataLakeOrganizationConfigurationResponseTypeDef(BaseModel):
    autoEnableNewAccount: List[DataLakeAutoEnableNewAccountConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomLogSourceRequestRequestTypeDef(BaseModel):
    configuration: CustomLogSourceConfigurationTypeDef
    sourceName: str
    eventClasses: Optional[Sequence[str]] = None
    sourceVersion: Optional[str] = None

class CreateCustomLogSourceResponseTypeDef(BaseModel):
    source: CustomLogSourceResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LogSourceResourceTypeDef(BaseModel):
    awsLogSource: Optional[AwsLogSourceResourceTypeDef] = None
    customLogSource: Optional[CustomLogSourceResourceTypeDef] = None

class DataLakeConfigurationTypeDef(BaseModel):
    region: str
    encryptionConfiguration: Optional[DataLakeEncryptionConfigurationTypeDef] = None
    lifecycleConfiguration: Optional[DataLakeLifecycleConfigurationTypeDef] = None
    replicationConfiguration: Optional[DataLakeReplicationConfigurationTypeDef] = None

class GetDataLakeSourcesResponseTypeDef(BaseModel):
    dataLakeArn: str
    dataLakeSources: List[DataLakeSourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataLakeResourceTypeDef(BaseModel):
    dataLakeArn: str
    region: str
    createStatus: Optional[DataLakeStatusType] = None
    encryptionConfiguration: Optional[DataLakeEncryptionConfigurationTypeDef] = None
    lifecycleConfiguration: Optional[DataLakeLifecycleConfigurationOutputTypeDef] = None
    replicationConfiguration: Optional[DataLakeReplicationConfigurationOutputTypeDef] = None
    s3BucketArn: Optional[str] = None
    updateStatus: Optional[DataLakeUpdateStatusTypeDef] = None

class CreateSubscriberNotificationRequestRequestTypeDef(BaseModel):
    configuration: NotificationConfigurationTypeDef
    subscriberId: str

class UpdateSubscriberNotificationRequestRequestTypeDef(BaseModel):
    configuration: NotificationConfigurationTypeDef
    subscriberId: str

class CreateDataLakeOrganizationConfigurationRequestRequestTypeDef(BaseModel):
    autoEnableNewAccount: Optional[       Sequence[DataLakeAutoEnableNewAccountConfigurationUnionTypeDef]     ] = None

class DeleteDataLakeOrganizationConfigurationRequestRequestTypeDef(BaseModel):
    autoEnableNewAccount: Optional[       Sequence[DataLakeAutoEnableNewAccountConfigurationUnionTypeDef]     ] = None

class CreateSubscriberRequestRequestTypeDef(BaseModel):
    sources: Sequence[LogSourceResourceTypeDef]
    subscriberIdentity: AwsIdentityTypeDef
    subscriberName: str
    accessTypes: Optional[Sequence[AccessTypeType]] = None
    subscriberDescription: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListLogSourcesRequestListLogSourcesPaginateTypeDef(BaseModel):
    accounts: Optional[Sequence[str]] = None
    regions: Optional[Sequence[str]] = None
    sources: Optional[Sequence[LogSourceResourceTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLogSourcesRequestRequestTypeDef(BaseModel):
    accounts: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regions: Optional[Sequence[str]] = None
    sources: Optional[Sequence[LogSourceResourceTypeDef]] = None

class LogSourceTypeDef(BaseModel):
    account: Optional[str] = None
    region: Optional[str] = None
    sources: Optional[List[LogSourceResourceTypeDef]] = None

class SubscriberResourceTypeDef(BaseModel):
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

class UpdateSubscriberRequestRequestTypeDef(BaseModel):
    subscriberId: str
    sources: Optional[Sequence[LogSourceResourceTypeDef]] = None
    subscriberDescription: Optional[str] = None
    subscriberIdentity: Optional[AwsIdentityTypeDef] = None
    subscriberName: Optional[str] = None

class CreateDataLakeRequestRequestTypeDef(BaseModel):
    configurations: Sequence[DataLakeConfigurationTypeDef]
    metaStoreManagerRoleArn: str
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateDataLakeRequestRequestTypeDef(BaseModel):
    configurations: Sequence[DataLakeConfigurationTypeDef]
    metaStoreManagerRoleArn: Optional[str] = None

class CreateDataLakeResponseTypeDef(BaseModel):
    dataLakes: List[DataLakeResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataLakesResponseTypeDef(BaseModel):
    dataLakes: List[DataLakeResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataLakeResponseTypeDef(BaseModel):
    dataLakes: List[DataLakeResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListLogSourcesResponseTypeDef(BaseModel):
    nextToken: str
    sources: List[LogSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubscriberResponseTypeDef(BaseModel):
    subscriber: SubscriberResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriberResponseTypeDef(BaseModel):
    subscriber: SubscriberResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscribersResponseTypeDef(BaseModel):
    nextToken: str
    subscribers: List[SubscriberResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSubscriberResponseTypeDef(BaseModel):
    subscriber: SubscriberResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

