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
from aws_resource_validator.pydantic_models.privatenetworks_constants import *

class AcknowledgeOrderReceiptRequestRequestTypeDef(BaseModel):
    orderArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ActivateDeviceIdentifierRequestRequestTypeDef(BaseModel):
    deviceIdentifierArn: str
    clientToken: Optional[str] = None

class DeviceIdentifierTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    deviceIdentifierArn: Optional[str] = None
    iccid: Optional[str] = None
    imsi: Optional[str] = None
    networkArn: Optional[str] = None
    orderArn: Optional[str] = None
    status: Optional[DeviceIdentifierStatusType] = None
    trafficGroupArn: Optional[str] = None
    vendor: Optional[str] = None

class AddressTypeDef(BaseModel):
    city: str
    country: str
    name: str
    postalCode: str
    stateOrProvince: str
    street1: str
    company: Optional[str] = None
    emailAddress: Optional[str] = None
    phoneNumber: Optional[str] = None
    street2: Optional[str] = None
    street3: Optional[str] = None

class CommitmentConfigurationTypeDef(BaseModel):
    automaticRenewal: bool
    commitmentLength: CommitmentLengthType

class PositionTypeDef(BaseModel):
    elevation: Optional[float] = None
    elevationReference: Optional[ElevationReferenceType] = None
    elevationUnit: Optional[Literal["FEET"]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class CreateNetworkRequestRequestTypeDef(BaseModel):
    networkName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class NetworkTypeDef(BaseModel):
    networkArn: str
    networkName: str
    status: NetworkStatusType
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    statusReason: Optional[str] = None

class DeactivateDeviceIdentifierRequestRequestTypeDef(BaseModel):
    deviceIdentifierArn: str
    clientToken: Optional[str] = None

class DeleteNetworkRequestRequestTypeDef(BaseModel):
    networkArn: str
    clientToken: Optional[str] = None

class DeleteNetworkSiteRequestRequestTypeDef(BaseModel):
    networkSiteArn: str
    clientToken: Optional[str] = None

class GetDeviceIdentifierRequestRequestTypeDef(BaseModel):
    deviceIdentifierArn: str

class GetNetworkRequestRequestTypeDef(BaseModel):
    networkArn: str

class GetNetworkResourceRequestRequestTypeDef(BaseModel):
    networkResourceArn: str

class GetNetworkSiteRequestRequestTypeDef(BaseModel):
    networkSiteArn: str

class GetOrderRequestRequestTypeDef(BaseModel):
    orderArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDeviceIdentifiersRequestRequestTypeDef(BaseModel):
    networkArn: str
    filters: Optional[Mapping[DeviceIdentifierFilterKeysType, Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None

class ListNetworkResourcesRequestRequestTypeDef(BaseModel):
    networkArn: str
    filters: Optional[Mapping[NetworkResourceFilterKeysType, Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None

class ListNetworkSitesRequestRequestTypeDef(BaseModel):
    networkArn: str
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None

class ListNetworksRequestRequestTypeDef(BaseModel):
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None

class ListOrdersRequestRequestTypeDef(BaseModel):
    networkArn: str
    filters: Optional[Mapping[OrderFilterKeysType, Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class NameValuePairTypeDef(BaseModel):
    name: str
    value: Optional[str] = None

class TrackingInformationTypeDef(BaseModel):
    trackingNumber: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateNetworkSiteRequestRequestTypeDef(BaseModel):
    networkSiteArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PingResponseTypeDef(BaseModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class ActivateDeviceIdentifierResponseTypeDef(BaseModel):
    deviceIdentifier: DeviceIdentifierTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeactivateDeviceIdentifierResponseTypeDef(BaseModel):
    deviceIdentifier: DeviceIdentifierTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeviceIdentifierResponseTypeDef(BaseModel):
    deviceIdentifier: DeviceIdentifierTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeviceIdentifiersResponseTypeDef(BaseModel):
    deviceIdentifiers: List[DeviceIdentifierTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReturnInformationTypeDef(BaseModel):
    replacementOrderArn: Optional[str] = None
    returnReason: Optional[str] = None
    shippingAddress: Optional[AddressTypeDef] = None
    shippingLabel: Optional[str] = None

class ActivateNetworkSiteRequestRequestTypeDef(BaseModel):
    networkSiteArn: str
    shippingAddress: AddressTypeDef
    clientToken: Optional[str] = None
    commitmentConfiguration: Optional[CommitmentConfigurationTypeDef] = None

class CommitmentInformationTypeDef(BaseModel):
    commitmentConfiguration: CommitmentConfigurationTypeDef
    expiresOn: Optional[datetime] = None
    startAt: Optional[datetime] = None

class OrderedResourceDefinitionTypeDef(BaseModel):
    count: int
    type: NetworkResourceDefinitionTypeType
    commitmentConfiguration: Optional[CommitmentConfigurationTypeDef] = None

class StartNetworkResourceUpdateRequestRequestTypeDef(BaseModel):
    networkResourceArn: str
    updateType: UpdateTypeType
    commitmentConfiguration: Optional[CommitmentConfigurationTypeDef] = None
    returnReason: Optional[str] = None
    shippingAddress: Optional[AddressTypeDef] = None

class ConfigureAccessPointRequestRequestTypeDef(BaseModel):
    accessPointArn: str
    cpiSecretKey: Optional[str] = None
    cpiUserId: Optional[str] = None
    cpiUserPassword: Optional[str] = None
    cpiUsername: Optional[str] = None
    position: Optional[PositionTypeDef] = None

class CreateNetworkResponseTypeDef(BaseModel):
    network: NetworkTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkResponseTypeDef(BaseModel):
    network: NetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkResponseTypeDef(BaseModel):
    network: NetworkTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNetworksResponseTypeDef(BaseModel):
    networks: List[NetworkTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeviceIdentifiersRequestListDeviceIdentifiersPaginateTypeDef(BaseModel):
    networkArn: str
    filters: Optional[Mapping[DeviceIdentifierFilterKeysType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNetworkResourcesRequestListNetworkResourcesPaginateTypeDef(BaseModel):
    networkArn: str
    filters: Optional[Mapping[NetworkResourceFilterKeysType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNetworkSitesRequestListNetworkSitesPaginateTypeDef(BaseModel):
    networkArn: str
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNetworksRequestListNetworksPaginateTypeDef(BaseModel):
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrdersRequestListOrdersPaginateTypeDef(BaseModel):
    networkArn: str
    filters: Optional[Mapping[OrderFilterKeysType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class NetworkResourceDefinitionTypeDef(BaseModel):
    count: int
    type: NetworkResourceDefinitionTypeType
    options: Optional[List[NameValuePairTypeDef]] = None

class NetworkResourceTypeDef(BaseModel):
    attributes: Optional[List[NameValuePairTypeDef]] = None
    commitmentInformation: Optional[CommitmentInformationTypeDef] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    health: Optional[HealthStatusType] = None
    model: Optional[str] = None
    networkArn: Optional[str] = None
    networkResourceArn: Optional[str] = None
    networkSiteArn: Optional[str] = None
    orderArn: Optional[str] = None
    position: Optional[PositionTypeDef] = None
    returnInformation: Optional[ReturnInformationTypeDef] = None
    serialNumber: Optional[str] = None
    status: Optional[NetworkResourceStatusType] = None
    statusReason: Optional[str] = None
    type: Optional[Literal["RADIO_UNIT"]] = None
    vendor: Optional[str] = None

class OrderTypeDef(BaseModel):
    acknowledgmentStatus: Optional[AcknowledgmentStatusType] = None
    createdAt: Optional[datetime] = None
    networkArn: Optional[str] = None
    networkSiteArn: Optional[str] = None
    orderArn: Optional[str] = None
    orderedResources: Optional[List[OrderedResourceDefinitionTypeDef]] = None
    shippingAddress: Optional[AddressTypeDef] = None
    trackingInformation: Optional[List[TrackingInformationTypeDef]] = None

class SitePlanTypeDef(BaseModel):
    options: Optional[List[NameValuePairTypeDef]] = None
    resourceDefinitions: Optional[List[NetworkResourceDefinitionTypeDef]] = None

class ConfigureAccessPointResponseTypeDef(BaseModel):
    accessPoint: NetworkResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkResourceResponseTypeDef(BaseModel):
    networkResource: NetworkResourceTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNetworkResourcesResponseTypeDef(BaseModel):
    networkResources: List[NetworkResourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartNetworkResourceUpdateResponseTypeDef(BaseModel):
    networkResource: NetworkResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AcknowledgeOrderReceiptResponseTypeDef(BaseModel):
    order: OrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrderResponseTypeDef(BaseModel):
    order: OrderTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrdersResponseTypeDef(BaseModel):
    nextToken: str
    orders: List[OrderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkSiteRequestRequestTypeDef(BaseModel):
    networkArn: str
    networkSiteName: str
    availabilityZone: Optional[str] = None
    availabilityZoneId: Optional[str] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    pendingPlan: Optional[SitePlanTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class NetworkSiteTypeDef(BaseModel):
    networkArn: str
    networkSiteArn: str
    networkSiteName: str
    status: NetworkSiteStatusType
    availabilityZone: Optional[str] = None
    availabilityZoneId: Optional[str] = None
    createdAt: Optional[datetime] = None
    currentPlan: Optional[SitePlanTypeDef] = None
    description: Optional[str] = None
    pendingPlan: Optional[SitePlanTypeDef] = None
    statusReason: Optional[str] = None

class UpdateNetworkSitePlanRequestRequestTypeDef(BaseModel):
    networkSiteArn: str
    pendingPlan: SitePlanTypeDef
    clientToken: Optional[str] = None

class ActivateNetworkSiteResponseTypeDef(BaseModel):
    networkSite: NetworkSiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkSiteResponseTypeDef(BaseModel):
    networkSite: NetworkSiteTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkSiteResponseTypeDef(BaseModel):
    networkSite: NetworkSiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkSiteResponseTypeDef(BaseModel):
    networkSite: NetworkSiteTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNetworkSitesResponseTypeDef(BaseModel):
    networkSites: List[NetworkSiteTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNetworkSiteResponseTypeDef(BaseModel):
    networkSite: NetworkSiteTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

