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


# This class is the input for the 'describe_backups' function.
class DescribeBackupsRequest(BaseValidatorModel):
    BackupId: Optional[str] = None
    ServerName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_events' function.
class DescribeEventsRequest(BaseValidatorModel):
    ServerName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ServerEvent(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    ServerName: Optional[str] = None
    Message: Optional[str] = None
    LogUrl: Optional[str] = None


# This class is the input for the 'describe_node_association_status' function.
class DescribeNodeAssociationStatusRequest(BaseValidatorModel):
    NodeAssociationStatusToken: str
    ServerName: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_servers' function.
class DescribeServersRequest(BaseValidatorModel):
    ServerName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'restore_server' function.
class RestoreServerRequest(BaseValidatorModel):
    BackupId: str
    ServerName: str
    InstanceType: Optional[str] = None
    KeyPair: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_server_engine_attributes' function.
class UpdateServerEngineAttributesRequest(BaseValidatorModel):
    ServerName: str
    AttributeName: str
    AttributeValue: Optional[str] = None


# This class is the input for the 'update_server' function.
class UpdateServerRequest(BaseValidatorModel):
    ServerName: str
    DisableAutomatedBackup: Optional[bool] = None
    BackupRetentionCount: Optional[int] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None


# This class is the input for the 'associate_node' function.
class AssociateNodeRequest(BaseValidatorModel):
    ServerName: str
    NodeName: str
    EngineAttributes: List[EngineAttribute]


# This class is the input for the 'disassociate_node' function.
class DisassociateNodeRequest(BaseValidatorModel):
    ServerName: str
    NodeName: str
    EngineAttributes: Optional[List[EngineAttribute]] = None


# This class is the input for the 'export_server_engine_attribute' function.
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


# This class is the input for the 'start_maintenance' function.
class StartMaintenanceRequest(BaseValidatorModel):
    ServerName: str
    EngineAttributes: Optional[List[EngineAttribute]] = None


# This class is the output for the 'associate_node' function.
class AssociateNodeResponse(BaseValidatorModel):
    NodeAssociationStatusToken: str
    ResponseMetadata: ResponseMetadata


class DescribeAccountAttributesResponse(BaseValidatorModel):
    Attributes: List[AccountAttribute]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_node_association_status' function.
class DescribeNodeAssociationStatusResponse(BaseValidatorModel):
    NodeAssociationStatus: NodeAssociationStatusType
    EngineAttributes: List[EngineAttribute]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_node' function.
class DisassociateNodeResponse(BaseValidatorModel):
    NodeAssociationStatusToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_server_engine_attribute' function.
class ExportServerEngineAttributeResponse(BaseValidatorModel):
    EngineAttribute: EngineAttribute
    ServerName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_backup' function.
class CreateBackupResponse(BaseValidatorModel):
    Backup: Backup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_backups' function.
class DescribeBackupsResponse(BaseValidatorModel):
    Backups: List[Backup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_backup' function.
class CreateBackupRequest(BaseValidatorModel):
    ServerName: str
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_server' function.
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


# This class is the output for the 'list_tags_for_resource' function.
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


# This class is the output for the 'describe_events' function.
class DescribeEventsResponse(BaseValidatorModel):
    ServerEvents: List[ServerEvent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeNodeAssociationStatusRequestWait(BaseValidatorModel):
    NodeAssociationStatusToken: str
    ServerName: str
    WaiterConfig: Optional[WaiterConfig] = None


# This class is the output for the 'create_server' function.
class CreateServerResponse(BaseValidatorModel):
    Server: Server
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_servers' function.
class DescribeServersResponse(BaseValidatorModel):
    Servers: List[Server]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'restore_server' function.
class RestoreServerResponse(BaseValidatorModel):
    Server: Server
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_maintenance' function.
class StartMaintenanceResponse(BaseValidatorModel):
    Server: Server
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_server_engine_attributes' function.
class UpdateServerEngineAttributesResponse(BaseValidatorModel):
    Server: Server
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_server' function.
class UpdateServerResponse(BaseValidatorModel):
    Server: Server
    ResponseMetadata: ResponseMetadata