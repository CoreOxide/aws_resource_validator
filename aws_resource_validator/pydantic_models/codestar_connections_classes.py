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
from aws_resource_validator.pydantic_models.codestar_connections_constants import *

class ConnectionTypeDef(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    ConnectionArn: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    OwnerAccountId: Optional[str] = None
    ConnectionStatus: Optional[ConnectionStatusType] = None
    HostArn: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class VpcConfigurationTypeDef(BaseValidatorModel):
    VpcId: str
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]
    TlsCertificate: Optional[str] = None

class RepositoryLinkInfoTypeDef(BaseValidatorModel):
    ConnectionArn: str
    OwnerId: str
    ProviderType: ProviderTypeType
    RepositoryLinkArn: str
    RepositoryLinkId: str
    RepositoryName: str
    EncryptionKeyArn: Optional[str] = None

class CreateSyncConfigurationInputRequestTypeDef(BaseValidatorModel):
    Branch: str
    ConfigFile: str
    RepositoryLinkId: str
    ResourceName: str
    RoleArn: str
    SyncType: Literal["CFN_STACK_SYNC"]
    PublishDeploymentStatus: Optional[PublishDeploymentStatusType] = None
    TriggerResourceUpdateOn: Optional[TriggerResourceUpdateOnType] = None

class SyncConfigurationTypeDef(BaseValidatorModel):
    Branch: str
    OwnerId: str
    ProviderType: ProviderTypeType
    RepositoryLinkId: str
    RepositoryName: str
    ResourceName: str
    RoleArn: str
    SyncType: Literal["CFN_STACK_SYNC"]
    ConfigFile: Optional[str] = None
    PublishDeploymentStatus: Optional[PublishDeploymentStatusType] = None
    TriggerResourceUpdateOn: Optional[TriggerResourceUpdateOnType] = None

class DeleteConnectionInputRequestTypeDef(BaseValidatorModel):
    ConnectionArn: str

class DeleteHostInputRequestTypeDef(BaseValidatorModel):
    HostArn: str

class DeleteRepositoryLinkInputRequestTypeDef(BaseValidatorModel):
    RepositoryLinkId: str

class DeleteSyncConfigurationInputRequestTypeDef(BaseValidatorModel):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str

class GetConnectionInputRequestTypeDef(BaseValidatorModel):
    ConnectionArn: str

class GetHostInputRequestTypeDef(BaseValidatorModel):
    HostArn: str

class GetRepositoryLinkInputRequestTypeDef(BaseValidatorModel):
    RepositoryLinkId: str

class GetRepositorySyncStatusInputRequestTypeDef(BaseValidatorModel):
    Branch: str
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]

class GetResourceSyncStatusInputRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    SyncType: Literal["CFN_STACK_SYNC"]

class RevisionTypeDef(BaseValidatorModel):
    Branch: str
    Directory: str
    OwnerId: str
    RepositoryName: str
    ProviderType: ProviderTypeType
    Sha: str

class GetSyncBlockerSummaryInputRequestTypeDef(BaseValidatorModel):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str

class GetSyncConfigurationInputRequestTypeDef(BaseValidatorModel):
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str

class ListConnectionsInputRequestTypeDef(BaseValidatorModel):
    ProviderTypeFilter: Optional[ProviderTypeType] = None
    HostArnFilter: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListHostsInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRepositoryLinksInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRepositorySyncDefinitionsInputRequestTypeDef(BaseValidatorModel):
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]

class RepositorySyncDefinitionTypeDef(BaseValidatorModel):
    Branch: str
    Directory: str
    Parent: str
    Target: str

class ListSyncConfigurationsInputRequestTypeDef(BaseValidatorModel):
    RepositoryLinkId: str
    SyncType: Literal["CFN_STACK_SYNC"]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class RepositorySyncEventTypeDef(BaseValidatorModel):
    Event: str
    Time: datetime
    Type: str
    ExternalId: Optional[str] = None

class ResourceSyncEventTypeDef(BaseValidatorModel):
    Event: str
    Time: datetime
    Type: str
    ExternalId: Optional[str] = None

class SyncBlockerContextTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateRepositoryLinkInputRequestTypeDef(BaseValidatorModel):
    RepositoryLinkId: str
    ConnectionArn: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None

class UpdateSyncBlockerInputRequestTypeDef(BaseValidatorModel):
    Id: str
    SyncType: Literal["CFN_STACK_SYNC"]
    ResourceName: str
    ResolvedReason: str

class UpdateSyncConfigurationInputRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    SyncType: Literal["CFN_STACK_SYNC"]
    Branch: Optional[str] = None
    ConfigFile: Optional[str] = None
    RepositoryLinkId: Optional[str] = None
    RoleArn: Optional[str] = None
    PublishDeploymentStatus: Optional[PublishDeploymentStatusType] = None
    TriggerResourceUpdateOn: Optional[TriggerResourceUpdateOnType] = None

class CreateConnectionInputRequestTypeDef(BaseValidatorModel):
    ConnectionName: str
    ProviderType: Optional[ProviderTypeType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    HostArn: Optional[str] = None

class CreateRepositoryLinkInputRequestTypeDef(BaseValidatorModel):
    ConnectionArn: str
    OwnerId: str
    RepositoryName: str
    EncryptionKeyArn: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateConnectionOutputTypeDef(BaseValidatorModel):
    ConnectionArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHostOutputTypeDef(BaseValidatorModel):
    HostArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionOutputTypeDef(BaseValidatorModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectionsOutputTypeDef(BaseValidatorModel):
    Connections: List[ConnectionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHostInputRequestTypeDef(BaseValidatorModel):
    Name: str
    ProviderType: ProviderTypeType
    ProviderEndpoint: str
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class GetHostOutputTypeDef(BaseValidatorModel):
    Name: str
    Status: str
    ProviderType: ProviderTypeType
    ProviderEndpoint: str
    VpcConfiguration: VpcConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HostTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    HostArn: Optional[str] = None
    ProviderType: Optional[ProviderTypeType] = None
    ProviderEndpoint: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None

class UpdateHostInputRequestTypeDef(BaseValidatorModel):
    HostArn: str
    ProviderEndpoint: Optional[str] = None
    VpcConfiguration: Optional[VpcConfigurationTypeDef] = None

class CreateRepositoryLinkOutputTypeDef(BaseValidatorModel):
    RepositoryLinkInfo: RepositoryLinkInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositoryLinkOutputTypeDef(BaseValidatorModel):
    RepositoryLinkInfo: RepositoryLinkInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositoryLinksOutputTypeDef(BaseValidatorModel):
    RepositoryLinks: List[RepositoryLinkInfoTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRepositoryLinkOutputTypeDef(BaseValidatorModel):
    RepositoryLinkInfo: RepositoryLinkInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSyncConfigurationOutputTypeDef(BaseValidatorModel):
    SyncConfiguration: SyncConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSyncConfigurationOutputTypeDef(BaseValidatorModel):
    SyncConfiguration: SyncConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSyncConfigurationsOutputTypeDef(BaseValidatorModel):
    SyncConfigurations: List[SyncConfigurationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSyncConfigurationOutputTypeDef(BaseValidatorModel):
    SyncConfiguration: SyncConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositorySyncDefinitionsOutputTypeDef(BaseValidatorModel):
    RepositorySyncDefinitions: List[RepositorySyncDefinitionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RepositorySyncAttemptTypeDef(BaseValidatorModel):
    StartedAt: datetime
    Status: RepositorySyncStatusType
    Events: List[RepositorySyncEventTypeDef]

class ResourceSyncAttemptTypeDef(BaseValidatorModel):
    Events: List[ResourceSyncEventTypeDef]
    InitialRevision: RevisionTypeDef
    StartedAt: datetime
    Status: ResourceSyncStatusType
    TargetRevision: RevisionTypeDef
    Target: str

class SyncBlockerTypeDef(BaseValidatorModel):
    Id: str
    Type: Literal["AUTOMATED"]
    Status: BlockerStatusType
    CreatedReason: str
    CreatedAt: datetime
    Contexts: Optional[List[SyncBlockerContextTypeDef]] = None
    ResolvedReason: Optional[str] = None
    ResolvedAt: Optional[datetime] = None

class ListHostsOutputTypeDef(BaseValidatorModel):
    Hosts: List[HostTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositorySyncStatusOutputTypeDef(BaseValidatorModel):
    LatestSync: RepositorySyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceSyncStatusOutputTypeDef(BaseValidatorModel):
    DesiredState: RevisionTypeDef
    LatestSuccessfulSync: ResourceSyncAttemptTypeDef
    LatestSync: ResourceSyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SyncBlockerSummaryTypeDef(BaseValidatorModel):
    ResourceName: str
    ParentResourceName: Optional[str] = None
    LatestBlockers: Optional[List[SyncBlockerTypeDef]] = None

class UpdateSyncBlockerOutputTypeDef(BaseValidatorModel):
    ResourceName: str
    ParentResourceName: str
    SyncBlocker: SyncBlockerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSyncBlockerSummaryOutputTypeDef(BaseValidatorModel):
    SyncBlockerSummary: SyncBlockerSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

