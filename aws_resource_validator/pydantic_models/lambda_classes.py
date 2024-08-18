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
from botocore.response import StreamingBody
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

class AddLayerVersionPermissionRequestRequestTypeDef(BaseValidatorModel):
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

class AddPermissionRequestRequestTypeDef(BaseValidatorModel):
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

class AliasRoutingConfigurationPaginatorTypeDef(BaseValidatorModel):
    AdditionalVersionWeights: Optional[Dict[str, float]] = None

class AliasRoutingConfigurationTypeDef(BaseValidatorModel):
    AdditionalVersionWeights: Optional[Mapping[str, float]] = None

class AllowedPublishersPaginatorTypeDef(BaseValidatorModel):
    SigningProfileVersionArns: List[str]

class AllowedPublishersTypeDef(BaseValidatorModel):
    SigningProfileVersionArns: Sequence[str]

class AmazonManagedKafkaEventSourceConfigTypeDef(BaseValidatorModel):
    ConsumerGroupId: Optional[str] = None

class CodeSigningPoliciesTypeDef(BaseValidatorModel):
    UntrustedArtifactOnDeployment: Optional[CodeSigningPolicyType] = None

class ConcurrencyTypeDef(BaseValidatorModel):
    ReservedConcurrentExecutions: Optional[int] = None

class CorsPaginatorTypeDef(BaseValidatorModel):
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

class ScalingConfigTypeDef(BaseValidatorModel):
    MaximumConcurrency: Optional[int] = None

class SelfManagedEventSourceTypeDef(BaseValidatorModel):
    Endpoints: Optional[Mapping[Literal["KAFKA_BOOTSTRAP_SERVERS"], Sequence[str]]] = None

class SelfManagedKafkaEventSourceConfigTypeDef(BaseValidatorModel):
    ConsumerGroupId: Optional[str] = None

class SourceAccessConfigurationTypeDef(BaseValidatorModel):
    Type: Optional[SourceAccessTypeType] = None
    URI: Optional[str] = None

class DeadLetterConfigTypeDef(BaseValidatorModel):
    TargetArn: Optional[str] = None

class EnvironmentTypeDef(BaseValidatorModel):
    Variables: Optional[Mapping[str, str]] = None

class EphemeralStorageTypeDef(BaseValidatorModel):
    Size: int

class FileSystemConfigTypeDef(BaseValidatorModel):
    Arn: str
    LocalMountPath: str

class ImageConfigTypeDef(BaseValidatorModel):
    EntryPoint: Optional[Sequence[str]] = None
    Command: Optional[Sequence[str]] = None
    WorkingDirectory: Optional[str] = None

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

class DeleteAliasRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Name: str

class DeleteCodeSigningConfigRequestRequestTypeDef(BaseValidatorModel):
    CodeSigningConfigArn: str

class DeleteEventSourceMappingRequestRequestTypeDef(BaseValidatorModel):
    UUID: str

class DeleteFunctionCodeSigningConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str

class DeleteFunctionConcurrencyRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str

class DeleteFunctionEventInvokeConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class DeleteFunctionRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class DeleteFunctionUrlConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class DeleteLayerVersionRequestRequestTypeDef(BaseValidatorModel):
    LayerName: str
    VersionNumber: int

class DeleteProvisionedConcurrencyConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: str

class OnFailureTypeDef(BaseValidatorModel):
    Destination: Optional[str] = None

class OnSuccessTypeDef(BaseValidatorModel):
    Destination: Optional[str] = None

class EnvironmentErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None

class SelfManagedEventSourcePaginatorTypeDef(BaseValidatorModel):
    Endpoints: Optional[Dict[Literal["KAFKA_BOOTSTRAP_SERVERS"], List[str]]] = None

class FilterTypeDef(BaseValidatorModel):
    Pattern: Optional[str] = None

class FunctionCodeLocationTypeDef(BaseValidatorModel):
    RepositoryType: Optional[str] = None
    Location: Optional[str] = None
    ImageUri: Optional[str] = None
    ResolvedImageUri: Optional[str] = None

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

class GetAliasRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Name: str

class GetCodeSigningConfigRequestRequestTypeDef(BaseValidatorModel):
    CodeSigningConfigArn: str

class GetEventSourceMappingRequestRequestTypeDef(BaseValidatorModel):
    UUID: str

class GetFunctionCodeSigningConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str

class GetFunctionConcurrencyRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetFunctionConfigurationRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class GetFunctionEventInvokeConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class GetFunctionRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class GetFunctionUrlConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class GetLayerVersionByArnRequestRequestTypeDef(BaseValidatorModel):
    Arn: str

class GetLayerVersionPolicyRequestRequestTypeDef(BaseValidatorModel):
    LayerName: str
    VersionNumber: int

class GetLayerVersionRequestRequestTypeDef(BaseValidatorModel):
    LayerName: str
    VersionNumber: int

class LayerVersionContentOutputTypeDef(BaseValidatorModel):
    Location: Optional[str] = None
    CodeSha256: Optional[str] = None
    CodeSize: Optional[int] = None
    SigningProfileVersionArn: Optional[str] = None
    SigningJobArn: Optional[str] = None

class GetPolicyRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class GetProvisionedConcurrencyConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: str

class GetRuntimeManagementConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None

class ImageConfigErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None

class ImageConfigPaginatorTypeDef(BaseValidatorModel):
    EntryPoint: Optional[List[str]] = None
    Command: Optional[List[str]] = None
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

class ListAliasesRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    FunctionVersion: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListCodeSigningConfigsRequestRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListEventSourceMappingsRequestRequestTypeDef(BaseValidatorModel):
    EventSourceArn: Optional[str] = None
    FunctionName: Optional[str] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListFunctionEventInvokeConfigsRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListFunctionUrlConfigsRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListFunctionsByCodeSigningConfigRequestRequestTypeDef(BaseValidatorModel):
    CodeSigningConfigArn: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListFunctionsRequestRequestTypeDef(BaseValidatorModel):
    MasterRegion: Optional[str] = None
    FunctionVersion: Optional[Literal["ALL"]] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class ListLayerVersionsRequestRequestTypeDef(BaseValidatorModel):
    LayerName: str
    CompatibleRuntime: Optional[RuntimeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None

class ListLayersRequestRequestTypeDef(BaseValidatorModel):
    CompatibleRuntime: Optional[RuntimeType] = None
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None

class ListProvisionedConcurrencyConfigsRequestRequestTypeDef(BaseValidatorModel):
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

class ListTagsRequestRequestTypeDef(BaseValidatorModel):
    Resource: str

class ListVersionsByFunctionRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Marker: Optional[str] = None
    MaxItems: Optional[int] = None

class PublishVersionRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    CodeSha256: Optional[str] = None
    Description: Optional[str] = None
    RevisionId: Optional[str] = None

class PutFunctionCodeSigningConfigRequestRequestTypeDef(BaseValidatorModel):
    CodeSigningConfigArn: str
    FunctionName: str

class PutFunctionConcurrencyRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    ReservedConcurrentExecutions: int

class PutProvisionedConcurrencyConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: str
    ProvisionedConcurrentExecutions: int

class PutRuntimeManagementConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    UpdateRuntimeOn: UpdateRuntimeOnType
    Qualifier: Optional[str] = None
    RuntimeVersionArn: Optional[str] = None

class RemoveLayerVersionPermissionRequestRequestTypeDef(BaseValidatorModel):
    LayerName: str
    VersionNumber: int
    StatementId: str
    RevisionId: Optional[str] = None

class RemovePermissionRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    StatementId: str
    Qualifier: Optional[str] = None
    RevisionId: Optional[str] = None

class RuntimeVersionErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    Resource: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
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

class AliasConfigurationPaginatorTypeDef(BaseValidatorModel):
    AliasArn: Optional[str] = None
    Name: Optional[str] = None
    FunctionVersion: Optional[str] = None
    Description: Optional[str] = None
    RoutingConfig: Optional[AliasRoutingConfigurationPaginatorTypeDef] = None
    RevisionId: Optional[str] = None

class AliasConfigurationResponseTypeDef(BaseValidatorModel):
    AliasArn: str
    Name: str
    FunctionVersion: str
    Description: str
    RoutingConfig: AliasRoutingConfigurationTypeDef
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AliasConfigurationTypeDef(BaseValidatorModel):
    AliasArn: Optional[str] = None
    Name: Optional[str] = None
    FunctionVersion: Optional[str] = None
    Description: Optional[str] = None
    RoutingConfig: Optional[AliasRoutingConfigurationTypeDef] = None
    RevisionId: Optional[str] = None

class CreateAliasRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Name: str
    FunctionVersion: str
    Description: Optional[str] = None
    RoutingConfig: Optional[AliasRoutingConfigurationTypeDef] = None

class UpdateAliasRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Name: str
    FunctionVersion: Optional[str] = None
    Description: Optional[str] = None
    RoutingConfig: Optional[AliasRoutingConfigurationTypeDef] = None
    RevisionId: Optional[str] = None

class FunctionCodeTypeDef(BaseValidatorModel):
    ZipFile: Optional[BlobTypeDef] = None
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    ImageUri: Optional[str] = None

class InvocationRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    InvocationType: Optional[InvocationTypeType] = None
    LogType: Optional[LogTypeType] = None
    ClientContext: Optional[str] = None
    Payload: Optional[BlobTypeDef] = None
    Qualifier: Optional[str] = None

class InvokeAsyncRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    InvokeArgs: BlobTypeDef

class InvokeWithResponseStreamRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateFunctionCodeRequestRequestTypeDef(BaseValidatorModel):
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

class CodeSigningConfigPaginatorTypeDef(BaseValidatorModel):
    CodeSigningConfigId: str
    CodeSigningConfigArn: str
    AllowedPublishers: AllowedPublishersPaginatorTypeDef
    CodeSigningPolicies: CodeSigningPoliciesTypeDef
    LastModified: str
    Description: Optional[str] = None

class CodeSigningConfigTypeDef(BaseValidatorModel):
    CodeSigningConfigId: str
    CodeSigningConfigArn: str
    AllowedPublishers: AllowedPublishersTypeDef
    CodeSigningPolicies: CodeSigningPoliciesTypeDef
    LastModified: str
    Description: Optional[str] = None

class CreateCodeSigningConfigRequestRequestTypeDef(BaseValidatorModel):
    AllowedPublishers: AllowedPublishersTypeDef
    Description: Optional[str] = None
    CodeSigningPolicies: Optional[CodeSigningPoliciesTypeDef] = None

class UpdateCodeSigningConfigRequestRequestTypeDef(BaseValidatorModel):
    CodeSigningConfigArn: str
    Description: Optional[str] = None
    AllowedPublishers: Optional[AllowedPublishersTypeDef] = None
    CodeSigningPolicies: Optional[CodeSigningPoliciesTypeDef] = None

class FunctionUrlConfigPaginatorTypeDef(BaseValidatorModel):
    FunctionUrl: str
    FunctionArn: str
    CreationTime: str
    LastModifiedTime: str
    AuthType: FunctionUrlAuthTypeType
    Cors: Optional[CorsPaginatorTypeDef] = None
    InvokeMode: Optional[InvokeModeType] = None

class CreateFunctionUrlConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    AuthType: FunctionUrlAuthTypeType
    Qualifier: Optional[str] = None
    Cors: Optional[CorsTypeDef] = None
    InvokeMode: Optional[InvokeModeType] = None

class CreateFunctionUrlConfigResponseTypeDef(BaseValidatorModel):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsTypeDef
    CreationTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionUrlConfigTypeDef(BaseValidatorModel):
    FunctionUrl: str
    FunctionArn: str
    CreationTime: str
    LastModifiedTime: str
    AuthType: FunctionUrlAuthTypeType
    Cors: Optional[CorsTypeDef] = None
    InvokeMode: Optional[InvokeModeType] = None

class GetFunctionUrlConfigResponseTypeDef(BaseValidatorModel):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsTypeDef
    CreationTime: str
    LastModifiedTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFunctionUrlConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    AuthType: Optional[FunctionUrlAuthTypeType] = None
    Cors: Optional[CorsTypeDef] = None
    InvokeMode: Optional[InvokeModeType] = None

class UpdateFunctionUrlConfigResponseTypeDef(BaseValidatorModel):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsTypeDef
    CreationTime: str
    LastModifiedTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFunctionConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class DestinationConfigTypeDef(BaseValidatorModel):
    OnSuccess: Optional[OnSuccessTypeDef] = None
    OnFailure: Optional[OnFailureTypeDef] = None

class EnvironmentResponseTypeDef(BaseValidatorModel):
    Variables: Optional[Dict[str, str]] = None
    Error: Optional[EnvironmentErrorTypeDef] = None

class FilterCriteriaPaginatorTypeDef(BaseValidatorModel):
    Filters: Optional[List[FilterTypeDef]] = None

class FilterCriteriaTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None

class GetFunctionConfigurationRequestFunctionActiveWaitTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetFunctionConfigurationRequestFunctionUpdatedWaitTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetFunctionConfigurationRequestPublishedVersionActiveWaitTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetFunctionRequestFunctionActiveV2WaitTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetFunctionRequestFunctionExistsWaitTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetFunctionRequestFunctionUpdatedV2WaitTypeDef(BaseValidatorModel):
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
    ImageConfig: Optional[ImageConfigTypeDef] = None
    Error: Optional[ImageConfigErrorTypeDef] = None

class ImageConfigResponsePaginatorTypeDef(BaseValidatorModel):
    ImageConfig: Optional[ImageConfigPaginatorTypeDef] = None
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

class ListAliasesRequestListAliasesPaginateTypeDef(BaseValidatorModel):
    FunctionName: str
    FunctionVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCodeSigningConfigsRequestListCodeSigningConfigsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventSourceMappingsRequestListEventSourceMappingsPaginateTypeDef(BaseValidatorModel):
    EventSourceArn: Optional[str] = None
    FunctionName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFunctionEventInvokeConfigsRequestListFunctionEventInvokeConfigsPaginateTypeDef(BaseValidatorModel):
    FunctionName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFunctionUrlConfigsRequestListFunctionUrlConfigsPaginateTypeDef(BaseValidatorModel):
    FunctionName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFunctionsByCodeSigningConfigRequestListFunctionsByCodeSigningConfigPaginateTypeDef(BaseValidatorModel):
    CodeSigningConfigArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFunctionsRequestListFunctionsPaginateTypeDef(BaseValidatorModel):
    MasterRegion: Optional[str] = None
    FunctionVersion: Optional[Literal["ALL"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLayerVersionsRequestListLayerVersionsPaginateTypeDef(BaseValidatorModel):
    LayerName: str
    CompatibleRuntime: Optional[RuntimeType] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLayersRequestListLayersPaginateTypeDef(BaseValidatorModel):
    CompatibleRuntime: Optional[RuntimeType] = None
    CompatibleArchitecture: Optional[ArchitectureType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVersionsByFunctionRequestListVersionsByFunctionPaginateTypeDef(BaseValidatorModel):
    FunctionName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProvisionedConcurrencyConfigsResponseTypeDef(BaseValidatorModel):
    ProvisionedConcurrencyConfigs: List[ProvisionedConcurrencyConfigListItemTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class RuntimeVersionConfigTypeDef(BaseValidatorModel):
    RuntimeVersionArn: Optional[str] = None
    Error: Optional[RuntimeVersionErrorTypeDef] = None

class ListAliasesResponsePaginatorTypeDef(BaseValidatorModel):
    NextMarker: str
    Aliases: List[AliasConfigurationPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    Aliases: List[AliasConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionRequestRequestTypeDef(BaseValidatorModel):
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

class PublishLayerVersionRequestRequestTypeDef(BaseValidatorModel):
    LayerName: str
    Content: LayerVersionContentInputTypeDef
    Description: Optional[str] = None
    CompatibleRuntimes: Optional[Sequence[RuntimeType]] = None
    LicenseInfo: Optional[str] = None
    CompatibleArchitectures: Optional[Sequence[ArchitectureType]] = None

class ListCodeSigningConfigsResponsePaginatorTypeDef(BaseValidatorModel):
    NextMarker: str
    CodeSigningConfigs: List[CodeSigningConfigPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListFunctionUrlConfigsResponsePaginatorTypeDef(BaseValidatorModel):
    FunctionUrlConfigs: List[FunctionUrlConfigPaginatorTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionUrlConfigsResponseTypeDef(BaseValidatorModel):
    FunctionUrlConfigs: List[FunctionUrlConfigTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class PutFunctionEventInvokeConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    MaximumRetryAttempts: Optional[int] = None
    MaximumEventAgeInSeconds: Optional[int] = None
    DestinationConfig: Optional[DestinationConfigTypeDef] = None

class UpdateFunctionEventInvokeConfigRequestRequestTypeDef(BaseValidatorModel):
    FunctionName: str
    Qualifier: Optional[str] = None
    MaximumRetryAttempts: Optional[int] = None
    MaximumEventAgeInSeconds: Optional[int] = None
    DestinationConfig: Optional[DestinationConfigTypeDef] = None

class EventSourceMappingConfigurationPaginatorTypeDef(BaseValidatorModel):
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

class CreateEventSourceMappingRequestRequestTypeDef(BaseValidatorModel):
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

class EventSourceMappingConfigurationResponseTypeDef(BaseValidatorModel):
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

class EventSourceMappingConfigurationTypeDef(BaseValidatorModel):
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

class UpdateEventSourceMappingRequestRequestTypeDef(BaseValidatorModel):
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

class InvokeWithResponseStreamResponseTypeDef(BaseValidatorModel):
    StatusCode: int
    ExecutedVersion: str
    EventStream: "EventStream[InvokeWithResponseStreamResponseEventTypeDef]"
    ResponseStreamContentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLayersResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    Layers: List[LayersListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionConfigurationPaginatorTypeDef(BaseValidatorModel):
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

class ListEventSourceMappingsResponsePaginatorTypeDef(BaseValidatorModel):
    NextMarker: str
    EventSourceMappings: List[EventSourceMappingConfigurationPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventSourceMappingsResponseTypeDef(BaseValidatorModel):
    NextMarker: str
    EventSourceMappings: List[EventSourceMappingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionsResponsePaginatorTypeDef(BaseValidatorModel):
    NextMarker: str
    Functions: List[FunctionConfigurationPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVersionsByFunctionResponsePaginatorTypeDef(BaseValidatorModel):
    NextMarker: str
    Versions: List[FunctionConfigurationPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionResponseTypeDef(BaseValidatorModel):
    Configuration: FunctionConfigurationTypeDef
    Code: FunctionCodeLocationTypeDef
    Tags: Dict[str, str]
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

