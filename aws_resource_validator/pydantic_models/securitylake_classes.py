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

class CreateDataLakeExceptionSubscriptionRequestRequestTypeDef(BaseValidatorModel):
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

class DataLakeReplicationConfigurationTypeDef(BaseValidatorModel):
    regions: Optional[Sequence[str]] = None
    roleArn: Optional[str] = None

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

class DataLakeSourceStatusTypeDef(BaseValidatorModel):
    resource: Optional[str] = None
    status: Optional[SourceCollectionStatusType] = None

class DataLakeUpdateExceptionTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    reason: Optional[str] = None

class DeleteCustomLogSourceRequestRequestTypeDef(BaseValidatorModel):
    sourceName: str
    sourceVersion: Optional[str] = None

class DeleteDataLakeRequestRequestTypeDef(BaseValidatorModel):
    regions: Sequence[str]

class DeleteSubscriberNotificationRequestRequestTypeDef(BaseValidatorModel):
    subscriberId: str

class DeleteSubscriberRequestRequestTypeDef(BaseValidatorModel):
    subscriberId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetDataLakeSourcesRequestRequestTypeDef(BaseValidatorModel):
    accounts: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetSubscriberRequestRequestTypeDef(BaseValidatorModel):
    subscriberId: str

class HttpsNotificationConfigurationTypeDef(BaseValidatorModel):
    endpoint: str
    targetRoleArn: str
    authorizationApiKeyName: Optional[str] = None
    authorizationApiKeyValue: Optional[str] = None
    httpMethod: Optional[HttpMethodType] = None

class ListDataLakeExceptionsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    regions: Optional[Sequence[str]] = None

class ListDataLakesRequestRequestTypeDef(BaseValidatorModel):
    regions: Optional[Sequence[str]] = None

class ListSubscribersRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class RegisterDataLakeDelegatedAdministratorRequestRequestTypeDef(BaseValidatorModel):
    accountId: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateDataLakeExceptionSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    notificationEndpoint: str
    subscriptionProtocol: str
    exceptionTimeToLive: Optional[int] = None

class CreateAwsLogSourceRequestRequestTypeDef(BaseValidatorModel):
    sources: Sequence[AwsLogSourceConfigurationTypeDef]

class DeleteAwsLogSourceRequestRequestTypeDef(BaseValidatorModel):
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

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class GetDataLakeSourcesRequestGetDataLakeSourcesPaginateTypeDef(BaseValidatorModel):
    accounts: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataLakeExceptionsRequestListDataLakeExceptionsPaginateTypeDef(BaseValidatorModel):
    regions: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscribersRequestListSubscribersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class NotificationConfigurationTypeDef(BaseValidatorModel):
    httpsNotificationConfiguration: Optional[HttpsNotificationConfigurationTypeDef] = None
    sqsNotificationConfiguration: Optional[Mapping[str, Any]] = None

class GetDataLakeOrganizationConfigurationResponseTypeDef(BaseValidatorModel):
    autoEnableNewAccount: List[DataLakeAutoEnableNewAccountConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomLogSourceRequestRequestTypeDef(BaseValidatorModel):
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

class DataLakeConfigurationTypeDef(BaseValidatorModel):
    region: str
    encryptionConfiguration: Optional[DataLakeEncryptionConfigurationTypeDef] = None
    lifecycleConfiguration: Optional[DataLakeLifecycleConfigurationTypeDef] = None
    replicationConfiguration: Optional[DataLakeReplicationConfigurationTypeDef] = None

class GetDataLakeSourcesResponseTypeDef(BaseValidatorModel):
    dataLakeArn: str
    dataLakeSources: List[DataLakeSourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataLakeResourceTypeDef(BaseValidatorModel):
    dataLakeArn: str
    region: str
    createStatus: Optional[DataLakeStatusType] = None
    encryptionConfiguration: Optional[DataLakeEncryptionConfigurationTypeDef] = None
    lifecycleConfiguration: Optional[DataLakeLifecycleConfigurationOutputTypeDef] = None
    replicationConfiguration: Optional[DataLakeReplicationConfigurationOutputTypeDef] = None
    s3BucketArn: Optional[str] = None
    updateStatus: Optional[DataLakeUpdateStatusTypeDef] = None

class CreateSubscriberNotificationRequestRequestTypeDef(BaseValidatorModel):
    configuration: NotificationConfigurationTypeDef
    subscriberId: str

class UpdateSubscriberNotificationRequestRequestTypeDef(BaseValidatorModel):
    configuration: NotificationConfigurationTypeDef
    subscriberId: str

class CreateDataLakeOrganizationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    autoEnableNewAccount: Optional[       Sequence[DataLakeAutoEnableNewAccountConfigurationUnionTypeDef]     ] = None

class DeleteDataLakeOrganizationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    autoEnableNewAccount: Optional[       Sequence[DataLakeAutoEnableNewAccountConfigurationUnionTypeDef]     ] = None

class CreateSubscriberRequestRequestTypeDef(BaseValidatorModel):
    sources: Sequence[LogSourceResourceTypeDef]
    subscriberIdentity: AwsIdentityTypeDef
    subscriberName: str
    accessTypes: Optional[Sequence[AccessTypeType]] = None
    subscriberDescription: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListLogSourcesRequestListLogSourcesPaginateTypeDef(BaseValidatorModel):
    accounts: Optional[Sequence[str]] = None
    regions: Optional[Sequence[str]] = None
    sources: Optional[Sequence[LogSourceResourceTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLogSourcesRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateSubscriberRequestRequestTypeDef(BaseValidatorModel):
    subscriberId: str
    sources: Optional[Sequence[LogSourceResourceTypeDef]] = None
    subscriberDescription: Optional[str] = None
    subscriberIdentity: Optional[AwsIdentityTypeDef] = None
    subscriberName: Optional[str] = None

class CreateDataLakeRequestRequestTypeDef(BaseValidatorModel):
    configurations: Sequence[DataLakeConfigurationTypeDef]
    metaStoreManagerRoleArn: str
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateDataLakeRequestRequestTypeDef(BaseValidatorModel):
    configurations: Sequence[DataLakeConfigurationTypeDef]
    metaStoreManagerRoleArn: Optional[str] = None

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
    nextToken: str
    sources: List[LogSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubscriberResponseTypeDef(BaseValidatorModel):
    subscriber: SubscriberResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriberResponseTypeDef(BaseValidatorModel):
    subscriber: SubscriberResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscribersResponseTypeDef(BaseValidatorModel):
    nextToken: str
    subscribers: List[SubscriberResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSubscriberResponseTypeDef(BaseValidatorModel):
    subscriber: SubscriberResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

