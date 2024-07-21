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
from aws_resource_validator.pydantic_models.opsworkscm_constants import *

class AccountAttributeTypeDef(BaseModel):
    Name: Optional[str] = None
    Maximum: Optional[int] = None
    Used: Optional[int] = None

class EngineAttributeTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BackupTypeDef(BaseModel):
    BackupArn: Optional[str] = None
    BackupId: Optional[str] = None
    BackupType: Optional[BackupTypeType] = None
    CreatedAt: Optional[datetime] = None
    Description: Optional[str] = None
    Engine: Optional[str] = None
    EngineModel: Optional[str] = None
    EngineVersion: Optional[str] = None
    InstanceProfileArn: Optional[str] = None
    InstanceType: Optional[str] = None
    KeyPair: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    S3DataSize: Optional[int] = None
    S3DataUrl: Optional[str] = None
    S3LogUrl: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    ServerName: Optional[str] = None
    ServiceRoleArn: Optional[str] = None
    Status: Optional[BackupStatusType] = None
    StatusDescription: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    ToolsVersion: Optional[str] = None
    UserArn: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class DeleteBackupRequestRequestTypeDef(BaseModel):
    BackupId: str

class DeleteServerRequestRequestTypeDef(BaseModel):
    ServerName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeBackupsRequestRequestTypeDef(BaseModel):
    BackupId: Optional[str] = None
    ServerName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeEventsRequestRequestTypeDef(BaseModel):
    ServerName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ServerEventTypeDef(BaseModel):
    CreatedAt: Optional[datetime] = None
    ServerName: Optional[str] = None
    Message: Optional[str] = None
    LogUrl: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeNodeAssociationStatusRequestRequestTypeDef(BaseModel):
    NodeAssociationStatusToken: str
    ServerName: str

class DescribeServersRequestRequestTypeDef(BaseModel):
    ServerName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RestoreServerRequestRequestTypeDef(BaseModel):
    BackupId: str
    ServerName: str
    InstanceType: Optional[str] = None
    KeyPair: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateServerEngineAttributesRequestRequestTypeDef(BaseModel):
    ServerName: str
    AttributeName: str
    AttributeValue: Optional[str] = None

class UpdateServerRequestRequestTypeDef(BaseModel):
    ServerName: str
    DisableAutomatedBackup: Optional[bool] = None
    BackupRetentionCount: Optional[int] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None

class AssociateNodeRequestRequestTypeDef(BaseModel):
    ServerName: str
    NodeName: str
    EngineAttributes: Sequence[EngineAttributeTypeDef]

class DisassociateNodeRequestRequestTypeDef(BaseModel):
    ServerName: str
    NodeName: str
    EngineAttributes: Optional[Sequence[EngineAttributeTypeDef]] = None

class ExportServerEngineAttributeRequestRequestTypeDef(BaseModel):
    ExportAttributeName: str
    ServerName: str
    InputAttributes: Optional[Sequence[EngineAttributeTypeDef]] = None

class ServerTypeDef(BaseModel):
    AssociatePublicIpAddress: Optional[bool] = None
    BackupRetentionCount: Optional[int] = None
    ServerName: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    CloudFormationStackArn: Optional[str] = None
    CustomDomain: Optional[str] = None
    DisableAutomatedBackup: Optional[bool] = None
    Endpoint: Optional[str] = None
    Engine: Optional[str] = None
    EngineModel: Optional[str] = None
    EngineAttributes: Optional[List[EngineAttributeTypeDef]] = None
    EngineVersion: Optional[str] = None
    InstanceProfileArn: Optional[str] = None
    InstanceType: Optional[str] = None
    KeyPair: Optional[str] = None
    MaintenanceStatus: Optional[MaintenanceStatusType] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    ServiceRoleArn: Optional[str] = None
    Status: Optional[ServerStatusType] = None
    StatusReason: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    ServerArn: Optional[str] = None

class StartMaintenanceRequestRequestTypeDef(BaseModel):
    ServerName: str
    EngineAttributes: Optional[Sequence[EngineAttributeTypeDef]] = None

class AssociateNodeResponseTypeDef(BaseModel):
    NodeAssociationStatusToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountAttributesResponseTypeDef(BaseModel):
    Attributes: List[AccountAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNodeAssociationStatusResponseTypeDef(BaseModel):
    NodeAssociationStatus: NodeAssociationStatusType
    EngineAttributes: List[EngineAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateNodeResponseTypeDef(BaseModel):
    NodeAssociationStatusToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExportServerEngineAttributeResponseTypeDef(BaseModel):
    EngineAttribute: EngineAttributeTypeDef
    ServerName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackupResponseTypeDef(BaseModel):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupsResponseTypeDef(BaseModel):
    Backups: List[BackupTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackupRequestRequestTypeDef(BaseModel):
    ServerName: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateServerRequestRequestTypeDef(BaseModel):
    Engine: str
    ServerName: str
    InstanceProfileArn: str
    InstanceType: str
    ServiceRoleArn: str
    AssociatePublicIpAddress: Optional[bool] = None
    CustomDomain: Optional[str] = None
    CustomCertificate: Optional[str] = None
    CustomPrivateKey: Optional[str] = None
    DisableAutomatedBackup: Optional[bool] = None
    EngineModel: Optional[str] = None
    EngineVersion: Optional[str] = None
    EngineAttributes: Optional[Sequence[EngineAttributeTypeDef]] = None
    BackupRetentionCount: Optional[int] = None
    KeyPair: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    BackupId: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class DescribeBackupsRequestDescribeBackupsPaginateTypeDef(BaseModel):
    BackupId: Optional[str] = None
    ServerName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsRequestDescribeEventsPaginateTypeDef(BaseModel):
    ServerName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeServersRequestDescribeServersPaginateTypeDef(BaseModel):
    ServerName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsResponseTypeDef(BaseModel):
    ServerEvents: List[ServerEventTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNodeAssociationStatusRequestNodeAssociatedWaitTypeDef(BaseModel):
    NodeAssociationStatusToken: str
    ServerName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class CreateServerResponseTypeDef(BaseModel):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServersResponseTypeDef(BaseModel):
    Servers: List[ServerTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreServerResponseTypeDef(BaseModel):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartMaintenanceResponseTypeDef(BaseModel):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServerEngineAttributesResponseTypeDef(BaseModel):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServerResponseTypeDef(BaseModel):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

