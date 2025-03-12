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
from aws_resource_validator.pydantic_models.outposts_constants import *

class AddressTypeDef(BaseValidatorModel):
    AddressLine1: str
    City: str
    StateOrRegion: str
    PostalCode: str
    CountryCode: str
    ContactName: Optional[str] = None
    ContactPhoneNumber: Optional[str] = None
    AddressLine2: Optional[str] = None
    AddressLine3: Optional[str] = None
    DistrictOrCounty: Optional[str] = None
    Municipality: Optional[str] = None


class AssetLocationTypeDef(BaseValidatorModel):
    RackElevation: Optional[float] = None


class AssetInstanceTypeCapacityTypeDef(BaseValidatorModel):
    InstanceType: str
    Count: int


class AssetInstanceTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    AssetId: Optional[str] = None
    AccountId: Optional[str] = None
    AwsServiceName: Optional[AWSServiceNameType] = None


class BlockingInstanceTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    AccountId: Optional[str] = None
    AwsServiceName: Optional[AWSServiceNameType] = None


class CancelCapacityTaskInputTypeDef(BaseValidatorModel):
    CapacityTaskId: str
    OutpostIdentifier: str


class CancelOrderInputTypeDef(BaseValidatorModel):
    OrderId: str


class CapacityTaskSummaryTypeDef(BaseValidatorModel):
    CapacityTaskId: Optional[str] = None
    OutpostId: Optional[str] = None
    OrderId: Optional[str] = None
    CapacityTaskStatus: Optional[CapacityTaskStatusType] = None
    CreationDate: Optional[datetime] = None
    CompletionDate: Optional[datetime] = None
    LastModifiedDate: Optional[datetime] = None


class EC2CapacityTypeDef(BaseValidatorModel):
    Family: Optional[str] = None
    MaxSize: Optional[str] = None
    Quantity: Optional[str] = None


class ConnectionDetailsTypeDef(BaseValidatorModel):
    ClientPublicKey: Optional[str] = None
    ServerPublicKey: Optional[str] = None
    ServerEndpoint: Optional[str] = None
    ClientTunnelAddress: Optional[str] = None
    ServerTunnelAddress: Optional[str] = None
    AllowedIps: Optional[List[str]] = None


class LineItemRequestTypeDef(BaseValidatorModel):
    CatalogItemId: Optional[str] = None
    Quantity: Optional[int] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateOutpostInputTypeDef(BaseValidatorModel):
    Name: str
    SiteId: str
    Description: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    SupportedHardwareType: Optional[SupportedHardwareTypeType] = None


class OutpostTypeDef(BaseValidatorModel):
    OutpostId: Optional[str] = None
    OwnerId: Optional[str] = None
    OutpostArn: Optional[str] = None
    SiteId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    LifeCycleStatus: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    SiteArn: Optional[str] = None
    SupportedHardwareType: Optional[SupportedHardwareTypeType] = None


class RackPhysicalPropertiesTypeDef(BaseValidatorModel):
    PowerDrawKva: Optional[PowerDrawKvaType] = None
    PowerPhase: Optional[PowerPhaseType] = None
    PowerConnector: Optional[PowerConnectorType] = None
    PowerFeedDrop: Optional[PowerFeedDropType] = None
    UplinkGbps: Optional[UplinkGbpsType] = None
    UplinkCount: Optional[UplinkCountType] = None
    FiberOpticCableType: Optional[FiberOpticCableTypeType] = None
    OpticalStandard: Optional[OpticalStandardType] = None
    MaximumSupportedWeightLbs: Optional[MaximumSupportedWeightLbsType] = None


class DeleteOutpostInputTypeDef(BaseValidatorModel):
    OutpostId: str


class DeleteSiteInputTypeDef(BaseValidatorModel):
    SiteId: str


class GetCapacityTaskInputTypeDef(BaseValidatorModel):
    CapacityTaskId: str
    OutpostIdentifier: str


class InstanceTypeCapacityTypeDef(BaseValidatorModel):
    InstanceType: str
    Count: int


class InstancesToExcludeOutputTypeDef(BaseValidatorModel):
    Instances: Optional[List[str]] = None
    AccountIds: Optional[List[str]] = None
    Services: Optional[List[AWSServiceNameType]] = None


class GetCatalogItemInputTypeDef(BaseValidatorModel):
    CatalogItemId: str


class GetConnectionRequestTypeDef(BaseValidatorModel):
    ConnectionId: str


class GetOrderInputTypeDef(BaseValidatorModel):
    OrderId: str


class GetOutpostInputTypeDef(BaseValidatorModel):
    OutpostId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetOutpostInstanceTypesInputTypeDef(BaseValidatorModel):
    OutpostId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class InstanceTypeItemTypeDef(BaseValidatorModel):
    InstanceType: Optional[str] = None
    VCPUs: Optional[int] = None


class GetOutpostSupportedInstanceTypesInputTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    OrderId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetSiteAddressInputTypeDef(BaseValidatorModel):
    SiteId: str
    AddressType: AddressTypeType


class GetSiteInputTypeDef(BaseValidatorModel):
    SiteId: str


class InstancesToExcludeTypeDef(BaseValidatorModel):
    Instances: Optional[Sequence[str]] = None
    AccountIds: Optional[Sequence[str]] = None
    Services: Optional[Sequence[AWSServiceNameType]] = None


class LineItemAssetInformationTypeDef(BaseValidatorModel):
    AssetId: Optional[str] = None
    MacAddressList: Optional[List[str]] = None


class ShipmentInformationTypeDef(BaseValidatorModel):
    ShipmentTrackingNumber: Optional[str] = None
    ShipmentCarrier: Optional[ShipmentCarrierType] = None


class ListAssetInstancesInputTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    AssetIdFilter: Optional[Sequence[str]] = None
    InstanceTypeFilter: Optional[Sequence[str]] = None
    AccountIdFilter: Optional[Sequence[str]] = None
    AwsServiceFilter: Optional[Sequence[AWSServiceNameType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAssetsInputTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    HostIdFilter: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StatusFilter: Optional[Sequence[AssetStateType]] = None


class ListBlockingInstancesForCapacityTaskInputTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    CapacityTaskId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCapacityTasksInputTypeDef(BaseValidatorModel):
    OutpostIdentifierFilter: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    CapacityTaskStatusFilter: Optional[Sequence[CapacityTaskStatusType]] = None


class ListCatalogItemsInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ItemClassFilter: Optional[Sequence[CatalogItemClassType]] = None
    SupportedStorageFilter: Optional[Sequence[SupportedStorageEnumType]] = None
    EC2FamilyFilter: Optional[Sequence[str]] = None


class ListOrdersInputTypeDef(BaseValidatorModel):
    OutpostIdentifierFilter: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OrderSummaryTypeDef(BaseValidatorModel):
    OutpostId: Optional[str] = None
    OrderId: Optional[str] = None
    OrderType: Optional[OrderTypeType] = None
    Status: Optional[OrderStatusType] = None
    LineItemCountsByStatus: Optional[Dict[LineItemStatusType, int]] = None
    OrderSubmissionDate: Optional[datetime] = None
    OrderFulfilledDate: Optional[datetime] = None


class ListOutpostsInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LifeCycleStatusFilter: Optional[Sequence[str]] = None
    AvailabilityZoneFilter: Optional[Sequence[str]] = None
    AvailabilityZoneIdFilter: Optional[Sequence[str]] = None


class ListSitesInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    OperatingAddressCountryCodeFilter: Optional[Sequence[str]] = None
    OperatingAddressStateOrRegionFilter: Optional[Sequence[str]] = None
    OperatingAddressCityFilter: Optional[Sequence[str]] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class StartConnectionRequestTypeDef(BaseValidatorModel):
    AssetId: str
    ClientPublicKey: str
    NetworkInterfaceDeviceIndex: int
    DeviceSerialNumber: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateOutpostInputTypeDef(BaseValidatorModel):
    OutpostId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    SupportedHardwareType: Optional[SupportedHardwareTypeType] = None


class UpdateSiteInputTypeDef(BaseValidatorModel):
    SiteId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Notes: Optional[str] = None


class UpdateSiteRackPhysicalPropertiesInputTypeDef(BaseValidatorModel):
    SiteId: str
    PowerDrawKva: Optional[PowerDrawKvaType] = None
    PowerPhase: Optional[PowerPhaseType] = None
    PowerConnector: Optional[PowerConnectorType] = None
    PowerFeedDrop: Optional[PowerFeedDropType] = None
    UplinkGbps: Optional[UplinkGbpsType] = None
    UplinkCount: Optional[UplinkCountType] = None
    FiberOpticCableType: Optional[FiberOpticCableTypeType] = None
    OpticalStandard: Optional[OpticalStandardType] = None
    MaximumSupportedWeightLbs: Optional[MaximumSupportedWeightLbsType] = None


class UpdateSiteAddressInputTypeDef(BaseValidatorModel):
    SiteId: str
    AddressType: AddressTypeType
    Address: AddressTypeDef


class ComputeAttributesTypeDef(BaseValidatorModel):
    HostId: Optional[str] = None
    State: Optional[ComputeAssetStateType] = None
    InstanceFamilies: Optional[List[str]] = None
    InstanceTypeCapacities: Optional[List[AssetInstanceTypeCapacityTypeDef]] = None
    MaxVcpus: Optional[int] = None


class CatalogItemTypeDef(BaseValidatorModel):
    CatalogItemId: Optional[str] = None
    ItemStatus: Optional[CatalogItemStatusType] = None
    EC2Capacities: Optional[List[EC2CapacityTypeDef]] = None
    PowerKva: Optional[float] = None
    WeightLbs: Optional[int] = None
    SupportedUplinkGbps: Optional[List[int]] = None
    SupportedStorage: Optional[List[SupportedStorageEnumType]] = None


class CreateOrderInputTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    LineItems: Sequence[LineItemRequestTypeDef]
    PaymentOption: PaymentOptionType
    PaymentTerm: Optional[PaymentTermType] = None


class GetConnectionResponseTypeDef(BaseValidatorModel):
    ConnectionId: str
    ConnectionDetails: ConnectionDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSiteAddressOutputTypeDef(BaseValidatorModel):
    SiteId: str
    AddressType: AddressTypeType
    Address: AddressTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAssetInstancesOutputTypeDef(BaseValidatorModel):
    AssetInstances: List[AssetInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListBlockingInstancesForCapacityTaskOutputTypeDef(BaseValidatorModel):
    BlockingInstances: List[BlockingInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCapacityTasksOutputTypeDef(BaseValidatorModel):
    CapacityTasks: List[CapacityTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartConnectionResponseTypeDef(BaseValidatorModel):
    ConnectionId: str
    UnderlayIpAddress: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSiteAddressOutputTypeDef(BaseValidatorModel):
    AddressType: AddressTypeType
    Address: AddressTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOutpostOutputTypeDef(BaseValidatorModel):
    Outpost: OutpostTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetOutpostOutputTypeDef(BaseValidatorModel):
    Outpost: OutpostTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListOutpostsOutputTypeDef(BaseValidatorModel):
    Outposts: List[OutpostTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateOutpostOutputTypeDef(BaseValidatorModel):
    Outpost: OutpostTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSiteInputTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Notes: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    OperatingAddress: Optional[AddressTypeDef] = None
    ShippingAddress: Optional[AddressTypeDef] = None
    RackPhysicalProperties: Optional[RackPhysicalPropertiesTypeDef] = None


class SiteTypeDef(BaseValidatorModel):
    SiteId: Optional[str] = None
    AccountId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    SiteArn: Optional[str] = None
    Notes: Optional[str] = None
    OperatingAddressCountryCode: Optional[str] = None
    OperatingAddressStateOrRegion: Optional[str] = None
    OperatingAddressCity: Optional[str] = None
    RackPhysicalProperties: Optional[RackPhysicalPropertiesTypeDef] = None


class CapacityTaskFailureTypeDef(BaseValidatorModel):
    pass


class GetCapacityTaskOutputTypeDef(BaseValidatorModel):
    CapacityTaskId: str
    OutpostId: str
    OrderId: str
    RequestedInstancePools: List[InstanceTypeCapacityTypeDef]
    InstancesToExclude: InstancesToExcludeOutputTypeDef
    DryRun: bool
    CapacityTaskStatus: CapacityTaskStatusType
    Failed: CapacityTaskFailureTypeDef
    CreationDate: datetime
    CompletionDate: datetime
    LastModifiedDate: datetime
    TaskActionOnBlockingInstances: TaskActionOnBlockingInstancesType
    ResponseMetadata: ResponseMetadataTypeDef


class StartCapacityTaskOutputTypeDef(BaseValidatorModel):
    CapacityTaskId: str
    OutpostId: str
    OrderId: str
    RequestedInstancePools: List[InstanceTypeCapacityTypeDef]
    InstancesToExclude: InstancesToExcludeOutputTypeDef
    DryRun: bool
    CapacityTaskStatus: CapacityTaskStatusType
    Failed: CapacityTaskFailureTypeDef
    CreationDate: datetime
    CompletionDate: datetime
    LastModifiedDate: datetime
    TaskActionOnBlockingInstances: TaskActionOnBlockingInstancesType
    ResponseMetadata: ResponseMetadataTypeDef


class GetOutpostInstanceTypesInputPaginateTypeDef(BaseValidatorModel):
    OutpostId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetOutpostSupportedInstanceTypesInputPaginateTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    OrderId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssetInstancesInputPaginateTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    AssetIdFilter: Optional[Sequence[str]] = None
    InstanceTypeFilter: Optional[Sequence[str]] = None
    AccountIdFilter: Optional[Sequence[str]] = None
    AwsServiceFilter: Optional[Sequence[AWSServiceNameType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssetsInputPaginateTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    HostIdFilter: Optional[Sequence[str]] = None
    StatusFilter: Optional[Sequence[AssetStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBlockingInstancesForCapacityTaskInputPaginateTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    CapacityTaskId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCapacityTasksInputPaginateTypeDef(BaseValidatorModel):
    OutpostIdentifierFilter: Optional[str] = None
    CapacityTaskStatusFilter: Optional[Sequence[CapacityTaskStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCatalogItemsInputPaginateTypeDef(BaseValidatorModel):
    ItemClassFilter: Optional[Sequence[CatalogItemClassType]] = None
    SupportedStorageFilter: Optional[Sequence[SupportedStorageEnumType]] = None
    EC2FamilyFilter: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOrdersInputPaginateTypeDef(BaseValidatorModel):
    OutpostIdentifierFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOutpostsInputPaginateTypeDef(BaseValidatorModel):
    LifeCycleStatusFilter: Optional[Sequence[str]] = None
    AvailabilityZoneFilter: Optional[Sequence[str]] = None
    AvailabilityZoneIdFilter: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSitesInputPaginateTypeDef(BaseValidatorModel):
    OperatingAddressCountryCodeFilter: Optional[Sequence[str]] = None
    OperatingAddressStateOrRegionFilter: Optional[Sequence[str]] = None
    OperatingAddressCityFilter: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetOutpostInstanceTypesOutputTypeDef(BaseValidatorModel):
    InstanceTypes: List[InstanceTypeItemTypeDef]
    OutpostId: str
    OutpostArn: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetOutpostSupportedInstanceTypesOutputTypeDef(BaseValidatorModel):
    InstanceTypes: List[InstanceTypeItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LineItemTypeDef(BaseValidatorModel):
    CatalogItemId: Optional[str] = None
    LineItemId: Optional[str] = None
    Quantity: Optional[int] = None
    Status: Optional[LineItemStatusType] = None
    ShipmentInformation: Optional[ShipmentInformationTypeDef] = None
    AssetInformationList: Optional[List[LineItemAssetInformationTypeDef]] = None
    PreviousLineItemId: Optional[str] = None
    PreviousOrderId: Optional[str] = None


class ListOrdersOutputTypeDef(BaseValidatorModel):
    Orders: List[OrderSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AssetInfoTypeDef(BaseValidatorModel):
    AssetId: Optional[str] = None
    RackId: Optional[str] = None
    AssetType: Optional[Literal["COMPUTE"]] = None
    ComputeAttributes: Optional[ComputeAttributesTypeDef] = None
    AssetLocation: Optional[AssetLocationTypeDef] = None


class GetCatalogItemOutputTypeDef(BaseValidatorModel):
    CatalogItem: CatalogItemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListCatalogItemsOutputTypeDef(BaseValidatorModel):
    CatalogItems: List[CatalogItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateSiteOutputTypeDef(BaseValidatorModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSiteOutputTypeDef(BaseValidatorModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListSitesOutputTypeDef(BaseValidatorModel):
    Sites: List[SiteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateSiteOutputTypeDef(BaseValidatorModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSiteRackPhysicalPropertiesOutputTypeDef(BaseValidatorModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class InstancesToExcludeUnionTypeDef(BaseValidatorModel):
    pass


class StartCapacityTaskInputTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    InstancePools: Sequence[InstanceTypeCapacityTypeDef]
    OrderId: Optional[str] = None
    InstancesToExclude: Optional[InstancesToExcludeUnionTypeDef] = None
    DryRun: Optional[bool] = None
    TaskActionOnBlockingInstances: Optional[TaskActionOnBlockingInstancesType] = None


class OrderTypeDef(BaseValidatorModel):
    OutpostId: Optional[str] = None
    OrderId: Optional[str] = None
    Status: Optional[OrderStatusType] = None
    LineItems: Optional[List[LineItemTypeDef]] = None
    PaymentOption: Optional[PaymentOptionType] = None
    OrderSubmissionDate: Optional[datetime] = None
    OrderFulfilledDate: Optional[datetime] = None
    PaymentTerm: Optional[PaymentTermType] = None
    OrderType: Optional[OrderTypeType] = None


class ListAssetsOutputTypeDef(BaseValidatorModel):
    Assets: List[AssetInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateOrderOutputTypeDef(BaseValidatorModel):
    Order: OrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetOrderOutputTypeDef(BaseValidatorModel):
    Order: OrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


