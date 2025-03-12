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

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateHapgRequestTypeDef(BaseValidatorModel):
    Label: str


class CreateHsmRequestTypeDef(BaseValidatorModel):
    SubnetId: str
    SshKey: str
    IamRoleArn: str
    SubscriptionType: Literal["PRODUCTION"]
    EniIp: Optional[str] = None
    ExternalId: Optional[str] = None
    ClientToken: Optional[str] = None
    SyslogIp: Optional[str] = None


class CreateLunaClientRequestTypeDef(BaseValidatorModel):
    Certificate: str
    Label: Optional[str] = None


class DeleteHapgRequestTypeDef(BaseValidatorModel):
    HapgArn: str


class DeleteHsmRequestTypeDef(BaseValidatorModel):
    HsmArn: str


class DeleteLunaClientRequestTypeDef(BaseValidatorModel):
    ClientArn: str


class DescribeHapgRequestTypeDef(BaseValidatorModel):
    HapgArn: str


class DescribeHsmRequestTypeDef(BaseValidatorModel):
    HsmArn: Optional[str] = None
    HsmSerialNumber: Optional[str] = None


class DescribeLunaClientRequestTypeDef(BaseValidatorModel):
    ClientArn: Optional[str] = None
    CertificateFingerprint: Optional[str] = None


class GetConfigRequestTypeDef(BaseValidatorModel):
    ClientArn: str
    ClientVersion: ClientVersionType
    HapgList: Sequence[str]


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListHapgsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListHsmsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListLunaClientsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ModifyHapgRequestTypeDef(BaseValidatorModel):
    HapgArn: str
    Label: Optional[str] = None
    PartitionSerialList: Optional[Sequence[str]] = None


class ModifyHsmRequestTypeDef(BaseValidatorModel):
    HsmArn: str
    SubnetId: Optional[str] = None
    EniIp: Optional[str] = None
    IamRoleArn: Optional[str] = None
    ExternalId: Optional[str] = None
    SyslogIp: Optional[str] = None


class ModifyLunaClientRequestTypeDef(BaseValidatorModel):
    ClientArn: str
    Certificate: str


class RemoveTagsFromResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeyList: Sequence[str]


class AddTagsToResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagList: Sequence[TagTypeDef]


class AddTagsToResourceResponseTypeDef(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateHapgResponseTypeDef(BaseValidatorModel):
    HapgArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateHsmResponseTypeDef(BaseValidatorModel):
    HsmArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLunaClientResponseTypeDef(BaseValidatorModel):
    ClientArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteHapgResponseTypeDef(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteHsmResponseTypeDef(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteLunaClientResponseTypeDef(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeHapgResponseTypeDef(BaseValidatorModel):
    HapgArn: str
    HapgSerial: str
    HsmsLastActionFailed: List[str]
    HsmsPendingDeletion: List[str]
    HsmsPendingRegistration: List[str]
    Label: str
    LastModifiedTimestamp: str
    PartitionSerialList: List[str]
    State: CloudHsmObjectStateType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeHsmResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLunaClientResponseTypeDef(BaseValidatorModel):
    ClientArn: str
    Certificate: str
    CertificateFingerprint: str
    LastModifiedTimestamp: str
    Label: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetConfigResponseTypeDef(BaseValidatorModel):
    ConfigType: str
    ConfigFile: str
    ConfigCred: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAvailableZonesResponseTypeDef(BaseValidatorModel):
    AZList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListHapgsResponseTypeDef(BaseValidatorModel):
    HapgList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListHsmsResponseTypeDef(BaseValidatorModel):
    HsmList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListLunaClientsResponseTypeDef(BaseValidatorModel):
    ClientList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyHapgResponseTypeDef(BaseValidatorModel):
    HapgArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyHsmResponseTypeDef(BaseValidatorModel):
    HsmArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyLunaClientResponseTypeDef(BaseValidatorModel):
    ClientArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class RemoveTagsFromResourceResponseTypeDef(BaseValidatorModel):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListHapgsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListHsmsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLunaClientsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


