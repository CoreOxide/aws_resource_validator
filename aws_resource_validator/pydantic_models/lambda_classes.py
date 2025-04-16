from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel, EventStream
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
from aws_resource_validator.pydantic_models.lambda_constants import *

class AccountLimit(BaseValidatorModel):
    TotalCodeSize: Optional[int] = None
    CodeSizeUnzipped: Optional[int] = None
    CodeSizeZipped: Optional[int] = None
    ConcurrentExecutions: Optional[int] = None
    UnreservedConcurrentExecutions: Optional[int] = None


class AccountUsage(BaseValidatorModel):
    TotalCodeSize: Optional[int] = None
    FunctionCount: Optional[int] = None


class AddLayerVersionPermissionRequest(BaseValidatorModel):
    LayerName: str
    VersionNumber: int
    StatementId: str
    Action: str
    Principal: str
    OrganizationId: Optional[str] = None
    RevisionId: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AddPermissionRequest(BaseValidatorModel):
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


class AliasRoutingConfigurationOutput(BaseValidatorModel):
    AdditionalVersionWeights: Optional[Dict[str, float]] = None


class AliasRoutingConfiguration(BaseValidatorModel):
    AdditionalVersionWeights: Optional[Mapping[str, float]] = None


class AllowedPublishersOutput(BaseValidatorModel):
    SigningProfileVersionArns: List[str]


class AllowedPublishers(BaseValidatorModel):
    SigningProfileVersionArns: Sequence[str]


class AmazonManagedKafkaEventSourceConfig(BaseValidatorModel):
    ConsumerGroupId: Optional[str] = None


class CodeSigningPolicies(BaseValidatorModel):
    UntrustedArtifactOnDeployment: Optional[CodeSigningPolicyType] = None


class Concurrency(BaseValidatorModel):
    ReservedConcurrentExecutions: Optional[int] = None


class CorsOutput(BaseValidatorModel):
    AllowCredentials: Optional[bool] = None
    AllowHeaders: Optional[List[str]] = None
    AllowMethods: Optional[List[str]] = None
    AllowOrigins: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None


class Cors(BaseValidatorModel):
    AllowCredentials: Optional[bool] = None
    AllowHeaders: Optional[Sequence[str]] = None
    AllowMethods: Optional[Sequence[str]] = None
    AllowOrigins: Optional[Sequence[str]] = None
    ExposeHeaders: Optional[Sequence[str]] = None
    MaxAge: Optional[int] = None


class DocumentDBEventSourceConfig(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    CollectionName: Optional[str] = None
    FullDocument: Optional[FullDocumentType] = None


class ProvisionedPollerConfig(BaseValidatorModel):
    MinimumPollers: Optional[int] = None
    MaximumPollers: Optional[int] = None


class ScalingConfig(BaseValidatorModel):
    MaximumConcurrency: Optional[int] = None


class SelfManagedKafkaEventSourceConfig(BaseValidatorModel):
    ConsumerGroupId: Optional[str] = None


class DeadLetterConfig(BaseValidatorModel):
    TargetArn: Optional[str] = None


class Environment(BaseValidatorModel):
    Variables: Optional[Mapping[str, str]] = None


class EphemeralStorage(BaseValidatorModel):
    Size: int


class FileSystemConfig(BaseValidatorModel):
    Arn: str
    LocalMountPath: str


class LoggingConfig(BaseValidatorModel):
    LogFormat: Optional[LogFormatType] = None
    ApplicationLogLevel: Optional[ApplicationLogLevelType] = None
    SystemLogLevel: Optional[SystemLogLevelType] = None
    LogGroup: Optional[str] = None


class SnapStart(BaseValidatorModel):
    ApplyOn: Optional[SnapStartApplyOnType] = None


class TracingConfig(BaseValidatorModel):
    Mode: Optional[TracingModeType] = None


class VpcConfig(BaseValidatorModel):
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Ipv6AllowedForDualStack: Optional[bool] = None


class DeleteAliasRequest(BaseValidatorModel):
    FunctionName: str
    Name: str


class DeleteCodeSigningConfigRequest(BaseValidatorModel):
    CodeSigningConfigArn: str


class DeleteEventSourceMappingRequest(BaseValidatorModel):
    UUID: str


class DeleteFunctionCodeSigningConfigRequest(BaseValidatorModel):
    FunctionName: str


class DeleteFunctionConcurrencyRequest(BaseValidatorModel):
    FunctionName: str


class DeleteFunctionEventInvokeConfigRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class DeleteFunctionRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class DeleteFunctionUrlConfigRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class DeleteLayerVersionRequest(BaseValidatorModel):
    LayerName: str
    VersionNumber: int


class DeleteProvisionedConcurrencyConfigRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: str


class OnFailure(BaseValidatorModel):
    Destination: Optional[str] = None


class OnSuccess(BaseValidatorModel):
    Destination: Optional[str] = None


class EnvironmentError(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class EventSourceMappingMetricsConfigOutput(BaseValidatorModel):
    Metrics: Optional[List[Literal["EventCount"]]] = None


class FilterCriteriaError(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class SelfManagedEventSourceOutput(BaseValidatorModel):
    Endpoints: Optional[Dict[Literal["KAFKA_BOOTSTRAP_SERVERS"], List[str]]] = None


class EventSourceMappingMetricsConfig(BaseValidatorModel):
    Metrics: Optional[Sequence[Literal["EventCount"]]] = None


class FunctionCodeLocation(BaseValidatorModel):
    RepositoryType: Optional[str] = None
    Location: Optional[str] = None
    ImageUri: Optional[str] = None
    ResolvedImageUri: Optional[str] = None
    SourceKMSKeyArn: Optional[str] = None


class Layer(BaseValidatorModel):
    Arn: Optional[str] = None
    CodeSize: Optional[int] = None
    SigningProfileVersionArn: Optional[str] = None
    SigningJobArn: Optional[str] = None


class SnapStartResponse(BaseValidatorModel):
    ApplyOn: Optional[SnapStartApplyOnType] = None
    OptimizationStatus: Optional[SnapStartOptimizationStatusType] = None


class TracingConfigResponse(BaseValidatorModel):
    Mode: Optional[TracingModeType] = None


class VpcConfigResponse(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    VpcId: Optional[str] = None
    Ipv6AllowedForDualStack: Optional[bool] = None


class GetAliasRequest(BaseValidatorModel):
    FunctionName: str
    Name: str


class GetCodeSigningConfigRequest(BaseValidatorModel):
    CodeSigningConfigArn: str


class GetEventSourceMappingRequest(BaseValidatorModel):
    UUID: str


class GetFunctionCodeSigningConfigRequest(BaseValidatorModel):
    FunctionName: str


class GetFunctionConcurrencyRequest(BaseValidatorModel):
    FunctionName: str


class GetFunctionConfigurationRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetFunctionEventInvokeConfigRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class GetFunctionRecursionConfigRequest(BaseValidatorModel):
    FunctionName: str


class GetFunctionRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class TagsError(BaseValidatorModel):
    ErrorCode: str
    Message: str


class GetFunctionUrlConfigRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class GetLayerVersionByArnRequest(BaseValidatorModel):
    Arn: str


class GetLayerVersionPolicyRequest(BaseValidatorModel):
    LayerName: str
    VersionNumber: int


class GetLayerVersionRequest(BaseValidatorModel):
    LayerName: str
    VersionNumber: int


class LayerVersionContentOutput(BaseValidatorModel):
    Location: Optional[str] = None
    CodeSha256: Optional[str] = None
    CodeSize: Optional[int] = None
    SigningProfileVersionArn: Optional[str] = None
    SigningJobArn: Optional[str] = None


class GetPolicyRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class GetProvisionedConcurrencyConfigRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: str


class GetRuntimeManagementConfigRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class ImageConfigError(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class ImageConfigOutput(BaseValidatorModel):
    EntryPoint: Optional[List[str]] = None
    Command: Optional[List[str]] = None
    WorkingDirectory: Optional[str] = None


class ImageConfig(BaseValidatorModel):
    EntryPoint: Optional[Sequence[str]] = None
    Command: Optional[Sequence[str]] = None
    WorkingDirectory: Optional[str] = None


class InvokeResponseStreamUpdate(BaseValidatorModel):
    Payload: Optional[bytes] = None


class InvokeWithResponseStreamCompleteEvent(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorDetails: Optional[str] = None
    LogResult: Optional[str] = None


class LayerVersionsListItem(BaseValidatorModel):
    LayerVersionArn: Optional[str] = None
    Version: Optional[int] = None
    Description: Optional[str] = None
    CreatedDate: Optional[str] = None
    CompatibleRuntimes: Optional[List[RuntimeType]] = None
    LicenseInfo: Optional[str] = None
    CompatibleArchitectures: Optional[List[ArchitectureType]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAliasesRequest(BaseValidatorModel):
    FunctionName: str
    FunctionVersion: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListCodeSigningConfigsRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListEventSourceMappingsRequest(BaseValidatorModel):
    EventSourceArn: Optional[str] = None
    FunctionName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListFunctionEventInvokeConfigsRequest(BaseValidatorModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListFunctionUrlConfigsRequest(BaseValidatorModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListFunctionsByCodeSigningConfigRequest(BaseValidatorModel):
    CodeSigningConfigArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListFunctionsRequest(BaseValidatorModel):
    MasterRegion: Optional[str] = None
    FunctionVersion: Optional[Literal["ALL"]] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListLayerVersionsRequest(BaseValidatorModel):
    LayerName: str
    CompatibleRuntime: Optional[RuntimeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None


class ListLayersRequest(BaseValidatorModel):
    CompatibleRuntime: Optional[RuntimeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None


class ListProvisionedConcurrencyConfigsRequest(BaseValidatorModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ProvisionedConcurrencyConfigListItem(BaseValidatorModel):
    FunctionArn: Optional[str] = None
    RequestedProvisionedConcurrentExecutions: Optional[int] = None
    AvailableProvisionedConcurrentExecutions: Optional[int] = None
    AllocatedProvisionedConcurrentExecutions: Optional[int] = None
    Status: Optional[ProvisionedConcurrencyStatusEnumType] = None
    StatusReason: Optional[str] = None
    LastModified: Optional[str] = None


class ListTagsRequest(BaseValidatorModel):
    Resource: str


class ListVersionsByFunctionRequest(BaseValidatorModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class PublishVersionRequest(BaseValidatorModel):
    FunctionName: str
    CodeSha256: Optional[str] = None
    Description: Optional[str] = None
    RevisionId: Optional[str] = None


class PutFunctionCodeSigningConfigRequest(BaseValidatorModel):
    CodeSigningConfigArn: str
    FunctionName: str


class PutFunctionConcurrencyRequest(BaseValidatorModel):
    FunctionName: str
    ReservedConcurrentExecutions: int


class PutFunctionRecursionConfigRequest(BaseValidatorModel):
    FunctionName: str
    RecursiveLoop: RecursiveLoopType


class PutProvisionedConcurrencyConfigRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: str
    ProvisionedConcurrentExecutions: int


class PutRuntimeManagementConfigRequest(BaseValidatorModel):
    FunctionName: str
    UpdateRuntimeOn: UpdateRuntimeOnType
    Qualifier: Optional[str] = None
    RuntimeVersionArn: Optional[str] = None


class RemoveLayerVersionPermissionRequest(BaseValidatorModel):
    LayerName: str
    VersionNumber: int
    StatementId: str
    RevisionId: Optional[str] = None


class RemovePermissionRequest(BaseValidatorModel):
    FunctionName: str
    StatementId: str
    Qualifier: Optional[str] = None
    RevisionId: Optional[str] = None


class RuntimeVersionError(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class SelfManagedEventSource(BaseValidatorModel):
    Endpoints: Optional[Mapping[Literal["KAFKA_BOOTSTRAP_SERVERS"], Sequence[str]]] = None


class TagResourceRequest(BaseValidatorModel):
    Resource: str
    Tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    Resource: str
    TagKeys: Sequence[str]


class AddLayerVersionPermissionResponse(BaseValidatorModel):
    Statement: str
    RevisionId: str
    ResponseMetadata: ResponseMetadata


class AddPermissionResponse(BaseValidatorModel):
    Statement: str
    ResponseMetadata: ResponseMetadata


class ConcurrencyResponse(BaseValidatorModel):
    ReservedConcurrentExecutions: int
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAccountSettingsResponse(BaseValidatorModel):
    AccountLimit: AccountLimit
    AccountUsage: AccountUsage
    ResponseMetadata: ResponseMetadata


class GetFunctionCodeSigningConfigResponse(BaseValidatorModel):
    CodeSigningConfigArn: str
    FunctionName: str
    ResponseMetadata: ResponseMetadata


class GetFunctionConcurrencyResponse(BaseValidatorModel):
    ReservedConcurrentExecutions: int
    ResponseMetadata: ResponseMetadata


class GetFunctionRecursionConfigResponse(BaseValidatorModel):
    RecursiveLoop: RecursiveLoopType
    ResponseMetadata: ResponseMetadata


class GetLayerVersionPolicyResponse(BaseValidatorModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadata


class GetPolicyResponse(BaseValidatorModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadata


class GetProvisionedConcurrencyConfigResponse(BaseValidatorModel):
    RequestedProvisionedConcurrentExecutions: int
    AvailableProvisionedConcurrentExecutions: int
    AllocatedProvisionedConcurrentExecutions: int
    Status: ProvisionedConcurrencyStatusEnumType
    StatusReason: str
    LastModified: str
    ResponseMetadata: ResponseMetadata


class GetRuntimeManagementConfigResponse(BaseValidatorModel):
    UpdateRuntimeOn: UpdateRuntimeOnType
    RuntimeVersionArn: str
    FunctionArn: str
    ResponseMetadata: ResponseMetadata


class InvocationResponse(BaseValidatorModel):
    StatusCode: int
    FunctionError: str
    LogResult: str
    Payload: StreamingBody
    ExecutedVersion: str
    ResponseMetadata: ResponseMetadata


class InvokeAsyncResponse(BaseValidatorModel):
    Status: int
    ResponseMetadata: ResponseMetadata


class ListFunctionsByCodeSigningConfigResponse(BaseValidatorModel):
    NextMarker: str
    FunctionArns: List[str]
    ResponseMetadata: ResponseMetadata


class ListTagsResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutFunctionCodeSigningConfigResponse(BaseValidatorModel):
    CodeSigningConfigArn: str
    FunctionName: str
    ResponseMetadata: ResponseMetadata


class PutFunctionRecursionConfigResponse(BaseValidatorModel):
    RecursiveLoop: RecursiveLoopType
    ResponseMetadata: ResponseMetadata


class PutProvisionedConcurrencyConfigResponse(BaseValidatorModel):
    RequestedProvisionedConcurrentExecutions: int
    AvailableProvisionedConcurrentExecutions: int
    AllocatedProvisionedConcurrentExecutions: int
    Status: ProvisionedConcurrencyStatusEnumType
    StatusReason: str
    LastModified: str
    ResponseMetadata: ResponseMetadata


class PutRuntimeManagementConfigResponse(BaseValidatorModel):
    UpdateRuntimeOn: UpdateRuntimeOnType
    FunctionArn: str
    RuntimeVersionArn: str
    ResponseMetadata: ResponseMetadata


class AliasConfigurationResponse(BaseValidatorModel):
    AliasArn: str
    Name: str
    FunctionVersion: str
    Description: str
    RoutingConfig: AliasRoutingConfigurationOutput
    RevisionId: str
    ResponseMetadata: ResponseMetadata


class AliasConfiguration(BaseValidatorModel):
    AliasArn: Optional[str] = None
    Name: Optional[str] = None
    FunctionVersion: Optional[str] = None
    Description: Optional[str] = None
    RoutingConfig: Optional[AliasRoutingConfigurationOutput] = None
    RevisionId: Optional[str] = None


class Blob(BaseValidatorModel):
    pass


class FunctionCode(BaseValidatorModel):
    ZipFile: Optional[Blob] = None
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    ImageUri: Optional[str] = None
    SourceKMSKeyArn: Optional[str] = None


class InvocationRequest(BaseValidatorModel):
    FunctionName: str
    InvocationType: Optional[InvocationTypeType] = None
    LogType: Optional[LogTypeType] = None
    ClientContext: Optional[str] = None
    Payload: Optional[Blob] = None
    Qualifier: Optional[str] = None


class InvokeAsyncRequest(BaseValidatorModel):
    FunctionName: str
    InvokeArgs: Blob


class InvokeWithResponseStreamRequest(BaseValidatorModel):
    FunctionName: str
    InvocationType: Optional[ResponseStreamingInvocationTypeType] = None
    LogType: Optional[LogTypeType] = None
    ClientContext: Optional[str] = None
    Qualifier: Optional[str] = None
    Payload: Optional[Blob] = None


class LayerVersionContentInput(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    ZipFile: Optional[Blob] = None


class UpdateFunctionCodeRequest(BaseValidatorModel):
    FunctionName: str
    ZipFile: Optional[Blob] = None
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    ImageUri: Optional[str] = None
    Publish: Optional[bool] = None
    DryRun: Optional[bool] = None
    RevisionId: Optional[str] = None
    Architectures: Optional[Sequence[ArchitectureType]] = None
    SourceKMSKeyArn: Optional[str] = None


class CodeSigningConfig(BaseValidatorModel):
    CodeSigningConfigId: str
    CodeSigningConfigArn: str
    AllowedPublishers: AllowedPublishersOutput
    CodeSigningPolicies: CodeSigningPolicies
    LastModified: str
    Description: Optional[str] = None


class CreateFunctionUrlConfigResponse(BaseValidatorModel):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsOutput
    CreationTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadata


class FunctionUrlConfig(BaseValidatorModel):
    FunctionUrl: str
    FunctionArn: str
    CreationTime: str
    LastModifiedTime: str
    AuthType: FunctionUrlAuthTypeType
    Cors: Optional[CorsOutput] = None
    InvokeMode: Optional[InvokeModeType] = None


class GetFunctionUrlConfigResponse(BaseValidatorModel):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsOutput
    CreationTime: str
    LastModifiedTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadata


class UpdateFunctionUrlConfigResponse(BaseValidatorModel):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsOutput
    CreationTime: str
    LastModifiedTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadata


class DestinationConfig(BaseValidatorModel):
    OnSuccess: Optional[OnSuccess] = None
    OnFailure: Optional[OnFailure] = None


class EnvironmentResponse(BaseValidatorModel):
    Variables: Optional[Dict[str, str]] = None
    Error: Optional[EnvironmentError] = None


class Filter(BaseValidatorModel):
    pass


class FilterCriteriaOutput(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None


class FilterCriteria(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None


class GetFunctionConfigurationRequestWaitExtraExtra(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class GetFunctionConfigurationRequestWaitExtra(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class GetFunctionConfigurationRequestWait(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class GetFunctionRequestWaitExtraExtra(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class GetFunctionRequestWaitExtra(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class GetFunctionRequestWait(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class GetLayerVersionResponse(BaseValidatorModel):
    Content: LayerVersionContentOutput
    LayerArn: str
    LayerVersionArn: str
    Description: str
    CreatedDate: str
    Version: int
    CompatibleRuntimes: List[RuntimeType]
    LicenseInfo: str
    CompatibleArchitectures: List[ArchitectureType]
    ResponseMetadata: ResponseMetadata


class PublishLayerVersionResponse(BaseValidatorModel):
    Content: LayerVersionContentOutput
    LayerArn: str
    LayerVersionArn: str
    Description: str
    CreatedDate: str
    Version: int
    CompatibleRuntimes: List[RuntimeType]
    LicenseInfo: str
    CompatibleArchitectures: List[ArchitectureType]
    ResponseMetadata: ResponseMetadata


class ImageConfigResponse(BaseValidatorModel):
    ImageConfig: Optional[ImageConfigOutput] = None
    Error: Optional[ImageConfigError] = None


class InvokeWithResponseStreamResponseEvent(BaseValidatorModel):
    PayloadChunk: Optional[InvokeResponseStreamUpdate] = None
    InvokeComplete: Optional[InvokeWithResponseStreamCompleteEvent] = None


class LayersListItem(BaseValidatorModel):
    LayerName: Optional[str] = None
    LayerArn: Optional[str] = None
    LatestMatchingVersion: Optional[LayerVersionsListItem] = None


class ListLayerVersionsResponse(BaseValidatorModel):
    NextMarker: str
    LayerVersions: List[LayerVersionsListItem]
    ResponseMetadata: ResponseMetadata


class ListAliasesRequestPaginate(BaseValidatorModel):
    FunctionName: str
    FunctionVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCodeSigningConfigsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEventSourceMappingsRequestPaginate(BaseValidatorModel):
    EventSourceArn: Optional[str] = None
    FunctionName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFunctionEventInvokeConfigsRequestPaginate(BaseValidatorModel):
    FunctionName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFunctionUrlConfigsRequestPaginate(BaseValidatorModel):
    FunctionName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFunctionsByCodeSigningConfigRequestPaginate(BaseValidatorModel):
    CodeSigningConfigArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFunctionsRequestPaginate(BaseValidatorModel):
    MasterRegion: Optional[str] = None
    FunctionVersion: Optional[Literal["ALL"]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLayerVersionsRequestPaginate(BaseValidatorModel):
    LayerName: str
    CompatibleRuntime: Optional[RuntimeType] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLayersRequestPaginate(BaseValidatorModel):
    CompatibleRuntime: Optional[RuntimeType] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProvisionedConcurrencyConfigsRequestPaginate(BaseValidatorModel):
    FunctionName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVersionsByFunctionRequestPaginate(BaseValidatorModel):
    FunctionName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProvisionedConcurrencyConfigsResponse(BaseValidatorModel):
    ProvisionedConcurrencyConfigs: List[ProvisionedConcurrencyConfigListItem]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class RuntimeVersionConfig(BaseValidatorModel):
    RuntimeVersionArn: Optional[str] = None
    Error: Optional[RuntimeVersionError] = None


class ListAliasesResponse(BaseValidatorModel):
    NextMarker: str
    Aliases: List[AliasConfiguration]
    ResponseMetadata: ResponseMetadata


class AliasRoutingConfigurationUnion(BaseValidatorModel):
    pass


class CreateAliasRequest(BaseValidatorModel):
    FunctionName: str
    Name: str
    FunctionVersion: str
    Description: Optional[str] = None
    RoutingConfig: Optional[AliasRoutingConfigurationUnion] = None


class UpdateAliasRequest(BaseValidatorModel):
    FunctionName: str
    Name: str
    FunctionVersion: Optional[str] = None
    Description: Optional[str] = None
    RoutingConfig: Optional[AliasRoutingConfigurationUnion] = None
    RevisionId: Optional[str] = None


class AllowedPublishersUnion(BaseValidatorModel):
    pass


class CreateCodeSigningConfigRequest(BaseValidatorModel):
    AllowedPublishers: AllowedPublishersUnion
    Description: Optional[str] = None
    CodeSigningPolicies: Optional[CodeSigningPolicies] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateCodeSigningConfigRequest(BaseValidatorModel):
    CodeSigningConfigArn: str
    Description: Optional[str] = None
    AllowedPublishers: Optional[AllowedPublishersUnion] = None
    CodeSigningPolicies: Optional[CodeSigningPolicies] = None


class PublishLayerVersionRequest(BaseValidatorModel):
    LayerName: str
    Content: LayerVersionContentInput
    Description: Optional[str] = None
    CompatibleRuntimes: Optional[Sequence[RuntimeType]] = None
    LicenseInfo: Optional[str] = None
    CompatibleArchitectures: Optional[Sequence[ArchitectureType]] = None


class CreateCodeSigningConfigResponse(BaseValidatorModel):
    CodeSigningConfig: CodeSigningConfig
    ResponseMetadata: ResponseMetadata


class GetCodeSigningConfigResponse(BaseValidatorModel):
    CodeSigningConfig: CodeSigningConfig
    ResponseMetadata: ResponseMetadata


class ListCodeSigningConfigsResponse(BaseValidatorModel):
    NextMarker: str
    CodeSigningConfigs: List[CodeSigningConfig]
    ResponseMetadata: ResponseMetadata


class UpdateCodeSigningConfigResponse(BaseValidatorModel):
    CodeSigningConfig: CodeSigningConfig
    ResponseMetadata: ResponseMetadata


class ListFunctionUrlConfigsResponse(BaseValidatorModel):
    FunctionUrlConfigs: List[FunctionUrlConfig]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class CorsUnion(BaseValidatorModel):
    pass


class CreateFunctionUrlConfigRequest(BaseValidatorModel):
    FunctionName: str
    AuthType: FunctionUrlAuthTypeType
    Qualifier: Optional[str] = None
    Cors: Optional[CorsUnion] = None
    InvokeMode: Optional[InvokeModeType] = None


class UpdateFunctionUrlConfigRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    AuthType: Optional[FunctionUrlAuthTypeType] = None
    Cors: Optional[CorsUnion] = None
    InvokeMode: Optional[InvokeModeType] = None


class FunctionEventInvokeConfigResponse(BaseValidatorModel):
    LastModified: datetime
    FunctionArn: str
    MaximumRetryAttempts: int
    MaximumEventAgeInSeconds: int
    DestinationConfig: DestinationConfig
    ResponseMetadata: ResponseMetadata


class FunctionEventInvokeConfig(BaseValidatorModel):
    LastModified: Optional[datetime] = None
    FunctionArn: Optional[str] = None
    MaximumRetryAttempts: Optional[int] = None
    MaximumEventAgeInSeconds: Optional[int] = None
    DestinationConfig: Optional[DestinationConfig] = None


class PutFunctionEventInvokeConfigRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    MaximumRetryAttempts: Optional[int] = None
    MaximumEventAgeInSeconds: Optional[int] = None
    DestinationConfig: Optional[DestinationConfig] = None


class UpdateFunctionEventInvokeConfigRequest(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    MaximumRetryAttempts: Optional[int] = None
    MaximumEventAgeInSeconds: Optional[int] = None
    DestinationConfig: Optional[DestinationConfig] = None


class SourceAccessConfiguration(BaseValidatorModel):
    pass


class EventSourceMappingConfigurationResponse(BaseValidatorModel):
    UUID: str
    StartingPosition: EventSourcePositionType
    StartingPositionTimestamp: datetime
    BatchSize: int
    MaximumBatchingWindowInSeconds: int
    ParallelizationFactor: int
    EventSourceArn: str
    FilterCriteria: FilterCriteriaOutput
    FunctionArn: str
    LastModified: datetime
    LastProcessingResult: str
    State: str
    StateTransitionReason: str
    DestinationConfig: DestinationConfig
    Topics: List[str]
    Queues: List[str]
    SourceAccessConfigurations: List[SourceAccessConfiguration]
    SelfManagedEventSource: SelfManagedEventSourceOutput
    MaximumRecordAgeInSeconds: int
    BisectBatchOnFunctionError: bool
    MaximumRetryAttempts: int
    TumblingWindowInSeconds: int
    FunctionResponseTypes: List[Literal["ReportBatchItemFailures"]]
    AmazonManagedKafkaEventSourceConfig: AmazonManagedKafkaEventSourceConfig
    SelfManagedKafkaEventSourceConfig: SelfManagedKafkaEventSourceConfig
    ScalingConfig: ScalingConfig
    DocumentDBEventSourceConfig: DocumentDBEventSourceConfig
    KMSKeyArn: str
    FilterCriteriaError: FilterCriteriaError
    EventSourceMappingArn: str
    MetricsConfig: EventSourceMappingMetricsConfigOutput
    ProvisionedPollerConfig: ProvisionedPollerConfig
    ResponseMetadata: ResponseMetadata


class EventSourceMappingConfiguration(BaseValidatorModel):
    UUID: Optional[str] = None
    StartingPosition: Optional[EventSourcePositionType] = None
    StartingPositionTimestamp: Optional[datetime] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    EventSourceArn: Optional[str] = None
    FilterCriteria: Optional[FilterCriteriaOutput] = None
    FunctionArn: Optional[str] = None
    LastModified: Optional[datetime] = None
    LastProcessingResult: Optional[str] = None
    State: Optional[str] = None
    StateTransitionReason: Optional[str] = None
    DestinationConfig: Optional[DestinationConfig] = None
    Topics: Optional[List[str]] = None
    Queues: Optional[List[str]] = None
    SourceAccessConfigurations: Optional[List[SourceAccessConfiguration]] = None
    SelfManagedEventSource: Optional[SelfManagedEventSourceOutput] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    BisectBatchOnFunctionError: Optional[bool] = None
    MaximumRetryAttempts: Optional[int] = None
    TumblingWindowInSeconds: Optional[int] = None
    FunctionResponseTypes: Optional[List[Literal["ReportBatchItemFailures"]]] = None
    AmazonManagedKafkaEventSourceConfig: Optional[AmazonManagedKafkaEventSourceConfig] = None
    SelfManagedKafkaEventSourceConfig: Optional[SelfManagedKafkaEventSourceConfig] = None
    ScalingConfig: Optional[ScalingConfig] = None
    DocumentDBEventSourceConfig: Optional[DocumentDBEventSourceConfig] = None
    KMSKeyArn: Optional[str] = None
    FilterCriteriaError: Optional[FilterCriteriaError] = None
    EventSourceMappingArn: Optional[str] = None
    MetricsConfig: Optional[EventSourceMappingMetricsConfigOutput] = None
    ProvisionedPollerConfig: Optional[ProvisionedPollerConfig] = None


class ImageConfigUnion(BaseValidatorModel):
    pass


class CreateFunctionRequest(BaseValidatorModel):
    FunctionName: str
    Role: str
    Code: FunctionCode
    Runtime: Optional[RuntimeType] = None
    Handler: Optional[str] = None
    Description: Optional[str] = None
    Timeout: Optional[int] = None
    MemorySize: Optional[int] = None
    Publish: Optional[bool] = None
    VpcConfig: Optional[VpcConfig] = None
    PackageType: Optional[PackageTypeType] = None
    DeadLetterConfig: Optional[DeadLetterConfig] = None
    Environment: Optional[Environment] = None
    KMSKeyArn: Optional[str] = None
    TracingConfig: Optional[TracingConfig] = None
    Tags: Optional[Mapping[str, str]] = None
    Layers: Optional[Sequence[str]] = None
    FileSystemConfigs: Optional[Sequence[FileSystemConfig]] = None
    ImageConfig: Optional[ImageConfigUnion] = None
    CodeSigningConfigArn: Optional[str] = None
    Architectures: Optional[Sequence[ArchitectureType]] = None
    EphemeralStorage: Optional[EphemeralStorage] = None
    SnapStart: Optional[SnapStart] = None
    LoggingConfig: Optional[LoggingConfig] = None


class UpdateFunctionConfigurationRequest(BaseValidatorModel):
    FunctionName: str
    Role: Optional[str] = None
    Handler: Optional[str] = None
    Description: Optional[str] = None
    Timeout: Optional[int] = None
    MemorySize: Optional[int] = None
    VpcConfig: Optional[VpcConfig] = None
    Environment: Optional[Environment] = None
    Runtime: Optional[RuntimeType] = None
    DeadLetterConfig: Optional[DeadLetterConfig] = None
    KMSKeyArn: Optional[str] = None
    TracingConfig: Optional[TracingConfig] = None
    RevisionId: Optional[str] = None
    Layers: Optional[Sequence[str]] = None
    FileSystemConfigs: Optional[Sequence[FileSystemConfig]] = None
    ImageConfig: Optional[ImageConfigUnion] = None
    EphemeralStorage: Optional[EphemeralStorage] = None
    SnapStart: Optional[SnapStart] = None
    LoggingConfig: Optional[LoggingConfig] = None


class InvokeWithResponseStreamResponse(BaseValidatorModel):
    StatusCode: int
    ExecutedVersion: str
    EventStream: EventStream[InvokeWithResponseStreamResponseEvent]
    ResponseStreamContentType: str
    ResponseMetadata: ResponseMetadata


class ListLayersResponse(BaseValidatorModel):
    NextMarker: str
    Layers: List[LayersListItem]
    ResponseMetadata: ResponseMetadata


class FunctionConfigurationResponse(BaseValidatorModel):
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
    VpcConfig: VpcConfigResponse
    DeadLetterConfig: DeadLetterConfig
    Environment: EnvironmentResponse
    KMSKeyArn: str
    TracingConfig: TracingConfigResponse
    MasterArn: str
    RevisionId: str
    Layers: List[Layer]
    State: StateType
    StateReason: str
    StateReasonCode: StateReasonCodeType
    LastUpdateStatus: LastUpdateStatusType
    LastUpdateStatusReason: str
    LastUpdateStatusReasonCode: LastUpdateStatusReasonCodeType
    FileSystemConfigs: List[FileSystemConfig]
    PackageType: PackageTypeType
    ImageConfigResponse: ImageConfigResponse
    SigningProfileVersionArn: str
    SigningJobArn: str
    Architectures: List[ArchitectureType]
    EphemeralStorage: EphemeralStorage
    SnapStart: SnapStartResponse
    RuntimeVersionConfig: RuntimeVersionConfig
    LoggingConfig: LoggingConfig
    ResponseMetadata: ResponseMetadata


class FunctionConfiguration(BaseValidatorModel):
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
    VpcConfig: Optional[VpcConfigResponse] = None
    DeadLetterConfig: Optional[DeadLetterConfig] = None
    Environment: Optional[EnvironmentResponse] = None
    KMSKeyArn: Optional[str] = None
    TracingConfig: Optional[TracingConfigResponse] = None
    MasterArn: Optional[str] = None
    RevisionId: Optional[str] = None
    Layers: Optional[List[Layer]] = None
    State: Optional[StateType] = None
    StateReason: Optional[str] = None
    StateReasonCode: Optional[StateReasonCodeType] = None
    LastUpdateStatus: Optional[LastUpdateStatusType] = None
    LastUpdateStatusReason: Optional[str] = None
    LastUpdateStatusReasonCode: Optional[LastUpdateStatusReasonCodeType] = None
    FileSystemConfigs: Optional[List[FileSystemConfig]] = None
    PackageType: Optional[PackageTypeType] = None
    ImageConfigResponse: Optional[ImageConfigResponse] = None
    SigningProfileVersionArn: Optional[str] = None
    SigningJobArn: Optional[str] = None
    Architectures: Optional[List[ArchitectureType]] = None
    EphemeralStorage: Optional[EphemeralStorage] = None
    SnapStart: Optional[SnapStartResponse] = None
    RuntimeVersionConfig: Optional[RuntimeVersionConfig] = None
    LoggingConfig: Optional[LoggingConfig] = None


class ListFunctionEventInvokeConfigsResponse(BaseValidatorModel):
    FunctionEventInvokeConfigs: List[FunctionEventInvokeConfig]
    NextMarker: str
    ResponseMetadata: ResponseMetadata


class ListEventSourceMappingsResponse(BaseValidatorModel):
    NextMarker: str
    EventSourceMappings: List[EventSourceMappingConfiguration]
    ResponseMetadata: ResponseMetadata


class FilterCriteriaUnion(BaseValidatorModel):
    pass


class Timestamp(BaseValidatorModel):
    pass


class EventSourceMappingMetricsConfigUnion(BaseValidatorModel):
    pass


class SelfManagedEventSourceUnion(BaseValidatorModel):
    pass


class CreateEventSourceMappingRequest(BaseValidatorModel):
    FunctionName: str
    EventSourceArn: Optional[str] = None
    Enabled: Optional[bool] = None
    BatchSize: Optional[int] = None
    FilterCriteria: Optional[FilterCriteriaUnion] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    StartingPosition: Optional[EventSourcePositionType] = None
    StartingPositionTimestamp: Optional[Timestamp] = None
    DestinationConfig: Optional[DestinationConfig] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    BisectBatchOnFunctionError: Optional[bool] = None
    MaximumRetryAttempts: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None
    TumblingWindowInSeconds: Optional[int] = None
    Topics: Optional[Sequence[str]] = None
    Queues: Optional[Sequence[str]] = None
    SourceAccessConfigurations: Optional[Sequence[SourceAccessConfiguration]] = None
    SelfManagedEventSource: Optional[SelfManagedEventSourceUnion] = None
    FunctionResponseTypes: Optional[Sequence[Literal["ReportBatchItemFailures"]]] = None
    AmazonManagedKafkaEventSourceConfig: Optional[AmazonManagedKafkaEventSourceConfig] = None
    SelfManagedKafkaEventSourceConfig: Optional[SelfManagedKafkaEventSourceConfig] = None
    ScalingConfig: Optional[ScalingConfig] = None
    DocumentDBEventSourceConfig: Optional[DocumentDBEventSourceConfig] = None
    KMSKeyArn: Optional[str] = None
    MetricsConfig: Optional[EventSourceMappingMetricsConfigUnion] = None
    ProvisionedPollerConfig: Optional[ProvisionedPollerConfig] = None


class UpdateEventSourceMappingRequest(BaseValidatorModel):
    UUID: str
    FunctionName: Optional[str] = None
    Enabled: Optional[bool] = None
    BatchSize: Optional[int] = None
    FilterCriteria: Optional[FilterCriteriaUnion] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    DestinationConfig: Optional[DestinationConfig] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    BisectBatchOnFunctionError: Optional[bool] = None
    MaximumRetryAttempts: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    SourceAccessConfigurations: Optional[Sequence[SourceAccessConfiguration]] = None
    TumblingWindowInSeconds: Optional[int] = None
    FunctionResponseTypes: Optional[Sequence[Literal["ReportBatchItemFailures"]]] = None
    ScalingConfig: Optional[ScalingConfig] = None
    DocumentDBEventSourceConfig: Optional[DocumentDBEventSourceConfig] = None
    KMSKeyArn: Optional[str] = None
    MetricsConfig: Optional[EventSourceMappingMetricsConfigUnion] = None
    ProvisionedPollerConfig: Optional[ProvisionedPollerConfig] = None


class GetFunctionResponse(BaseValidatorModel):
    Configuration: FunctionConfiguration
    Code: FunctionCodeLocation
    Tags: Dict[str, str]
    TagsError: TagsError
    Concurrency: Concurrency
    ResponseMetadata: ResponseMetadata


class ListFunctionsResponse(BaseValidatorModel):
    NextMarker: str
    Functions: List[FunctionConfiguration]
    ResponseMetadata: ResponseMetadata


class ListVersionsByFunctionResponse(BaseValidatorModel):
    NextMarker: str
    Versions: List[FunctionConfiguration]
    ResponseMetadata: ResponseMetadata


