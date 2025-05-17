from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.tnb.tnb_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Blob = Union[str, bytes, IO[Any], StreamingBody]


# This class is the input for the 'cancel_sol_network_operation' function.
class CancelSolNetworkOperationInput(BaseValidatorModel):
    nsLcmOpOccId: str


# This class is the input for the 'create_sol_function_package' function.
class CreateSolFunctionPackageInput(BaseValidatorModel):
    tags: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_sol_network_instance' function.
class CreateSolNetworkInstanceInput(BaseValidatorModel):
    nsName: str
    nsdInfoId: str
    nsDescription: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_sol_network_package' function.
class CreateSolNetworkPackageInput(BaseValidatorModel):
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'delete_sol_function_package' function.
class DeleteSolFunctionPackageInput(BaseValidatorModel):
    vnfPkgId: str


# This class is the input for the 'delete_sol_network_instance' function.
class DeleteSolNetworkInstanceInput(BaseValidatorModel):
    nsInstanceId: str


# This class is the input for the 'delete_sol_network_package' function.
class DeleteSolNetworkPackageInput(BaseValidatorModel):
    nsdInfoId: str


class ErrorInfo(BaseValidatorModel):
    cause: Optional[str] = None
    details: Optional[str] = None


class ToscaOverride(BaseValidatorModel):
    defaultValue: Optional[str] = None
    name: Optional[str] = None


# This class is the input for the 'get_sol_function_instance' function.
class GetSolFunctionInstanceInput(BaseValidatorModel):
    vnfInstanceId: str


class GetSolFunctionInstanceMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


# This class is the input for the 'get_sol_function_package_content' function.
class GetSolFunctionPackageContentInput(BaseValidatorModel):
    accept: Literal['application/zip']
    vnfPkgId: str


# This class is the input for the 'get_sol_function_package_descriptor' function.
class GetSolFunctionPackageDescriptorInput(BaseValidatorModel):
    accept: Literal['text/plain']
    vnfPkgId: str


# This class is the input for the 'get_sol_function_package' function.
class GetSolFunctionPackageInput(BaseValidatorModel):
    vnfPkgId: str


class GetSolInstantiatedVnfInfo(BaseValidatorModel):
    vnfState: Optional[VnfOperationalStateType] = None


# This class is the input for the 'get_sol_network_instance' function.
class GetSolNetworkInstanceInput(BaseValidatorModel):
    nsInstanceId: str


class GetSolNetworkInstanceMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


class LcmOperationInfo(BaseValidatorModel):
    nsLcmOpOccId: str


# This class is the input for the 'get_sol_network_operation' function.
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


# This class is the input for the 'get_sol_network_package_content' function.
class GetSolNetworkPackageContentInput(BaseValidatorModel):
    accept: Literal['application/zip']
    nsdInfoId: str


# This class is the input for the 'get_sol_network_package_descriptor' function.
class GetSolNetworkPackageDescriptorInput(BaseValidatorModel):
    nsdInfoId: str


# This class is the input for the 'get_sol_network_package' function.
class GetSolNetworkPackageInput(BaseValidatorModel):
    nsdInfoId: str


class GetSolVnfcResourceInfoMetadata(BaseValidatorModel):
    cluster: Optional[str] = None
    helmChart: Optional[str] = None
    nodeGroup: Optional[str] = None


# This class is the input for the 'instantiate_sol_network_instance' function.
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


# This class is the input for the 'list_sol_function_instances' function.
class ListSolFunctionInstancesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSolFunctionPackageMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


# This class is the input for the 'list_sol_function_packages' function.
class ListSolFunctionPackagesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSolNetworkInstanceMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


# This class is the input for the 'list_sol_network_instances' function.
class ListSolNetworkInstancesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSolNetworkOperationsMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime
    nsdInfoId: Optional[str] = None
    vnfInstanceId: Optional[str] = None


# This class is the input for the 'list_sol_network_operations' function.
class ListSolNetworkOperationsInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    nsInstanceId: Optional[str] = None


class ListSolNetworkPackageMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


# This class is the input for the 'list_sol_network_packages' function.
class ListSolNetworkPackagesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


# This class is the input for the 'terminate_sol_network_instance' function.
class TerminateSolNetworkInstanceInput(BaseValidatorModel):
    nsInstanceId: str
    tags: Optional[Dict[str, str]] = None


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_sol_function_package' function.
class UpdateSolFunctionPackageInput(BaseValidatorModel):
    operationalState: OperationalStateType
    vnfPkgId: str


class UpdateSolNetworkModify(BaseValidatorModel):
    vnfConfigurableProperties: Dict[str, Any]
    vnfInstanceId: str


class UpdateSolNetworkServiceData(BaseValidatorModel):
    nsdInfoId: str
    additionalParamsForNs: Optional[Dict[str, Any]] = None


# This class is the input for the 'update_sol_network_package' function.
class UpdateSolNetworkPackageInput(BaseValidatorModel):
    nsdInfoId: str
    nsdOperationalState: NsdOperationalStateType


# This class is the input for the 'put_sol_function_package_content' function.
class PutSolFunctionPackageContentInput(BaseValidatorModel):
    file: Blob
    vnfPkgId: str
    contentType: Optional[Literal['application/zip']] = None


# This class is the input for the 'put_sol_network_package_content' function.
class PutSolNetworkPackageContentInput(BaseValidatorModel):
    file: Blob
    nsdInfoId: str
    contentType: Optional[Literal['application/zip']] = None


# This class is the input for the 'validate_sol_function_package_content' function.
class ValidateSolFunctionPackageContentInput(BaseValidatorModel):
    file: Blob
    vnfPkgId: str
    contentType: Optional[Literal['application/zip']] = None


# This class is the input for the 'validate_sol_network_package_content' function.
class ValidateSolNetworkPackageContentInput(BaseValidatorModel):
    file: Blob
    nsdInfoId: str
    contentType: Optional[Literal['application/zip']] = None


# This class is the output for the 'create_sol_function_package' function.
class CreateSolFunctionPackageOutput(BaseValidatorModel):
    arn: str
    id: str
    onboardingState: OnboardingStateType
    operationalState: OperationalStateType
    tags: Dict[str, str]
    usageState: UsageStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_sol_network_instance' function.
class CreateSolNetworkInstanceOutput(BaseValidatorModel):
    arn: str
    id: str
    nsInstanceName: str
    nsdInfoId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_sol_network_package' function.
class CreateSolNetworkPackageOutput(BaseValidatorModel):
    arn: str
    id: str
    nsdOnboardingState: NsdOnboardingStateType
    nsdOperationalState: NsdOperationalStateType
    nsdUsageState: NsdUsageStateType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_sol_network_package' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sol_function_package_content' function.
class GetSolFunctionPackageContentOutput(BaseValidatorModel):
    contentType: Literal['application/zip']
    packageContent: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sol_function_package_descriptor' function.
class GetSolFunctionPackageDescriptorOutput(BaseValidatorModel):
    contentType: Literal['text/plain']
    vnfd: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sol_network_package_content' function.
class GetSolNetworkPackageContentOutput(BaseValidatorModel):
    contentType: Literal['application/zip']
    nsdContent: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sol_network_package_descriptor' function.
class GetSolNetworkPackageDescriptorOutput(BaseValidatorModel):
    contentType: Literal['text/plain']
    nsd: StreamingBody
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'instantiate_sol_network_instance' function.
class InstantiateSolNetworkInstanceOutput(BaseValidatorModel):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'terminate_sol_network_instance' function.
class TerminateSolNetworkInstanceOutput(BaseValidatorModel):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_sol_function_package' function.
class UpdateSolFunctionPackageOutput(BaseValidatorModel):
    operationalState: OperationalStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_sol_network_instance' function.
class UpdateSolNetworkInstanceOutput(BaseValidatorModel):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_sol_network_package' function.
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


# This class is the output for the 'get_sol_network_instance' function.
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


# This class is the input for the 'update_sol_network_instance' function.
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


# This class is the output for the 'get_sol_network_operation' function.
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


# This class is the output for the 'list_sol_function_instances' function.
class ListSolFunctionInstancesOutput(BaseValidatorModel):
    functionInstances: List[ListSolFunctionInstanceInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_sol_function_packages' function.
class ListSolFunctionPackagesOutput(BaseValidatorModel):
    functionPackages: List[ListSolFunctionPackageInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_sol_network_instances' function.
class ListSolNetworkInstancesOutput(BaseValidatorModel):
    networkInstances: List[ListSolNetworkInstanceInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_sol_network_operations' function.
class ListSolNetworkOperationsOutput(BaseValidatorModel):
    networkOperations: List[ListSolNetworkOperationsInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_sol_network_packages' function.
class ListSolNetworkPackagesOutput(BaseValidatorModel):
    networkPackages: List[ListSolNetworkPackageInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_sol_function_package' function.
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


# This class is the output for the 'put_sol_function_package_content' function.
class PutSolFunctionPackageContentOutput(BaseValidatorModel):
    id: str
    metadata: PutSolFunctionPackageContentMetadata
    vnfProductName: str
    vnfProvider: str
    vnfdId: str
    vnfdVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'validate_sol_function_package_content' function.
class ValidateSolFunctionPackageContentOutput(BaseValidatorModel):
    id: str
    metadata: ValidateSolFunctionPackageContentMetadata
    vnfProductName: str
    vnfProvider: str
    vnfdId: str
    vnfdVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sol_network_package' function.
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


# This class is the output for the 'put_sol_network_package_content' function.
class PutSolNetworkPackageContentOutput(BaseValidatorModel):
    arn: str
    id: str
    metadata: PutSolNetworkPackageContentMetadata
    nsdId: str
    nsdName: str
    nsdVersion: str
    vnfPkgIds: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'validate_sol_network_package_content' function.
class ValidateSolNetworkPackageContentOutput(BaseValidatorModel):
    arn: str
    id: str
    metadata: ValidateSolNetworkPackageContentMetadata
    nsdId: str
    nsdName: str
    nsdVersion: str
    vnfPkgIds: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sol_function_instance' function.
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