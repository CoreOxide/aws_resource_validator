from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.outposts.outposts_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Address(BaseValidatorModel):
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


class AssetLocation(BaseValidatorModel):
    RackElevation: Optional[float] = None


class AssetInstanceTypeCapacity(BaseValidatorModel):
    InstanceType: str
    Count: int


class AssetInstance(BaseValidatorModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    AssetId: Optional[str] = None
    AccountId: Optional[str] = None
    AwsServiceName: Optional[AWSServiceNameType] = None


class BlockingInstance(BaseValidatorModel):
    InstanceId: Optional[str] = None
    AccountId: Optional[str] = None
    AwsServiceName: Optional[AWSServiceNameType] = None


class CancelCapacityTaskInput(BaseValidatorModel):
    CapacityTaskId: str
    OutpostIdentifier: str


class CancelOrderInput(BaseValidatorModel):
    OrderId: str


class CapacityTaskFailure(BaseValidatorModel):
    Reason: str
    Type: Optional[CapacityTaskFailureTypeType] = None


class CapacityTaskSummary(BaseValidatorModel):
    CapacityTaskId: Optional[str] = None
    OutpostId: Optional[str] = None
    OrderId: Optional[str] = None
    CapacityTaskStatus: Optional[CapacityTaskStatusType] = None
    CreationDate: Optional[datetime] = None
    CompletionDate: Optional[datetime] = None
    LastModifiedDate: Optional[datetime] = None


class EC2Capacity(BaseValidatorModel):
    Family: Optional[str] = None
    MaxSize: Optional[str] = None
    Quantity: Optional[str] = None


class ConnectionDetails(BaseValidatorModel):
    ClientPublicKey: Optional[str] = None
    ServerPublicKey: Optional[str] = None
    ServerEndpoint: Optional[str] = None
    ClientTunnelAddress: Optional[str] = None
    ServerTunnelAddress: Optional[str] = None
    AllowedIps: Optional[List[str]] = None


class LineItemRequest(BaseValidatorModel):
    CatalogItemId: Optional[str] = None
    Quantity: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateOutpostInput(BaseValidatorModel):
    Name: str
    SiteId: str
    Description: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    SupportedHardwareType: Optional[SupportedHardwareTypeType] = None


class Outpost(BaseValidatorModel):
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


class RackPhysicalProperties(BaseValidatorModel):
    PowerDrawKva: Optional[PowerDrawKvaType] = None
    PowerPhase: Optional[PowerPhaseType] = None
    PowerConnector: Optional[PowerConnectorType] = None
    PowerFeedDrop: Optional[PowerFeedDropType] = None
    UplinkGbps: Optional[UplinkGbpsType] = None
    UplinkCount: Optional[UplinkCountType] = None
    FiberOpticCableType: Optional[FiberOpticCableTypeType] = None
    OpticalStandard: Optional[OpticalStandardType] = None
    MaximumSupportedWeightLbs: Optional[MaximumSupportedWeightLbsType] = None


class DeleteOutpostInput(BaseValidatorModel):
    OutpostId: str


class DeleteSiteInput(BaseValidatorModel):
    SiteId: str


class GetCapacityTaskInput(BaseValidatorModel):
    CapacityTaskId: str
    OutpostIdentifier: str


class InstanceTypeCapacity(BaseValidatorModel):
    InstanceType: str
    Count: int


class InstancesToExcludeOutput(BaseValidatorModel):
    Instances: Optional[List[str]] = None
    AccountIds: Optional[List[str]] = None
    Services: Optional[List[AWSServiceNameType]] = None


class GetCatalogItemInput(BaseValidatorModel):
    CatalogItemId: str


class GetConnectionRequest(BaseValidatorModel):
    ConnectionId: str


class GetOrderInput(BaseValidatorModel):
    OrderId: str


class GetOutpostInput(BaseValidatorModel):
    OutpostId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetOutpostInstanceTypesInput(BaseValidatorModel):
    OutpostId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class InstanceTypeItem(BaseValidatorModel):
    InstanceType: Optional[str] = None
    VCPUs: Optional[int] = None


class GetOutpostSupportedInstanceTypesInput(BaseValidatorModel):
    OutpostIdentifier: str
    OrderId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetSiteAddressInput(BaseValidatorModel):
    SiteId: str
    AddressType: AddressTypeType


class GetSiteInput(BaseValidatorModel):
    SiteId: str


class InstancesToExclude(BaseValidatorModel):
    Instances: Optional[List[str]] = None
    AccountIds: Optional[List[str]] = None
    Services: Optional[List[AWSServiceNameType]] = None


class LineItemAssetInformation(BaseValidatorModel):
    AssetId: Optional[str] = None
    MacAddressList: Optional[List[str]] = None


class ShipmentInformation(BaseValidatorModel):
    ShipmentTrackingNumber: Optional[str] = None
    ShipmentCarrier: Optional[ShipmentCarrierType] = None


class ListAssetInstancesInput(BaseValidatorModel):
    OutpostIdentifier: str
    AssetIdFilter: Optional[List[str]] = None
    InstanceTypeFilter: Optional[List[str]] = None
    AccountIdFilter: Optional[List[str]] = None
    AwsServiceFilter: Optional[List[AWSServiceNameType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAssetsInput(BaseValidatorModel):
    OutpostIdentifier: str
    HostIdFilter: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StatusFilter: Optional[List[AssetStateType]] = None


class ListBlockingInstancesForCapacityTaskInput(BaseValidatorModel):
    OutpostIdentifier: str
    CapacityTaskId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCapacityTasksInput(BaseValidatorModel):
    OutpostIdentifierFilter: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    CapacityTaskStatusFilter: Optional[List[CapacityTaskStatusType]] = None


class ListCatalogItemsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ItemClassFilter: Optional[List[CatalogItemClassType]] = None
    SupportedStorageFilter: Optional[List[SupportedStorageEnumType]] = None
    EC2FamilyFilter: Optional[List[str]] = None


class ListOrdersInput(BaseValidatorModel):
    OutpostIdentifierFilter: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OrderSummary(BaseValidatorModel):
    OutpostId: Optional[str] = None
    OrderId: Optional[str] = None
    OrderType: Optional[OrderTypeType] = None
    Status: Optional[OrderStatusType] = None
    LineItemCountsByStatus: Optional[Dict[LineItemStatusType, int]] = None
    OrderSubmissionDate: Optional[datetime] = None
    OrderFulfilledDate: Optional[datetime] = None


class ListOutpostsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    LifeCycleStatusFilter: Optional[List[str]] = None
    AvailabilityZoneFilter: Optional[List[str]] = None
    AvailabilityZoneIdFilter: Optional[List[str]] = None


class ListSitesInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    OperatingAddressCountryCodeFilter: Optional[List[str]] = None
    OperatingAddressStateOrRegionFilter: Optional[List[str]] = None
    OperatingAddressCityFilter: Optional[List[str]] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class StartConnectionRequest(BaseValidatorModel):
    AssetId: str
    ClientPublicKey: str
    NetworkInterfaceDeviceIndex: int
    DeviceSerialNumber: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateOutpostInput(BaseValidatorModel):
    OutpostId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    SupportedHardwareType: Optional[SupportedHardwareTypeType] = None


class UpdateSiteInput(BaseValidatorModel):
    SiteId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Notes: Optional[str] = None


class UpdateSiteRackPhysicalPropertiesInput(BaseValidatorModel):
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


class UpdateSiteAddressInput(BaseValidatorModel):
    SiteId: str
    AddressType: AddressTypeType
    Address: Address


class ComputeAttributes(BaseValidatorModel):
    HostId: Optional[str] = None
    State: Optional[ComputeAssetStateType] = None
    InstanceFamilies: Optional[List[str]] = None
    InstanceTypeCapacities: Optional[List[AssetInstanceTypeCapacity]] = None
    MaxVcpus: Optional[int] = None


class CatalogItem(BaseValidatorModel):
    CatalogItemId: Optional[str] = None
    ItemStatus: Optional[CatalogItemStatusType] = None
    EC2Capacities: Optional[List[EC2Capacity]] = None
    PowerKva: Optional[float] = None
    WeightLbs: Optional[int] = None
    SupportedUplinkGbps: Optional[List[int]] = None
    SupportedStorage: Optional[List[SupportedStorageEnumType]] = None


class CreateOrderInput(BaseValidatorModel):
    OutpostIdentifier: str
    LineItems: List[LineItemRequest]
    PaymentOption: PaymentOptionType
    PaymentTerm: Optional[PaymentTermType] = None


class GetConnectionResponse(BaseValidatorModel):
    ConnectionId: str
    ConnectionDetails: ConnectionDetails
    ResponseMetadata: ResponseMetadata


class GetSiteAddressOutput(BaseValidatorModel):
    SiteId: str
    AddressType: AddressTypeType
    Address: Address
    ResponseMetadata: ResponseMetadata


class ListAssetInstancesOutput(BaseValidatorModel):
    AssetInstances: List[AssetInstance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListBlockingInstancesForCapacityTaskOutput(BaseValidatorModel):
    BlockingInstances: List[BlockingInstance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCapacityTasksOutput(BaseValidatorModel):
    CapacityTasks: List[CapacityTaskSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartConnectionResponse(BaseValidatorModel):
    ConnectionId: str
    UnderlayIpAddress: str
    ResponseMetadata: ResponseMetadata


class UpdateSiteAddressOutput(BaseValidatorModel):
    AddressType: AddressTypeType
    Address: Address
    ResponseMetadata: ResponseMetadata


class CreateOutpostOutput(BaseValidatorModel):
    Outpost: Outpost
    ResponseMetadata: ResponseMetadata


class GetOutpostOutput(BaseValidatorModel):
    Outpost: Outpost
    ResponseMetadata: ResponseMetadata


class ListOutpostsOutput(BaseValidatorModel):
    Outposts: List[Outpost]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateOutpostOutput(BaseValidatorModel):
    Outpost: Outpost
    ResponseMetadata: ResponseMetadata


class CreateSiteInput(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Notes: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    OperatingAddress: Optional[Address] = None
    ShippingAddress: Optional[Address] = None
    RackPhysicalProperties: Optional[RackPhysicalProperties] = None


class Site(BaseValidatorModel):
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
    RackPhysicalProperties: Optional[RackPhysicalProperties] = None


class GetCapacityTaskOutput(BaseValidatorModel):
    CapacityTaskId: str
    OutpostId: str
    OrderId: str
    RequestedInstancePools: List[InstanceTypeCapacity]
    InstancesToExclude: InstancesToExcludeOutput
    DryRun: bool
    CapacityTaskStatus: CapacityTaskStatusType
    Failed: CapacityTaskFailure
    CreationDate: datetime
    CompletionDate: datetime
    LastModifiedDate: datetime
    TaskActionOnBlockingInstances: TaskActionOnBlockingInstancesType
    ResponseMetadata: ResponseMetadata


class StartCapacityTaskOutput(BaseValidatorModel):
    CapacityTaskId: str
    OutpostId: str
    OrderId: str
    RequestedInstancePools: List[InstanceTypeCapacity]
    InstancesToExclude: InstancesToExcludeOutput
    DryRun: bool
    CapacityTaskStatus: CapacityTaskStatusType
    Failed: CapacityTaskFailure
    CreationDate: datetime
    CompletionDate: datetime
    LastModifiedDate: datetime
    TaskActionOnBlockingInstances: TaskActionOnBlockingInstancesType
    ResponseMetadata: ResponseMetadata


class GetOutpostInstanceTypesInputPaginate(BaseValidatorModel):
    OutpostId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetOutpostSupportedInstanceTypesInputPaginate(BaseValidatorModel):
    OutpostIdentifier: str
    OrderId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssetInstancesInputPaginate(BaseValidatorModel):
    OutpostIdentifier: str
    AssetIdFilter: Optional[List[str]] = None
    InstanceTypeFilter: Optional[List[str]] = None
    AccountIdFilter: Optional[List[str]] = None
    AwsServiceFilter: Optional[List[AWSServiceNameType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssetsInputPaginate(BaseValidatorModel):
    OutpostIdentifier: str
    HostIdFilter: Optional[List[str]] = None
    StatusFilter: Optional[List[AssetStateType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBlockingInstancesForCapacityTaskInputPaginate(BaseValidatorModel):
    OutpostIdentifier: str
    CapacityTaskId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCapacityTasksInputPaginate(BaseValidatorModel):
    OutpostIdentifierFilter: Optional[str] = None
    CapacityTaskStatusFilter: Optional[List[CapacityTaskStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCatalogItemsInputPaginate(BaseValidatorModel):
    ItemClassFilter: Optional[List[CatalogItemClassType]] = None
    SupportedStorageFilter: Optional[List[SupportedStorageEnumType]] = None
    EC2FamilyFilter: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOrdersInputPaginate(BaseValidatorModel):
    OutpostIdentifierFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOutpostsInputPaginate(BaseValidatorModel):
    LifeCycleStatusFilter: Optional[List[str]] = None
    AvailabilityZoneFilter: Optional[List[str]] = None
    AvailabilityZoneIdFilter: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSitesInputPaginate(BaseValidatorModel):
    OperatingAddressCountryCodeFilter: Optional[List[str]] = None
    OperatingAddressStateOrRegionFilter: Optional[List[str]] = None
    OperatingAddressCityFilter: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetOutpostInstanceTypesOutput(BaseValidatorModel):
    InstanceTypes: List[InstanceTypeItem]
    OutpostId: str
    OutpostArn: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetOutpostSupportedInstanceTypesOutput(BaseValidatorModel):
    InstanceTypes: List[InstanceTypeItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

InstancesToExcludeUnion = Union[InstancesToExclude, InstancesToExcludeOutput]


class LineItem(BaseValidatorModel):
    CatalogItemId: Optional[str] = None
    LineItemId: Optional[str] = None
    Quantity: Optional[int] = None
    Status: Optional[LineItemStatusType] = None
    ShipmentInformation: Optional[ShipmentInformation] = None
    AssetInformationList: Optional[List[LineItemAssetInformation]] = None
    PreviousLineItemId: Optional[str] = None
    PreviousOrderId: Optional[str] = None


class ListOrdersOutput(BaseValidatorModel):
    Orders: List[OrderSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AssetInfo(BaseValidatorModel):
    AssetId: Optional[str] = None
    RackId: Optional[str] = None
    AssetType: Optional[Literal['COMPUTE']] = None
    ComputeAttributes: Optional[ComputeAttributes] = None
    AssetLocation: Optional[AssetLocation] = None


class GetCatalogItemOutput(BaseValidatorModel):
    CatalogItem: CatalogItem
    ResponseMetadata: ResponseMetadata


class ListCatalogItemsOutput(BaseValidatorModel):
    CatalogItems: List[CatalogItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateSiteOutput(BaseValidatorModel):
    Site: Site
    ResponseMetadata: ResponseMetadata


class GetSiteOutput(BaseValidatorModel):
    Site: Site
    ResponseMetadata: ResponseMetadata


class ListSitesOutput(BaseValidatorModel):
    Sites: List[Site]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateSiteOutput(BaseValidatorModel):
    Site: Site
    ResponseMetadata: ResponseMetadata


class UpdateSiteRackPhysicalPropertiesOutput(BaseValidatorModel):
    Site: Site
    ResponseMetadata: ResponseMetadata


class StartCapacityTaskInput(BaseValidatorModel):
    OutpostIdentifier: str
    InstancePools: List[InstanceTypeCapacity]
    OrderId: Optional[str] = None
    InstancesToExclude: Optional[InstancesToExcludeUnion] = None
    DryRun: Optional[bool] = None
    TaskActionOnBlockingInstances: Optional[TaskActionOnBlockingInstancesType] = None


class Order(BaseValidatorModel):
    OutpostId: Optional[str] = None
    OrderId: Optional[str] = None
    Status: Optional[OrderStatusType] = None
    LineItems: Optional[List[LineItem]] = None
    PaymentOption: Optional[PaymentOptionType] = None
    OrderSubmissionDate: Optional[datetime] = None
    OrderFulfilledDate: Optional[datetime] = None
    PaymentTerm: Optional[PaymentTermType] = None
    OrderType: Optional[OrderTypeType] = None


class ListAssetsOutput(BaseValidatorModel):
    Assets: List[AssetInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateOrderOutput(BaseValidatorModel):
    Order: Order
    ResponseMetadata: ResponseMetadata


class GetOrderOutput(BaseValidatorModel):
    Order: Order
    ResponseMetadata: ResponseMetadata