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

class ComputeAttributesTypeDef(BaseValidatorModel):
    HostId: Optional[str] = None
    State: Optional[ComputeAssetStateType] = None
    InstanceFamilies: Optional[List[str]] = None

class CancelCapacityTaskInputRequestTypeDef(BaseValidatorModel):
    CapacityTaskId: str
    OutpostIdentifier: str

class CancelOrderInputRequestTypeDef(BaseValidatorModel):
    OrderId: str

class CapacityTaskFailureTypeDef(BaseValidatorModel):
    Reason: str
    Type: Optional[Literal["UNSUPPORTED_CAPACITY_CONFIGURATION"]] = None

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

class CreateOutpostInputRequestTypeDef(BaseValidatorModel):
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

class DeleteOutpostInputRequestTypeDef(BaseValidatorModel):
    OutpostId: str

class DeleteSiteInputRequestTypeDef(BaseValidatorModel):
    SiteId: str

class GetCapacityTaskInputRequestTypeDef(BaseValidatorModel):
    CapacityTaskId: str
    OutpostIdentifier: str

class InstanceTypeCapacityTypeDef(BaseValidatorModel):
    InstanceType: str
    Count: int

class GetCatalogItemInputRequestTypeDef(BaseValidatorModel):
    CatalogItemId: str

class GetConnectionRequestRequestTypeDef(BaseValidatorModel):
    ConnectionId: str

class GetOrderInputRequestTypeDef(BaseValidatorModel):
    OrderId: str

class GetOutpostInputRequestTypeDef(BaseValidatorModel):
    OutpostId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetOutpostInstanceTypesInputRequestTypeDef(BaseValidatorModel):
    OutpostId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class InstanceTypeItemTypeDef(BaseValidatorModel):
    InstanceType: Optional[str] = None

class GetOutpostSupportedInstanceTypesInputRequestTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    OrderId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetSiteAddressInputRequestTypeDef(BaseValidatorModel):
    SiteId: str
    AddressType: AddressTypeType

class GetSiteInputRequestTypeDef(BaseValidatorModel):
    SiteId: str

class LineItemAssetInformationTypeDef(BaseValidatorModel):
    AssetId: Optional[str] = None
    MacAddressList: Optional[List[str]] = None

class ShipmentInformationTypeDef(BaseValidatorModel):
    ShipmentTrackingNumber: Optional[str] = None
    ShipmentCarrier: Optional[ShipmentCarrierType] = None

class ListAssetsInputRequestTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    HostIdFilter: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StatusFilter: Optional[Sequence[AssetStateType]] = None

class ListCapacityTasksInputRequestTypeDef(BaseValidatorModel):
    OutpostIdentifierFilter: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    CapacityTaskStatusFilter: Optional[Sequence[CapacityTaskStatusType]] = None

class ListCatalogItemsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ItemClassFilter: Optional[Sequence[CatalogItemClassType]] = None
    SupportedStorageFilter: Optional[Sequence[SupportedStorageEnumType]] = None
    EC2FamilyFilter: Optional[Sequence[str]] = None

class ListOrdersInputRequestTypeDef(BaseValidatorModel):
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

class ListOutpostsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LifeCycleStatusFilter: Optional[Sequence[str]] = None
    AvailabilityZoneFilter: Optional[Sequence[str]] = None
    AvailabilityZoneIdFilter: Optional[Sequence[str]] = None

class ListSitesInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    OperatingAddressCountryCodeFilter: Optional[Sequence[str]] = None
    OperatingAddressStateOrRegionFilter: Optional[Sequence[str]] = None
    OperatingAddressCityFilter: Optional[Sequence[str]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class StartConnectionRequestRequestTypeDef(BaseValidatorModel):
    AssetId: str
    ClientPublicKey: str
    NetworkInterfaceDeviceIndex: int
    DeviceSerialNumber: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateOutpostInputRequestTypeDef(BaseValidatorModel):
    OutpostId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    SupportedHardwareType: Optional[SupportedHardwareTypeType] = None

class UpdateSiteInputRequestTypeDef(BaseValidatorModel):
    SiteId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Notes: Optional[str] = None

class UpdateSiteRackPhysicalPropertiesInputRequestTypeDef(BaseValidatorModel):
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

class UpdateSiteAddressInputRequestTypeDef(BaseValidatorModel):
    SiteId: str
    AddressType: AddressTypeType
    Address: AddressTypeDef

class AssetInfoTypeDef(BaseValidatorModel):
    AssetId: Optional[str] = None
    RackId: Optional[str] = None
    AssetType: Optional[Literal["COMPUTE"]] = None
    ComputeAttributes: Optional[ComputeAttributesTypeDef] = None
    AssetLocation: Optional[AssetLocationTypeDef] = None

class CatalogItemTypeDef(BaseValidatorModel):
    CatalogItemId: Optional[str] = None
    ItemStatus: Optional[CatalogItemStatusType] = None
    EC2Capacities: Optional[List[EC2CapacityTypeDef]] = None
    PowerKva: Optional[float] = None
    WeightLbs: Optional[int] = None
    SupportedUplinkGbps: Optional[List[int]] = None
    SupportedStorage: Optional[List[SupportedStorageEnumType]] = None

class CreateOrderInputRequestTypeDef(BaseValidatorModel):
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

class ListCapacityTasksOutputTypeDef(BaseValidatorModel):
    CapacityTasks: List[CapacityTaskSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOutpostOutputTypeDef(BaseValidatorModel):
    Outpost: OutpostTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSiteInputRequestTypeDef(BaseValidatorModel):
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

class GetCapacityTaskOutputTypeDef(BaseValidatorModel):
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

class StartCapacityTaskInputRequestTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    OrderId: str
    InstancePools: Sequence[InstanceTypeCapacityTypeDef]
    DryRun: Optional[bool] = None

class StartCapacityTaskOutputTypeDef(BaseValidatorModel):
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

class GetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef(BaseValidatorModel):
    OutpostId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetOutpostSupportedInstanceTypesInputGetOutpostSupportedInstanceTypesPaginateTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    OrderId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssetsInputListAssetsPaginateTypeDef(BaseValidatorModel):
    OutpostIdentifier: str
    HostIdFilter: Optional[Sequence[str]] = None
    StatusFilter: Optional[Sequence[AssetStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCapacityTasksInputListCapacityTasksPaginateTypeDef(BaseValidatorModel):
    OutpostIdentifierFilter: Optional[str] = None
    CapacityTaskStatusFilter: Optional[Sequence[CapacityTaskStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCatalogItemsInputListCatalogItemsPaginateTypeDef(BaseValidatorModel):
    ItemClassFilter: Optional[Sequence[CatalogItemClassType]] = None
    SupportedStorageFilter: Optional[Sequence[SupportedStorageEnumType]] = None
    EC2FamilyFilter: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrdersInputListOrdersPaginateTypeDef(BaseValidatorModel):
    OutpostIdentifierFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOutpostsInputListOutpostsPaginateTypeDef(BaseValidatorModel):
    LifeCycleStatusFilter: Optional[Sequence[str]] = None
    AvailabilityZoneFilter: Optional[Sequence[str]] = None
    AvailabilityZoneIdFilter: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSitesInputListSitesPaginateTypeDef(BaseValidatorModel):
    OperatingAddressCountryCodeFilter: Optional[Sequence[str]] = None
    OperatingAddressStateOrRegionFilter: Optional[Sequence[str]] = None
    OperatingAddressCityFilter: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetOutpostInstanceTypesOutputTypeDef(BaseValidatorModel):
    InstanceTypes: List[InstanceTypeItemTypeDef]
    NextToken: str
    OutpostId: str
    OutpostArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOutpostSupportedInstanceTypesOutputTypeDef(BaseValidatorModel):
    InstanceTypes: List[InstanceTypeItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetsOutputTypeDef(BaseValidatorModel):
    Assets: List[AssetInfoTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCatalogItemOutputTypeDef(BaseValidatorModel):
    CatalogItem: CatalogItemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCatalogItemsOutputTypeDef(BaseValidatorModel):
    CatalogItems: List[CatalogItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSiteOutputTypeDef(BaseValidatorModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSiteOutputTypeDef(BaseValidatorModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSitesOutputTypeDef(BaseValidatorModel):
    Sites: List[SiteTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSiteOutputTypeDef(BaseValidatorModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSiteRackPhysicalPropertiesOutputTypeDef(BaseValidatorModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

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

class CreateOrderOutputTypeDef(BaseValidatorModel):
    Order: OrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrderOutputTypeDef(BaseValidatorModel):
    Order: OrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

