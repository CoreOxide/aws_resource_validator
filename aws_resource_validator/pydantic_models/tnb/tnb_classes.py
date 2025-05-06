from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.tnb.tnb_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Blob = Union[str, bytes, IO[Any], StreamingBody]


class CancelSolNetworkOperationInput(BaseValidatorModel):
    nsLcmOpOccId: str


class CreateSolFunctionPackageInput(BaseValidatorModel):
    tags: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateSolNetworkInstanceInput(BaseValidatorModel):
    nsName: str
    nsdInfoId: str
    nsDescription: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateSolNetworkPackageInput(BaseValidatorModel):
    tags: Optional[Dict[str, str]] = None


class DeleteSolFunctionPackageInput(BaseValidatorModel):
    vnfPkgId: str


class DeleteSolNetworkInstanceInput(BaseValidatorModel):
    nsInstanceId: str


class DeleteSolNetworkPackageInput(BaseValidatorModel):
    nsdInfoId: str


class ErrorInfo(BaseValidatorModel):
    cause: Optional[str] = None
    details: Optional[str] = None


class ToscaOverride(BaseValidatorModel):
    defaultValue: Optional[str] = None
    name: Optional[str] = None


class GetSolFunctionInstanceInput(BaseValidatorModel):
    vnfInstanceId: str


class GetSolFunctionInstanceMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


class GetSolFunctionPackageContentInput(BaseValidatorModel):
    accept: Literal['application/zip']
    vnfPkgId: str


class GetSolFunctionPackageDescriptorInput(BaseValidatorModel):
    accept: Literal['text/plain']
    vnfPkgId: str


class GetSolFunctionPackageInput(BaseValidatorModel):
    vnfPkgId: str


class GetSolInstantiatedVnfInfo(BaseValidatorModel):
    vnfState: Optional[VnfOperationalStateType] = None


class GetSolNetworkInstanceInput(BaseValidatorModel):
    nsInstanceId: str


class GetSolNetworkInstanceMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


class LcmOperationInfo(BaseValidatorModel):
    nsLcmOpOccId: str


class GetSolNetworkOperationInput(BaseValidatorModel):
    nsLcmOpOccId: str


class InstantiateMetadata(BaseValidatorModel):
    nsdInfoId: str
    additionalParamsForNs: Optional[Dict[str, Any]] = None


class ModifyVnfInfoMetadata(BaseValidatorModel):
    vnfConfigurableProperties: Dict[str, Any]
    vnfInstanceId: str


class UpdateNsMetadata(BaseValidatorModel):
    nsdInfoId: str
    additionalParamsForNs: Optional[Dict[str, Any]] = None


class ProblemDetails(BaseValidatorModel):
    detail: str
    title: Optional[str] = None


class GetSolNetworkPackageContentInput(BaseValidatorModel):
    accept: Literal['application/zip']
    nsdInfoId: str


class GetSolNetworkPackageDescriptorInput(BaseValidatorModel):
    nsdInfoId: str


class GetSolNetworkPackageInput(BaseValidatorModel):
    nsdInfoId: str


class GetSolVnfcResourceInfoMetadata(BaseValidatorModel):
    cluster: Optional[str] = None
    helmChart: Optional[str] = None
    nodeGroup: Optional[str] = None


class InstantiateSolNetworkInstanceInput(BaseValidatorModel):
    nsInstanceId: str
    additionalParamsForNs: Optional[Dict[str, Any]] = None
    dryRun: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None


class ListSolFunctionInstanceMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListSolFunctionInstancesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSolFunctionPackageMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


class ListSolFunctionPackagesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSolNetworkInstanceMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


class ListSolNetworkInstancesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSolNetworkOperationsMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime
    nsdInfoId: Optional[str] = None
    vnfInstanceId: Optional[str] = None


class ListSolNetworkOperationsInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    nsInstanceId: Optional[str] = None


class ListSolNetworkPackageMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


class ListSolNetworkPackagesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class TerminateSolNetworkInstanceInput(BaseValidatorModel):
    nsInstanceId: str
    tags: Optional[Dict[str, str]] = None


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateSolFunctionPackageInput(BaseValidatorModel):
    operationalState: OperationalStateType
    vnfPkgId: str


class UpdateSolNetworkModify(BaseValidatorModel):
    vnfConfigurableProperties: Dict[str, Any]
    vnfInstanceId: str


class UpdateSolNetworkServiceData(BaseValidatorModel):
    nsdInfoId: str
    additionalParamsForNs: Optional[Dict[str, Any]] = None


class UpdateSolNetworkPackageInput(BaseValidatorModel):
    nsdInfoId: str
    nsdOperationalState: NsdOperationalStateType


class PutSolFunctionPackageContentInput(BaseValidatorModel):
    file: Blob
    vnfPkgId: str
    contentType: Optional[Literal['application/zip']] = None


class PutSolNetworkPackageContentInput(BaseValidatorModel):
    file: Blob
    nsdInfoId: str
    contentType: Optional[Literal['application/zip']] = None


class ValidateSolFunctionPackageContentInput(BaseValidatorModel):
    file: Blob
    vnfPkgId: str
    contentType: Optional[Literal['application/zip']] = None


class ValidateSolNetworkPackageContentInput(BaseValidatorModel):
    file: Blob
    nsdInfoId: str
    contentType: Optional[Literal['application/zip']] = None


class CreateSolFunctionPackageOutput(BaseValidatorModel):
    arn: str
    id: str
    onboardingState: OnboardingStateType
    operationalState: OperationalStateType
    tags: Dict[str, str]
    usageState: UsageStateType
    ResponseMetadata: ResponseMetadata


class CreateSolNetworkInstanceOutput(BaseValidatorModel):
    arn: str
    id: str
    nsInstanceName: str
    nsdInfoId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateSolNetworkPackageOutput(BaseValidatorModel):
    arn: str
    id: str
    nsdOnboardingState: NsdOnboardingStateType
    nsdOperationalState: NsdOperationalStateType
    nsdUsageState: NsdUsageStateType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetSolFunctionPackageContentOutput(BaseValidatorModel):
    contentType: Literal['application/zip']
    packageContent: StreamingBody
    ResponseMetadata: ResponseMetadata


class GetSolFunctionPackageDescriptorOutput(BaseValidatorModel):
    contentType: Literal['text/plain']
    vnfd: StreamingBody
    ResponseMetadata: ResponseMetadata


class GetSolNetworkPackageContentOutput(BaseValidatorModel):
    contentType: Literal['application/zip']
    nsdContent: StreamingBody
    ResponseMetadata: ResponseMetadata


class GetSolNetworkPackageDescriptorOutput(BaseValidatorModel):
    contentType: Literal['text/plain']
    nsd: StreamingBody
    ResponseMetadata: ResponseMetadata


class InstantiateSolNetworkInstanceOutput(BaseValidatorModel):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class TerminateSolNetworkInstanceOutput(BaseValidatorModel):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateSolFunctionPackageOutput(BaseValidatorModel):
    operationalState: OperationalStateType
    ResponseMetadata: ResponseMetadata


class UpdateSolNetworkInstanceOutput(BaseValidatorModel):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateSolNetworkPackageOutput(BaseValidatorModel):
    nsdOperationalState: NsdOperationalStateType
    ResponseMetadata: ResponseMetadata


class GetSolNetworkOperationTaskDetails(BaseValidatorModel):
    taskContext: Optional[Dict[str, str]] = None
    taskEndTime: Optional[datetime] = None
    taskErrorDetails: Optional[ErrorInfo] = None
    taskName: Optional[str] = None
    taskStartTime: Optional[datetime] = None
    taskStatus: Optional[TaskStatusType] = None


class FunctionArtifactMeta(BaseValidatorModel):
    overrides: Optional[List[ToscaOverride]] = None


class NetworkArtifactMeta(BaseValidatorModel):
    overrides: Optional[List[ToscaOverride]] = None


class GetSolNetworkInstanceOutput(BaseValidatorModel):
    arn: str
    id: str
    lcmOpInfo: LcmOperationInfo
    metadata: GetSolNetworkInstanceMetadata
    nsInstanceDescription: str
    nsInstanceName: str
    nsState: NsStateType
    nsdId: str
    nsdInfoId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetSolNetworkOperationMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime
    instantiateMetadata: Optional[InstantiateMetadata] = None
    modifyVnfInfoMetadata: Optional[ModifyVnfInfoMetadata] = None
    updateNsMetadata: Optional[UpdateNsMetadata] = None


class GetSolVnfcResourceInfo(BaseValidatorModel):
    metadata: Optional[GetSolVnfcResourceInfoMetadata] = None


class ListSolFunctionInstanceInfo(BaseValidatorModel):
    arn: str
    id: str
    instantiationState: VnfInstantiationStateType
    metadata: ListSolFunctionInstanceMetadata
    nsInstanceId: str
    vnfPkgId: str
    instantiatedVnfInfo: Optional[GetSolInstantiatedVnfInfo] = None
    vnfPkgName: Optional[str] = None


class ListSolFunctionInstancesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSolFunctionPackagesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSolNetworkInstancesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSolNetworkOperationsInputPaginate(BaseValidatorModel):
    nsInstanceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSolNetworkPackagesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSolFunctionPackageInfo(BaseValidatorModel):
    arn: str
    id: str
    onboardingState: OnboardingStateType
    operationalState: OperationalStateType
    usageState: UsageStateType
    metadata: Optional[ListSolFunctionPackageMetadata] = None
    vnfProductName: Optional[str] = None
    vnfProvider: Optional[str] = None
    vnfdId: Optional[str] = None
    vnfdVersion: Optional[str] = None


class ListSolNetworkInstanceInfo(BaseValidatorModel):
    arn: str
    id: str
    metadata: ListSolNetworkInstanceMetadata
    nsInstanceDescription: str
    nsInstanceName: str
    nsState: NsStateType
    nsdId: str
    nsdInfoId: str


class ListSolNetworkOperationsInfo(BaseValidatorModel):
    arn: str
    id: str
    lcmOperationType: LcmOperationTypeType
    nsInstanceId: str
    operationState: NsLcmOperationStateType
    error: Optional[ProblemDetails] = None
    metadata: Optional[ListSolNetworkOperationsMetadata] = None
    updateType: Optional[UpdateSolNetworkTypeType] = None


class ListSolNetworkPackageInfo(BaseValidatorModel):
    arn: str
    id: str
    metadata: ListSolNetworkPackageMetadata
    nsdOnboardingState: NsdOnboardingStateType
    nsdOperationalState: NsdOperationalStateType
    nsdUsageState: NsdUsageStateType
    nsdDesigner: Optional[str] = None
    nsdId: Optional[str] = None
    nsdInvariantId: Optional[str] = None
    nsdName: Optional[str] = None
    nsdVersion: Optional[str] = None
    vnfPkgIds: Optional[List[str]] = None


class UpdateSolNetworkInstanceInput(BaseValidatorModel):
    nsInstanceId: str
    updateType: UpdateSolNetworkTypeType
    modifyVnfInfoData: Optional[UpdateSolNetworkModify] = None
    tags: Optional[Dict[str, str]] = None
    updateNs: Optional[UpdateSolNetworkServiceData] = None


class GetSolFunctionPackageMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime
    vnfd: Optional[FunctionArtifactMeta] = None


class PutSolFunctionPackageContentMetadata(BaseValidatorModel):
    vnfd: Optional[FunctionArtifactMeta] = None


class ValidateSolFunctionPackageContentMetadata(BaseValidatorModel):
    vnfd: Optional[FunctionArtifactMeta] = None


class GetSolNetworkPackageMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime
    nsd: Optional[NetworkArtifactMeta] = None


class PutSolNetworkPackageContentMetadata(BaseValidatorModel):
    nsd: Optional[NetworkArtifactMeta] = None


class ValidateSolNetworkPackageContentMetadata(BaseValidatorModel):
    nsd: Optional[NetworkArtifactMeta] = None


class GetSolNetworkOperationOutput(BaseValidatorModel):
    arn: str
    error: ProblemDetails
    id: str
    lcmOperationType: LcmOperationTypeType
    metadata: GetSolNetworkOperationMetadata
    nsInstanceId: str
    operationState: NsLcmOperationStateType
    tags: Dict[str, str]
    tasks: List[GetSolNetworkOperationTaskDetails]
    updateType: UpdateSolNetworkTypeType
    ResponseMetadata: ResponseMetadata


class GetSolVnfInfo(BaseValidatorModel):
    vnfState: Optional[VnfOperationalStateType] = None
    vnfcResourceInfo: Optional[List[GetSolVnfcResourceInfo]] = None


class ListSolFunctionInstancesOutput(BaseValidatorModel):
    functionInstances: List[ListSolFunctionInstanceInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSolFunctionPackagesOutput(BaseValidatorModel):
    functionPackages: List[ListSolFunctionPackageInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSolNetworkInstancesOutput(BaseValidatorModel):
    networkInstances: List[ListSolNetworkInstanceInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSolNetworkOperationsOutput(BaseValidatorModel):
    networkOperations: List[ListSolNetworkOperationsInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSolNetworkPackagesOutput(BaseValidatorModel):
    networkPackages: List[ListSolNetworkPackageInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetSolFunctionPackageOutput(BaseValidatorModel):
    arn: str
    id: str
    metadata: GetSolFunctionPackageMetadata
    onboardingState: OnboardingStateType
    operationalState: OperationalStateType
    tags: Dict[str, str]
    usageState: UsageStateType
    vnfProductName: str
    vnfProvider: str
    vnfdId: str
    vnfdVersion: str
    ResponseMetadata: ResponseMetadata


class PutSolFunctionPackageContentOutput(BaseValidatorModel):
    id: str
    metadata: PutSolFunctionPackageContentMetadata
    vnfProductName: str
    vnfProvider: str
    vnfdId: str
    vnfdVersion: str
    ResponseMetadata: ResponseMetadata


class ValidateSolFunctionPackageContentOutput(BaseValidatorModel):
    id: str
    metadata: ValidateSolFunctionPackageContentMetadata
    vnfProductName: str
    vnfProvider: str
    vnfdId: str
    vnfdVersion: str
    ResponseMetadata: ResponseMetadata


class GetSolNetworkPackageOutput(BaseValidatorModel):
    arn: str
    id: str
    metadata: GetSolNetworkPackageMetadata
    nsdId: str
    nsdName: str
    nsdOnboardingState: NsdOnboardingStateType
    nsdOperationalState: NsdOperationalStateType
    nsdUsageState: NsdUsageStateType
    nsdVersion: str
    tags: Dict[str, str]
    vnfPkgIds: List[str]
    ResponseMetadata: ResponseMetadata


class PutSolNetworkPackageContentOutput(BaseValidatorModel):
    arn: str
    id: str
    metadata: PutSolNetworkPackageContentMetadata
    nsdId: str
    nsdName: str
    nsdVersion: str
    vnfPkgIds: List[str]
    ResponseMetadata: ResponseMetadata


class ValidateSolNetworkPackageContentOutput(BaseValidatorModel):
    arn: str
    id: str
    metadata: ValidateSolNetworkPackageContentMetadata
    nsdId: str
    nsdName: str
    nsdVersion: str
    vnfPkgIds: List[str]
    ResponseMetadata: ResponseMetadata


class GetSolFunctionInstanceOutput(BaseValidatorModel):
    arn: str
    id: str
    instantiatedVnfInfo: GetSolVnfInfo
    instantiationState: VnfInstantiationStateType
    metadata: GetSolFunctionInstanceMetadata
    nsInstanceId: str
    tags: Dict[str, str]
    vnfPkgId: str
    vnfProductName: str
    vnfProvider: str
    vnfdId: str
    vnfdVersion: str
    ResponseMetadata: ResponseMetadata