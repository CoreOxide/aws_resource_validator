from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cloudhsm.cloudhsm_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_hapg' function.
class CreateHapgRequest(BaseValidatorModel):
    Label: str


# This class is the input for the 'create_hsm' function.
class CreateHsmRequest(BaseValidatorModel):
    SubnetId: str
    SshKey: str
    IamRoleArn: str
    SubscriptionType: Literal['PRODUCTION']
    EniIp: Optional[str] = None
    ExternalId: Optional[str] = None
    ClientToken: Optional[str] = None
    SyslogIp: Optional[str] = None


# This class is the input for the 'create_luna_client' function.
class CreateLunaClientRequest(BaseValidatorModel):
    Certificate: str
    Label: Optional[str] = None


# This class is the input for the 'delete_hapg' function.
class DeleteHapgRequest(BaseValidatorModel):
    HapgArn: str


# This class is the input for the 'delete_hsm' function.
class DeleteHsmRequest(BaseValidatorModel):
    HsmArn: str


# This class is the input for the 'delete_luna_client' function.
class DeleteLunaClientRequest(BaseValidatorModel):
    ClientArn: str


# This class is the input for the 'describe_hapg' function.
class DescribeHapgRequest(BaseValidatorModel):
    HapgArn: str


# This class is the input for the 'describe_hsm' function.
class DescribeHsmRequest(BaseValidatorModel):
    HsmArn: Optional[str] = None
    HsmSerialNumber: Optional[str] = None


# This class is the input for the 'describe_luna_client' function.
class DescribeLunaClientRequest(BaseValidatorModel):
    ClientArn: Optional[str] = None
    CertificateFingerprint: Optional[str] = None


# This class is the input for the 'get_config' function.
class GetConfigRequest(BaseValidatorModel):
    ClientArn: str
    ClientVersion: ClientVersionType
    HapgList: List[str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_hapgs' function.
class ListHapgsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


# This class is the input for the 'list_hsms' function.
class ListHsmsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


# This class is the input for the 'list_luna_clients' function.
class ListLunaClientsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'modify_hapg' function.
class ModifyHapgRequest(BaseValidatorModel):
    HapgArn: str
    Label: Optional[str] = None
    PartitionSerialList: Optional[List[str]] = None


# This class is the input for the 'modify_hsm' function.
class ModifyHsmRequest(BaseValidatorModel):
    HsmArn: str
    SubnetId: Optional[str] = None
    EniIp: Optional[str] = None
    IamRoleArn: Optional[str] = None
    ExternalId: Optional[str] = None
    SyslogIp: Optional[str] = None


# This class is the input for the 'modify_luna_client' function.
class ModifyLunaClientRequest(BaseValidatorModel):
    ClientArn: str
    Certificate: str


# This class is the input for the 'remove_tags_from_resource' function.
class RemoveTagsFromResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeyList: List[str]


# This class is the input for the 'add_tags_to_resource' function.
class AddTagsToResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagList: List[Tag]


# This class is the output for the 'add_tags_to_resource' function.
class AddTagsToResourceResponse(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_hapg' function.
class CreateHapgResponse(BaseValidatorModel):
    HapgArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_hsm' function.
class CreateHsmResponse(BaseValidatorModel):
    HsmArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_luna_client' function.
class CreateLunaClientResponse(BaseValidatorModel):
    ClientArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_hapg' function.
class DeleteHapgResponse(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_hsm' function.
class DeleteHsmResponse(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_luna_client' function.
class DeleteLunaClientResponse(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_hapg' function.
class DescribeHapgResponse(BaseValidatorModel):
    HapgArn: str
    HapgSerial: str
    HsmsLastActionFailed: List[str]
    HsmsPendingDeletion: List[str]
    HsmsPendingRegistration: List[str]
    Label: str
    LastModifiedTimestamp: str
    PartitionSerialList: List[str]
    State: CloudHsmObjectStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_hsm' function.
class DescribeHsmResponse(BaseValidatorModel):
    HsmArn: str
    Status: HsmStatusType
    StatusDetails: str
    AvailabilityZone: str
    EniId: str
    EniIp: str
    SubscriptionType: Literal['PRODUCTION']
    SubscriptionStartDate: str
    SubscriptionEndDate: str
    VpcId: str
    SubnetId: str
    IamRoleArn: str
    SerialNumber: str
    VendorName: str
    HsmType: str
    SoftwareVersion: str
    SshPublicKey: str
    SshKeyLastUpdated: str
    ServerCertUri: str
    ServerCertLastUpdated: str
    Partitions: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_luna_client' function.
class DescribeLunaClientResponse(BaseValidatorModel):
    ClientArn: str
    Certificate: str
    CertificateFingerprint: str
    LastModifiedTimestamp: str
    Label: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_config' function.
class GetConfigResponse(BaseValidatorModel):
    ConfigType: str
    ConfigFile: str
    ConfigCred: str
    ResponseMetadata: ResponseMetadata


class ListAvailableZonesResponse(BaseValidatorModel):
    AZList: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_hapgs' function.
class ListHapgsResponse(BaseValidatorModel):
    HapgList: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_hsms' function.
class ListHsmsResponse(BaseValidatorModel):
    HsmList: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_luna_clients' function.
class ListLunaClientsResponse(BaseValidatorModel):
    ClientList: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_hapg' function.
class ModifyHapgResponse(BaseValidatorModel):
    HapgArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_hsm' function.
class ModifyHsmResponse(BaseValidatorModel):
    HsmArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_luna_client' function.
class ModifyLunaClientResponse(BaseValidatorModel):
    ClientArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_tags_from_resource' function.
class RemoveTagsFromResourceResponse(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadata


class ListHapgsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHsmsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLunaClientsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None