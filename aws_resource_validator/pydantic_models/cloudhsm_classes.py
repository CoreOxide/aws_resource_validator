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
from aws_resource_validator.pydantic_models.cloudhsm_constants import *

class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateHapgRequest(BaseValidatorModel):
    Label: str


class CreateHsmRequest(BaseValidatorModel):
    SubnetId: str
    SshKey: str
    IamRoleArn: str
    SubscriptionType: Literal["PRODUCTION"]
    EniIp: Optional[str] = None
    ExternalId: Optional[str] = None
    ClientToken: Optional[str] = None
    SyslogIp: Optional[str] = None


class CreateLunaClientRequest(BaseValidatorModel):
    Certificate: str
    Label: Optional[str] = None


class DeleteHapgRequest(BaseValidatorModel):
    HapgArn: str


class DeleteHsmRequest(BaseValidatorModel):
    HsmArn: str


class DeleteLunaClientRequest(BaseValidatorModel):
    ClientArn: str


class DescribeHapgRequest(BaseValidatorModel):
    HapgArn: str


class DescribeHsmRequest(BaseValidatorModel):
    HsmArn: Optional[str] = None
    HsmSerialNumber: Optional[str] = None


class DescribeLunaClientRequest(BaseValidatorModel):
    ClientArn: Optional[str] = None
    CertificateFingerprint: Optional[str] = None


class GetConfigRequest(BaseValidatorModel):
    ClientArn: str
    ClientVersion: ClientVersionType
    HapgList: Sequence[str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListHapgsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListHsmsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListLunaClientsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ModifyHapgRequest(BaseValidatorModel):
    HapgArn: str
    Label: Optional[str] = None
    PartitionSerialList: Optional[Sequence[str]] = None


class ModifyHsmRequest(BaseValidatorModel):
    HsmArn: str
    SubnetId: Optional[str] = None
    EniIp: Optional[str] = None
    IamRoleArn: Optional[str] = None
    ExternalId: Optional[str] = None
    SyslogIp: Optional[str] = None


class ModifyLunaClientRequest(BaseValidatorModel):
    ClientArn: str
    Certificate: str


class RemoveTagsFromResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeyList: Sequence[str]


class AddTagsToResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagList: Sequence[Tag]


class AddTagsToResourceResponse(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadata


class CreateHapgResponse(BaseValidatorModel):
    HapgArn: str
    ResponseMetadata: ResponseMetadata


class CreateHsmResponse(BaseValidatorModel):
    HsmArn: str
    ResponseMetadata: ResponseMetadata


class CreateLunaClientResponse(BaseValidatorModel):
    ClientArn: str
    ResponseMetadata: ResponseMetadata


class DeleteHapgResponse(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadata


class DeleteHsmResponse(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadata


class DeleteLunaClientResponse(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadata


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


class DescribeHsmResponse(BaseValidatorModel):
    HsmArn: str
    Status: HsmStatusType
    StatusDetails: str
    AvailabilityZone: str
    EniId: str
    EniIp: str
    SubscriptionType: Literal["PRODUCTION"]
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


class DescribeLunaClientResponse(BaseValidatorModel):
    ClientArn: str
    Certificate: str
    CertificateFingerprint: str
    LastModifiedTimestamp: str
    Label: str
    ResponseMetadata: ResponseMetadata


class GetConfigResponse(BaseValidatorModel):
    ConfigType: str
    ConfigFile: str
    ConfigCred: str
    ResponseMetadata: ResponseMetadata


class ListAvailableZonesResponse(BaseValidatorModel):
    AZList: List[str]
    ResponseMetadata: ResponseMetadata


class ListHapgsResponse(BaseValidatorModel):
    HapgList: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListHsmsResponse(BaseValidatorModel):
    HsmList: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListLunaClientsResponse(BaseValidatorModel):
    ClientList: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class ModifyHapgResponse(BaseValidatorModel):
    HapgArn: str
    ResponseMetadata: ResponseMetadata


class ModifyHsmResponse(BaseValidatorModel):
    HsmArn: str
    ResponseMetadata: ResponseMetadata


class ModifyLunaClientResponse(BaseValidatorModel):
    ClientArn: str
    ResponseMetadata: ResponseMetadata


class RemoveTagsFromResourceResponse(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadata


class ListHapgsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHsmsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLunaClientsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


