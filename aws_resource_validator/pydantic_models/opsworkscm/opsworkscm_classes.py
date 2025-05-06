from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.opsworkscm.opsworkscm_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountAttribute(BaseValidatorModel):
    Name: Optional[str] = None
    Maximum: Optional[int] = None
    Used: Optional[int] = None


class EngineAttribute(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Backup(BaseValidatorModel):
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


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class DeleteBackupRequest(BaseValidatorModel):
    BackupId: str


class DeleteServerRequest(BaseValidatorModel):
    ServerName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeBackupsRequest(BaseValidatorModel):
    BackupId: Optional[str] = None
    ServerName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeEventsRequest(BaseValidatorModel):
    ServerName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ServerEvent(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    ServerName: Optional[str] = None
    Message: Optional[str] = None
    LogUrl: Optional[str] = None


class DescribeNodeAssociationStatusRequest(BaseValidatorModel):
    NodeAssociationStatusToken: str
    ServerName: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeServersRequest(BaseValidatorModel):
    ServerName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RestoreServerRequest(BaseValidatorModel):
    BackupId: str
    ServerName: str
    InstanceType: Optional[str] = None
    KeyPair: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateServerEngineAttributesRequest(BaseValidatorModel):
    ServerName: str
    AttributeName: str
    AttributeValue: Optional[str] = None


class UpdateServerRequest(BaseValidatorModel):
    ServerName: str
    DisableAutomatedBackup: Optional[bool] = None
    BackupRetentionCount: Optional[int] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None


class AssociateNodeRequest(BaseValidatorModel):
    ServerName: str
    NodeName: str
    EngineAttributes: List[EngineAttribute]


class DisassociateNodeRequest(BaseValidatorModel):
    ServerName: str
    NodeName: str
    EngineAttributes: Optional[List[EngineAttribute]] = None


class ExportServerEngineAttributeRequest(BaseValidatorModel):
    ExportAttributeName: str
    ServerName: str
    InputAttributes: Optional[List[EngineAttribute]] = None


class Server(BaseValidatorModel):
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
    EngineAttributes: Optional[List[EngineAttribute]] = None
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


class StartMaintenanceRequest(BaseValidatorModel):
    ServerName: str
    EngineAttributes: Optional[List[EngineAttribute]] = None


class AssociateNodeResponse(BaseValidatorModel):
    NodeAssociationStatusToken: str
    ResponseMetadata: ResponseMetadata


class DescribeAccountAttributesResponse(BaseValidatorModel):
    Attributes: List[AccountAttribute]
    ResponseMetadata: ResponseMetadata


class DescribeNodeAssociationStatusResponse(BaseValidatorModel):
    NodeAssociationStatus: NodeAssociationStatusType
    EngineAttributes: List[EngineAttribute]
    ResponseMetadata: ResponseMetadata


class DisassociateNodeResponse(BaseValidatorModel):
    NodeAssociationStatusToken: str
    ResponseMetadata: ResponseMetadata


class ExportServerEngineAttributeResponse(BaseValidatorModel):
    EngineAttribute: EngineAttribute
    ServerName: str
    ResponseMetadata: ResponseMetadata


class CreateBackupResponse(BaseValidatorModel):
    Backup: Backup
    ResponseMetadata: ResponseMetadata


class DescribeBackupsResponse(BaseValidatorModel):
    Backups: List[Backup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateBackupRequest(BaseValidatorModel):
    ServerName: str
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreateServerRequest(BaseValidatorModel):
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
    EngineAttributes: Optional[List[EngineAttribute]] = None
    BackupRetentionCount: Optional[int] = None
    KeyPair: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    BackupId: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class DescribeBackupsRequestPaginate(BaseValidatorModel):
    BackupId: Optional[str] = None
    ServerName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventsRequestPaginate(BaseValidatorModel):
    ServerName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeServersRequestPaginate(BaseValidatorModel):
    ServerName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventsResponse(BaseValidatorModel):
    ServerEvents: List[ServerEvent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeNodeAssociationStatusRequestWait(BaseValidatorModel):
    NodeAssociationStatusToken: str
    ServerName: str
    WaiterConfig: Optional[WaiterConfig] = None


class CreateServerResponse(BaseValidatorModel):
    Server: Server
    ResponseMetadata: ResponseMetadata


class DescribeServersResponse(BaseValidatorModel):
    Servers: List[Server]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RestoreServerResponse(BaseValidatorModel):
    Server: Server
    ResponseMetadata: ResponseMetadata


class StartMaintenanceResponse(BaseValidatorModel):
    Server: Server
    ResponseMetadata: ResponseMetadata


class UpdateServerEngineAttributesResponse(BaseValidatorModel):
    Server: Server
    ResponseMetadata: ResponseMetadata


class UpdateServerResponse(BaseValidatorModel):
    Server: Server
    ResponseMetadata: ResponseMetadata