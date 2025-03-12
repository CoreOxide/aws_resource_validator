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
from aws_resource_validator.pydantic_models.privatenetworks_constants import *

class AcknowledgeOrderReceiptRequestTypeDef(BaseValidatorModel):
    orderArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ActivateDeviceIdentifierRequestTypeDef(BaseValidatorModel):
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


class CreateNetworkRequestTypeDef(BaseValidatorModel):
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


class DeactivateDeviceIdentifierRequestTypeDef(BaseValidatorModel):
    deviceIdentifierArn: str
    clientToken: Optional[str] = None


class DeleteNetworkRequestTypeDef(BaseValidatorModel):
    networkArn: str
    clientToken: Optional[str] = None


class DeleteNetworkSiteRequestTypeDef(BaseValidatorModel):
    networkSiteArn: str
    clientToken: Optional[str] = None


class GetDeviceIdentifierRequestTypeDef(BaseValidatorModel):
    deviceIdentifierArn: str


class GetNetworkRequestTypeDef(BaseValidatorModel):
    networkArn: str


class GetNetworkResourceRequestTypeDef(BaseValidatorModel):
    networkResourceArn: str


class GetNetworkSiteRequestTypeDef(BaseValidatorModel):
    networkSiteArn: str


class GetOrderRequestTypeDef(BaseValidatorModel):
    orderArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDeviceIdentifiersRequestTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[DeviceIdentifierFilterKeysType, Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


class ListNetworkResourcesRequestTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[NetworkResourceFilterKeysType, Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


class ListNetworkSitesRequestTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


class ListNetworksRequestTypeDef(BaseValidatorModel):
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


class ListOrdersRequestTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[OrderFilterKeysType, Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class NameValuePairTypeDef(BaseValidatorModel):
    name: str
    value: Optional[str] = None


class TrackingInformationTypeDef(BaseValidatorModel):
    trackingNumber: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateNetworkSiteRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ReturnInformationTypeDef(BaseValidatorModel):
    replacementOrderArn: Optional[str] = None
    returnReason: Optional[str] = None
    shippingAddress: Optional[AddressTypeDef] = None
    shippingLabel: Optional[str] = None


class ActivateNetworkSiteRequestTypeDef(BaseValidatorModel):
    networkSiteArn: str
    shippingAddress: AddressTypeDef
    clientToken: Optional[str] = None
    commitmentConfiguration: Optional[CommitmentConfigurationTypeDef] = None


class CommitmentInformationTypeDef(BaseValidatorModel):
    commitmentConfiguration: CommitmentConfigurationTypeDef
    expiresOn: Optional[datetime] = None
    startAt: Optional[datetime] = None


class StartNetworkResourceUpdateRequestTypeDef(BaseValidatorModel):
    networkResourceArn: str
    updateType: UpdateTypeType
    commitmentConfiguration: Optional[CommitmentConfigurationTypeDef] = None
    returnReason: Optional[str] = None
    shippingAddress: Optional[AddressTypeDef] = None


class ConfigureAccessPointRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListDeviceIdentifiersRequestPaginateTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[DeviceIdentifierFilterKeysType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNetworkResourcesRequestPaginateTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[NetworkResourceFilterKeysType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNetworkSitesRequestPaginateTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNetworksRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOrdersRequestPaginateTypeDef(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[OrderFilterKeysType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class OrderedResourceDefinitionTypeDef(BaseValidatorModel):
    pass


class OrderTypeDef(BaseValidatorModel):
    acknowledgmentStatus: Optional[AcknowledgmentStatusType] = None
    createdAt: Optional[datetime] = None
    networkArn: Optional[str] = None
    networkSiteArn: Optional[str] = None
    orderArn: Optional[str] = None
    orderedResources: Optional[List[OrderedResourceDefinitionTypeDef]] = None
    shippingAddress: Optional[AddressTypeDef] = None
    trackingInformation: Optional[List[TrackingInformationTypeDef]] = None


class NetworkResourceDefinitionOutputTypeDef(BaseValidatorModel):
    pass


class SitePlanOutputTypeDef(BaseValidatorModel):
    options: Optional[List[NameValuePairTypeDef]] = None
    resourceDefinitions: Optional[List[NetworkResourceDefinitionOutputTypeDef]] = None


class NetworkResourceDefinitionTypeDef(BaseValidatorModel):
    pass


class SitePlanTypeDef(BaseValidatorModel):
    options: Optional[Sequence[NameValuePairTypeDef]] = None
    resourceDefinitions: Optional[Sequence[NetworkResourceDefinitionTypeDef]] = None


class NetworkResourceTypeDef(BaseValidatorModel):
    pass


class ConfigureAccessPointResponseTypeDef(BaseValidatorModel):
    accessPoint: NetworkResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetNetworkResourceResponseTypeDef(BaseValidatorModel):
    networkResource: NetworkResourceTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListNetworkResourcesResponseTypeDef(BaseValidatorModel):
    networkResources: List[NetworkResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    orders: List[OrderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class NetworkSiteTypeDef(BaseValidatorModel):
    networkArn: str
    networkSiteArn: str
    networkSiteName: str
    status: NetworkSiteStatusType
    availabilityZone: Optional[str] = None
    availabilityZoneId: Optional[str] = None
    createdAt: Optional[datetime] = None
    currentPlan: Optional[SitePlanOutputTypeDef] = None
    description: Optional[str] = None
    pendingPlan: Optional[SitePlanOutputTypeDef] = None
    statusReason: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateNetworkSiteResponseTypeDef(BaseValidatorModel):
    networkSite: NetworkSiteTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class SitePlanUnionTypeDef(BaseValidatorModel):
    pass


class CreateNetworkSiteRequestTypeDef(BaseValidatorModel):
    networkArn: str
    networkSiteName: str
    availabilityZone: Optional[str] = None
    availabilityZoneId: Optional[str] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    pendingPlan: Optional[SitePlanUnionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateNetworkSitePlanRequestTypeDef(BaseValidatorModel):
    networkSiteArn: str
    pendingPlan: SitePlanUnionTypeDef
    clientToken: Optional[str] = None


