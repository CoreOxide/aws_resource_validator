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
from aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_constants import *

class DeregisterSubscriptionProviderRequest(BaseValidatorModel):
    SubscriptionProviderArn: str


class Filter(BaseValidatorModel):
    Name: Optional[str] = None
    Operator: Optional[OperatorType] = None
    Values: Optional[Sequence[str]] = None


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
    SourceRegions: Sequence[str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListRegisteredSubscriptionProvidersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SubscriptionProviderSources: Optional[Sequence[Literal["RedHat"]]] = None


class RegisteredSubscriptionProvider(BaseValidatorModel):
    LastSuccessfulDataRetrievalTime: Optional[str] = None
    SecretArn: Optional[str] = None
    SubscriptionProviderArn: Optional[str] = None
    SubscriptionProviderSource: Optional[Literal["RedHat"]] = None
    SubscriptionProviderStatus: Optional[SubscriptionProviderStatusType] = None
    SubscriptionProviderStatusMessage: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class RegisterSubscriptionProviderRequest(BaseValidatorModel):
    SecretArn: str
    SubscriptionProviderSource: Literal["RedHat"]
    Tags: Optional[Mapping[str, str]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class ListLinuxSubscriptionInstancesRequest(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLinuxSubscriptionsRequest(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetRegisteredSubscriptionProviderResponse(BaseValidatorModel):
    LastSuccessfulDataRetrievalTime: str
    SecretArn: str
    SubscriptionProviderArn: str
    SubscriptionProviderSource: Literal["RedHat"]
    SubscriptionProviderStatus: SubscriptionProviderStatusType
    SubscriptionProviderStatusMessage: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class RegisterSubscriptionProviderResponse(BaseValidatorModel):
    SubscriptionProviderArn: str
    SubscriptionProviderSource: Literal["RedHat"]
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


class ListLinuxSubscriptionInstancesRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLinuxSubscriptionsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRegisteredSubscriptionProvidersRequestPaginate(BaseValidatorModel):
    SubscriptionProviderSources: Optional[Sequence[Literal["RedHat"]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class Subscription(BaseValidatorModel):
    pass


class ListLinuxSubscriptionsResponse(BaseValidatorModel):
    Subscriptions: List[Subscription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRegisteredSubscriptionProvidersResponse(BaseValidatorModel):
    RegisteredSubscriptionProviders: List[RegisteredSubscriptionProvider]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LinuxSubscriptionsDiscoverySettingsUnion(BaseValidatorModel):
    pass


class UpdateServiceSettingsRequest(BaseValidatorModel):
    LinuxSubscriptionsDiscovery: LinuxSubscriptionsDiscoveryType
    LinuxSubscriptionsDiscoverySettings: LinuxSubscriptionsDiscoverySettingsUnion
    AllowUpdate: Optional[bool] = None


