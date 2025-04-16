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
from aws_resource_validator.pydantic_models.tnb_constants import *

class CancelSolNetworkOperationInput(BaseValidatorModel):
    nsLcmOpOccId: str


class CreateSolFunctionPackageInput(BaseValidatorModel):
    tags: Optional[Mapping[str, str]] = None


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
    tags: Optional[Mapping[str, str]] = None


class CreateSolNetworkPackageInput(BaseValidatorModel):
    tags: Optional[Mapping[str, str]] = None


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
    accept: Literal["application/zip"]
    vnfPkgId: str


class GetSolFunctionPackageDescriptorInput(BaseValidatorModel):
    accept: Literal["text/plain"]
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
    accept: Literal["application/zip"]
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
    additionalParamsForNs: Optional[Mapping[str, Any]] = None
    dryRun: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None


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
    tags: Mapping[str, str]


class TerminateSolNetworkInstanceInput(BaseValidatorModel):
    nsInstanceId: str
    tags: Optional[Mapping[str, str]] = None


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateSolFunctionPackageInput(BaseValidatorModel):
    operationalState: OperationalStateType
    vnfPkgId: str


class UpdateSolNetworkModify(BaseValidatorModel):
    vnfConfigurableProperties: Mapping[str, Any]
    vnfInstanceId: str


class UpdateSolNetworkServiceData(BaseValidatorModel):
    nsdInfoId: str
    additionalParamsForNs: Optional[Mapping[str, Any]] = None


class UpdateSolNetworkPackageInput(BaseValidatorModel):
    nsdInfoId: str
    nsdOperationalState: NsdOperationalStateType


class Blob(BaseValidatorModel):
    pass


class PutSolFunctionPackageContentInput(BaseValidatorModel):
    file: Blob
    vnfPkgId: str
    contentType: Optional[Literal["application/zip"]] = None


class PutSolNetworkPackageContentInput(BaseValidatorModel):
    file: Blob
    nsdInfoId: str
    contentType: Optional[Literal["application/zip"]] = None


class ValidateSolFunctionPackageContentInput(BaseValidatorModel):
    file: Blob
    vnfPkgId: str
    contentType: Optional[Literal["application/zip"]] = None


class ValidateSolNetworkPackageContentInput(BaseValidatorModel):
    file: Blob
    nsdInfoId: str
    contentType: Optional[Literal["application/zip"]] = None


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetSolFunctionPackageContentOutput(BaseValidatorModel):
    contentType: Literal["application/zip"]
    packageContent: StreamingBody
    ResponseMetadata: ResponseMetadata


class GetSolFunctionPackageDescriptorOutput(BaseValidatorModel):
    contentType: Literal["text/plain"]
    vnfd: StreamingBody
    ResponseMetadata: ResponseMetadata


class GetSolNetworkPackageContentOutput(BaseValidatorModel):
    contentType: Literal["application/zip"]
    nsdContent: StreamingBody
    ResponseMetadata: ResponseMetadata


class GetSolNetworkPackageDescriptorOutput(BaseValidatorModel):
    contentType: Literal["text/plain"]
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


class GetSolNetworkOperationMetadata(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime
    instantiateMetadata: Optional[InstantiateMetadata] = None
    modifyVnfInfoMetadata: Optional[ModifyVnfInfoMetadata] = None
    updateNsMetadata: Optional[UpdateNsMetadata] = None


class GetSolVnfcResourceInfo(BaseValidatorModel):
    metadata: Optional[GetSolVnfcResourceInfoMetadata] = None


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


class UpdateSolNetworkInstanceInput(BaseValidatorModel):
    nsInstanceId: str
    updateType: UpdateSolNetworkTypeType
    modifyVnfInfoData: Optional[UpdateSolNetworkModify] = None
    tags: Optional[Mapping[str, str]] = None
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


class GetSolVnfInfo(BaseValidatorModel):
    vnfState: Optional[VnfOperationalStateType] = None
    vnfcResourceInfo: Optional[List[GetSolVnfcResourceInfo]] = None


class ListSolFunctionInstanceInfo(BaseValidatorModel):
    pass


class ListSolFunctionInstancesOutput(BaseValidatorModel):
    functionInstances: List[ListSolFunctionInstanceInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSolFunctionPackageInfo(BaseValidatorModel):
    pass


class ListSolFunctionPackagesOutput(BaseValidatorModel):
    functionPackages: List[ListSolFunctionPackageInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSolNetworkInstanceInfo(BaseValidatorModel):
    pass


class ListSolNetworkInstancesOutput(BaseValidatorModel):
    networkInstances: List[ListSolNetworkInstanceInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSolNetworkOperationsInfo(BaseValidatorModel):
    pass


class ListSolNetworkOperationsOutput(BaseValidatorModel):
    networkOperations: List[ListSolNetworkOperationsInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSolNetworkPackageInfo(BaseValidatorModel):
    pass


class ListSolNetworkPackagesOutput(BaseValidatorModel):
    networkPackages: List[ListSolNetworkPackageInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


