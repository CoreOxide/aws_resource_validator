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
from aws_resource_validator.pydantic_models.outposts_constants import *

class AddressTypeDef(BaseModel):
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

class AssetLocationTypeDef(BaseModel):
    RackElevation: Optional[float] = None

class ComputeAttributesTypeDef(BaseModel):
    HostId: Optional[str] = None
    State: Optional[ComputeAssetStateType] = None
    InstanceFamilies: Optional[List[str]] = None

class CancelCapacityTaskInputRequestTypeDef(BaseModel):
    CapacityTaskId: str
    OutpostIdentifier: str

class CancelOrderInputRequestTypeDef(BaseModel):
    OrderId: str

class CapacityTaskFailureTypeDef(BaseModel):
    Reason: str
    Type: Optional[Literal["UNSUPPORTED_CAPACITY_CONFIGURATION"]] = None

class CapacityTaskSummaryTypeDef(BaseModel):
    CapacityTaskId: Optional[str] = None
    OutpostId: Optional[str] = None
    OrderId: Optional[str] = None
    CapacityTaskStatus: Optional[CapacityTaskStatusType] = None
    CreationDate: Optional[datetime] = None
    CompletionDate: Optional[datetime] = None
    LastModifiedDate: Optional[datetime] = None

class EC2CapacityTypeDef(BaseModel):
    Family: Optional[str] = None
    MaxSize: Optional[str] = None
    Quantity: Optional[str] = None

class ConnectionDetailsTypeDef(BaseModel):
    ClientPublicKey: Optional[str] = None
    ServerPublicKey: Optional[str] = None
    ServerEndpoint: Optional[str] = None
    ClientTunnelAddress: Optional[str] = None
    ServerTunnelAddress: Optional[str] = None
    AllowedIps: Optional[List[str]] = None

class LineItemRequestTypeDef(BaseModel):
    CatalogItemId: Optional[str] = None
    Quantity: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateOutpostInputRequestTypeDef(BaseModel):
    Name: str
    SiteId: str
    Description: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    SupportedHardwareType: Optional[SupportedHardwareTypeType] = None

class OutpostTypeDef(BaseModel):
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

class RackPhysicalPropertiesTypeDef(BaseModel):
    PowerDrawKva: Optional[PowerDrawKvaType] = None
    PowerPhase: Optional[PowerPhaseType] = None
    PowerConnector: Optional[PowerConnectorType] = None
    PowerFeedDrop: Optional[PowerFeedDropType] = None
    UplinkGbps: Optional[UplinkGbpsType] = None
    UplinkCount: Optional[UplinkCountType] = None
    FiberOpticCableType: Optional[FiberOpticCableTypeType] = None
    OpticalStandard: Optional[OpticalStandardType] = None
    MaximumSupportedWeightLbs: Optional[MaximumSupportedWeightLbsType] = None

class DeleteOutpostInputRequestTypeDef(BaseModel):
    OutpostId: str

class DeleteSiteInputRequestTypeDef(BaseModel):
    SiteId: str

class GetCapacityTaskInputRequestTypeDef(BaseModel):
    CapacityTaskId: str
    OutpostIdentifier: str

class InstanceTypeCapacityTypeDef(BaseModel):
    InstanceType: str
    Count: int

class GetCatalogItemInputRequestTypeDef(BaseModel):
    CatalogItemId: str

class GetConnectionRequestRequestTypeDef(BaseModel):
    ConnectionId: str

class GetOrderInputRequestTypeDef(BaseModel):
    OrderId: str

class GetOutpostInputRequestTypeDef(BaseModel):
    OutpostId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetOutpostInstanceTypesInputRequestTypeDef(BaseModel):
    OutpostId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class InstanceTypeItemTypeDef(BaseModel):
    InstanceType: Optional[str] = None

class GetOutpostSupportedInstanceTypesInputRequestTypeDef(BaseModel):
    OutpostIdentifier: str
    OrderId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetSiteAddressInputRequestTypeDef(BaseModel):
    SiteId: str
    AddressType: AddressTypeType

class GetSiteInputRequestTypeDef(BaseModel):
    SiteId: str

class LineItemAssetInformationTypeDef(BaseModel):
    AssetId: Optional[str] = None
    MacAddressList: Optional[List[str]] = None

class ShipmentInformationTypeDef(BaseModel):
    ShipmentTrackingNumber: Optional[str] = None
    ShipmentCarrier: Optional[ShipmentCarrierType] = None

class ListAssetsInputRequestTypeDef(BaseModel):
    OutpostIdentifier: str
    HostIdFilter: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StatusFilter: Optional[Sequence[AssetStateType]] = None

class ListCapacityTasksInputRequestTypeDef(BaseModel):
    OutpostIdentifierFilter: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    CapacityTaskStatusFilter: Optional[Sequence[CapacityTaskStatusType]] = None

class ListCatalogItemsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ItemClassFilter: Optional[Sequence[CatalogItemClassType]] = None
    SupportedStorageFilter: Optional[Sequence[SupportedStorageEnumType]] = None
    EC2FamilyFilter: Optional[Sequence[str]] = None

class ListOrdersInputRequestTypeDef(BaseModel):
    OutpostIdentifierFilter: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class OrderSummaryTypeDef(BaseModel):
    OutpostId: Optional[str] = None
    OrderId: Optional[str] = None
    OrderType: Optional[OrderTypeType] = None
    Status: Optional[OrderStatusType] = None
    LineItemCountsByStatus: Optional[Dict[LineItemStatusType, int]] = None
    OrderSubmissionDate: Optional[datetime] = None
    OrderFulfilledDate: Optional[datetime] = None

class ListOutpostsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LifeCycleStatusFilter: Optional[Sequence[str]] = None
    AvailabilityZoneFilter: Optional[Sequence[str]] = None
    AvailabilityZoneIdFilter: Optional[Sequence[str]] = None

class ListSitesInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    OperatingAddressCountryCodeFilter: Optional[Sequence[str]] = None
    OperatingAddressStateOrRegionFilter: Optional[Sequence[str]] = None
    OperatingAddressCityFilter: Optional[Sequence[str]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class StartConnectionRequestRequestTypeDef(BaseModel):
    AssetId: str
    ClientPublicKey: str
    NetworkInterfaceDeviceIndex: int
    DeviceSerialNumber: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateOutpostInputRequestTypeDef(BaseModel):
    OutpostId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    SupportedHardwareType: Optional[SupportedHardwareTypeType] = None

class UpdateSiteInputRequestTypeDef(BaseModel):
    SiteId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Notes: Optional[str] = None

class UpdateSiteRackPhysicalPropertiesInputRequestTypeDef(BaseModel):
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

class UpdateSiteAddressInputRequestTypeDef(BaseModel):
    SiteId: str
    AddressType: AddressTypeType
    Address: AddressTypeDef

class AssetInfoTypeDef(BaseModel):
    AssetId: Optional[str] = None
    RackId: Optional[str] = None
    AssetType: Optional[Literal["COMPUTE"]] = None
    ComputeAttributes: Optional[ComputeAttributesTypeDef] = None
    AssetLocation: Optional[AssetLocationTypeDef] = None

class CatalogItemTypeDef(BaseModel):
    CatalogItemId: Optional[str] = None
    ItemStatus: Optional[CatalogItemStatusType] = None
    EC2Capacities: Optional[List[EC2CapacityTypeDef]] = None
    PowerKva: Optional[float] = None
    WeightLbs: Optional[int] = None
    SupportedUplinkGbps: Optional[List[int]] = None
    SupportedStorage: Optional[List[SupportedStorageEnumType]] = None

class CreateOrderInputRequestTypeDef(BaseModel):
    OutpostIdentifier: str
    LineItems: Sequence[LineItemRequestTypeDef]
    PaymentOption: PaymentOptionType
    PaymentTerm: Optional[PaymentTermType] = None

class GetConnectionResponseTypeDef(BaseModel):
    ConnectionId: str
    ConnectionDetails: ConnectionDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSiteAddressOutputTypeDef(BaseModel):
    SiteId: str
    AddressType: AddressTypeType
    Address: AddressTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCapacityTasksOutputTypeDef(BaseModel):
    CapacityTasks: List[CapacityTaskSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartConnectionResponseTypeDef(BaseModel):
    ConnectionId: str
    UnderlayIpAddress: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSiteAddressOutputTypeDef(BaseModel):
    AddressType: AddressTypeType
    Address: AddressTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOutpostOutputTypeDef(BaseModel):
    Outpost: OutpostTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOutpostOutputTypeDef(BaseModel):
    Outpost: OutpostTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOutpostsOutputTypeDef(BaseModel):
    Outposts: List[OutpostTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOutpostOutputTypeDef(BaseModel):
    Outpost: OutpostTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSiteInputRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    Notes: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    OperatingAddress: Optional[AddressTypeDef] = None
    ShippingAddress: Optional[AddressTypeDef] = None
    RackPhysicalProperties: Optional[RackPhysicalPropertiesTypeDef] = None

class SiteTypeDef(BaseModel):
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

class GetCapacityTaskOutputTypeDef(BaseModel):
    CapacityTaskId: str
    OutpostId: str
    OrderId: str
    RequestedInstancePools: List[InstanceTypeCapacityTypeDef]
    DryRun: bool
    CapacityTaskStatus: CapacityTaskStatusType
    Failed: CapacityTaskFailureTypeDef
    CreationDate: datetime
    CompletionDate: datetime
    LastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartCapacityTaskInputRequestTypeDef(BaseModel):
    OutpostIdentifier: str
    OrderId: str
    InstancePools: Sequence[InstanceTypeCapacityTypeDef]
    DryRun: Optional[bool] = None

class StartCapacityTaskOutputTypeDef(BaseModel):
    CapacityTaskId: str
    OutpostId: str
    OrderId: str
    RequestedInstancePools: List[InstanceTypeCapacityTypeDef]
    DryRun: bool
    CapacityTaskStatus: CapacityTaskStatusType
    Failed: CapacityTaskFailureTypeDef
    CreationDate: datetime
    CompletionDate: datetime
    LastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef(BaseModel):
    OutpostId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetOutpostSupportedInstanceTypesInputGetOutpostSupportedInstanceTypesPaginateTypeDef(BaseModel):
    OutpostIdentifier: str
    OrderId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetsInputListAssetsPaginateTypeDef(BaseModel):
    OutpostIdentifier: str
    HostIdFilter: Optional[Sequence[str]] = None
    StatusFilter: Optional[Sequence[AssetStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCapacityTasksInputListCapacityTasksPaginateTypeDef(BaseModel):
    OutpostIdentifierFilter: Optional[str] = None
    CapacityTaskStatusFilter: Optional[Sequence[CapacityTaskStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCatalogItemsInputListCatalogItemsPaginateTypeDef(BaseModel):
    ItemClassFilter: Optional[Sequence[CatalogItemClassType]] = None
    SupportedStorageFilter: Optional[Sequence[SupportedStorageEnumType]] = None
    EC2FamilyFilter: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrdersInputListOrdersPaginateTypeDef(BaseModel):
    OutpostIdentifierFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOutpostsInputListOutpostsPaginateTypeDef(BaseModel):
    LifeCycleStatusFilter: Optional[Sequence[str]] = None
    AvailabilityZoneFilter: Optional[Sequence[str]] = None
    AvailabilityZoneIdFilter: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSitesInputListSitesPaginateTypeDef(BaseModel):
    OperatingAddressCountryCodeFilter: Optional[Sequence[str]] = None
    OperatingAddressStateOrRegionFilter: Optional[Sequence[str]] = None
    OperatingAddressCityFilter: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetOutpostInstanceTypesOutputTypeDef(BaseModel):
    InstanceTypes: List[InstanceTypeItemTypeDef]
    NextToken: str
    OutpostId: str
    OutpostArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOutpostSupportedInstanceTypesOutputTypeDef(BaseModel):
    InstanceTypes: List[InstanceTypeItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LineItemTypeDef(BaseModel):
    CatalogItemId: Optional[str] = None
    LineItemId: Optional[str] = None
    Quantity: Optional[int] = None
    Status: Optional[LineItemStatusType] = None
    ShipmentInformation: Optional[ShipmentInformationTypeDef] = None
    AssetInformationList: Optional[List[LineItemAssetInformationTypeDef]] = None
    PreviousLineItemId: Optional[str] = None
    PreviousOrderId: Optional[str] = None

class ListOrdersOutputTypeDef(BaseModel):
    Orders: List[OrderSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetsOutputTypeDef(BaseModel):
    Assets: List[AssetInfoTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCatalogItemOutputTypeDef(BaseModel):
    CatalogItem: CatalogItemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCatalogItemsOutputTypeDef(BaseModel):
    CatalogItems: List[CatalogItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSiteOutputTypeDef(BaseModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSiteOutputTypeDef(BaseModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSitesOutputTypeDef(BaseModel):
    Sites: List[SiteTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSiteOutputTypeDef(BaseModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSiteRackPhysicalPropertiesOutputTypeDef(BaseModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OrderTypeDef(BaseModel):
    OutpostId: Optional[str] = None
    OrderId: Optional[str] = None
    Status: Optional[OrderStatusType] = None
    LineItems: Optional[List[LineItemTypeDef]] = None
    PaymentOption: Optional[PaymentOptionType] = None
    OrderSubmissionDate: Optional[datetime] = None
    OrderFulfilledDate: Optional[datetime] = None
    PaymentTerm: Optional[PaymentTermType] = None
    OrderType: Optional[OrderTypeType] = None

class CreateOrderOutputTypeDef(BaseModel):
    Order: OrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrderOutputTypeDef(BaseModel):
    Order: OrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

