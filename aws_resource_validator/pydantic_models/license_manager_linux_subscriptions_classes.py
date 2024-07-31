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
from aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_constants import *

class DeregisterSubscriptionProviderRequestRequestTypeDef(BaseModel):
    SubscriptionProviderArn: str

class FilterTypeDef(BaseModel):
    Name: Optional[str] = None
    Operator: Optional[OperatorType] = None
    Values: Optional[Sequence[str]] = None

class GetRegisteredSubscriptionProviderRequestRequestTypeDef(BaseModel):
    SubscriptionProviderArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class LinuxSubscriptionsDiscoverySettingsOutputTypeDef(BaseModel):
    OrganizationIntegration: OrganizationIntegrationType
    SourceRegions: List[str]

class InstanceTypeDef(BaseModel):
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

class LinuxSubscriptionsDiscoverySettingsTypeDef(BaseModel):
    OrganizationIntegration: OrganizationIntegrationType
    SourceRegions: Sequence[str]

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class SubscriptionTypeDef(BaseModel):
    InstanceCount: Optional[int] = None
    Name: Optional[str] = None
    Type: Optional[str] = None

class ListRegisteredSubscriptionProvidersRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SubscriptionProviderSources: Optional[Sequence[Literal["RedHat"]]] = None

class RegisteredSubscriptionProviderTypeDef(BaseModel):
    LastSuccessfulDataRetrievalTime: Optional[str] = None
    SecretArn: Optional[str] = None
    SubscriptionProviderArn: Optional[str] = None
    SubscriptionProviderSource: Optional[Literal["RedHat"]] = None
    SubscriptionProviderStatus: Optional[SubscriptionProviderStatusType] = None
    SubscriptionProviderStatusMessage: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class RegisterSubscriptionProviderRequestRequestTypeDef(BaseModel):
    SecretArn: str
    SubscriptionProviderSource: Literal["RedHat"]
    Tags: Optional[Mapping[str, str]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class ListLinuxSubscriptionInstancesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListLinuxSubscriptionsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetRegisteredSubscriptionProviderResponseTypeDef(BaseModel):
    LastSuccessfulDataRetrievalTime: str
    SecretArn: str
    SubscriptionProviderArn: str
    SubscriptionProviderSource: Literal["RedHat"]
    SubscriptionProviderStatus: SubscriptionProviderStatusType
    SubscriptionProviderStatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterSubscriptionProviderResponseTypeDef(BaseModel):
    SubscriptionProviderArn: str
    SubscriptionProviderSource: Literal["RedHat"]
    SubscriptionProviderStatus: SubscriptionProviderStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceSettingsResponseTypeDef(BaseModel):
    HomeRegions: List[str]
    LinuxSubscriptionsDiscovery: LinuxSubscriptionsDiscoveryType
    LinuxSubscriptionsDiscoverySettings: LinuxSubscriptionsDiscoverySettingsOutputTypeDef
    Status: StatusType
    StatusMessage: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceSettingsResponseTypeDef(BaseModel):
    HomeRegions: List[str]
    LinuxSubscriptionsDiscovery: LinuxSubscriptionsDiscoveryType
    LinuxSubscriptionsDiscoverySettings: LinuxSubscriptionsDiscoverySettingsOutputTypeDef
    Status: StatusType
    StatusMessage: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListLinuxSubscriptionInstancesResponseTypeDef(BaseModel):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateServiceSettingsRequestRequestTypeDef(BaseModel):
    LinuxSubscriptionsDiscovery: LinuxSubscriptionsDiscoveryType
    LinuxSubscriptionsDiscoverySettings: LinuxSubscriptionsDiscoverySettingsTypeDef
    AllowUpdate: Optional[bool] = None

class ListLinuxSubscriptionInstancesRequestListLinuxSubscriptionInstancesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLinuxSubscriptionsRequestListLinuxSubscriptionsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRegisteredSubscriptionProvidersRequestListRegisteredSubscriptionProvidersPaginateTypeDef(BaseModel):
    SubscriptionProviderSources: Optional[Sequence[Literal["RedHat"]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLinuxSubscriptionsResponseTypeDef(BaseModel):
    Subscriptions: List[SubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRegisteredSubscriptionProvidersResponseTypeDef(BaseModel):
    RegisteredSubscriptionProviders: List[RegisteredSubscriptionProviderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

