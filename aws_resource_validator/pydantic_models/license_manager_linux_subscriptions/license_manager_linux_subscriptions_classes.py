from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.license_manager_linux_subscriptions.license_manager_linux_subscriptions_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class DeregisterSubscriptionProviderRequest(BaseValidatorModel):
    SubscriptionProviderArn: str


class Filter(BaseValidatorModel):
    Name: Optional[str] = None
    Operator: Optional[OperatorType] = None
    Values: Optional[List[str]] = None


class GetRegisteredSubscriptionProviderRequest(BaseValidatorModel):
    SubscriptionProviderArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class LinuxSubscriptionsDiscoverySettingsOutput(BaseValidatorModel):
    OrganizationIntegration: OrganizationIntegrationType
    SourceRegions: List[str]


class Instance(BaseValidatorModel):
    AccountID: Optional[str] = None
    AmiId: Optional[str] = None
    DualSubscription: Optional[str] = None
    InstanceID: Optional[str] = None
    InstanceType: Optional[str] = None
    LastUpdatedTime: Optional[str] = None
    OsVersion: Optional[str] = None
    ProductCode: Optional[List[str]] = None
    Region: Optional[str] = None
    RegisteredWithSubscriptionProvider: Optional[str] = None
    Status: Optional[str] = None
    SubscriptionName: Optional[str] = None
    SubscriptionProviderCreateTime: Optional[str] = None
    SubscriptionProviderUpdateTime: Optional[str] = None
    UsageOperation: Optional[str] = None


class LinuxSubscriptionsDiscoverySettings(BaseValidatorModel):
    OrganizationIntegration: OrganizationIntegrationType
    SourceRegions: List[str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class Subscription(BaseValidatorModel):
    InstanceCount: Optional[int] = None
    Name: Optional[str] = None
    Type: Optional[str] = None


class ListRegisteredSubscriptionProvidersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SubscriptionProviderSources: Optional[List[Literal['RedHat']]] = None


class RegisteredSubscriptionProvider(BaseValidatorModel):
    LastSuccessfulDataRetrievalTime: Optional[str] = None
    SecretArn: Optional[str] = None
    SubscriptionProviderArn: Optional[str] = None
    SubscriptionProviderSource: Optional[Literal['RedHat']] = None
    SubscriptionProviderStatus: Optional[SubscriptionProviderStatusType] = None
    SubscriptionProviderStatusMessage: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class RegisterSubscriptionProviderRequest(BaseValidatorModel):
    SecretArn: str
    SubscriptionProviderSource: Literal['RedHat']
    Tags: Optional[Dict[str, str]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class ListLinuxSubscriptionInstancesRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLinuxSubscriptionsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetRegisteredSubscriptionProviderResponse(BaseValidatorModel):
    LastSuccessfulDataRetrievalTime: str
    SecretArn: str
    SubscriptionProviderArn: str
    SubscriptionProviderSource: Literal['RedHat']
    SubscriptionProviderStatus: SubscriptionProviderStatusType
    SubscriptionProviderStatusMessage: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class RegisterSubscriptionProviderResponse(BaseValidatorModel):
    SubscriptionProviderArn: str
    SubscriptionProviderSource: Literal['RedHat']
    SubscriptionProviderStatus: SubscriptionProviderStatusType
    ResponseMetadata: ResponseMetadata


class GetServiceSettingsResponse(BaseValidatorModel):
    HomeRegions: List[str]
    LinuxSubscriptionsDiscovery: LinuxSubscriptionsDiscoveryType
    LinuxSubscriptionsDiscoverySettings: LinuxSubscriptionsDiscoverySettingsOutput
    Status: StatusType
    StatusMessage: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateServiceSettingsResponse(BaseValidatorModel):
    HomeRegions: List[str]
    LinuxSubscriptionsDiscovery: LinuxSubscriptionsDiscoveryType
    LinuxSubscriptionsDiscoverySettings: LinuxSubscriptionsDiscoverySettingsOutput
    Status: StatusType
    StatusMessage: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListLinuxSubscriptionInstancesResponse(BaseValidatorModel):
    Instances: List[Instance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

LinuxSubscriptionsDiscoverySettingsUnion = Union[LinuxSubscriptionsDiscoverySettings, LinuxSubscriptionsDiscoverySettingsOutput]


class ListLinuxSubscriptionInstancesRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLinuxSubscriptionsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRegisteredSubscriptionProvidersRequestPaginate(BaseValidatorModel):
    SubscriptionProviderSources: Optional[List[Literal['RedHat']]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLinuxSubscriptionsResponse(BaseValidatorModel):
    Subscriptions: List[Subscription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRegisteredSubscriptionProvidersResponse(BaseValidatorModel):
    RegisteredSubscriptionProviders: List[RegisteredSubscriptionProvider]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateServiceSettingsRequest(BaseValidatorModel):
    LinuxSubscriptionsDiscovery: LinuxSubscriptionsDiscoveryType
    LinuxSubscriptionsDiscoverySettings: LinuxSubscriptionsDiscoverySettingsUnion
    AllowUpdate: Optional[bool] = None