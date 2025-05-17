from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'acknowledge_order_receipt' function.
class AcknowledgeOrderReceiptRequest(BaseValidatorModel):
    orderArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'activate_device_identifier' function.
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
    elevationUnit: Optional[Literal['FEET']] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


# This class is the input for the 'create_network' function.
class CreateNetworkRequest(BaseValidatorModel):
    networkName: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Network(BaseValidatorModel):
    networkArn: str
    networkName: str
    status: NetworkStatusType
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    statusReason: Optional[str] = None


# This class is the input for the 'deactivate_device_identifier' function.
class DeactivateDeviceIdentifierRequest(BaseValidatorModel):
    deviceIdentifierArn: str
    clientToken: Optional[str] = None


# This class is the input for the 'delete_network' function.
class DeleteNetworkRequest(BaseValidatorModel):
    networkArn: str
    clientToken: Optional[str] = None


# This class is the input for the 'delete_network_site' function.
class DeleteNetworkSiteRequest(BaseValidatorModel):
    networkSiteArn: str
    clientToken: Optional[str] = None


# This class is the input for the 'get_device_identifier' function.
class GetDeviceIdentifierRequest(BaseValidatorModel):
    deviceIdentifierArn: str


# This class is the input for the 'get_network' function.
class GetNetworkRequest(BaseValidatorModel):
    networkArn: str


# This class is the input for the 'get_network_resource' function.
class GetNetworkResourceRequest(BaseValidatorModel):
    networkResourceArn: str


# This class is the input for the 'get_network_site' function.
class GetNetworkSiteRequest(BaseValidatorModel):
    networkSiteArn: str


# This class is the input for the 'get_order' function.
class GetOrderRequest(BaseValidatorModel):
    orderArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_device_identifiers' function.
class ListDeviceIdentifiersRequest(BaseValidatorModel):
    networkArn: str
    filters: Optional[Dict[DeviceIdentifierFilterKeysType, List[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


# This class is the input for the 'list_network_resources' function.
class ListNetworkResourcesRequest(BaseValidatorModel):
    networkArn: str
    filters: Optional[Dict[NetworkResourceFilterKeysType, List[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


# This class is the input for the 'list_network_sites' function.
class ListNetworkSitesRequest(BaseValidatorModel):
    networkArn: str
    filters: Optional[Dict[Literal['STATUS'], List[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


# This class is the input for the 'list_networks' function.
class ListNetworksRequest(BaseValidatorModel):
    filters: Optional[Dict[Literal['STATUS'], List[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


# This class is the input for the 'list_orders' function.
class ListOrdersRequest(BaseValidatorModel):
    networkArn: str
    filters: Optional[Dict[OrderFilterKeysType, List[str]]] = None
    maxResults: Optional[int] = None
    startToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class NameValuePair(BaseValidatorModel):
    name: str
    value: Optional[str] = None


class TrackingInformation(BaseValidatorModel):
    trackingNumber: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_network_site' function.
class UpdateNetworkSiteRequest(BaseValidatorModel):
    networkSiteArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PingResponse(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'activate_device_identifier' function.
class ActivateDeviceIdentifierResponse(BaseValidatorModel):
    deviceIdentifier: DeviceIdentifier
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deactivate_device_identifier' function.
class DeactivateDeviceIdentifierResponse(BaseValidatorModel):
    deviceIdentifier: DeviceIdentifier
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_device_identifier' function.
class GetDeviceIdentifierResponse(BaseValidatorModel):
    deviceIdentifier: DeviceIdentifier
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_device_identifiers' function.
class ListDeviceIdentifiersResponse(BaseValidatorModel):
    deviceIdentifiers: List[DeviceIdentifier]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ReturnInformation(BaseValidatorModel):
    replacementOrderArn: Optional[str] = None
    returnReason: Optional[str] = None
    shippingAddress: Optional[Address] = None
    shippingLabel: Optional[str] = None


# This class is the input for the 'activate_network_site' function.
class ActivateNetworkSiteRequest(BaseValidatorModel):
    networkSiteArn: str
    shippingAddress: Address
    clientToken: Optional[str] = None
    commitmentConfiguration: Optional[CommitmentConfiguration] = None


class CommitmentInformation(BaseValidatorModel):
    commitmentConfiguration: CommitmentConfiguration
    expiresOn: Optional[datetime] = None
    startAt: Optional[datetime] = None


class OrderedResourceDefinition(BaseValidatorModel):
    count: int
    type: NetworkResourceDefinitionTypeType
    commitmentConfiguration: Optional[CommitmentConfiguration] = None


# This class is the input for the 'start_network_resource_update' function.
class StartNetworkResourceUpdateRequest(BaseValidatorModel):
    networkResourceArn: str
    updateType: UpdateTypeType
    commitmentConfiguration: Optional[CommitmentConfiguration] = None
    returnReason: Optional[str] = None
    shippingAddress: Optional[Address] = None


# This class is the input for the 'configure_access_point' function.
class ConfigureAccessPointRequest(BaseValidatorModel):
    accessPointArn: str
    cpiSecretKey: Optional[str] = None
    cpiUserId: Optional[str] = None
    cpiUserPassword: Optional[str] = None
    cpiUsername: Optional[str] = None
    position: Optional[Position] = None


# This class is the output for the 'create_network' function.
class CreateNetworkResponse(BaseValidatorModel):
    network: Network
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_network' function.
class DeleteNetworkResponse(BaseValidatorModel):
    network: Network
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_network' function.
class GetNetworkResponse(BaseValidatorModel):
    network: Network
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_networks' function.
class ListNetworksResponse(BaseValidatorModel):
    networks: List[Network]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDeviceIdentifiersRequestPaginate(BaseValidatorModel):
    networkArn: str
    filters: Optional[Dict[DeviceIdentifierFilterKeysType, List[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNetworkResourcesRequestPaginate(BaseValidatorModel):
    networkArn: str
    filters: Optional[Dict[NetworkResourceFilterKeysType, List[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNetworkSitesRequestPaginate(BaseValidatorModel):
    networkArn: str
    filters: Optional[Dict[Literal['STATUS'], List[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNetworksRequestPaginate(BaseValidatorModel):
    filters: Optional[Dict[Literal['STATUS'], List[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOrdersRequestPaginate(BaseValidatorModel):
    networkArn: str
    filters: Optional[Dict[OrderFilterKeysType, List[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class NetworkResourceDefinitionOutput(BaseValidatorModel):
    count: int
    type: NetworkResourceDefinitionTypeType
    options: Optional[List[NameValuePair]] = None


class NetworkResourceDefinition(BaseValidatorModel):
    count: int
    type: NetworkResourceDefinitionTypeType
    options: Optional[List[NameValuePair]] = None


class NetworkResource(BaseValidatorModel):
    attributes: Optional[List[NameValuePair]] = None
    commitmentInformation: Optional[CommitmentInformation] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    health: Optional[HealthStatusType] = None
    model: Optional[str] = None
    networkArn: Optional[str] = None
    networkResourceArn: Optional[str] = None
    networkSiteArn: Optional[str] = None
    orderArn: Optional[str] = None
    position: Optional[Position] = None
    returnInformation: Optional[ReturnInformation] = None
    serialNumber: Optional[str] = None
    status: Optional[NetworkResourceStatusType] = None
    statusReason: Optional[str] = None
    type: Optional[Literal['RADIO_UNIT']] = None
    vendor: Optional[str] = None


class Order(BaseValidatorModel):
    acknowledgmentStatus: Optional[AcknowledgmentStatusType] = None
    createdAt: Optional[datetime] = None
    networkArn: Optional[str] = None
    networkSiteArn: Optional[str] = None
    orderArn: Optional[str] = None
    orderedResources: Optional[List[OrderedResourceDefinition]] = None
    shippingAddress: Optional[Address] = None
    trackingInformation: Optional[List[TrackingInformation]] = None


class SitePlanOutput(BaseValidatorModel):
    options: Optional[List[NameValuePair]] = None
    resourceDefinitions: Optional[List[NetworkResourceDefinitionOutput]] = None


class SitePlan(BaseValidatorModel):
    options: Optional[List[NameValuePair]] = None
    resourceDefinitions: Optional[List[NetworkResourceDefinition]] = None


# This class is the output for the 'configure_access_point' function.
class ConfigureAccessPointResponse(BaseValidatorModel):
    accessPoint: NetworkResource
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_network_resource' function.
class GetNetworkResourceResponse(BaseValidatorModel):
    networkResource: NetworkResource
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_network_resources' function.
class ListNetworkResourcesResponse(BaseValidatorModel):
    networkResources: List[NetworkResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'start_network_resource_update' function.
class StartNetworkResourceUpdateResponse(BaseValidatorModel):
    networkResource: NetworkResource
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'acknowledge_order_receipt' function.
class AcknowledgeOrderReceiptResponse(BaseValidatorModel):
    order: Order
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_order' function.
class GetOrderResponse(BaseValidatorModel):
    order: Order
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_orders' function.
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

SitePlanUnion = Union[SitePlan, SitePlanOutput]


# This class is the output for the 'activate_network_site' function.
class ActivateNetworkSiteResponse(BaseValidatorModel):
    networkSite: NetworkSite
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_network_site' function.
class CreateNetworkSiteResponse(BaseValidatorModel):
    networkSite: NetworkSite
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_network_site' function.
class DeleteNetworkSiteResponse(BaseValidatorModel):
    networkSite: NetworkSite
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_network_site' function.
class GetNetworkSiteResponse(BaseValidatorModel):
    networkSite: NetworkSite
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_network_sites' function.
class ListNetworkSitesResponse(BaseValidatorModel):
    networkSites: List[NetworkSite]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_network_site_plan' function.
class UpdateNetworkSiteResponse(BaseValidatorModel):
    networkSite: NetworkSite
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_network_site' function.
class CreateNetworkSiteRequest(BaseValidatorModel):
    networkArn: str
    networkSiteName: str
    availabilityZone: Optional[str] = None
    availabilityZoneId: Optional[str] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    pendingPlan: Optional[SitePlanUnion] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_network_site_plan' function.
class UpdateNetworkSitePlanRequest(BaseValidatorModel):
    networkSiteArn: str
    pendingPlan: SitePlanUnion
    clientToken: Optional[str] = None