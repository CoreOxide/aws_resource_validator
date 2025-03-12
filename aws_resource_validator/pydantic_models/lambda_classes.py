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
from aws_resource_validator.pydantic_models.lambda_constants import *

class AccountLimitTypeDef(BaseValidatorModel):
    TotalCodeSize: Optional[int] = None
    CodeSizeUnzipped: Optional[int] = None
    CodeSizeZipped: Optional[int] = None
    ConcurrentExecutions: Optional[int] = None
    UnreservedConcurrentExecutions: Optional[int] = None


class AccountUsageTypeDef(BaseValidatorModel):
    TotalCodeSize: Optional[int] = None
    FunctionCount: Optional[int] = None


class AddLayerVersionPermissionRequestTypeDef(BaseValidatorModel):
    LayerName: str
    VersionNumber: int
    StatementId: str
    Action: str
    Principal: str
    OrganizationId: Optional[str] = None
    RevisionId: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AddPermissionRequestTypeDef(BaseValidatorModel):
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


class AliasRoutingConfigurationOutputTypeDef(BaseValidatorModel):
    AdditionalVersionWeights: Optional[Dict[str, float]] = None


class AliasRoutingConfigurationTypeDef(BaseValidatorModel):
    AdditionalVersionWeights: Optional[Mapping[str, float]] = None


class AllowedPublishersOutputTypeDef(BaseValidatorModel):
    SigningProfileVersionArns: List[str]


class AllowedPublishersTypeDef(BaseValidatorModel):
    SigningProfileVersionArns: Sequence[str]


class AmazonManagedKafkaEventSourceConfigTypeDef(BaseValidatorModel):
    ConsumerGroupId: Optional[str] = None


class CodeSigningPoliciesTypeDef(BaseValidatorModel):
    UntrustedArtifactOnDeployment: Optional[CodeSigningPolicyType] = None


class ConcurrencyTypeDef(BaseValidatorModel):
    ReservedConcurrentExecutions: Optional[int] = None


class CorsOutputTypeDef(BaseValidatorModel):
    AllowCredentials: Optional[bool] = None
    AllowHeaders: Optional[List[str]] = None
    AllowMethods: Optional[List[str]] = None
    AllowOrigins: Optional[List[str]] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None


class CorsTypeDef(BaseValidatorModel):
    AllowCredentials: Optional[bool] = None
    AllowHeaders: Optional[Sequence[str]] = None
    AllowMethods: Optional[Sequence[str]] = None
    AllowOrigins: Optional[Sequence[str]] = None
    ExposeHeaders: Optional[Sequence[str]] = None
    MaxAge: Optional[int] = None


class DocumentDBEventSourceConfigTypeDef(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    CollectionName: Optional[str] = None
    FullDocument: Optional[FullDocumentType] = None


class ProvisionedPollerConfigTypeDef(BaseValidatorModel):
    MinimumPollers: Optional[int] = None
    MaximumPollers: Optional[int] = None


class ScalingConfigTypeDef(BaseValidatorModel):
    MaximumConcurrency: Optional[int] = None


class SelfManagedKafkaEventSourceConfigTypeDef(BaseValidatorModel):
    ConsumerGroupId: Optional[str] = None


class DeadLetterConfigTypeDef(BaseValidatorModel):
    TargetArn: Optional[str] = None


class EnvironmentTypeDef(BaseValidatorModel):
    Variables: Optional[Mapping[str, str]] = None


class EphemeralStorageTypeDef(BaseValidatorModel):
    Size: int


class FileSystemConfigTypeDef(BaseValidatorModel):
    Arn: str
    LocalMountPath: str


class LoggingConfigTypeDef(BaseValidatorModel):
    LogFormat: Optional[LogFormatType] = None
    ApplicationLogLevel: Optional[ApplicationLogLevelType] = None
    SystemLogLevel: Optional[SystemLogLevelType] = None
    LogGroup: Optional[str] = None


class SnapStartTypeDef(BaseValidatorModel):
    ApplyOn: Optional[SnapStartApplyOnType] = None


class TracingConfigTypeDef(BaseValidatorModel):
    Mode: Optional[TracingModeType] = None


class VpcConfigTypeDef(BaseValidatorModel):
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Ipv6AllowedForDualStack: Optional[bool] = None


class DeleteAliasRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Name: str


class DeleteCodeSigningConfigRequestTypeDef(BaseValidatorModel):
    CodeSigningConfigArn: str


class DeleteEventSourceMappingRequestTypeDef(BaseValidatorModel):
    UUID: str


class DeleteFunctionCodeSigningConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str


class DeleteFunctionConcurrencyRequestTypeDef(BaseValidatorModel):
    FunctionName: str


class DeleteFunctionEventInvokeConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class DeleteFunctionRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class DeleteFunctionUrlConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class DeleteLayerVersionRequestTypeDef(BaseValidatorModel):
    LayerName: str
    VersionNumber: int


class DeleteProvisionedConcurrencyConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: str


class OnFailureTypeDef(BaseValidatorModel):
    Destination: Optional[str] = None


class OnSuccessTypeDef(BaseValidatorModel):
    Destination: Optional[str] = None


class EnvironmentErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class EventSourceMappingMetricsConfigOutputTypeDef(BaseValidatorModel):
    Metrics: Optional[List[Literal["EventCount"]]] = None


class FilterCriteriaErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class SelfManagedEventSourceOutputTypeDef(BaseValidatorModel):
    Endpoints: Optional[Dict[Literal["KAFKA_BOOTSTRAP_SERVERS"], List[str]]] = None


class EventSourceMappingMetricsConfigTypeDef(BaseValidatorModel):
    Metrics: Optional[Sequence[Literal["EventCount"]]] = None


class FunctionCodeLocationTypeDef(BaseValidatorModel):
    RepositoryType: Optional[str] = None
    Location: Optional[str] = None
    ImageUri: Optional[str] = None
    ResolvedImageUri: Optional[str] = None
    SourceKMSKeyArn: Optional[str] = None


class LayerTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CodeSize: Optional[int] = None
    SigningProfileVersionArn: Optional[str] = None
    SigningJobArn: Optional[str] = None


class SnapStartResponseTypeDef(BaseValidatorModel):
    ApplyOn: Optional[SnapStartApplyOnType] = None
    OptimizationStatus: Optional[SnapStartOptimizationStatusType] = None


class TracingConfigResponseTypeDef(BaseValidatorModel):
    Mode: Optional[TracingModeType] = None


class VpcConfigResponseTypeDef(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    VpcId: Optional[str] = None
    Ipv6AllowedForDualStack: Optional[bool] = None


class GetAliasRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Name: str


class GetCodeSigningConfigRequestTypeDef(BaseValidatorModel):
    CodeSigningConfigArn: str


class GetEventSourceMappingRequestTypeDef(BaseValidatorModel):
    UUID: str


class GetFunctionCodeSigningConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str


class GetFunctionConcurrencyRequestTypeDef(BaseValidatorModel):
    FunctionName: str


class GetFunctionConfigurationRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetFunctionEventInvokeConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class GetFunctionRecursionConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str


class GetFunctionRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class TagsErrorTypeDef(BaseValidatorModel):
    ErrorCode: str
    Message: str


class GetFunctionUrlConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class GetLayerVersionByArnRequestTypeDef(BaseValidatorModel):
    Arn: str


class GetLayerVersionPolicyRequestTypeDef(BaseValidatorModel):
    LayerName: str
    VersionNumber: int


class GetLayerVersionRequestTypeDef(BaseValidatorModel):
    LayerName: str
    VersionNumber: int


class LayerVersionContentOutputTypeDef(BaseValidatorModel):
    Location: Optional[str] = None
    CodeSha256: Optional[str] = None
    CodeSize: Optional[int] = None
    SigningProfileVersionArn: Optional[str] = None
    SigningJobArn: Optional[str] = None


class GetPolicyRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class GetProvisionedConcurrencyConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: str


class GetRuntimeManagementConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None


class ImageConfigErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class ImageConfigOutputTypeDef(BaseValidatorModel):
    EntryPoint: Optional[List[str]] = None
    Command: Optional[List[str]] = None
    WorkingDirectory: Optional[str] = None


class ImageConfigTypeDef(BaseValidatorModel):
    EntryPoint: Optional[Sequence[str]] = None
    Command: Optional[Sequence[str]] = None
    WorkingDirectory: Optional[str] = None


class InvokeResponseStreamUpdateTypeDef(BaseValidatorModel):
    Payload: Optional[bytes] = None


class InvokeWithResponseStreamCompleteEventTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorDetails: Optional[str] = None
    LogResult: Optional[str] = None


class LayerVersionsListItemTypeDef(BaseValidatorModel):
    LayerVersionArn: Optional[str] = None
    Version: Optional[int] = None
    Description: Optional[str] = None
    CreatedDate: Optional[str] = None
    CompatibleRuntimes: Optional[List[RuntimeType]] = None
    LicenseInfo: Optional[str] = None
    CompatibleArchitectures: Optional[List[ArchitectureType]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAliasesRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    FunctionVersion: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListCodeSigningConfigsRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListEventSourceMappingsRequestTypeDef(BaseValidatorModel):
    EventSourceArn: Optional[str] = None
    FunctionName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListFunctionEventInvokeConfigsRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListFunctionUrlConfigsRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListFunctionsByCodeSigningConfigRequestTypeDef(BaseValidatorModel):
    CodeSigningConfigArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListFunctionsRequestTypeDef(BaseValidatorModel):
    MasterRegion: Optional[str] = None
    FunctionVersion: Optional[Literal["ALL"]] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ListLayerVersionsRequestTypeDef(BaseValidatorModel):
    LayerName: str
    CompatibleRuntime: Optional[RuntimeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None


class ListLayersRequestTypeDef(BaseValidatorModel):
    CompatibleRuntime: Optional[RuntimeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None


class ListProvisionedConcurrencyConfigsRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class ProvisionedConcurrencyConfigListItemTypeDef(BaseValidatorModel):
    FunctionArn: Optional[str] = None
    RequestedProvisionedConcurrentExecutions: Optional[int] = None
    AvailableProvisionedConcurrentExecutions: Optional[int] = None
    AllocatedProvisionedConcurrentExecutions: Optional[int] = None
    Status: Optional[ProvisionedConcurrencyStatusEnumType] = None
    StatusReason: Optional[str] = None
    LastModified: Optional[str] = None


class ListTagsRequestTypeDef(BaseValidatorModel):
    Resource: str


class ListVersionsByFunctionRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None


class PublishVersionRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    CodeSha256: Optional[str] = None
    Description: Optional[str] = None
    RevisionId: Optional[str] = None


class PutFunctionCodeSigningConfigRequestTypeDef(BaseValidatorModel):
    CodeSigningConfigArn: str
    FunctionName: str


class PutFunctionConcurrencyRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    ReservedConcurrentExecutions: int


class PutFunctionRecursionConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    RecursiveLoop: RecursiveLoopType


class PutProvisionedConcurrencyConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: str
    ProvisionedConcurrentExecutions: int


class PutRuntimeManagementConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    UpdateRuntimeOn: UpdateRuntimeOnType
    Qualifier: Optional[str] = None
    RuntimeVersionArn: Optional[str] = None


class RemoveLayerVersionPermissionRequestTypeDef(BaseValidatorModel):
    LayerName: str
    VersionNumber: int
    StatementId: str
    RevisionId: Optional[str] = None


class RemovePermissionRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    StatementId: str
    Qualifier: Optional[str] = None
    RevisionId: Optional[str] = None


class RuntimeVersionErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class SelfManagedEventSourceTypeDef(BaseValidatorModel):
    Endpoints: Optional[Mapping[Literal["KAFKA_BOOTSTRAP_SERVERS"], Sequence[str]]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    Resource: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    Resource: str
    TagKeys: Sequence[str]


class AddLayerVersionPermissionResponseTypeDef(BaseValidatorModel):
    Statement: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class AddPermissionResponseTypeDef(BaseValidatorModel):
    Statement: str
    ResponseMetadata: ResponseMetadataTypeDef


class ConcurrencyResponseTypeDef(BaseValidatorModel):
    ReservedConcurrentExecutions: int
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccountSettingsResponseTypeDef(BaseValidatorModel):
    AccountLimit: AccountLimitTypeDef
    AccountUsage: AccountUsageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetFunctionCodeSigningConfigResponseTypeDef(BaseValidatorModel):
    CodeSigningConfigArn: str
    FunctionName: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetFunctionConcurrencyResponseTypeDef(BaseValidatorModel):
    ReservedConcurrentExecutions: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetFunctionRecursionConfigResponseTypeDef(BaseValidatorModel):
    RecursiveLoop: RecursiveLoopType
    ResponseMetadata: ResponseMetadataTypeDef


class GetLayerVersionPolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetPolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetProvisionedConcurrencyConfigResponseTypeDef(BaseValidatorModel):
    RequestedProvisionedConcurrentExecutions: int
    AvailableProvisionedConcurrentExecutions: int
    AllocatedProvisionedConcurrentExecutions: int
    Status: ProvisionedConcurrencyStatusEnumType
    StatusReason: str
    LastModified: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRuntimeManagementConfigResponseTypeDef(BaseValidatorModel):
    UpdateRuntimeOn: UpdateRuntimeOnType
    RuntimeVersionArn: str
    FunctionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class InvocationResponseTypeDef(BaseValidatorModel):
    StatusCode: int
    FunctionError: str
    LogResult: str
    Payload: StreamingBody
    ExecutedVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class InvokeAsyncResponseTypeDef(BaseValidatorModel):
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef


class ListFunctionsByCodeSigningConfigResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    FunctionArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutFunctionCodeSigningConfigResponseTypeDef(BaseValidatorModel):
    CodeSigningConfigArn: str
    FunctionName: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutFunctionRecursionConfigResponseTypeDef(BaseValidatorModel):
    RecursiveLoop: RecursiveLoopType
    ResponseMetadata: ResponseMetadataTypeDef


class PutProvisionedConcurrencyConfigResponseTypeDef(BaseValidatorModel):
    RequestedProvisionedConcurrentExecutions: int
    AvailableProvisionedConcurrentExecutions: int
    AllocatedProvisionedConcurrentExecutions: int
    Status: ProvisionedConcurrencyStatusEnumType
    StatusReason: str
    LastModified: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutRuntimeManagementConfigResponseTypeDef(BaseValidatorModel):
    UpdateRuntimeOn: UpdateRuntimeOnType
    FunctionArn: str
    RuntimeVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AliasConfigurationResponseTypeDef(BaseValidatorModel):
    AliasArn: str
    Name: str
    FunctionVersion: str
    Description: str
    RoutingConfig: AliasRoutingConfigurationOutputTypeDef
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class AliasConfigurationTypeDef(BaseValidatorModel):
    AliasArn: Optional[str] = None
    Name: Optional[str] = None
    FunctionVersion: Optional[str] = None
    Description: Optional[str] = None
    RoutingConfig: Optional[AliasRoutingConfigurationOutputTypeDef] = None
    RevisionId: Optional[str] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class FunctionCodeTypeDef(BaseValidatorModel):
    ZipFile: Optional[BlobTypeDef] = None
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    ImageUri: Optional[str] = None
    SourceKMSKeyArn: Optional[str] = None


class InvocationRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    InvocationType: Optional[InvocationTypeType] = None
    LogType: Optional[LogTypeType] = None
    ClientContext: Optional[str] = None
    Payload: Optional[BlobTypeDef] = None
    Qualifier: Optional[str] = None


class InvokeAsyncRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    InvokeArgs: BlobTypeDef


class InvokeWithResponseStreamRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    InvocationType: Optional[ResponseStreamingInvocationTypeType] = None
    LogType: Optional[LogTypeType] = None
    ClientContext: Optional[str] = None
    Qualifier: Optional[str] = None
    Payload: Optional[BlobTypeDef] = None


class LayerVersionContentInputTypeDef(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    ZipFile: Optional[BlobTypeDef] = None


class UpdateFunctionCodeRequestTypeDef(BaseValidatorModel):
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
    SourceKMSKeyArn: Optional[str] = None


class CodeSigningConfigTypeDef(BaseValidatorModel):
    CodeSigningConfigId: str
    CodeSigningConfigArn: str
    AllowedPublishers: AllowedPublishersOutputTypeDef
    CodeSigningPolicies: CodeSigningPoliciesTypeDef
    LastModified: str
    Description: Optional[str] = None


class CreateFunctionUrlConfigResponseTypeDef(BaseValidatorModel):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsOutputTypeDef
    CreationTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadataTypeDef


class FunctionUrlConfigTypeDef(BaseValidatorModel):
    FunctionUrl: str
    FunctionArn: str
    CreationTime: str
    LastModifiedTime: str
    AuthType: FunctionUrlAuthTypeType
    Cors: Optional[CorsOutputTypeDef] = None
    InvokeMode: Optional[InvokeModeType] = None


class GetFunctionUrlConfigResponseTypeDef(BaseValidatorModel):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsOutputTypeDef
    CreationTime: str
    LastModifiedTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFunctionUrlConfigResponseTypeDef(BaseValidatorModel):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsOutputTypeDef
    CreationTime: str
    LastModifiedTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadataTypeDef


class DestinationConfigTypeDef(BaseValidatorModel):
    OnSuccess: Optional[OnSuccessTypeDef] = None
    OnFailure: Optional[OnFailureTypeDef] = None


class EnvironmentResponseTypeDef(BaseValidatorModel):
    Variables: Optional[Dict[str, str]] = None
    Error: Optional[EnvironmentErrorTypeDef] = None


class FilterTypeDef(BaseValidatorModel):
    pass


class FilterCriteriaOutputTypeDef(BaseValidatorModel):
    Filters: Optional[List[FilterTypeDef]] = None


class FilterCriteriaTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None


class GetFunctionConfigurationRequestWaitExtraExtraTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetFunctionConfigurationRequestWaitExtraTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetFunctionConfigurationRequestWaitTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetFunctionRequestWaitExtraExtraTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetFunctionRequestWaitExtraTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetFunctionRequestWaitTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetLayerVersionResponseTypeDef(BaseValidatorModel):
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


class PublishLayerVersionResponseTypeDef(BaseValidatorModel):
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


class ImageConfigResponseTypeDef(BaseValidatorModel):
    ImageConfig: Optional[ImageConfigOutputTypeDef] = None
    Error: Optional[ImageConfigErrorTypeDef] = None


class InvokeWithResponseStreamResponseEventTypeDef(BaseValidatorModel):
    PayloadChunk: Optional[InvokeResponseStreamUpdateTypeDef] = None
    InvokeComplete: Optional[InvokeWithResponseStreamCompleteEventTypeDef] = None


class LayersListItemTypeDef(BaseValidatorModel):
    LayerName: Optional[str] = None
    LayerArn: Optional[str] = None
    LatestMatchingVersion: Optional[LayerVersionsListItemTypeDef] = None


class ListLayerVersionsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    LayerVersions: List[LayerVersionsListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListAliasesRequestPaginateTypeDef(BaseValidatorModel):
    FunctionName: str
    FunctionVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCodeSigningConfigsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEventSourceMappingsRequestPaginateTypeDef(BaseValidatorModel):
    EventSourceArn: Optional[str] = None
    FunctionName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFunctionEventInvokeConfigsRequestPaginateTypeDef(BaseValidatorModel):
    FunctionName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFunctionUrlConfigsRequestPaginateTypeDef(BaseValidatorModel):
    FunctionName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFunctionsByCodeSigningConfigRequestPaginateTypeDef(BaseValidatorModel):
    CodeSigningConfigArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFunctionsRequestPaginateTypeDef(BaseValidatorModel):
    MasterRegion: Optional[str] = None
    FunctionVersion: Optional[Literal["ALL"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLayerVersionsRequestPaginateTypeDef(BaseValidatorModel):
    LayerName: str
    CompatibleRuntime: Optional[RuntimeType] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLayersRequestPaginateTypeDef(BaseValidatorModel):
    CompatibleRuntime: Optional[RuntimeType] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProvisionedConcurrencyConfigsRequestPaginateTypeDef(BaseValidatorModel):
    FunctionName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVersionsByFunctionRequestPaginateTypeDef(BaseValidatorModel):
    FunctionName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProvisionedConcurrencyConfigsResponseTypeDef(BaseValidatorModel):
    ProvisionedConcurrencyConfigs: List[ProvisionedConcurrencyConfigListItemTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class RuntimeVersionConfigTypeDef(BaseValidatorModel):
    RuntimeVersionArn: Optional[str] = None
    Error: Optional[RuntimeVersionErrorTypeDef] = None


class ListAliasesResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    Aliases: List[AliasConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AliasRoutingConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateAliasRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Name: str
    FunctionVersion: str
    Description: Optional[str] = None
    RoutingConfig: Optional[AliasRoutingConfigurationUnionTypeDef] = None


class UpdateAliasRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Name: str
    FunctionVersion: Optional[str] = None
    Description: Optional[str] = None
    RoutingConfig: Optional[AliasRoutingConfigurationUnionTypeDef] = None
    RevisionId: Optional[str] = None


class AllowedPublishersUnionTypeDef(BaseValidatorModel):
    pass


class CreateCodeSigningConfigRequestTypeDef(BaseValidatorModel):
    AllowedPublishers: AllowedPublishersUnionTypeDef
    Description: Optional[str] = None
    CodeSigningPolicies: Optional[CodeSigningPoliciesTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateCodeSigningConfigRequestTypeDef(BaseValidatorModel):
    CodeSigningConfigArn: str
    Description: Optional[str] = None
    AllowedPublishers: Optional[AllowedPublishersUnionTypeDef] = None
    CodeSigningPolicies: Optional[CodeSigningPoliciesTypeDef] = None


class PublishLayerVersionRequestTypeDef(BaseValidatorModel):
    LayerName: str
    Content: LayerVersionContentInputTypeDef
    Description: Optional[str] = None
    CompatibleRuntimes: Optional[Sequence[RuntimeType]] = None
    LicenseInfo: Optional[str] = None
    CompatibleArchitectures: Optional[Sequence[ArchitectureType]] = None


class CreateCodeSigningConfigResponseTypeDef(BaseValidatorModel):
    CodeSigningConfig: CodeSigningConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCodeSigningConfigResponseTypeDef(BaseValidatorModel):
    CodeSigningConfig: CodeSigningConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListCodeSigningConfigsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    CodeSigningConfigs: List[CodeSigningConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCodeSigningConfigResponseTypeDef(BaseValidatorModel):
    CodeSigningConfig: CodeSigningConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListFunctionUrlConfigsResponseTypeDef(BaseValidatorModel):
    FunctionUrlConfigs: List[FunctionUrlConfigTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class CorsUnionTypeDef(BaseValidatorModel):
    pass


class CreateFunctionUrlConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    AuthType: FunctionUrlAuthTypeType
    Qualifier: Optional[str] = None
    Cors: Optional[CorsUnionTypeDef] = None
    InvokeMode: Optional[InvokeModeType] = None


class UpdateFunctionUrlConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    AuthType: Optional[FunctionUrlAuthTypeType] = None
    Cors: Optional[CorsUnionTypeDef] = None
    InvokeMode: Optional[InvokeModeType] = None


class FunctionEventInvokeConfigResponseTypeDef(BaseValidatorModel):
    LastModified: datetime
    FunctionArn: str
    MaximumRetryAttempts: int
    MaximumEventAgeInSeconds: int
    DestinationConfig: DestinationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FunctionEventInvokeConfigTypeDef(BaseValidatorModel):
    LastModified: Optional[datetime] = None
    FunctionArn: Optional[str] = None
    MaximumRetryAttempts: Optional[int] = None
    MaximumEventAgeInSeconds: Optional[int] = None
    DestinationConfig: Optional[DestinationConfigTypeDef] = None


class PutFunctionEventInvokeConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    MaximumRetryAttempts: Optional[int] = None
    MaximumEventAgeInSeconds: Optional[int] = None
    DestinationConfig: Optional[DestinationConfigTypeDef] = None


class UpdateFunctionEventInvokeConfigRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    MaximumRetryAttempts: Optional[int] = None
    MaximumEventAgeInSeconds: Optional[int] = None
    DestinationConfig: Optional[DestinationConfigTypeDef] = None


class SourceAccessConfigurationTypeDef(BaseValidatorModel):
    pass


class EventSourceMappingConfigurationResponseTypeDef(BaseValidatorModel):
    UUID: str
    StartingPosition: EventSourcePositionType
    StartingPositionTimestamp: datetime
    BatchSize: int
    MaximumBatchingWindowInSeconds: int
    ParallelizationFactor: int
    EventSourceArn: str
    FilterCriteria: FilterCriteriaOutputTypeDef
    FunctionArn: str
    LastModified: datetime
    LastProcessingResult: str
    State: str
    StateTransitionReason: str
    DestinationConfig: DestinationConfigTypeDef
    Topics: List[str]
    Queues: List[str]
    SourceAccessConfigurations: List[SourceAccessConfigurationTypeDef]
    SelfManagedEventSource: SelfManagedEventSourceOutputTypeDef
    MaximumRecordAgeInSeconds: int
    BisectBatchOnFunctionError: bool
    MaximumRetryAttempts: int
    TumblingWindowInSeconds: int
    FunctionResponseTypes: List[Literal["ReportBatchItemFailures"]]
    AmazonManagedKafkaEventSourceConfig: AmazonManagedKafkaEventSourceConfigTypeDef
    SelfManagedKafkaEventSourceConfig: SelfManagedKafkaEventSourceConfigTypeDef
    ScalingConfig: ScalingConfigTypeDef
    DocumentDBEventSourceConfig: DocumentDBEventSourceConfigTypeDef
    KMSKeyArn: str
    FilterCriteriaError: FilterCriteriaErrorTypeDef
    EventSourceMappingArn: str
    MetricsConfig: EventSourceMappingMetricsConfigOutputTypeDef
    ProvisionedPollerConfig: ProvisionedPollerConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EventSourceMappingConfigurationTypeDef(BaseValidatorModel):
    UUID: Optional[str] = None
    StartingPosition: Optional[EventSourcePositionType] = None
    StartingPositionTimestamp: Optional[datetime] = None
    BatchSize: Optional[int] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    EventSourceArn: Optional[str] = None
    FilterCriteria: Optional[FilterCriteriaOutputTypeDef] = None
    FunctionArn: Optional[str] = None
    LastModified: Optional[datetime] = None
    LastProcessingResult: Optional[str] = None
    State: Optional[str] = None
    StateTransitionReason: Optional[str] = None
    DestinationConfig: Optional[DestinationConfigTypeDef] = None
    Topics: Optional[List[str]] = None
    Queues: Optional[List[str]] = None
    SourceAccessConfigurations: Optional[List[SourceAccessConfigurationTypeDef]] = None
    SelfManagedEventSource: Optional[SelfManagedEventSourceOutputTypeDef] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    BisectBatchOnFunctionError: Optional[bool] = None
    MaximumRetryAttempts: Optional[int] = None
    TumblingWindowInSeconds: Optional[int] = None
    FunctionResponseTypes: Optional[List[Literal["ReportBatchItemFailures"]]] = None
    AmazonManagedKafkaEventSourceConfig: Optional[AmazonManagedKafkaEventSourceConfigTypeDef] = None
    SelfManagedKafkaEventSourceConfig: Optional[SelfManagedKafkaEventSourceConfigTypeDef] = None
    ScalingConfig: Optional[ScalingConfigTypeDef] = None
    DocumentDBEventSourceConfig: Optional[DocumentDBEventSourceConfigTypeDef] = None
    KMSKeyArn: Optional[str] = None
    FilterCriteriaError: Optional[FilterCriteriaErrorTypeDef] = None
    EventSourceMappingArn: Optional[str] = None
    MetricsConfig: Optional[EventSourceMappingMetricsConfigOutputTypeDef] = None
    ProvisionedPollerConfig: Optional[ProvisionedPollerConfigTypeDef] = None


class ImageConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateFunctionRequestTypeDef(BaseValidatorModel):
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
    ImageConfig: Optional[ImageConfigUnionTypeDef] = None
    CodeSigningConfigArn: Optional[str] = None
    Architectures: Optional[Sequence[ArchitectureType]] = None
    EphemeralStorage: Optional[EphemeralStorageTypeDef] = None
    SnapStart: Optional[SnapStartTypeDef] = None
    LoggingConfig: Optional[LoggingConfigTypeDef] = None


class UpdateFunctionConfigurationRequestTypeDef(BaseValidatorModel):
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
    ImageConfig: Optional[ImageConfigUnionTypeDef] = None
    EphemeralStorage: Optional[EphemeralStorageTypeDef] = None
    SnapStart: Optional[SnapStartTypeDef] = None
    LoggingConfig: Optional[LoggingConfigTypeDef] = None


class InvokeWithResponseStreamResponseTypeDef(BaseValidatorModel):
    StatusCode: int
    ExecutedVersion: str
    EventStream: EventStream[InvokeWithResponseStreamResponseEventTypeDef]
    ResponseStreamContentType: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListLayersResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    Layers: List[LayersListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class FunctionConfigurationResponseTypeDef(BaseValidatorModel):
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


class FunctionConfigurationTypeDef(BaseValidatorModel):
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


class ListFunctionEventInvokeConfigsResponseTypeDef(BaseValidatorModel):
    FunctionEventInvokeConfigs: List[FunctionEventInvokeConfigTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListEventSourceMappingsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    EventSourceMappings: List[EventSourceMappingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class FilterCriteriaUnionTypeDef(BaseValidatorModel):
    pass


class TimestampTypeDef(BaseValidatorModel):
    pass


class EventSourceMappingMetricsConfigUnionTypeDef(BaseValidatorModel):
    pass


class SelfManagedEventSourceUnionTypeDef(BaseValidatorModel):
    pass


class CreateEventSourceMappingRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    EventSourceArn: Optional[str] = None
    Enabled: Optional[bool] = None
    BatchSize: Optional[int] = None
    FilterCriteria: Optional[FilterCriteriaUnionTypeDef] = None
    MaximumBatchingWindowInSeconds: Optional[int] = None
    ParallelizationFactor: Optional[int] = None
    StartingPosition: Optional[EventSourcePositionType] = None
    StartingPositionTimestamp: Optional[TimestampTypeDef] = None
    DestinationConfig: Optional[DestinationConfigTypeDef] = None
    MaximumRecordAgeInSeconds: Optional[int] = None
    BisectBatchOnFunctionError: Optional[bool] = None
    MaximumRetryAttempts: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None
    TumblingWindowInSeconds: Optional[int] = None
    Topics: Optional[Sequence[str]] = None
    Queues: Optional[Sequence[str]] = None
    SourceAccessConfigurations: Optional[Sequence[SourceAccessConfigurationTypeDef]] = None
    SelfManagedEventSource: Optional[SelfManagedEventSourceUnionTypeDef] = None
    FunctionResponseTypes: Optional[Sequence[Literal["ReportBatchItemFailures"]]] = None
    AmazonManagedKafkaEventSourceConfig: Optional[AmazonManagedKafkaEventSourceConfigTypeDef] = None
    SelfManagedKafkaEventSourceConfig: Optional[SelfManagedKafkaEventSourceConfigTypeDef] = None
    ScalingConfig: Optional[ScalingConfigTypeDef] = None
    DocumentDBEventSourceConfig: Optional[DocumentDBEventSourceConfigTypeDef] = None
    KMSKeyArn: Optional[str] = None
    MetricsConfig: Optional[EventSourceMappingMetricsConfigUnionTypeDef] = None
    ProvisionedPollerConfig: Optional[ProvisionedPollerConfigTypeDef] = None


class UpdateEventSourceMappingRequestTypeDef(BaseValidatorModel):
    UUID: str
    FunctionName: Optional[str] = None
    Enabled: Optional[bool] = None
    BatchSize: Optional[int] = None
    FilterCriteria: Optional[FilterCriteriaUnionTypeDef] = None
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
    KMSKeyArn: Optional[str] = None
    MetricsConfig: Optional[EventSourceMappingMetricsConfigUnionTypeDef] = None
    ProvisionedPollerConfig: Optional[ProvisionedPollerConfigTypeDef] = None


class GetFunctionResponseTypeDef(BaseValidatorModel):
    Configuration: FunctionConfigurationTypeDef
    Code: FunctionCodeLocationTypeDef
    Tags: Dict[str, str]
    TagsError: TagsErrorTypeDef
    Concurrency: ConcurrencyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListFunctionsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    Functions: List[FunctionConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListVersionsByFunctionResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    Versions: List[FunctionConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


