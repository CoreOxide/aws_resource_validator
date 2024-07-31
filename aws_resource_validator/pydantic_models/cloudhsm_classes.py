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
from aws_resource_validator.pydantic_models.cloudhsm_constants import *

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateHapgRequestRequestTypeDef(BaseModel):
    Label: str

class CreateHsmRequestRequestTypeDef(BaseModel):
    SubnetId: str
    SshKey: str
    IamRoleArn: str
    SubscriptionType: Literal["PRODUCTION"]
    EniIp: Optional[str] = None
    ExternalId: Optional[str] = None
    ClientToken: Optional[str] = None
    SyslogIp: Optional[str] = None

class CreateLunaClientRequestRequestTypeDef(BaseModel):
    Certificate: str
    Label: Optional[str] = None

class DeleteHapgRequestRequestTypeDef(BaseModel):
    HapgArn: str

class DeleteHsmRequestRequestTypeDef(BaseModel):
    HsmArn: str

class DeleteLunaClientRequestRequestTypeDef(BaseModel):
    ClientArn: str

class DescribeHapgRequestRequestTypeDef(BaseModel):
    HapgArn: str

class DescribeHsmRequestRequestTypeDef(BaseModel):
    HsmArn: Optional[str] = None
    HsmSerialNumber: Optional[str] = None

class DescribeLunaClientRequestRequestTypeDef(BaseModel):
    ClientArn: Optional[str] = None
    CertificateFingerprint: Optional[str] = None

class GetConfigRequestRequestTypeDef(BaseModel):
    ClientArn: str
    ClientVersion: ClientVersionType
    HapgList: Sequence[str]

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListHapgsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class ListHsmsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class ListLunaClientsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ModifyHapgRequestRequestTypeDef(BaseModel):
    HapgArn: str
    Label: Optional[str] = None
    PartitionSerialList: Optional[Sequence[str]] = None

class ModifyHsmRequestRequestTypeDef(BaseModel):
    HsmArn: str
    SubnetId: Optional[str] = None
    EniIp: Optional[str] = None
    IamRoleArn: Optional[str] = None
    ExternalId: Optional[str] = None
    SyslogIp: Optional[str] = None

class ModifyLunaClientRequestRequestTypeDef(BaseModel):
    ClientArn: str
    Certificate: str

class RemoveTagsFromResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeyList: Sequence[str]

class AddTagsToResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagList: Sequence[TagTypeDef]

class AddTagsToResourceResponseTypeDef(BaseModel):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHapgResponseTypeDef(BaseModel):
    HapgArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHsmResponseTypeDef(BaseModel):
    HsmArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLunaClientResponseTypeDef(BaseModel):
    ClientArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteHapgResponseTypeDef(BaseModel):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteHsmResponseTypeDef(BaseModel):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLunaClientResponseTypeDef(BaseModel):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeHapgResponseTypeDef(BaseModel):
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

class DescribeHsmResponseTypeDef(BaseModel):
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

class DescribeLunaClientResponseTypeDef(BaseModel):
    ClientArn: str
    Certificate: str
    CertificateFingerprint: str
    LastModifiedTimestamp: str
    Label: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfigResponseTypeDef(BaseModel):
    ConfigType: str
    ConfigFile: str
    ConfigCred: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAvailableZonesResponseTypeDef(BaseModel):
    AZList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListHapgsResponseTypeDef(BaseModel):
    HapgList: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListHsmsResponseTypeDef(BaseModel):
    HsmList: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLunaClientsResponseTypeDef(BaseModel):
    ClientList: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyHapgResponseTypeDef(BaseModel):
    HapgArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyHsmResponseTypeDef(BaseModel):
    HsmArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyLunaClientResponseTypeDef(BaseModel):
    ClientArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveTagsFromResourceResponseTypeDef(BaseModel):
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListHapgsRequestListHapgsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHsmsRequestListHsmsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLunaClientsRequestListLunaClientsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

