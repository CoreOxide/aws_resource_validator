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

class AcknowledgeOrderReceiptRequest(BaseValidatorModel):
    orderArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ActivateDeviceIdentifierRequest(BaseValidatorModel):
    deviceIdentifierArn: str
    clientToken: Optional[str] = None


class DeviceIdentifier(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    deviceIdentifierArn: Optional[str] = None
    iccid: Optional[str] = None
    imsi: Optional[str] = None
    networkArn: Optional[str] = None
    orderArn: Optional[str] = None
    status: Optional[DeviceIdentifierStatusType] = None
    trafficGroupArn: Optional[str] = None
    vendor: Optional[str] = None


class Address(BaseValidatorModel):
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


class CommitmentConfiguration(BaseValidatorModel):
    automaticRenewal: bool
    commitmentLength: CommitmentLengthType


class Position(BaseValidatorModel):
    elevation: Optional[float] = None
    elevationReference: Optional[ElevationReferenceType] = None
    elevationUnit: Optional[Literal["FEET"]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class CreateNetworkRequest(BaseValidatorModel):
    networkName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class Network(BaseValidatorModel):
    networkArn: str
    networkName: str
    status: NetworkStatusType
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    statusReason: Optional[str] = None


class DeactivateDeviceIdentifierRequest(BaseValidatorModel):
    deviceIdentifierArn: str
    clientToken: Optional[str] = None


class DeleteNetworkRequest(BaseValidatorModel):
    networkArn: str
    clientToken: Optional[str] = None


class DeleteNetworkSiteRequest(BaseValidatorModel):
    networkSiteArn: str
    clientToken: Optional[str] = None


class GetDeviceIdentifierRequest(BaseValidatorModel):
    deviceIdentifierArn: str


class GetNetworkRequest(BaseValidatorModel):
    networkArn: str


class GetNetworkResourceRequest(BaseValidatorModel):
    networkResourceArn: str


class GetNetworkSiteRequest(BaseValidatorModel):
    networkSiteArn: str


class GetOrderRequest(BaseValidatorModel):
    orderArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDeviceIdentifiersRequest(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[DeviceIdentifierFilterKeysType, Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


class ListNetworkResourcesRequest(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[NetworkResourceFilterKeysType, Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


class ListNetworkSitesRequest(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


class ListNetworksRequest(BaseValidatorModel):
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


class ListOrdersRequest(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[OrderFilterKeysType, Sequence[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class NameValuePair(BaseValidatorModel):
    name: str
    value: Optional[str] = None


class TrackingInformation(BaseValidatorModel):
    trackingNumber: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateNetworkSiteRequest(BaseValidatorModel):
    networkSiteArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PingResponse(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


class ActivateDeviceIdentifierResponse(BaseValidatorModel):
    deviceIdentifier: DeviceIdentifier
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DeactivateDeviceIdentifierResponse(BaseValidatorModel):
    deviceIdentifier: DeviceIdentifier
    ResponseMetadata: ResponseMetadata


class GetDeviceIdentifierResponse(BaseValidatorModel):
    deviceIdentifier: DeviceIdentifier
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListDeviceIdentifiersResponse(BaseValidatorModel):
    deviceIdentifiers: List[DeviceIdentifier]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ReturnInformation(BaseValidatorModel):
    replacementOrderArn: Optional[str] = None
    returnReason: Optional[str] = None
    shippingAddress: Optional[Address] = None
    shippingLabel: Optional[str] = None


class ActivateNetworkSiteRequest(BaseValidatorModel):
    networkSiteArn: str
    shippingAddress: Address
    clientToken: Optional[str] = None
    commitmentConfiguration: Optional[CommitmentConfiguration] = None


class CommitmentInformation(BaseValidatorModel):
    commitmentConfiguration: CommitmentConfiguration
    expiresOn: Optional[datetime] = None
    startAt: Optional[datetime] = None


class StartNetworkResourceUpdateRequest(BaseValidatorModel):
    networkResourceArn: str
    updateType: UpdateTypeType
    commitmentConfiguration: Optional[CommitmentConfiguration] = None
    returnReason: Optional[str] = None
    shippingAddress: Optional[Address] = None


class ConfigureAccessPointRequest(BaseValidatorModel):
    accessPointArn: str
    cpiSecretKey: Optional[str] = None
    cpiUserId: Optional[str] = None
    cpiUserPassword: Optional[str] = None
    cpiUsername: Optional[str] = None
    position: Optional[Position] = None


class CreateNetworkResponse(BaseValidatorModel):
    network: Network
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DeleteNetworkResponse(BaseValidatorModel):
    network: Network
    ResponseMetadata: ResponseMetadata


class GetNetworkResponse(BaseValidatorModel):
    network: Network
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListNetworksResponse(BaseValidatorModel):
    networks: List[Network]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDeviceIdentifiersRequestPaginate(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[DeviceIdentifierFilterKeysType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNetworkResourcesRequestPaginate(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[NetworkResourceFilterKeysType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNetworkSitesRequestPaginate(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNetworksRequestPaginate(BaseValidatorModel):
    filters: Optional[Mapping[Literal["STATUS"], Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOrdersRequestPaginate(BaseValidatorModel):
    networkArn: str
    filters: Optional[Mapping[OrderFilterKeysType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class OrderedResourceDefinition(BaseValidatorModel):
    pass


class Order(BaseValidatorModel):
    acknowledgmentStatus: Optional[AcknowledgmentStatusType] = None
    createdAt: Optional[datetime] = None
    networkArn: Optional[str] = None
    networkSiteArn: Optional[str] = None
    orderArn: Optional[str] = None
    orderedResources: Optional[List[OrderedResourceDefinition]] = None
    shippingAddress: Optional[Address] = None
    trackingInformation: Optional[List[TrackingInformation]] = None


class NetworkResourceDefinitionOutput(BaseValidatorModel):
    pass


class SitePlanOutput(BaseValidatorModel):
    options: Optional[List[NameValuePair]] = None
    resourceDefinitions: Optional[List[NetworkResourceDefinitionOutput]] = None


class NetworkResourceDefinition(BaseValidatorModel):
    pass


class SitePlan(BaseValidatorModel):
    options: Optional[Sequence[NameValuePair]] = None
    resourceDefinitions: Optional[Sequence[NetworkResourceDefinition]] = None


class NetworkResource(BaseValidatorModel):
    pass


class ConfigureAccessPointResponse(BaseValidatorModel):
    accessPoint: NetworkResource
    ResponseMetadata: ResponseMetadata


class GetNetworkResourceResponse(BaseValidatorModel):
    networkResource: NetworkResource
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListNetworkResourcesResponse(BaseValidatorModel):
    networkResources: List[NetworkResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartNetworkResourceUpdateResponse(BaseValidatorModel):
    networkResource: NetworkResource
    ResponseMetadata: ResponseMetadata


class AcknowledgeOrderReceiptResponse(BaseValidatorModel):
    order: Order
    ResponseMetadata: ResponseMetadata


class GetOrderResponse(BaseValidatorModel):
    order: Order
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListOrdersResponse(BaseValidatorModel):
    orders: List[Order]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class NetworkSite(BaseValidatorModel):
    networkArn: str
    networkSiteArn: str
    networkSiteName: str
    status: NetworkSiteStatusType
    availabilityZone: Optional[str] = None
    availabilityZoneId: Optional[str] = None
    createdAt: Optional[datetime] = None
    currentPlan: Optional[SitePlanOutput] = None
    description: Optional[str] = None
    pendingPlan: Optional[SitePlanOutput] = None
    statusReason: Optional[str] = None


class ActivateNetworkSiteResponse(BaseValidatorModel):
    networkSite: NetworkSite
    ResponseMetadata: ResponseMetadata


class CreateNetworkSiteResponse(BaseValidatorModel):
    networkSite: NetworkSite
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DeleteNetworkSiteResponse(BaseValidatorModel):
    networkSite: NetworkSite
    ResponseMetadata: ResponseMetadata


class GetNetworkSiteResponse(BaseValidatorModel):
    networkSite: NetworkSite
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListNetworkSitesResponse(BaseValidatorModel):
    networkSites: List[NetworkSite]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateNetworkSiteResponse(BaseValidatorModel):
    networkSite: NetworkSite
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class SitePlanUnion(BaseValidatorModel):
    pass


class CreateNetworkSiteRequest(BaseValidatorModel):
    networkArn: str
    networkSiteName: str
    availabilityZone: Optional[str] = None
    availabilityZoneId: Optional[str] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    pendingPlan: Optional[SitePlanUnion] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateNetworkSitePlanRequest(BaseValidatorModel):
    networkSiteArn: str
    pendingPlan: SitePlanUnion
    clientToken: Optional[str] = None


