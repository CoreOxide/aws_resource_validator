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
from aws_resource_validator.pydantic_models.opsworkscm_constants import *

class AccountAttributeTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Maximum: Optional[int] = None
    Used: Optional[int] = None

class EngineAttributeTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BackupTypeDef(BaseValidatorModel):
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

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class DeleteBackupRequestRequestTypeDef(BaseValidatorModel):
    BackupId: str

class DeleteServerRequestRequestTypeDef(BaseValidatorModel):
    ServerName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeBackupsRequestRequestTypeDef(BaseValidatorModel):
    BackupId: Optional[str] = None
    ServerName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeEventsRequestRequestTypeDef(BaseValidatorModel):
    ServerName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ServerEventTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    ServerName: Optional[str] = None
    Message: Optional[str] = None
    LogUrl: Optional[str] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeNodeAssociationStatusRequestRequestTypeDef(BaseValidatorModel):
    NodeAssociationStatusToken: str
    ServerName: str

class DescribeServersRequestRequestTypeDef(BaseValidatorModel):
    ServerName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RestoreServerRequestRequestTypeDef(BaseValidatorModel):
    BackupId: str
    ServerName: str
    InstanceType: Optional[str] = None
    KeyPair: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateServerEngineAttributesRequestRequestTypeDef(BaseValidatorModel):
    ServerName: str
    AttributeName: str
    AttributeValue: Optional[str] = None

class UpdateServerRequestRequestTypeDef(BaseValidatorModel):
    ServerName: str
    DisableAutomatedBackup: Optional[bool] = None
    BackupRetentionCount: Optional[int] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None

class AssociateNodeRequestRequestTypeDef(BaseValidatorModel):
    ServerName: str
    NodeName: str
    EngineAttributes: Sequence[EngineAttributeTypeDef]

class DisassociateNodeRequestRequestTypeDef(BaseValidatorModel):
    ServerName: str
    NodeName: str
    EngineAttributes: Optional[Sequence[EngineAttributeTypeDef]] = None

class ExportServerEngineAttributeRequestRequestTypeDef(BaseValidatorModel):
    ExportAttributeName: str
    ServerName: str
    InputAttributes: Optional[Sequence[EngineAttributeTypeDef]] = None

class ServerTypeDef(BaseValidatorModel):
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

class StartMaintenanceRequestRequestTypeDef(BaseValidatorModel):
    ServerName: str
    EngineAttributes: Optional[Sequence[EngineAttributeTypeDef]] = None

class AssociateNodeResponseTypeDef(BaseValidatorModel):
    NodeAssociationStatusToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: List[AccountAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNodeAssociationStatusResponseTypeDef(BaseValidatorModel):
    NodeAssociationStatus: NodeAssociationStatusType
    EngineAttributes: List[EngineAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateNodeResponseTypeDef(BaseValidatorModel):
    NodeAssociationStatusToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExportServerEngineAttributeResponseTypeDef(BaseValidatorModel):
    EngineAttribute: EngineAttributeTypeDef
    ServerName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackupResponseTypeDef(BaseValidatorModel):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupsResponseTypeDef(BaseValidatorModel):
    Backups: List[BackupTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackupRequestRequestTypeDef(BaseValidatorModel):
    ServerName: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateServerRequestRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class DescribeBackupsRequestDescribeBackupsPaginateTypeDef(BaseValidatorModel):
    BackupId: Optional[str] = None
    ServerName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsRequestDescribeEventsPaginateTypeDef(BaseValidatorModel):
    ServerName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeServersRequestDescribeServersPaginateTypeDef(BaseValidatorModel):
    ServerName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsResponseTypeDef(BaseValidatorModel):
    ServerEvents: List[ServerEventTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNodeAssociationStatusRequestNodeAssociatedWaitTypeDef(BaseValidatorModel):
    NodeAssociationStatusToken: str
    ServerName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class CreateServerResponseTypeDef(BaseValidatorModel):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServersResponseTypeDef(BaseValidatorModel):
    Servers: List[ServerTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreServerResponseTypeDef(BaseValidatorModel):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartMaintenanceResponseTypeDef(BaseValidatorModel):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServerEngineAttributesResponseTypeDef(BaseValidatorModel):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServerResponseTypeDef(BaseValidatorModel):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

