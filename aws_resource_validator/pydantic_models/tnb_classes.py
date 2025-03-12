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

class CancelSolNetworkOperationInputTypeDef(BaseValidatorModel):
    nsLcmOpOccId: str


class CreateSolFunctionPackageInputTypeDef(BaseValidatorModel):
    tags: Optional[Mapping[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateSolNetworkInstanceInputTypeDef(BaseValidatorModel):
    nsName: str
    nsdInfoId: str
    nsDescription: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateSolNetworkPackageInputTypeDef(BaseValidatorModel):
    tags: Optional[Mapping[str, str]] = None


class DeleteSolFunctionPackageInputTypeDef(BaseValidatorModel):
    vnfPkgId: str


class DeleteSolNetworkInstanceInputTypeDef(BaseValidatorModel):
    nsInstanceId: str


class DeleteSolNetworkPackageInputTypeDef(BaseValidatorModel):
    nsdInfoId: str


class ErrorInfoTypeDef(BaseValidatorModel):
    cause: Optional[str] = None
    details: Optional[str] = None


class ToscaOverrideTypeDef(BaseValidatorModel):
    defaultValue: Optional[str] = None
    name: Optional[str] = None


class GetSolFunctionInstanceInputTypeDef(BaseValidatorModel):
    vnfInstanceId: str


class GetSolFunctionInstanceMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


class GetSolFunctionPackageContentInputTypeDef(BaseValidatorModel):
    accept: Literal["application/zip"]
    vnfPkgId: str


class GetSolFunctionPackageDescriptorInputTypeDef(BaseValidatorModel):
    accept: Literal["text/plain"]
    vnfPkgId: str


class GetSolFunctionPackageInputTypeDef(BaseValidatorModel):
    vnfPkgId: str


class GetSolInstantiatedVnfInfoTypeDef(BaseValidatorModel):
    vnfState: Optional[VnfOperationalStateType] = None


class GetSolNetworkInstanceInputTypeDef(BaseValidatorModel):
    nsInstanceId: str


class GetSolNetworkInstanceMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


class LcmOperationInfoTypeDef(BaseValidatorModel):
    nsLcmOpOccId: str


class GetSolNetworkOperationInputTypeDef(BaseValidatorModel):
    nsLcmOpOccId: str


class InstantiateMetadataTypeDef(BaseValidatorModel):
    nsdInfoId: str
    additionalParamsForNs: Optional[Dict[str, Any]] = None


class ModifyVnfInfoMetadataTypeDef(BaseValidatorModel):
    vnfConfigurableProperties: Dict[str, Any]
    vnfInstanceId: str


class UpdateNsMetadataTypeDef(BaseValidatorModel):
    nsdInfoId: str
    additionalParamsForNs: Optional[Dict[str, Any]] = None


class ProblemDetailsTypeDef(BaseValidatorModel):
    detail: str
    title: Optional[str] = None


class GetSolNetworkPackageContentInputTypeDef(BaseValidatorModel):
    accept: Literal["application/zip"]
    nsdInfoId: str


class GetSolNetworkPackageDescriptorInputTypeDef(BaseValidatorModel):
    nsdInfoId: str


class GetSolNetworkPackageInputTypeDef(BaseValidatorModel):
    nsdInfoId: str


class GetSolVnfcResourceInfoMetadataTypeDef(BaseValidatorModel):
    cluster: Optional[str] = None
    helmChart: Optional[str] = None
    nodeGroup: Optional[str] = None


class InstantiateSolNetworkInstanceInputTypeDef(BaseValidatorModel):
    nsInstanceId: str
    additionalParamsForNs: Optional[Mapping[str, Any]] = None
    dryRun: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None


class ListSolFunctionInstanceMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListSolFunctionInstancesInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSolFunctionPackageMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


class ListSolFunctionPackagesInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSolNetworkInstanceMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


class ListSolNetworkInstancesInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSolNetworkOperationsMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime
    nsdInfoId: Optional[str] = None
    vnfInstanceId: Optional[str] = None


class ListSolNetworkOperationsInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    nsInstanceId: Optional[str] = None


class ListSolNetworkPackageMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime


class ListSolNetworkPackagesInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TerminateSolNetworkInstanceInputTypeDef(BaseValidatorModel):
    nsInstanceId: str
    tags: Optional[Mapping[str, str]] = None


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateSolFunctionPackageInputTypeDef(BaseValidatorModel):
    operationalState: OperationalStateType
    vnfPkgId: str


class UpdateSolNetworkModifyTypeDef(BaseValidatorModel):
    vnfConfigurableProperties: Mapping[str, Any]
    vnfInstanceId: str


class UpdateSolNetworkServiceDataTypeDef(BaseValidatorModel):
    nsdInfoId: str
    additionalParamsForNs: Optional[Mapping[str, Any]] = None


class UpdateSolNetworkPackageInputTypeDef(BaseValidatorModel):
    nsdInfoId: str
    nsdOperationalState: NsdOperationalStateType


class BlobTypeDef(BaseValidatorModel):
    pass


class PutSolFunctionPackageContentInputTypeDef(BaseValidatorModel):
    file: BlobTypeDef
    vnfPkgId: str
    contentType: Optional[Literal["application/zip"]] = None


class PutSolNetworkPackageContentInputTypeDef(BaseValidatorModel):
    file: BlobTypeDef
    nsdInfoId: str
    contentType: Optional[Literal["application/zip"]] = None


class ValidateSolFunctionPackageContentInputTypeDef(BaseValidatorModel):
    file: BlobTypeDef
    vnfPkgId: str
    contentType: Optional[Literal["application/zip"]] = None


class ValidateSolNetworkPackageContentInputTypeDef(BaseValidatorModel):
    file: BlobTypeDef
    nsdInfoId: str
    contentType: Optional[Literal["application/zip"]] = None


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetSolFunctionPackageContentOutputTypeDef(BaseValidatorModel):
    contentType: Literal["application/zip"]
    packageContent: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class GetSolFunctionPackageDescriptorOutputTypeDef(BaseValidatorModel):
    contentType: Literal["text/plain"]
    vnfd: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class GetSolNetworkPackageContentOutputTypeDef(BaseValidatorModel):
    contentType: Literal["application/zip"]
    nsdContent: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class GetSolNetworkPackageDescriptorOutputTypeDef(BaseValidatorModel):
    contentType: Literal["text/plain"]
    nsd: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef


class InstantiateSolNetworkInstanceOutputTypeDef(BaseValidatorModel):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class TerminateSolNetworkInstanceOutputTypeDef(BaseValidatorModel):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSolFunctionPackageOutputTypeDef(BaseValidatorModel):
    operationalState: OperationalStateType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSolNetworkInstanceOutputTypeDef(BaseValidatorModel):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSolNetworkPackageOutputTypeDef(BaseValidatorModel):
    nsdOperationalState: NsdOperationalStateType
    ResponseMetadata: ResponseMetadataTypeDef


class GetSolNetworkOperationTaskDetailsTypeDef(BaseValidatorModel):
    taskContext: Optional[Dict[str, str]] = None
    taskEndTime: Optional[datetime] = None
    taskErrorDetails: Optional[ErrorInfoTypeDef] = None
    taskName: Optional[str] = None
    taskStartTime: Optional[datetime] = None
    taskStatus: Optional[TaskStatusType] = None


class FunctionArtifactMetaTypeDef(BaseValidatorModel):
    overrides: Optional[List[ToscaOverrideTypeDef]] = None


class NetworkArtifactMetaTypeDef(BaseValidatorModel):
    overrides: Optional[List[ToscaOverrideTypeDef]] = None


class GetSolNetworkOperationMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime
    instantiateMetadata: Optional[InstantiateMetadataTypeDef] = None
    modifyVnfInfoMetadata: Optional[ModifyVnfInfoMetadataTypeDef] = None
    updateNsMetadata: Optional[UpdateNsMetadataTypeDef] = None


class GetSolVnfcResourceInfoTypeDef(BaseValidatorModel):
    metadata: Optional[GetSolVnfcResourceInfoMetadataTypeDef] = None


class ListSolFunctionInstancesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSolFunctionPackagesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSolNetworkInstancesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSolNetworkOperationsInputPaginateTypeDef(BaseValidatorModel):
    nsInstanceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSolNetworkPackagesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class UpdateSolNetworkInstanceInputTypeDef(BaseValidatorModel):
    nsInstanceId: str
    updateType: UpdateSolNetworkTypeType
    modifyVnfInfoData: Optional[UpdateSolNetworkModifyTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    updateNs: Optional[UpdateSolNetworkServiceDataTypeDef] = None


class GetSolFunctionPackageMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime
    vnfd: Optional[FunctionArtifactMetaTypeDef] = None


class PutSolFunctionPackageContentMetadataTypeDef(BaseValidatorModel):
    vnfd: Optional[FunctionArtifactMetaTypeDef] = None


class ValidateSolFunctionPackageContentMetadataTypeDef(BaseValidatorModel):
    vnfd: Optional[FunctionArtifactMetaTypeDef] = None


class GetSolNetworkPackageMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime
    nsd: Optional[NetworkArtifactMetaTypeDef] = None


class PutSolNetworkPackageContentMetadataTypeDef(BaseValidatorModel):
    nsd: Optional[NetworkArtifactMetaTypeDef] = None


class ValidateSolNetworkPackageContentMetadataTypeDef(BaseValidatorModel):
    nsd: Optional[NetworkArtifactMetaTypeDef] = None


class GetSolVnfInfoTypeDef(BaseValidatorModel):
    vnfState: Optional[VnfOperationalStateType] = None
    vnfcResourceInfo: Optional[List[GetSolVnfcResourceInfoTypeDef]] = None


class ListSolFunctionInstanceInfoTypeDef(BaseValidatorModel):
    pass


class ListSolFunctionInstancesOutputTypeDef(BaseValidatorModel):
    functionInstances: List[ListSolFunctionInstanceInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSolFunctionPackageInfoTypeDef(BaseValidatorModel):
    pass


class ListSolFunctionPackagesOutputTypeDef(BaseValidatorModel):
    functionPackages: List[ListSolFunctionPackageInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSolNetworkInstanceInfoTypeDef(BaseValidatorModel):
    pass


class ListSolNetworkInstancesOutputTypeDef(BaseValidatorModel):
    networkInstances: List[ListSolNetworkInstanceInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSolNetworkOperationsInfoTypeDef(BaseValidatorModel):
    pass


class ListSolNetworkOperationsOutputTypeDef(BaseValidatorModel):
    networkOperations: List[ListSolNetworkOperationsInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSolNetworkPackageInfoTypeDef(BaseValidatorModel):
    pass


class ListSolNetworkPackagesOutputTypeDef(BaseValidatorModel):
    networkPackages: List[ListSolNetworkPackageInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


