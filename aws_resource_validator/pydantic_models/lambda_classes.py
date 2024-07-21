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
from aws_resource_validator.pydantic_models.lambda_constants import *

class AccountLimitTypeDef(BaseModel):
    TotalCodeSize: Optional[int] = None
    CodeSizeUnzipped: Optional[int] = None
    CodeSizeZipped: Optional[int] = None
    ConcurrentExecutions: Optional[int] = None
    UnreservedConcurrentExecutions: Optional[int] = None

class AccountUsageTypeDef(BaseModel):
    TotalCodeSize: Optional[int] = None
    FunctionCount: Optional[int] = None

class AddLayerVersionPermissionRequestRequestTypeDef(BaseModel):
    LayerName: str
    VersionNumber: int
    StatementId: str
    Action: str
    Principal: str
    OrganizationId: Optional[str] = None
    RevisionId: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AddPermissionRequestRequestTypeDef(BaseModel):
    FunctionName: str
    StatementId: str
    Action: str
    Principal: str
    SourceArn: Optional[str] = None
    SourceAccount: Optional[str] = None
    EventSourceToken: Optional[str] = None
    Qualifier: Optional[str] = None
    RevisionId: Optional[str] = None
    PrincipalOrgID: Optional[str] = None
    FunctionUrlAuthType: Optional[FunctionUrlAuthTypeType] = None

class AliasRoutingConfigurationPaginatorTypeDef(BaseModel):
    AdditionalVersionWeights: Optional[Dict[str, float]] = None

class AliasRoutingConfigurationTypeDef(BaseModel):
    AdditionalVersionWeights: Optional[Mapping[str, float]] = None

class AllowedPublishersPaginatorTypeDef(BaseModel):
    SigningProfileVersionArns: List[str]

class AllowedPublishersTypeDef(BaseModel):
    SigningProfileVersionArns: Sequence[str]

class AmazonManagedKafkaEventSourceConfigTypeDef(BaseModel):
    ConsumerGroupId: Optional[str] = None

class CodeSigningPoliciesTypeDef(BaseModel):
    UntrustedArtifactOnDeployment: Optional[CodeSigningPolicyType] = None

class ConcurrencyTypeDef(BaseModel):
    ReservedConcurrentExecutions: Optional[int] = None

class CorsPaginatorTypeDef(BaseModel):
    AllowCredentials: Optional[bool] = None
    AllowHeaders: Optional[List[str]] = None
    AllowMethods: Optional[List[str]] = None
    AllowOrigins: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None

class CorsTypeDef(BaseModel):
    AllowCredentials: Optional[bool] = None
    AllowHeaders: Optional[Sequence[str]] = None
    AllowMethods: Optional[Sequence[str]] = None
    AllowOrigins: Optional[Sequence[str]] = None
    ExposeHeaders: Optional[Sequence[str]] = None
    MaxAge: Optional[int] = None

class DocumentDBEventSourceConfigTypeDef(BaseModel):
    DatabaseName: Optional[str] = None
    CollectionName: Optional[str] = None
    FullDocument: Optional[FullDocumentType] = None

class ScalingConfigTypeDef(BaseModel):
    MaximumConcurrency: Optional[int] = None

class SelfManagedEventSourceTypeDef(BaseModel):
    Endpoints: Optional[Mapping[Literal["KAFKA_BOOTSTRAP_SERVERS"], Sequence[str]]] = None

class SelfManagedKafkaEventSourceConfigTypeDef(BaseModel):
    ConsumerGroupId: Optional[str] = None

class SourceAccessConfigurationTypeDef(BaseModel):
    Type: Optional[SourceAccessTypeType] = None
    URI: Optional[str] = None

class DeadLetterConfigTypeDef(BaseModel):
    TargetArn: Optional[str] = None

class EnvironmentTypeDef(BaseModel):
    Variables: Optional[Mapping[str, str]] = None

class EphemeralStorageTypeDef(BaseModel):
    Size: int

class FileSystemConfigTypeDef(BaseModel):
    Arn: str
    LocalMountPath: str

class ImageConfigTypeDef(BaseModel):
    EntryPoint: Optional[Sequence[str]] = None
    Command: Optional[Sequence[str]] = None
    WorkingDirectory: Optional[str] = None

class LoggingConfigTypeDef(BaseModel):
    LogFormat: Optional[LogFormatType] = None
    ApplicationLogLevel: Optional[ApplicationLogLevelType] = None
    SystemLogLevel: Optional[SystemLogLevelType] = None
    LogGroup: Optional[str] = None

class SnapStartTypeDef(BaseModel):
    ApplyOn: Optional[SnapStartApplyOnType] = None

class TracingConfigTypeDef(BaseModel):
    Mode: Optional[TracingModeType] = None

class VpcConfigTypeDef(BaseModel):
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Ipv6AllowedForDualStack: Optional[bool] = None

class DeleteAliasRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Name: str

class DeleteCodeSigningConfigRequestRequestTypeDef(BaseModel):
    CodeSigningConfigArn: str

class DeleteEventSourceMappingRequestRequestTypeDef(BaseModel):
    UUID: str

class DeleteFunctionCodeSigningConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str

class DeleteFunctionConcurrencyRequestRequestTypeDef(BaseModel):
    FunctionName: str

class DeleteFunctionEventInvokeConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class DeleteFunctionRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class DeleteFunctionUrlConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class DeleteLayerVersionRequestRequestTypeDef(BaseModel):
    LayerName: str
    VersionNumber: int

class DeleteProvisionedConcurrencyConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: str

class OnFailureTypeDef(BaseModel):
    Destination: Optional[str] = None

class OnSuccessTypeDef(BaseModel):
    Destination: Optional[str] = None

class EnvironmentErrorTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None

class SelfManagedEventSourcePaginatorTypeDef(BaseModel):
    Endpoints: Optional[Dict[Literal["KAFKA_BOOTSTRAP_SERVERS"], List[str]]] = None

class FilterTypeDef(BaseModel):
    Pattern: Optional[str] = None

class FunctionCodeLocationTypeDef(BaseModel):
    RepositoryType: Optional[str] = None
    Location: Optional[str] = None
    ImageUri: Optional[str] = None
    ResolvedImageUri: Optional[str] = None

class LayerTypeDef(BaseModel):
    Arn: Optional[str] = None
    CodeSize: Optional[int] = None
    SigningProfileVersionArn: Optional[str] = None
    SigningJobArn: Optional[str] = None

class SnapStartResponseTypeDef(BaseModel):
    ApplyOn: Optional[SnapStartApplyOnType] = None
    OptimizationStatus: Optional[SnapStartOptimizationStatusType] = None

class TracingConfigResponseTypeDef(BaseModel):
    Mode: Optional[TracingModeType] = None

class VpcConfigResponseTypeDef(BaseModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    VpcId: Optional[str] = None
    Ipv6AllowedForDualStack: Optional[bool] = None

class GetAliasRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Name: str

class GetCodeSigningConfigRequestRequestTypeDef(BaseModel):
    CodeSigningConfigArn: str

class GetEventSourceMappingRequestRequestTypeDef(BaseModel):
    UUID: str

class GetFunctionCodeSigningConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str

class GetFunctionConcurrencyRequestRequestTypeDef(BaseModel):
    FunctionName: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetFunctionConfigurationRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class GetFunctionEventInvokeConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class GetFunctionRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class GetFunctionUrlConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class GetLayerVersionByArnRequestRequestTypeDef(BaseModel):
    Arn: str

class GetLayerVersionPolicyRequestRequestTypeDef(BaseModel):
    LayerName: str
    VersionNumber: int

class GetLayerVersionRequestRequestTypeDef(BaseModel):
    LayerName: str
    VersionNumber: int

class LayerVersionContentOutputTypeDef(BaseModel):
    Location: Optional[str] = None
    CodeSha256: Optional[str] = None
    CodeSize: Optional[int] = None
    SigningProfileVersionArn: Optional[str] = None
    SigningJobArn: Optional[str] = None

class GetPolicyRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class GetProvisionedConcurrencyConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: str

class GetRuntimeManagementConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class ImageConfigErrorTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None

class ImageConfigPaginatorTypeDef(BaseModel):
    EntryPoint: Optional[List[str]] = None
    Command: Optional[List[str]] = None
    WorkingDirectory: Optional[str] = None

class InvokeResponseStreamUpdateTypeDef(BaseModel):
    Payload: Optional[bytes] = None

class InvokeWithResponseStreamCompleteEventTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorDetails: Optional[str] = None
    LogResult: Optional[str] = None

class LayerVersionsListItemTypeDef(BaseModel):
    LayerVersionArn: Optional[str] = None
    Version: Optional[int] = None
    Description: Optional[str] = None
    CreatedDate: Optional[str] = None
    CompatibleRuntimes: Optional[List[RuntimeType]] = None
    LicenseInfo: Optional[str] = None
    CompatibleArchitectures: Optional[List[ArchitectureType]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAliasesRequestRequestTypeDef(BaseModel):
    FunctionName: str
    FunctionVersion: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListCodeSigningConfigsRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListEventSourceMappingsRequestRequestTypeDef(BaseModel):
    EventSourceArn: Optional[str] = None
    FunctionName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListFunctionEventInvokeConfigsRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListFunctionUrlConfigsRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListFunctionsByCodeSigningConfigRequestRequestTypeDef(BaseModel):
    CodeSigningConfigArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListFunctionsRequestRequestTypeDef(BaseModel):
    MasterRegion: Optional[str] = None
    FunctionVersion: Optional[Literal["ALL"]] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListLayerVersionsRequestRequestTypeDef(BaseModel):
    LayerName: str
    CompatibleRuntime: Optional[RuntimeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None

class ListLayersRequestRequestTypeDef(BaseModel):
    CompatibleRuntime: Optional[RuntimeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None

class ListProvisionedConcurrencyConfigsRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ProvisionedConcurrencyConfigListItemTypeDef(BaseModel):
    FunctionArn: Optional[str] = None
    RequestedProvisionedConcurrentExecutions: Optional[int] = None
    AvailableProvisionedConcurrentExecutions: Optional[int] = None
    AllocatedProvisionedConcurrentExecutions: Optional[int] = None
    Status: Optional[ProvisionedConcurrencyStatusEnumType] = None
    StatusReason: Optional[str] = None
    LastModified: Optional[str] = None

class ListTagsRequestRequestTypeDef(BaseModel):
    Resource: str

class ListVersionsByFunctionRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class PublishVersionRequestRequestTypeDef(BaseModel):
    FunctionName: str
    CodeSha256: Optional[str] = None
    Description: Optional[str] = None
    RevisionId: Optional[str] = None

class PutFunctionCodeSigningConfigRequestRequestTypeDef(BaseModel):
    CodeSigningConfigArn: str
    FunctionName: str

class PutFunctionConcurrencyRequestRequestTypeDef(BaseModel):
    FunctionName: str
    ReservedConcurrentExecutions: int

class PutProvisionedConcurrencyConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: str
    ProvisionedConcurrentExecutions: int

class PutRuntimeManagementConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str
    UpdateRuntimeOn: UpdateRuntimeOnType
    Qualifier: Optional[str] = None
    RuntimeVersionArn: Optional[str] = None

class RemoveLayerVersionPermissionRequestRequestTypeDef(BaseModel):
    LayerName: str
    VersionNumber: int
    StatementId: str
    RevisionId: Optional[str] = None

class RemovePermissionRequestRequestTypeDef(BaseModel):
    FunctionName: str
    StatementId: str
    Qualifier: Optional[str] = None
    RevisionId: Optional[str] = None

class RuntimeVersionErrorTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    Resource: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    Resource: str
    TagKeys: Sequence[str]

class AddLayerVersionPermissionResponseTypeDef(BaseModel):
    Statement: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddPermissionResponseTypeDef(BaseModel):
    Statement: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConcurrencyResponseTypeDef(BaseModel):
    ReservedConcurrentExecutions: int
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSettingsResponseTypeDef(BaseModel):
    AccountLimit: AccountLimitTypeDef
    AccountUsage: AccountUsageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionCodeSigningConfigResponseTypeDef(BaseModel):
    CodeSigningConfigArn: str
    FunctionName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionConcurrencyResponseTypeDef(BaseModel):
    ReservedConcurrentExecutions: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetLayerVersionPolicyResponseTypeDef(BaseModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyResponseTypeDef(BaseModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetProvisionedConcurrencyConfigResponseTypeDef(BaseModel):
    RequestedProvisionedConcurrentExecutions: int
    AvailableProvisionedConcurrentExecutions: int
    AllocatedProvisionedConcurrentExecutions: int
    Status: ProvisionedConcurrencyStatusEnumType
    StatusReason: str
    LastModified: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRuntimeManagementConfigResponseTypeDef(BaseModel):
    UpdateRuntimeOn: UpdateRuntimeOnType
    RuntimeVersionArn: str
    FunctionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class InvocationResponseTypeDef(BaseModel):
    StatusCode: int
    FunctionError: str
    LogResult: str
    Payload: StreamingBody
    ExecutedVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class InvokeAsyncResponseTypeDef(BaseModel):
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionsByCodeSigningConfigResponseTypeDef(BaseModel):
    NextMarker: str
    FunctionArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutFunctionCodeSigningConfigResponseTypeDef(BaseModel):
    CodeSigningConfigArn: str
    FunctionName: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutProvisionedConcurrencyConfigResponseTypeDef(BaseModel):
    RequestedProvisionedConcurrentExecutions: int
    AvailableProvisionedConcurrentExecutions: int
    AllocatedProvisionedConcurrentExecutions: int
    Status: ProvisionedConcurrencyStatusEnumType
    StatusReason: str
    LastModified: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutRuntimeManagementConfigResponseTypeDef(BaseModel):
    UpdateRuntimeOn: UpdateRuntimeOnType
    FunctionArn: str
    RuntimeVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AliasConfigurationPaginatorTypeDef(BaseModel):
    AliasArn: Optional[str] = None
    Name: Optional[str] = None
    FunctionVersion: Optional[str] = None
    Description: Optional[str] = None
    RoutingConfig: Optional[AliasRoutingConfigurationPaginatorTypeDef] = None
    RevisionId: Optional[str] = None

class AliasConfigurationResponseTypeDef(BaseModel):
    AliasArn: str
    Name: str
    FunctionVersion: str
    Description: str
    RoutingConfig: AliasRoutingConfigurationTypeDef
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AliasConfigurationTypeDef(BaseModel):
    AliasArn: Optional[str] = None
    Name: Optional[str] = None
    FunctionVersion: Optional[str] = None
    Description: Optional[str] = None
    RoutingConfig: Optional[AliasRoutingConfigurationTypeDef] = None
    RevisionId: Optional[str] = None

class CreateAliasRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Name: str
    FunctionVersion: str
    Description: Optional[str] = None
    RoutingConfig: Optional[AliasRoutingConfigurationTypeDef] = None

class UpdateAliasRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Name: str
    FunctionVersion: Optional[str] = None
    Description: Optional[str] = None
    RoutingConfig: Optional[AliasRoutingConfigurationTypeDef] = None
    RevisionId: Optional[str] = None

class FunctionCodeTypeDef(BaseModel):
    ZipFile: Optional[BlobTypeDef] = None
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    ImageUri: Optional[str] = None

class InvocationRequestRequestTypeDef(BaseModel):
    FunctionName: str
    InvocationType: Optional[InvocationTypeType] = None
    LogType: Optional[LogTypeType] = None
    ClientContext: Optional[str] = None
    Payload: Optional[BlobTypeDef] = None
    Qualifier: Optional[str] = None

class InvokeAsyncRequestRequestTypeDef(BaseModel):
    FunctionName: str
    InvokeArgs: BlobTypeDef

class InvokeWithResponseStreamRequestRequestTypeDef(BaseModel):
    FunctionName: str
    InvocationType: Optional[ResponseStreamingInvocationTypeType] = None
    LogType: Optional[LogTypeType] = None
    ClientContext: Optional[str] = None
    Qualifier: Optional[str] = None
    Payload: Optional[BlobTypeDef] = None

class LayerVersionContentInputTypeDef(BaseModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    ZipFile: Optional[BlobTypeDef] = None

class UpdateFunctionCodeRequestRequestTypeDef(BaseModel):
    FunctionName: str
    ZipFile: Optional[BlobTypeDef] = None
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    ImageUri: Optional[str] = None
    Publish: Optional[bool] = None
    DryRun: Optional[bool] = None
    RevisionId: Optional[str] = None
    Architectures: Optional[Sequence[ArchitectureType]] = None

class CodeSigningConfigPaginatorTypeDef(BaseModel):
    CodeSigningConfigId: str
    CodeSigningConfigArn: str
    AllowedPublishers: AllowedPublishersPaginatorTypeDef
    CodeSigningPolicies: CodeSigningPoliciesTypeDef
    LastModified: str
    Description: Optional[str] = None

class CodeSigningConfigTypeDef(BaseModel):
    CodeSigningConfigId: str
    CodeSigningConfigArn: str
    AllowedPublishers: AllowedPublishersTypeDef
    CodeSigningPolicies: CodeSigningPoliciesTypeDef
    LastModified: str
    Description: Optional[str] = None

class CreateCodeSigningConfigRequestRequestTypeDef(BaseModel):
    AllowedPublishers: AllowedPublishersTypeDef
    Description: Optional[str] = None
    CodeSigningPolicies: Optional[CodeSigningPoliciesTypeDef] = None

class UpdateCodeSigningConfigRequestRequestTypeDef(BaseModel):
    CodeSigningConfigArn: str
    Description: Optional[str] = None
    AllowedPublishers: Optional[AllowedPublishersTypeDef] = None
    CodeSigningPolicies: Optional[CodeSigningPoliciesTypeDef] = None

class FunctionUrlConfigPaginatorTypeDef(BaseModel):
    FunctionUrl: str
    FunctionArn: str
    CreationTime: str
    LastModifiedTime: str
    AuthType: FunctionUrlAuthTypeType
    Cors: Optional[CorsPaginatorTypeDef] = None
    InvokeMode: Optional[InvokeModeType] = None

class CreateFunctionUrlConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str
    AuthType: FunctionUrlAuthTypeType
    Qualifier: Optional[str] = None
    Cors: Optional[CorsTypeDef] = None
    InvokeMode: Optional[InvokeModeType] = None

class CreateFunctionUrlConfigResponseTypeDef(BaseModel):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsTypeDef
    CreationTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionUrlConfigTypeDef(BaseModel):
    FunctionUrl: str
    FunctionArn: str
    CreationTime: str
    LastModifiedTime: str
    AuthType: FunctionUrlAuthTypeType
    Cors: Optional[CorsTypeDef] = None
    InvokeMode: Optional[InvokeModeType] = None

class GetFunctionUrlConfigResponseTypeDef(BaseModel):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsTypeDef
    CreationTime: str
    LastModifiedTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFunctionUrlConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    AuthType: Optional[FunctionUrlAuthTypeType] = None
    Cors: Optional[CorsTypeDef] = None
    InvokeMode: Optional[InvokeModeType] = None

class UpdateFunctionUrlConfigResponseTypeDef(BaseModel):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsTypeDef
    CreationTime: str
    LastModifiedTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFunctionConfigurationRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Role: Optional[str] = None
    Handler: Optional[str] = None
    Description: Optional[str] = None
    Timeout: Optional[int] = None
    MemorySize: Optional[int] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    Environment: Optional[EnvironmentTypeDef] = None
    Runtime: Optional[RuntimeType] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    KMSKeyArn: Optional[str] = None
    TracingConfig: Optional[TracingConfigTypeDef] = None
    RevisionId: Optional[str] = None
    Layers: Optional[Sequence[str]] = None
    FileSystemConfigs: Optional[Sequence[FileSystemConfigTypeDef]] = None
    ImageConfig: Optional[ImageConfigTypeDef] = None
    EphemeralStorage: Optional[EphemeralStorageTypeDef] = None
    SnapStart: Optional[SnapStartTypeDef] = None
    LoggingConfig: Optional[LoggingConfigTypeDef] = None

class DestinationConfigTypeDef(BaseModel):
    OnSuccess: Optional[OnSuccessTypeDef] = None
    OnFailure: Optional[OnFailureTypeDef] = None

class EnvironmentResponseTypeDef(BaseModel):
    Variables: Optional[Dict[str, str]] = None
    Error: Optional[EnvironmentErrorTypeDef] = None

class FilterCriteriaPaginatorTypeDef(BaseModel):
    Filters: Optional[List[FilterTypeDef]] = None

class FilterCriteriaTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None

class GetFunctionConfigurationRequestFunctionActiveWaitTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetFunctionConfigurationRequestFunctionUpdatedWaitTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetFunctionConfigurationRequestPublishedVersionActiveWaitTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetFunctionRequestFunctionActiveV2WaitTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetFunctionRequestFunctionExistsWaitTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetFunctionRequestFunctionUpdatedV2WaitTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetLayerVersionResponseTypeDef(BaseModel):
    Content: LayerVersionContentOutputTypeDef
    LayerArn: str
    LayerVersionArn: str
    Description: str
    CreatedDate: str
    Version: int
    CompatibleRuntimes: List[RuntimeType]
    LicenseInfo: str
    CompatibleArchitectures: List[ArchitectureType]
    ResponseMetadata: ResponseMetadataTypeDef

class PublishLayerVersionResponseTypeDef(BaseModel):
    Content: LayerVersionContentOutputTypeDef
    LayerArn: str
    LayerVersionArn: str
    Description: str
    CreatedDate: str
    Version: int
    CompatibleRuntimes: List[RuntimeType]
    LicenseInfo: str
    CompatibleArchitectures: List[ArchitectureType]
    ResponseMetadata: ResponseMetadataTypeDef

class ImageConfigResponseTypeDef(BaseModel):
    ImageConfig: Optional[ImageConfigTypeDef] = None
    Error: Optional[ImageConfigErrorTypeDef] = None

class ImageConfigResponsePaginatorTypeDef(BaseModel):
    ImageConfig: Optional[ImageConfigPaginatorTypeDef] = None
    Error: Optional[ImageConfigErrorTypeDef] = None

class InvokeWithResponseStreamResponseEventTypeDef(BaseModel):
    PayloadChunk: Optional[InvokeResponseStreamUpdateTypeDef] = None
    InvokeComplete: Optional[InvokeWithResponseStreamCompleteEventTypeDef] = None

class LayersListItemTypeDef(BaseModel):
    LayerName: Optional[str] = None
    LayerArn: Optional[str] = None
    LatestMatchingVersion: Optional[LayerVersionsListItemTypeDef] = None

class ListLayerVersionsResponseTypeDef(BaseModel):
    NextMarker: str
    LayerVersions: List[LayerVersionsListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesRequestListAliasesPaginateTypeDef(BaseModel):
    FunctionName: str
    FunctionVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCodeSigningConfigsRequestListCodeSigningConfigsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventSourceMappingsRequestListEventSourceMappingsPaginateTypeDef(BaseModel):
    EventSourceArn: Optional[str] = None
    FunctionName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFunctionEventInvokeConfigsRequestListFunctionEventInvokeConfigsPaginateTypeDef(BaseModel):
    FunctionName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFunctionUrlConfigsRequestListFunctionUrlConfigsPaginateTypeDef(BaseModel):
    FunctionName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFunctionsByCodeSigningConfigRequestListFunctionsByCodeSigningConfigPaginateTypeDef(BaseModel):
    CodeSigningConfigArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFunctionsRequestListFunctionsPaginateTypeDef(BaseModel):
    MasterRegion: Optional[str] = None
    FunctionVersion: Optional[Literal["ALL"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLayerVersionsRequestListLayerVersionsPaginateTypeDef(BaseModel):
    LayerName: str
    CompatibleRuntime: Optional[RuntimeType] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLayersRequestListLayersPaginateTypeDef(BaseModel):
    CompatibleRuntime: Optional[RuntimeType] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVersionsByFunctionRequestListVersionsByFunctionPaginateTypeDef(BaseModel):
    FunctionName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProvisionedConcurrencyConfigsResponseTypeDef(BaseModel):
    ProvisionedConcurrencyConfigs: List[ProvisionedConcurrencyConfigListItemTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class RuntimeVersionConfigTypeDef(BaseModel):
    RuntimeVersionArn: Optional[str] = None
    Error: Optional[RuntimeVersionErrorTypeDef] = None

class ListAliasesResponsePaginatorTypeDef(BaseModel):
    NextMarker: str
    Aliases: List[AliasConfigurationPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesResponseTypeDef(BaseModel):
    NextMarker: str
    Aliases: List[AliasConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Role: str
    Code: FunctionCodeTypeDef
    Runtime: Optional[RuntimeType] = None
    Handler: Optional[str] = None
    Description: Optional[str] = None
    Timeout: Optional[int] = None
    MemorySize: Optional[int] = None
    Publish: Optional[bool] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    PackageType: Optional[PackageTypeType] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    Environment: Optional[EnvironmentTypeDef] = None
    KMSKeyArn: Optional[str] = None
    TracingConfig: Optional[TracingConfigTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    Layers: Optional[Sequence[str]] = None
    FileSystemConfigs: Optional[Sequence[FileSystemConfigTypeDef]] = None
    ImageConfig: Optional[ImageConfigTypeDef] = None
    CodeSigningConfigArn: Optional[str] = None
    Architectures: Optional[Sequence[ArchitectureType]] = None
    EphemeralStorage: Optional[EphemeralStorageTypeDef] = None
    SnapStart: Optional[SnapStartTypeDef] = None
    LoggingConfig: Optional[LoggingConfigTypeDef] = None

class PublishLayerVersionRequestRequestTypeDef(BaseModel):
    LayerName: str
    Content: LayerVersionContentInputTypeDef
    Description: Optional[str] = None
    CompatibleRuntimes: Optional[Sequence[RuntimeType]] = None
    LicenseInfo: Optional[str] = None
    CompatibleArchitectures: Optional[Sequence[ArchitectureType]] = None

class ListCodeSigningConfigsResponsePaginatorTypeDef(BaseModel):
    NextMarker: str
    CodeSigningConfigs: List[CodeSigningConfigPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCodeSigningConfigResponseTypeDef(BaseModel):
    CodeSigningConfig: CodeSigningConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCodeSigningConfigResponseTypeDef(BaseModel):
    CodeSigningConfig: CodeSigningConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCodeSigningConfigsResponseTypeDef(BaseModel):
    NextMarker: str
    CodeSigningConfigs: List[CodeSigningConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCodeSigningConfigResponseTypeDef(BaseModel):
    CodeSigningConfig: CodeSigningConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionUrlConfigsResponsePaginatorTypeDef(BaseModel):
    FunctionUrlConfigs: List[FunctionUrlConfigPaginatorTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionUrlConfigsResponseTypeDef(BaseModel):
    FunctionUrlConfigs: List[FunctionUrlConfigTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionEventInvokeConfigResponseTypeDef(BaseModel):
    LastModified: datetime
    FunctionArn: str
    MaximumRetryAttempts: int
    MaximumEventAgeInSeconds: int
    DestinationConfig: DestinationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionEventInvokeConfigTypeDef(BaseModel):
    LastModified: Optional[datetime] = None
    FunctionArn: Optional[str] = None
    MaximumRetryAttempts: Optional[int] = None
    MaximumEventAgeInSeconds: Optional[int] = None
    DestinationConfig: Optional[DestinationConfigTypeDef] = None

class PutFunctionEventInvokeConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    MaximumRetryAttempts: Optional[int] = None
    MaximumEventAgeInSeconds: Optional[int] = None
    DestinationConfig: Optional[DestinationConfigTypeDef] = None

class UpdateFunctionEventInvokeConfigRequestRequestTypeDef(BaseModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    MaximumRetryAttempts: Optional[int] = None
    MaximumEventAgeInSeconds: Optional[int] = None
    DestinationConfig: Optional[DestinationConfigTypeDef] = None

class EventSourceMappingConfigurationPaginatorTypeDef(BaseModel):
    UUID: Optional[str] = None
    StartingPosition: Optional[EventSourcePositionType] = None
    StartingPositionTimestamp: Optional[datetime] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    EventSourceArn: Optional[str] = None
    FilterCriteria: Optional[FilterCriteriaPaginatorTypeDef] = None
    FunctionArn: Optional[str] = None
    LastModified: Optional[datetime] = None
    LastProcessingResult: Optional[str] = None
    State: Optional[str] = None
    StateTransitionReason: Optional[str] = None
    DestinationConfig: Optional[DestinationConfigTypeDef] = None
    Topics: Optional[List[str]] = None
    Queues: Optional[List[str]] = None
    SourceAccessConfigurations: Optional[List[SourceAccessConfigurationTypeDef]] = None
    SelfManagedEventSource: Optional[SelfManagedEventSourcePaginatorTypeDef] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    BisectBatchOnFunctionError: Optional[bool] = None
    MaximumRetryAttempts: Optional[int] = None
    TumblingWindowInSeconds: Optional[int] = None
    FunctionResponseTypes: Optional[List[Literal["ReportBatchItemFailures"]]] = None
    AmazonManagedKafkaEventSourceConfig: Optional[       AmazonManagedKafkaEventSourceConfigTypeDef     ] = None
    SelfManagedKafkaEventSourceConfig: Optional[SelfManagedKafkaEventSourceConfigTypeDef] = None
    ScalingConfig: Optional[ScalingConfigTypeDef] = None
    DocumentDBEventSourceConfig: Optional[DocumentDBEventSourceConfigTypeDef] = None

class CreateEventSourceMappingRequestRequestTypeDef(BaseModel):
    FunctionName: str
    EventSourceArn: Optional[str] = None
    Enabled: Optional[bool] = None
    BatchSize: Optional[int] = None
    FilterCriteria: Optional[FilterCriteriaTypeDef] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    StartingPosition: Optional[EventSourcePositionType] = None
    StartingPositionTimestamp: Optional[TimestampTypeDef] = None
    DestinationConfig: Optional[DestinationConfigTypeDef] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    BisectBatchOnFunctionError: Optional[bool] = None
    MaximumRetryAttempts: Optional[int] = None
    TumblingWindowInSeconds: Optional[int] = None
    Topics: Optional[Sequence[str]] = None
    Queues: Optional[Sequence[str]] = None
    SourceAccessConfigurations: Optional[Sequence[SourceAccessConfigurationTypeDef]] = None
    SelfManagedEventSource: Optional[SelfManagedEventSourceTypeDef] = None
    FunctionResponseTypes: Optional[Sequence[Literal["ReportBatchItemFailures"]]] = None
    AmazonManagedKafkaEventSourceConfig: Optional[       AmazonManagedKafkaEventSourceConfigTypeDef     ] = None
    SelfManagedKafkaEventSourceConfig: Optional[SelfManagedKafkaEventSourceConfigTypeDef] = None
    ScalingConfig: Optional[ScalingConfigTypeDef] = None
    DocumentDBEventSourceConfig: Optional[DocumentDBEventSourceConfigTypeDef] = None

class EventSourceMappingConfigurationResponseTypeDef(BaseModel):
    UUID: str
    StartingPosition: EventSourcePositionType
    StartingPositionTimestamp: datetime
    BatchSize: int
    MaximumBatchingWindowInSeconds: int
    ParallelizationFactor: int
    EventSourceArn: str
    FilterCriteria: FilterCriteriaTypeDef
    FunctionArn: str
    LastModified: datetime
    LastProcessingResult: str
    State: str
    StateTransitionReason: str
    DestinationConfig: DestinationConfigTypeDef
    Topics: List[str]
    Queues: List[str]
    SourceAccessConfigurations: List[SourceAccessConfigurationTypeDef]
    SelfManagedEventSource: SelfManagedEventSourceTypeDef
    MaximumRecordAgeInSeconds: int
    BisectBatchOnFunctionError: bool
    MaximumRetryAttempts: int
    TumblingWindowInSeconds: int
    FunctionResponseTypes: List[Literal["ReportBatchItemFailures"]]
    AmazonManagedKafkaEventSourceConfig: AmazonManagedKafkaEventSourceConfigTypeDef
    SelfManagedKafkaEventSourceConfig: SelfManagedKafkaEventSourceConfigTypeDef
    ScalingConfig: ScalingConfigTypeDef
    DocumentDBEventSourceConfig: DocumentDBEventSourceConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EventSourceMappingConfigurationTypeDef(BaseModel):
    UUID: Optional[str] = None
    StartingPosition: Optional[EventSourcePositionType] = None
    StartingPositionTimestamp: Optional[datetime] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    EventSourceArn: Optional[str] = None
    FilterCriteria: Optional[FilterCriteriaTypeDef] = None
    FunctionArn: Optional[str] = None
    LastModified: Optional[datetime] = None
    LastProcessingResult: Optional[str] = None
    State: Optional[str] = None
    StateTransitionReason: Optional[str] = None
    DestinationConfig: Optional[DestinationConfigTypeDef] = None
    Topics: Optional[List[str]] = None
    Queues: Optional[List[str]] = None
    SourceAccessConfigurations: Optional[List[SourceAccessConfigurationTypeDef]] = None
    SelfManagedEventSource: Optional[SelfManagedEventSourceTypeDef] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    BisectBatchOnFunctionError: Optional[bool] = None
    MaximumRetryAttempts: Optional[int] = None
    TumblingWindowInSeconds: Optional[int] = None
    FunctionResponseTypes: Optional[List[Literal["ReportBatchItemFailures"]]] = None
    AmazonManagedKafkaEventSourceConfig: Optional[       AmazonManagedKafkaEventSourceConfigTypeDef     ] = None
    SelfManagedKafkaEventSourceConfig: Optional[SelfManagedKafkaEventSourceConfigTypeDef] = None
    ScalingConfig: Optional[ScalingConfigTypeDef] = None
    DocumentDBEventSourceConfig: Optional[DocumentDBEventSourceConfigTypeDef] = None

class UpdateEventSourceMappingRequestRequestTypeDef(BaseModel):
    UUID: str
    FunctionName: Optional[str] = None
    Enabled: Optional[bool] = None
    BatchSize: Optional[int] = None
    FilterCriteria: Optional[FilterCriteriaTypeDef] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    DestinationConfig: Optional[DestinationConfigTypeDef] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    BisectBatchOnFunctionError: Optional[bool] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    SourceAccessConfigurations: Optional[Sequence[SourceAccessConfigurationTypeDef]] = None
    TumblingWindowInSeconds: Optional[int] = None
    FunctionResponseTypes: Optional[Sequence[Literal["ReportBatchItemFailures"]]] = None
    ScalingConfig: Optional[ScalingConfigTypeDef] = None
    DocumentDBEventSourceConfig: Optional[DocumentDBEventSourceConfigTypeDef] = None

class InvokeWithResponseStreamResponseTypeDef(BaseModel):
    StatusCode: int
    ExecutedVersion: str
    EventStream: "EventStream[InvokeWithResponseStreamResponseEventTypeDef]"
    ResponseStreamContentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLayersResponseTypeDef(BaseModel):
    NextMarker: str
    Layers: List[LayersListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionConfigurationPaginatorTypeDef(BaseModel):
    FunctionName: Optional[str] = None
    FunctionArn: Optional[str] = None
    Runtime: Optional[RuntimeType] = None
    Role: Optional[str] = None
    Handler: Optional[str] = None
    CodeSize: Optional[int] = None
    Description: Optional[str] = None
    Timeout: Optional[int] = None
    MemorySize: Optional[int] = None
    LastModified: Optional[str] = None
    CodeSha256: Optional[str] = None
    Version: Optional[str] = None
    VpcConfig: Optional[VpcConfigResponseTypeDef] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    Environment: Optional[EnvironmentResponseTypeDef] = None
    KMSKeyArn: Optional[str] = None
    TracingConfig: Optional[TracingConfigResponseTypeDef] = None
    MasterArn: Optional[str] = None
    RevisionId: Optional[str] = None
    Layers: Optional[List[LayerTypeDef]] = None
    State: Optional[StateType] = None
    StateReason: Optional[str] = None
    StateReasonCode: Optional[StateReasonCodeType] = None
    LastUpdateStatus: Optional[LastUpdateStatusType] = None
    LastUpdateStatusReason: Optional[str] = None
    LastUpdateStatusReasonCode: Optional[LastUpdateStatusReasonCodeType] = None
    FileSystemConfigs: Optional[List[FileSystemConfigTypeDef]] = None
    PackageType: Optional[PackageTypeType] = None
    ImageConfigResponse: Optional[ImageConfigResponsePaginatorTypeDef] = None
    SigningProfileVersionArn: Optional[str] = None
    SigningJobArn: Optional[str] = None
    Architectures: Optional[List[ArchitectureType]] = None
    EphemeralStorage: Optional[EphemeralStorageTypeDef] = None
    SnapStart: Optional[SnapStartResponseTypeDef] = None
    RuntimeVersionConfig: Optional[RuntimeVersionConfigTypeDef] = None
    LoggingConfig: Optional[LoggingConfigTypeDef] = None

class FunctionConfigurationResponseTypeDef(BaseModel):
    FunctionName: str
    FunctionArn: str
    Runtime: RuntimeType
    Role: str
    Handler: str
    CodeSize: int
    Description: str
    Timeout: int
    MemorySize: int
    LastModified: str
    CodeSha256: str
    Version: str
    VpcConfig: VpcConfigResponseTypeDef
    DeadLetterConfig: DeadLetterConfigTypeDef
    Environment: EnvironmentResponseTypeDef
    KMSKeyArn: str
    TracingConfig: TracingConfigResponseTypeDef
    MasterArn: str
    RevisionId: str
    Layers: List[LayerTypeDef]
    State: StateType
    StateReason: str
    StateReasonCode: StateReasonCodeType
    LastUpdateStatus: LastUpdateStatusType
    LastUpdateStatusReason: str
    LastUpdateStatusReasonCode: LastUpdateStatusReasonCodeType
    FileSystemConfigs: List[FileSystemConfigTypeDef]
    PackageType: PackageTypeType
    ImageConfigResponse: ImageConfigResponseTypeDef
    SigningProfileVersionArn: str
    SigningJobArn: str
    Architectures: List[ArchitectureType]
    EphemeralStorage: EphemeralStorageTypeDef
    SnapStart: SnapStartResponseTypeDef
    RuntimeVersionConfig: RuntimeVersionConfigTypeDef
    LoggingConfig: LoggingConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionConfigurationTypeDef(BaseModel):
    FunctionName: Optional[str] = None
    FunctionArn: Optional[str] = None
    Runtime: Optional[RuntimeType] = None
    Role: Optional[str] = None
    Handler: Optional[str] = None
    CodeSize: Optional[int] = None
    Description: Optional[str] = None
    Timeout: Optional[int] = None
    MemorySize: Optional[int] = None
    LastModified: Optional[str] = None
    CodeSha256: Optional[str] = None
    Version: Optional[str] = None
    VpcConfig: Optional[VpcConfigResponseTypeDef] = None
    DeadLetterConfig: Optional[DeadLetterConfigTypeDef] = None
    Environment: Optional[EnvironmentResponseTypeDef] = None
    KMSKeyArn: Optional[str] = None
    TracingConfig: Optional[TracingConfigResponseTypeDef] = None
    MasterArn: Optional[str] = None
    RevisionId: Optional[str] = None
    Layers: Optional[List[LayerTypeDef]] = None
    State: Optional[StateType] = None
    StateReason: Optional[str] = None
    StateReasonCode: Optional[StateReasonCodeType] = None
    LastUpdateStatus: Optional[LastUpdateStatusType] = None
    LastUpdateStatusReason: Optional[str] = None
    LastUpdateStatusReasonCode: Optional[LastUpdateStatusReasonCodeType] = None
    FileSystemConfigs: Optional[List[FileSystemConfigTypeDef]] = None
    PackageType: Optional[PackageTypeType] = None
    ImageConfigResponse: Optional[ImageConfigResponseTypeDef] = None
    SigningProfileVersionArn: Optional[str] = None
    SigningJobArn: Optional[str] = None
    Architectures: Optional[List[ArchitectureType]] = None
    EphemeralStorage: Optional[EphemeralStorageTypeDef] = None
    SnapStart: Optional[SnapStartResponseTypeDef] = None
    RuntimeVersionConfig: Optional[RuntimeVersionConfigTypeDef] = None
    LoggingConfig: Optional[LoggingConfigTypeDef] = None

class ListFunctionEventInvokeConfigsResponseTypeDef(BaseModel):
    FunctionEventInvokeConfigs: List[FunctionEventInvokeConfigTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventSourceMappingsResponsePaginatorTypeDef(BaseModel):
    NextMarker: str
    EventSourceMappings: List[EventSourceMappingConfigurationPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventSourceMappingsResponseTypeDef(BaseModel):
    NextMarker: str
    EventSourceMappings: List[EventSourceMappingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionsResponsePaginatorTypeDef(BaseModel):
    NextMarker: str
    Functions: List[FunctionConfigurationPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVersionsByFunctionResponsePaginatorTypeDef(BaseModel):
    NextMarker: str
    Versions: List[FunctionConfigurationPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionResponseTypeDef(BaseModel):
    Configuration: FunctionConfigurationTypeDef
    Code: FunctionCodeLocationTypeDef
    Tags: Dict[str, str]
    Concurrency: ConcurrencyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionsResponseTypeDef(BaseModel):
    NextMarker: str
    Functions: List[FunctionConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVersionsByFunctionResponseTypeDef(BaseModel):
    NextMarker: str
    Versions: List[FunctionConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

