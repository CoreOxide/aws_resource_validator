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
from aws_resource_validator.pydantic_models.nimble_constants import *

class AcceptEulasRequestRequestTypeDef(BaseModel):
    studioId: str
    clientToken: Optional[str] = None
    eulaIds: Optional[Sequence[str]] = None

class EulaAcceptanceTypeDef(BaseModel):
    acceptedAt: Optional[datetime] = None
    acceptedBy: Optional[str] = None
    accepteeId: Optional[str] = None
    eulaAcceptanceId: Optional[str] = None
    eulaId: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ActiveDirectoryComputerAttributeTypeDef(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class ComputeFarmConfigurationTypeDef(BaseModel):
    activeDirectoryUser: Optional[str] = None
    endpoint: Optional[str] = None

class CreateStreamingImageRequestRequestTypeDef(BaseModel):
    ec2ImageId: str
    name: str
    studioId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateStreamingSessionRequestRequestTypeDef(BaseModel):
    launchProfileId: str
    studioId: str
    clientToken: Optional[str] = None
    ec2InstanceType: Optional[StreamingInstanceTypeType] = None
    ownedBy: Optional[str] = None
    streamingImageId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateStreamingSessionStreamRequestRequestTypeDef(BaseModel):
    sessionId: str
    studioId: str
    clientToken: Optional[str] = None
    expirationInSeconds: Optional[int] = None

class StreamingSessionStreamTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    expiresAt: Optional[datetime] = None
    ownedBy: Optional[str] = None
    state: Optional[StreamingSessionStreamStateType] = None
    statusCode: Optional[StreamingSessionStreamStatusCodeType] = None
    streamId: Optional[str] = None
    url: Optional[str] = None

class ScriptParameterKeyValueTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class StudioComponentInitializationScriptTypeDef(BaseModel):
    launchProfileProtocolVersion: Optional[str] = None
    platform: Optional[LaunchProfilePlatformType] = None
    runContext: Optional[StudioComponentInitializationScriptRunContextType] = None
    script: Optional[str] = None

class StudioEncryptionConfigurationTypeDef(BaseModel):
    keyType: StudioEncryptionConfigurationKeyTypeType
    keyArn: Optional[str] = None

class DeleteLaunchProfileMemberRequestRequestTypeDef(BaseModel):
    launchProfileId: str
    principalId: str
    studioId: str
    clientToken: Optional[str] = None

class DeleteLaunchProfileRequestRequestTypeDef(BaseModel):
    launchProfileId: str
    studioId: str
    clientToken: Optional[str] = None

class DeleteStreamingImageRequestRequestTypeDef(BaseModel):
    streamingImageId: str
    studioId: str
    clientToken: Optional[str] = None

class DeleteStreamingSessionRequestRequestTypeDef(BaseModel):
    sessionId: str
    studioId: str
    clientToken: Optional[str] = None

class DeleteStudioComponentRequestRequestTypeDef(BaseModel):
    studioComponentId: str
    studioId: str
    clientToken: Optional[str] = None

class DeleteStudioMemberRequestRequestTypeDef(BaseModel):
    principalId: str
    studioId: str
    clientToken: Optional[str] = None

class DeleteStudioRequestRequestTypeDef(BaseModel):
    studioId: str
    clientToken: Optional[str] = None

class EulaTypeDef(BaseModel):
    content: Optional[str] = None
    createdAt: Optional[datetime] = None
    eulaId: Optional[str] = None
    name: Optional[str] = None
    updatedAt: Optional[datetime] = None

class GetEulaRequestRequestTypeDef(BaseModel):
    eulaId: str

class GetLaunchProfileDetailsRequestRequestTypeDef(BaseModel):
    launchProfileId: str
    studioId: str

class StudioComponentSummaryTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    studioComponentId: Optional[str] = None
    subtype: Optional[StudioComponentSubtypeType] = None
    type: Optional[StudioComponentTypeType] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class GetLaunchProfileInitializationRequestRequestTypeDef(BaseModel):
    launchProfileId: str
    launchProfileProtocolVersions: Sequence[str]
    launchPurpose: str
    platform: str
    studioId: str

class GetLaunchProfileMemberRequestRequestTypeDef(BaseModel):
    launchProfileId: str
    principalId: str
    studioId: str

class LaunchProfileMembershipTypeDef(BaseModel):
    identityStoreId: Optional[str] = None
    persona: Optional[Literal["USER"]] = None
    principalId: Optional[str] = None
    sid: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetLaunchProfileRequestRequestTypeDef(BaseModel):
    launchProfileId: str
    studioId: str

class GetStreamingImageRequestRequestTypeDef(BaseModel):
    streamingImageId: str
    studioId: str

class GetStreamingSessionBackupRequestRequestTypeDef(BaseModel):
    backupId: str
    studioId: str

class StreamingSessionBackupTypeDef(BaseModel):
    arn: Optional[str] = None
    backupId: Optional[str] = None
    createdAt: Optional[datetime] = None
    launchProfileId: Optional[str] = None
    ownedBy: Optional[str] = None
    sessionId: Optional[str] = None
    state: Optional[StreamingSessionStateType] = None
    statusCode: Optional[StreamingSessionStatusCodeType] = None
    statusMessage: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class GetStreamingSessionRequestRequestTypeDef(BaseModel):
    sessionId: str
    studioId: str

class GetStreamingSessionStreamRequestRequestTypeDef(BaseModel):
    sessionId: str
    streamId: str
    studioId: str

class GetStudioComponentRequestRequestTypeDef(BaseModel):
    studioComponentId: str
    studioId: str

class GetStudioMemberRequestRequestTypeDef(BaseModel):
    principalId: str
    studioId: str

class StudioMembershipTypeDef(BaseModel):
    identityStoreId: Optional[str] = None
    persona: Optional[Literal["ADMINISTRATOR"]] = None
    principalId: Optional[str] = None
    sid: Optional[str] = None

class GetStudioRequestRequestTypeDef(BaseModel):
    studioId: str

class LaunchProfileInitializationScriptTypeDef(BaseModel):
    runtimeRoleArn: Optional[str] = None
    script: Optional[str] = None
    secureInitializationRoleArn: Optional[str] = None
    studioComponentId: Optional[str] = None
    studioComponentName: Optional[str] = None

class ValidationResultTypeDef(BaseModel):
    state: LaunchProfileValidationStateType
    statusCode: LaunchProfileValidationStatusCodeType
    statusMessage: str
    type: LaunchProfileValidationTypeType

class LicenseServiceConfigurationTypeDef(BaseModel):
    endpoint: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListEulaAcceptancesRequestRequestTypeDef(BaseModel):
    studioId: str
    eulaIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None

class ListEulasRequestRequestTypeDef(BaseModel):
    eulaIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None

class ListLaunchProfileMembersRequestRequestTypeDef(BaseModel):
    launchProfileId: str
    studioId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLaunchProfilesRequestRequestTypeDef(BaseModel):
    studioId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    principalId: Optional[str] = None
    states: Optional[Sequence[LaunchProfileStateType]] = None

class ListStreamingImagesRequestRequestTypeDef(BaseModel):
    studioId: str
    nextToken: Optional[str] = None
    owner: Optional[str] = None

class ListStreamingSessionBackupsRequestRequestTypeDef(BaseModel):
    studioId: str
    nextToken: Optional[str] = None
    ownedBy: Optional[str] = None

class ListStreamingSessionsRequestRequestTypeDef(BaseModel):
    studioId: str
    createdBy: Optional[str] = None
    nextToken: Optional[str] = None
    ownedBy: Optional[str] = None
    sessionIds: Optional[str] = None

class ListStudioComponentsRequestRequestTypeDef(BaseModel):
    studioId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    states: Optional[Sequence[StudioComponentStateType]] = None
    types: Optional[Sequence[StudioComponentTypeType]] = None

class ListStudioMembersRequestRequestTypeDef(BaseModel):
    studioId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListStudiosRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class NewLaunchProfileMemberTypeDef(BaseModel):
    persona: Literal["USER"]
    principalId: str

class NewStudioMemberTypeDef(BaseModel):
    persona: Literal["ADMINISTRATOR"]
    principalId: str

class SharedFileSystemConfigurationTypeDef(BaseModel):
    endpoint: Optional[str] = None
    fileSystemId: Optional[str] = None
    linuxMountPoint: Optional[str] = None
    shareName: Optional[str] = None
    windowsMountDrive: Optional[str] = None

class StartStreamingSessionRequestRequestTypeDef(BaseModel):
    sessionId: str
    studioId: str
    backupId: Optional[str] = None
    clientToken: Optional[str] = None

class StartStudioSSOConfigurationRepairRequestRequestTypeDef(BaseModel):
    studioId: str
    clientToken: Optional[str] = None

class StopStreamingSessionRequestRequestTypeDef(BaseModel):
    sessionId: str
    studioId: str
    clientToken: Optional[str] = None
    volumeRetentionMode: Optional[VolumeRetentionModeType] = None

class StreamConfigurationSessionBackupTypeDef(BaseModel):
    maxBackupsToRetain: Optional[int] = None
    mode: Optional[SessionBackupModeType] = None

class VolumeConfigurationTypeDef(BaseModel):
    iops: Optional[int] = None
    size: Optional[int] = None
    throughput: Optional[int] = None

class StreamingSessionStorageRootTypeDef(BaseModel):
    linux: Optional[str] = None
    windows: Optional[str] = None

class StreamingImageEncryptionConfigurationTypeDef(BaseModel):
    keyType: Literal["CUSTOMER_MANAGED_KEY"]
    keyArn: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Optional[Mapping[str, str]] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateLaunchProfileMemberRequestRequestTypeDef(BaseModel):
    launchProfileId: str
    persona: Literal["USER"]
    principalId: str
    studioId: str
    clientToken: Optional[str] = None

class UpdateStreamingImageRequestRequestTypeDef(BaseModel):
    streamingImageId: str
    studioId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None

class UpdateStudioRequestRequestTypeDef(BaseModel):
    studioId: str
    adminRoleArn: Optional[str] = None
    clientToken: Optional[str] = None
    displayName: Optional[str] = None
    userRoleArn: Optional[str] = None

class AcceptEulasResponseTypeDef(BaseModel):
    eulaAcceptances: List[EulaAcceptanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEulaAcceptancesResponseTypeDef(BaseModel):
    eulaAcceptances: List[EulaAcceptanceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ActiveDirectoryConfigurationPaginatorTypeDef(BaseModel):
    computerAttributes: Optional[List[ActiveDirectoryComputerAttributeTypeDef]] = None
    directoryId: Optional[str] = None
    organizationalUnitDistinguishedName: Optional[str] = None

class ActiveDirectoryConfigurationTypeDef(BaseModel):
    computerAttributes: Optional[Sequence[ActiveDirectoryComputerAttributeTypeDef]] = None
    directoryId: Optional[str] = None
    organizationalUnitDistinguishedName: Optional[str] = None

class LaunchProfileInitializationActiveDirectoryTypeDef(BaseModel):
    computerAttributes: Optional[List[ActiveDirectoryComputerAttributeTypeDef]] = None
    directoryId: Optional[str] = None
    directoryName: Optional[str] = None
    dnsIpAddresses: Optional[List[str]] = None
    organizationalUnitDistinguishedName: Optional[str] = None
    studioComponentId: Optional[str] = None
    studioComponentName: Optional[str] = None

class CreateStreamingSessionStreamResponseTypeDef(BaseModel):
    stream: StreamingSessionStreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamingSessionStreamResponseTypeDef(BaseModel):
    stream: StreamingSessionStreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStudioRequestRequestTypeDef(BaseModel):
    adminRoleArn: str
    displayName: str
    studioName: str
    userRoleArn: str
    clientToken: Optional[str] = None
    studioEncryptionConfiguration: Optional[StudioEncryptionConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class StudioTypeDef(BaseModel):
    adminRoleArn: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    displayName: Optional[str] = None
    homeRegion: Optional[str] = None
    ssoClientId: Optional[str] = None
    state: Optional[StudioStateType] = None
    statusCode: Optional[StudioStatusCodeType] = None
    statusMessage: Optional[str] = None
    studioEncryptionConfiguration: Optional[StudioEncryptionConfigurationTypeDef] = None
    studioId: Optional[str] = None
    studioName: Optional[str] = None
    studioUrl: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    updatedAt: Optional[datetime] = None
    userRoleArn: Optional[str] = None

class GetEulaResponseTypeDef(BaseModel):
    eula: EulaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEulasResponseTypeDef(BaseModel):
    eulas: List[EulaTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLaunchProfileMemberResponseTypeDef(BaseModel):
    member: LaunchProfileMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLaunchProfileMembersResponseTypeDef(BaseModel):
    members: List[LaunchProfileMembershipTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLaunchProfileMemberResponseTypeDef(BaseModel):
    member: LaunchProfileMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLaunchProfileRequestLaunchProfileDeletedWaitTypeDef(BaseModel):
    launchProfileId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetLaunchProfileRequestLaunchProfileReadyWaitTypeDef(BaseModel):
    launchProfileId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingImageRequestStreamingImageDeletedWaitTypeDef(BaseModel):
    streamingImageId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingImageRequestStreamingImageReadyWaitTypeDef(BaseModel):
    streamingImageId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingSessionRequestStreamingSessionDeletedWaitTypeDef(BaseModel):
    sessionId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingSessionRequestStreamingSessionReadyWaitTypeDef(BaseModel):
    sessionId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingSessionRequestStreamingSessionStoppedWaitTypeDef(BaseModel):
    sessionId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingSessionStreamRequestStreamingSessionStreamReadyWaitTypeDef(BaseModel):
    sessionId: str
    streamId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStudioComponentRequestStudioComponentDeletedWaitTypeDef(BaseModel):
    studioComponentId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStudioComponentRequestStudioComponentReadyWaitTypeDef(BaseModel):
    studioComponentId: str
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStudioRequestStudioDeletedWaitTypeDef(BaseModel):
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStudioRequestStudioReadyWaitTypeDef(BaseModel):
    studioId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetStreamingSessionBackupResponseTypeDef(BaseModel):
    streamingSessionBackup: StreamingSessionBackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamingSessionBackupsResponseTypeDef(BaseModel):
    nextToken: str
    streamingSessionBackups: List[StreamingSessionBackupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetStudioMemberResponseTypeDef(BaseModel):
    member: StudioMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStudioMembersResponseTypeDef(BaseModel):
    members: List[StudioMembershipTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEulaAcceptancesRequestListEulaAcceptancesPaginateTypeDef(BaseModel):
    studioId: str
    eulaIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEulasRequestListEulasPaginateTypeDef(BaseModel):
    eulaIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLaunchProfileMembersRequestListLaunchProfileMembersPaginateTypeDef(BaseModel):
    launchProfileId: str
    studioId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLaunchProfilesRequestListLaunchProfilesPaginateTypeDef(BaseModel):
    studioId: str
    principalId: Optional[str] = None
    states: Optional[Sequence[LaunchProfileStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamingImagesRequestListStreamingImagesPaginateTypeDef(BaseModel):
    studioId: str
    owner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamingSessionBackupsRequestListStreamingSessionBackupsPaginateTypeDef(BaseModel):
    studioId: str
    ownedBy: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamingSessionsRequestListStreamingSessionsPaginateTypeDef(BaseModel):
    studioId: str
    createdBy: Optional[str] = None
    ownedBy: Optional[str] = None
    sessionIds: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStudioComponentsRequestListStudioComponentsPaginateTypeDef(BaseModel):
    studioId: str
    states: Optional[Sequence[StudioComponentStateType]] = None
    types: Optional[Sequence[StudioComponentTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStudioMembersRequestListStudioMembersPaginateTypeDef(BaseModel):
    studioId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStudiosRequestListStudiosPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class PutLaunchProfileMembersRequestRequestTypeDef(BaseModel):
    identityStoreId: str
    launchProfileId: str
    members: Sequence[NewLaunchProfileMemberTypeDef]
    studioId: str
    clientToken: Optional[str] = None

class PutStudioMembersRequestRequestTypeDef(BaseModel):
    identityStoreId: str
    members: Sequence[NewStudioMemberTypeDef]
    studioId: str
    clientToken: Optional[str] = None

class StreamingSessionTypeDef(BaseModel):
    arn: Optional[str] = None
    automaticTerminationMode: Optional[AutomaticTerminationModeType] = None
    backupMode: Optional[SessionBackupModeType] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    ec2InstanceType: Optional[str] = None
    launchProfileId: Optional[str] = None
    maxBackupsToRetain: Optional[int] = None
    ownedBy: Optional[str] = None
    sessionId: Optional[str] = None
    sessionPersistenceMode: Optional[SessionPersistenceModeType] = None
    startedAt: Optional[datetime] = None
    startedBy: Optional[str] = None
    startedFromBackupId: Optional[str] = None
    state: Optional[StreamingSessionStateType] = None
    statusCode: Optional[StreamingSessionStatusCodeType] = None
    statusMessage: Optional[str] = None
    stopAt: Optional[datetime] = None
    stoppedAt: Optional[datetime] = None
    stoppedBy: Optional[str] = None
    streamingImageId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    terminateAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    volumeConfiguration: Optional[VolumeConfigurationTypeDef] = None
    volumeRetentionMode: Optional[VolumeRetentionModeType] = None

class StreamConfigurationSessionStoragePaginatorTypeDef(BaseModel):
    mode: List[Literal["UPLOAD"]]
    root: Optional[StreamingSessionStorageRootTypeDef] = None

class StreamConfigurationSessionStorageTypeDef(BaseModel):
    mode: Sequence[Literal["UPLOAD"]]
    root: Optional[StreamingSessionStorageRootTypeDef] = None

class StreamingImageTypeDef(BaseModel):
    arn: Optional[str] = None
    description: Optional[str] = None
    ec2ImageId: Optional[str] = None
    encryptionConfiguration: Optional[StreamingImageEncryptionConfigurationTypeDef] = None
    eulaIds: Optional[List[str]] = None
    name: Optional[str] = None
    owner: Optional[str] = None
    platform: Optional[str] = None
    state: Optional[StreamingImageStateType] = None
    statusCode: Optional[StreamingImageStatusCodeType] = None
    statusMessage: Optional[str] = None
    streamingImageId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class StudioComponentConfigurationPaginatorTypeDef(BaseModel):
    activeDirectoryConfiguration: Optional[ActiveDirectoryConfigurationPaginatorTypeDef] = None
    computeFarmConfiguration: Optional[ComputeFarmConfigurationTypeDef] = None
    licenseServiceConfiguration: Optional[LicenseServiceConfigurationTypeDef] = None
    sharedFileSystemConfiguration: Optional[SharedFileSystemConfigurationTypeDef] = None

class StudioComponentConfigurationTypeDef(BaseModel):
    activeDirectoryConfiguration: Optional[ActiveDirectoryConfigurationTypeDef] = None
    computeFarmConfiguration: Optional[ComputeFarmConfigurationTypeDef] = None
    licenseServiceConfiguration: Optional[LicenseServiceConfigurationTypeDef] = None
    sharedFileSystemConfiguration: Optional[SharedFileSystemConfigurationTypeDef] = None

class LaunchProfileInitializationTypeDef(BaseModel):
    activeDirectory: Optional[LaunchProfileInitializationActiveDirectoryTypeDef] = None
    ec2SecurityGroupIds: Optional[List[str]] = None
    launchProfileId: Optional[str] = None
    launchProfileProtocolVersion: Optional[str] = None
    launchPurpose: Optional[str] = None
    name: Optional[str] = None
    platform: Optional[LaunchProfilePlatformType] = None
    systemInitializationScripts: Optional[List[LaunchProfileInitializationScriptTypeDef]] = None
    userInitializationScripts: Optional[List[LaunchProfileInitializationScriptTypeDef]] = None

class CreateStudioResponseTypeDef(BaseModel):
    studio: StudioTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteStudioResponseTypeDef(BaseModel):
    studio: StudioTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStudioResponseTypeDef(BaseModel):
    studio: StudioTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStudiosResponseTypeDef(BaseModel):
    nextToken: str
    studios: List[StudioTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartStudioSSOConfigurationRepairResponseTypeDef(BaseModel):
    studio: StudioTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStudioResponseTypeDef(BaseModel):
    studio: StudioTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamingSessionResponseTypeDef(BaseModel):
    session: StreamingSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteStreamingSessionResponseTypeDef(BaseModel):
    session: StreamingSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamingSessionResponseTypeDef(BaseModel):
    session: StreamingSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamingSessionsResponseTypeDef(BaseModel):
    nextToken: str
    sessions: List[StreamingSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartStreamingSessionResponseTypeDef(BaseModel):
    session: StreamingSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopStreamingSessionResponseTypeDef(BaseModel):
    session: StreamingSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StreamConfigurationPaginatorTypeDef(BaseModel):
    clipboardMode: StreamingClipboardModeType
    ec2InstanceTypes: List[StreamingInstanceTypeType]
    streamingImageIds: List[str]
    automaticTerminationMode: Optional[AutomaticTerminationModeType] = None
    maxSessionLengthInMinutes: Optional[int] = None
    maxStoppedSessionLengthInMinutes: Optional[int] = None
    sessionBackup: Optional[StreamConfigurationSessionBackupTypeDef] = None
    sessionPersistenceMode: Optional[SessionPersistenceModeType] = None
    sessionStorage: Optional[StreamConfigurationSessionStoragePaginatorTypeDef] = None
    volumeConfiguration: Optional[VolumeConfigurationTypeDef] = None

class StreamConfigurationCreateTypeDef(BaseModel):
    clipboardMode: StreamingClipboardModeType
    ec2InstanceTypes: Sequence[StreamingInstanceTypeType]
    streamingImageIds: Sequence[str]
    automaticTerminationMode: Optional[AutomaticTerminationModeType] = None
    maxSessionLengthInMinutes: Optional[int] = None
    maxStoppedSessionLengthInMinutes: Optional[int] = None
    sessionBackup: Optional[StreamConfigurationSessionBackupTypeDef] = None
    sessionPersistenceMode: Optional[SessionPersistenceModeType] = None
    sessionStorage: Optional[StreamConfigurationSessionStorageTypeDef] = None
    volumeConfiguration: Optional[VolumeConfigurationTypeDef] = None

class StreamConfigurationTypeDef(BaseModel):
    clipboardMode: StreamingClipboardModeType
    ec2InstanceTypes: List[StreamingInstanceTypeType]
    streamingImageIds: List[str]
    automaticTerminationMode: Optional[AutomaticTerminationModeType] = None
    maxSessionLengthInMinutes: Optional[int] = None
    maxStoppedSessionLengthInMinutes: Optional[int] = None
    sessionBackup: Optional[StreamConfigurationSessionBackupTypeDef] = None
    sessionPersistenceMode: Optional[SessionPersistenceModeType] = None
    sessionStorage: Optional[StreamConfigurationSessionStorageTypeDef] = None
    volumeConfiguration: Optional[VolumeConfigurationTypeDef] = None

class CreateStreamingImageResponseTypeDef(BaseModel):
    streamingImage: StreamingImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteStreamingImageResponseTypeDef(BaseModel):
    streamingImage: StreamingImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamingImageResponseTypeDef(BaseModel):
    streamingImage: StreamingImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamingImagesResponseTypeDef(BaseModel):
    nextToken: str
    streamingImages: List[StreamingImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStreamingImageResponseTypeDef(BaseModel):
    streamingImage: StreamingImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StudioComponentPaginatorTypeDef(BaseModel):
    arn: Optional[str] = None
    configuration: Optional[StudioComponentConfigurationPaginatorTypeDef] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    ec2SecurityGroupIds: Optional[List[str]] = None
    initializationScripts: Optional[List[StudioComponentInitializationScriptTypeDef]] = None
    name: Optional[str] = None
    runtimeRoleArn: Optional[str] = None
    scriptParameters: Optional[List[ScriptParameterKeyValueTypeDef]] = None
    secureInitializationRoleArn: Optional[str] = None
    state: Optional[StudioComponentStateType] = None
    statusCode: Optional[StudioComponentStatusCodeType] = None
    statusMessage: Optional[str] = None
    studioComponentId: Optional[str] = None
    subtype: Optional[StudioComponentSubtypeType] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[StudioComponentTypeType] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class CreateStudioComponentRequestRequestTypeDef(BaseModel):
    name: str
    studioId: str
    type: StudioComponentTypeType
    clientToken: Optional[str] = None
    configuration: Optional[StudioComponentConfigurationTypeDef] = None
    description: Optional[str] = None
    ec2SecurityGroupIds: Optional[Sequence[str]] = None
    initializationScripts: Optional[Sequence[StudioComponentInitializationScriptTypeDef]] = None
    runtimeRoleArn: Optional[str] = None
    scriptParameters: Optional[Sequence[ScriptParameterKeyValueTypeDef]] = None
    secureInitializationRoleArn: Optional[str] = None
    subtype: Optional[StudioComponentSubtypeType] = None
    tags: Optional[Mapping[str, str]] = None

class StudioComponentTypeDef(BaseModel):
    arn: Optional[str] = None
    configuration: Optional[StudioComponentConfigurationTypeDef] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    ec2SecurityGroupIds: Optional[List[str]] = None
    initializationScripts: Optional[List[StudioComponentInitializationScriptTypeDef]] = None
    name: Optional[str] = None
    runtimeRoleArn: Optional[str] = None
    scriptParameters: Optional[List[ScriptParameterKeyValueTypeDef]] = None
    secureInitializationRoleArn: Optional[str] = None
    state: Optional[StudioComponentStateType] = None
    statusCode: Optional[StudioComponentStatusCodeType] = None
    statusMessage: Optional[str] = None
    studioComponentId: Optional[str] = None
    subtype: Optional[StudioComponentSubtypeType] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[StudioComponentTypeType] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class UpdateStudioComponentRequestRequestTypeDef(BaseModel):
    studioComponentId: str
    studioId: str
    clientToken: Optional[str] = None
    configuration: Optional[StudioComponentConfigurationTypeDef] = None
    description: Optional[str] = None
    ec2SecurityGroupIds: Optional[Sequence[str]] = None
    initializationScripts: Optional[Sequence[StudioComponentInitializationScriptTypeDef]] = None
    name: Optional[str] = None
    runtimeRoleArn: Optional[str] = None
    scriptParameters: Optional[Sequence[ScriptParameterKeyValueTypeDef]] = None
    secureInitializationRoleArn: Optional[str] = None
    subtype: Optional[StudioComponentSubtypeType] = None
    type: Optional[StudioComponentTypeType] = None

class GetLaunchProfileInitializationResponseTypeDef(BaseModel):
    launchProfileInitialization: LaunchProfileInitializationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LaunchProfilePaginatorTypeDef(BaseModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    ec2SubnetIds: Optional[List[str]] = None
    launchProfileId: Optional[str] = None
    launchProfileProtocolVersions: Optional[List[str]] = None
    name: Optional[str] = None
    state: Optional[LaunchProfileStateType] = None
    statusCode: Optional[LaunchProfileStatusCodeType] = None
    statusMessage: Optional[str] = None
    streamConfiguration: Optional[StreamConfigurationPaginatorTypeDef] = None
    studioComponentIds: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    validationResults: Optional[List[ValidationResultTypeDef]] = None

class CreateLaunchProfileRequestRequestTypeDef(BaseModel):
    ec2SubnetIds: Sequence[str]
    launchProfileProtocolVersions: Sequence[str]
    name: str
    streamConfiguration: StreamConfigurationCreateTypeDef
    studioComponentIds: Sequence[str]
    studioId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateLaunchProfileRequestRequestTypeDef(BaseModel):
    launchProfileId: str
    studioId: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    launchProfileProtocolVersions: Optional[Sequence[str]] = None
    name: Optional[str] = None
    streamConfiguration: Optional[StreamConfigurationCreateTypeDef] = None
    studioComponentIds: Optional[Sequence[str]] = None

class LaunchProfileTypeDef(BaseModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    ec2SubnetIds: Optional[List[str]] = None
    launchProfileId: Optional[str] = None
    launchProfileProtocolVersions: Optional[List[str]] = None
    name: Optional[str] = None
    state: Optional[LaunchProfileStateType] = None
    statusCode: Optional[LaunchProfileStatusCodeType] = None
    statusMessage: Optional[str] = None
    streamConfiguration: Optional[StreamConfigurationTypeDef] = None
    studioComponentIds: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None
    validationResults: Optional[List[ValidationResultTypeDef]] = None

class ListStudioComponentsResponsePaginatorTypeDef(BaseModel):
    nextToken: str
    studioComponents: List[StudioComponentPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStudioComponentResponseTypeDef(BaseModel):
    studioComponent: StudioComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteStudioComponentResponseTypeDef(BaseModel):
    studioComponent: StudioComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStudioComponentResponseTypeDef(BaseModel):
    studioComponent: StudioComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStudioComponentsResponseTypeDef(BaseModel):
    nextToken: str
    studioComponents: List[StudioComponentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStudioComponentResponseTypeDef(BaseModel):
    studioComponent: StudioComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLaunchProfilesResponsePaginatorTypeDef(BaseModel):
    launchProfiles: List[LaunchProfilePaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLaunchProfileResponseTypeDef(BaseModel):
    launchProfile: LaunchProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLaunchProfileResponseTypeDef(BaseModel):
    launchProfile: LaunchProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLaunchProfileDetailsResponseTypeDef(BaseModel):
    launchProfile: LaunchProfileTypeDef
    streamingImages: List[StreamingImageTypeDef]
    studioComponentSummaries: List[StudioComponentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLaunchProfileResponseTypeDef(BaseModel):
    launchProfile: LaunchProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLaunchProfilesResponseTypeDef(BaseModel):
    launchProfiles: List[LaunchProfileTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLaunchProfileResponseTypeDef(BaseModel):
    launchProfile: LaunchProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

