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
from aws_resource_validator.pydantic_models.privatenetworks_constants import *

class AcknowledgeOrderReceiptRequestRequestTypeDef(BaseValidatorModel):
    orderArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ActivateDeviceIdentifierRequestRequestTypeDef(BaseValidatorModel):
    deviceIdentifierArn: str
    clientToken: Optional[str] = None

class DeviceIdentifierTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    deviceIdentifierArn: Optional[str] = None
    iccid: Optional[str] = None
    imsi: Optional[str] = None
    networkArn: Optional[str] = None
    orderArn: Optional[str] = None
    status: Optional[DeviceIdentifierStatusType] = None
    trafficGroupArn: Optional[str] = None
    vendor: Optional[str] = None

class AddressTypeDef(BaseValidatorModel):
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

class CommitmentConfigurationTypeDef(BaseValidatorModel):
    automaticRenewal: bool
    commitmentLength: CommitmentLengthType

class PositionTypeDef(BaseValidatorModel):
    elevation: Optional[float] = None
    elevationReference: Optional[ElevationReferenceType] = None
    elevationUnit: Optional[Literal["FEET"]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class CreateNetworkRequestRequestTypeDef(BaseValidatorModel):
    networkName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class NetworkTypeDef(BaseValidatorModel):
    networkArn: str
    networkName: str
    status: NetworkStatusType
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    statusReason: Optional[str] = None

class DeactivateDeviceIdentifierRequestRequestTypeDef(BaseValidatorModel):
    deviceIdentifierArn: str
    clientToken: Optional[str] = None

class DeleteNetworkRequestRequestTypeDef(BaseValidatorModel):
    networkArn: str
    clientToken: Optional[str] = None

class DeleteNetworkSiteRequestRequestTypeDef(BaseValidatorModel):
    networkSiteArn: str
    clientToken: Optional[str] = None

class GetDeviceIdentifierRequestRequestTypeDef(BaseValidatorModel):
    deviceIdentifierArn: str

class GetNetworkRequestRequestTypeDef(BaseValidatorModel):
    networkArn: str

class GetNetworkResourceRequestRequestTypeDef(BaseValidatorModel):
    networkResourceArn: str

class GetNetworkSiteRequestRequestTypeDef(BaseValidatorModel):
    networkSiteArn: str

class GetOrderRequestRequestTypeDef(BaseValidatorModel):
    orderArn: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDeviceIdentifiersRequestRequestTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[DeviceIdentifierFilterKeysType, Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None

class ListNetworkResourcesRequestRequestTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[NetworkResourceFilterKeysType, Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None

class ListNetworkSitesRequestRequestTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None

class ListNetworksRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None

class ListOrdersRequestRequestTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[OrderFilterKeysType, Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class NameValuePairTypeDef(BaseValidatorModel):
    name: str
    value: Optional[str] = None

class TrackingInformationTypeDef(BaseValidatorModel):
    trackingNumber: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateNetworkSiteRequestRequestTypeDef(BaseValidatorModel):
    networkSiteArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PingResponseTypeDef(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class ActivateDeviceIdentifierResponseTypeDef(BaseValidatorModel):
    deviceIdentifier: DeviceIdentifierTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeactivateDeviceIdentifierResponseTypeDef(BaseValidatorModel):
    deviceIdentifier: DeviceIdentifierTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeviceIdentifierResponseTypeDef(BaseValidatorModel):
    deviceIdentifier: DeviceIdentifierTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeviceIdentifiersResponseTypeDef(BaseValidatorModel):
    deviceIdentifiers: List[DeviceIdentifierTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReturnInformationTypeDef(BaseValidatorModel):
    replacementOrderArn: Optional[str] = None
    returnReason: Optional[str] = None
    shippingAddress: Optional[AddressTypeDef] = None
    shippingLabel: Optional[str] = None

class ActivateNetworkSiteRequestRequestTypeDef(BaseValidatorModel):
    networkSiteArn: str
    shippingAddress: AddressTypeDef
    clientToken: Optional[str] = None
    commitmentConfiguration: Optional[CommitmentConfigurationTypeDef] = None

class CommitmentInformationTypeDef(BaseValidatorModel):
    commitmentConfiguration: CommitmentConfigurationTypeDef
    expiresOn: Optional[datetime] = None
    startAt: Optional[datetime] = None

class OrderedResourceDefinitionTypeDef(BaseValidatorModel):
    count: int
    type: NetworkResourceDefinitionTypeType
    commitmentConfiguration: Optional[CommitmentConfigurationTypeDef] = None

class StartNetworkResourceUpdateRequestRequestTypeDef(BaseValidatorModel):
    networkResourceArn: str
    updateType: UpdateTypeType
    commitmentConfiguration: Optional[CommitmentConfigurationTypeDef] = None
    returnReason: Optional[str] = None
    shippingAddress: Optional[AddressTypeDef] = None

class ConfigureAccessPointRequestRequestTypeDef(BaseValidatorModel):
    accessPointArn: str
    cpiSecretKey: Optional[str] = None
    cpiUserId: Optional[str] = None
    cpiUserPassword: Optional[str] = None
    cpiUsername: Optional[str] = None
    position: Optional[PositionTypeDef] = None

class CreateNetworkResponseTypeDef(BaseValidatorModel):
    network: NetworkTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkResponseTypeDef(BaseValidatorModel):
    network: NetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkResponseTypeDef(BaseValidatorModel):
    network: NetworkTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNetworksResponseTypeDef(BaseValidatorModel):
    networks: List[NetworkTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeviceIdentifiersRequestListDeviceIdentifiersPaginateTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[DeviceIdentifierFilterKeysType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNetworkResourcesRequestListNetworkResourcesPaginateTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[NetworkResourceFilterKeysType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNetworkSitesRequestListNetworkSitesPaginateTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNetworksRequestListNetworksPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrdersRequestListOrdersPaginateTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[OrderFilterKeysType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class NetworkResourceDefinitionTypeDef(BaseValidatorModel):
    count: int
    type: NetworkResourceDefinitionTypeType
    options: Optional[List[NameValuePairTypeDef]] = None

class NetworkResourceTypeDef(BaseValidatorModel):
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

class OrderTypeDef(BaseValidatorModel):
    acknowledgmentStatus: Optional[AcknowledgmentStatusType] = None
    createdAt: Optional[datetime] = None
    networkArn: Optional[str] = None
    networkSiteArn: Optional[str] = None
    orderArn: Optional[str] = None
    orderedResources: Optional[List[OrderedResourceDefinitionTypeDef]] = None
    shippingAddress: Optional[AddressTypeDef] = None
    trackingInformation: Optional[List[TrackingInformationTypeDef]] = None

class SitePlanTypeDef(BaseValidatorModel):
    options: Optional[List[NameValuePairTypeDef]] = None
    resourceDefinitions: Optional[List[NetworkResourceDefinitionTypeDef]] = None

class ConfigureAccessPointResponseTypeDef(BaseValidatorModel):
    accessPoint: NetworkResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkResourceResponseTypeDef(BaseValidatorModel):
    networkResource: NetworkResourceTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNetworkResourcesResponseTypeDef(BaseValidatorModel):
    networkResources: List[NetworkResourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartNetworkResourceUpdateResponseTypeDef(BaseValidatorModel):
    networkResource: NetworkResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AcknowledgeOrderReceiptResponseTypeDef(BaseValidatorModel):
    order: OrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrderResponseTypeDef(BaseValidatorModel):
    order: OrderTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrdersResponseTypeDef(BaseValidatorModel):
    nextToken: str
    orders: List[OrderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkSiteRequestRequestTypeDef(BaseValidatorModel):
    networkArn: str
    networkSiteName: str
    availabilityZone: Optional[str] = None
    availabilityZoneId: Optional[str] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    pendingPlan: Optional[SitePlanTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class NetworkSiteTypeDef(BaseValidatorModel):
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

class UpdateNetworkSitePlanRequestRequestTypeDef(BaseValidatorModel):
    networkSiteArn: str
    pendingPlan: SitePlanTypeDef
    clientToken: Optional[str] = None

class ActivateNetworkSiteResponseTypeDef(BaseValidatorModel):
    networkSite: NetworkSiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkSiteResponseTypeDef(BaseValidatorModel):
    networkSite: NetworkSiteTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkSiteResponseTypeDef(BaseValidatorModel):
    networkSite: NetworkSiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkSiteResponseTypeDef(BaseValidatorModel):
    networkSite: NetworkSiteTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNetworkSitesResponseTypeDef(BaseValidatorModel):
    networkSites: List[NetworkSiteTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNetworkSiteResponseTypeDef(BaseValidatorModel):
    networkSite: NetworkSiteTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

