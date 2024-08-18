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
from aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_constants import *

class DeregisterSubscriptionProviderRequestRequestTypeDef(BaseValidatorModel):
    SubscriptionProviderArn: str

class FilterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Operator: Optional[OperatorType] = None
    Values: Optional[Sequence[str]] = None

class GetRegisteredSubscriptionProviderRequestRequestTypeDef(BaseValidatorModel):
    SubscriptionProviderArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class LinuxSubscriptionsDiscoverySettingsOutputTypeDef(BaseValidatorModel):
    OrganizationIntegration: OrganizationIntegrationType
    SourceRegions: List[str]

class InstanceTypeDef(BaseValidatorModel):
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

class LinuxSubscriptionsDiscoverySettingsTypeDef(BaseValidatorModel):
    OrganizationIntegration: OrganizationIntegrationType
    SourceRegions: Sequence[str]

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class SubscriptionTypeDef(BaseValidatorModel):
    InstanceCount: Optional[int] = None
    Name: Optional[str] = None
    Type: Optional[str] = None

class ListRegisteredSubscriptionProvidersRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SubscriptionProviderSources: Optional[Sequence[Literal["RedHat"]]] = None

class RegisteredSubscriptionProviderTypeDef(BaseValidatorModel):
    LastSuccessfulDataRetrievalTime: Optional[str] = None
    SecretArn: Optional[str] = None
    SubscriptionProviderArn: Optional[str] = None
    SubscriptionProviderSource: Optional[Literal["RedHat"]] = None
    SubscriptionProviderStatus: Optional[SubscriptionProviderStatusType] = None
    SubscriptionProviderStatusMessage: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class RegisterSubscriptionProviderRequestRequestTypeDef(BaseValidatorModel):
    SecretArn: str
    SubscriptionProviderSource: Literal["RedHat"]
    Tags: Optional[Mapping[str, str]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class ListLinuxSubscriptionInstancesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListLinuxSubscriptionsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetRegisteredSubscriptionProviderResponseTypeDef(BaseValidatorModel):
    LastSuccessfulDataRetrievalTime: str
    SecretArn: str
    SubscriptionProviderArn: str
    SubscriptionProviderSource: Literal["RedHat"]
    SubscriptionProviderStatus: SubscriptionProviderStatusType
    SubscriptionProviderStatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterSubscriptionProviderResponseTypeDef(BaseValidatorModel):
    SubscriptionProviderArn: str
    SubscriptionProviderSource: Literal["RedHat"]
    SubscriptionProviderStatus: SubscriptionProviderStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceSettingsResponseTypeDef(BaseValidatorModel):
    HomeRegions: List[str]
    LinuxSubscriptionsDiscovery: LinuxSubscriptionsDiscoveryType
    LinuxSubscriptionsDiscoverySettings: LinuxSubscriptionsDiscoverySettingsOutputTypeDef
    Status: StatusType
    StatusMessage: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceSettingsResponseTypeDef(BaseValidatorModel):
    HomeRegions: List[str]
    LinuxSubscriptionsDiscovery: LinuxSubscriptionsDiscoveryType
    LinuxSubscriptionsDiscoverySettings: LinuxSubscriptionsDiscoverySettingsOutputTypeDef
    Status: StatusType
    StatusMessage: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListLinuxSubscriptionInstancesResponseTypeDef(BaseValidatorModel):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateServiceSettingsRequestRequestTypeDef(BaseValidatorModel):
    LinuxSubscriptionsDiscovery: LinuxSubscriptionsDiscoveryType
    LinuxSubscriptionsDiscoverySettings: LinuxSubscriptionsDiscoverySettingsTypeDef
    AllowUpdate: Optional[bool] = None

class ListLinuxSubscriptionInstancesRequestListLinuxSubscriptionInstancesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLinuxSubscriptionsRequestListLinuxSubscriptionsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRegisteredSubscriptionProvidersRequestListRegisteredSubscriptionProvidersPaginateTypeDef(BaseValidatorModel):
    SubscriptionProviderSources: Optional[Sequence[Literal["RedHat"]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLinuxSubscriptionsResponseTypeDef(BaseValidatorModel):
    Subscriptions: List[SubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRegisteredSubscriptionProvidersResponseTypeDef(BaseValidatorModel):
    RegisteredSubscriptionProviders: List[RegisteredSubscriptionProviderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

