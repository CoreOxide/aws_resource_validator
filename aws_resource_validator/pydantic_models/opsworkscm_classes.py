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
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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


class DeleteBackupRequestTypeDef(BaseValidatorModel):
    BackupId: str


class DeleteServerRequestTypeDef(BaseValidatorModel):
    ServerName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeBackupsRequestTypeDef(BaseValidatorModel):
    BackupId: Optional[str] = None
    ServerName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeEventsRequestTypeDef(BaseValidatorModel):
    ServerName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ServerEventTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    ServerName: Optional[str] = None
    Message: Optional[str] = None
    LogUrl: Optional[str] = None


class DescribeNodeAssociationStatusRequestTypeDef(BaseValidatorModel):
    NodeAssociationStatusToken: str
    ServerName: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeServersRequestTypeDef(BaseValidatorModel):
    ServerName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RestoreServerRequestTypeDef(BaseValidatorModel):
    BackupId: str
    ServerName: str
    InstanceType: Optional[str] = None
    KeyPair: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateServerEngineAttributesRequestTypeDef(BaseValidatorModel):
    ServerName: str
    AttributeName: str
    AttributeValue: Optional[str] = None


class UpdateServerRequestTypeDef(BaseValidatorModel):
    ServerName: str
    DisableAutomatedBackup: Optional[bool] = None
    BackupRetentionCount: Optional[int] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None


class AssociateNodeRequestTypeDef(BaseValidatorModel):
    ServerName: str
    NodeName: str
    EngineAttributes: Sequence[EngineAttributeTypeDef]


class DisassociateNodeRequestTypeDef(BaseValidatorModel):
    ServerName: str
    NodeName: str
    EngineAttributes: Optional[Sequence[EngineAttributeTypeDef]] = None


class ExportServerEngineAttributeRequestTypeDef(BaseValidatorModel):
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


class StartMaintenanceRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateBackupRequestTypeDef(BaseValidatorModel):
    ServerName: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateServerRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class DescribeBackupsRequestPaginateTypeDef(BaseValidatorModel):
    BackupId: Optional[str] = None
    ServerName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEventsRequestPaginateTypeDef(BaseValidatorModel):
    ServerName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeServersRequestPaginateTypeDef(BaseValidatorModel):
    ServerName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEventsResponseTypeDef(BaseValidatorModel):
    ServerEvents: List[ServerEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeNodeAssociationStatusRequestWaitTypeDef(BaseValidatorModel):
    NodeAssociationStatusToken: str
    ServerName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class CreateServerResponseTypeDef(BaseValidatorModel):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeServersResponseTypeDef(BaseValidatorModel):
    Servers: List[ServerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


