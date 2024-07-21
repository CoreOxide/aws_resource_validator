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
from aws_resource_validator.pydantic_models.tnb_constants import *

class CancelSolNetworkOperationInputRequestTypeDef(BaseModel):
    nsLcmOpOccId: str

class CreateSolFunctionPackageInputRequestTypeDef(BaseModel):
    tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateSolNetworkInstanceInputRequestTypeDef(BaseModel):
    nsName: str
    nsdInfoId: str
    nsDescription: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateSolNetworkPackageInputRequestTypeDef(BaseModel):
    tags: Optional[Mapping[str, str]] = None

class DeleteSolFunctionPackageInputRequestTypeDef(BaseModel):
    vnfPkgId: str

class DeleteSolNetworkInstanceInputRequestTypeDef(BaseModel):
    nsInstanceId: str

class DeleteSolNetworkPackageInputRequestTypeDef(BaseModel):
    nsdInfoId: str

class ErrorInfoTypeDef(BaseModel):
    cause: Optional[str] = None
    details: Optional[str] = None

class ToscaOverrideTypeDef(BaseModel):
    defaultValue: Optional[str] = None
    name: Optional[str] = None

class GetSolFunctionInstanceInputRequestTypeDef(BaseModel):
    vnfInstanceId: str

class GetSolFunctionInstanceMetadataTypeDef(BaseModel):
    createdAt: datetime
    lastModified: datetime

class GetSolFunctionPackageContentInputRequestTypeDef(BaseModel):
    accept: Literal["application/zip"]
    vnfPkgId: str

class GetSolFunctionPackageDescriptorInputRequestTypeDef(BaseModel):
    accept: Literal["text/plain"]
    vnfPkgId: str

class GetSolFunctionPackageInputRequestTypeDef(BaseModel):
    vnfPkgId: str

class GetSolInstantiatedVnfInfoTypeDef(BaseModel):
    vnfState: Optional[VnfOperationalStateType] = None

class GetSolNetworkInstanceInputRequestTypeDef(BaseModel):
    nsInstanceId: str

class GetSolNetworkInstanceMetadataTypeDef(BaseModel):
    createdAt: datetime
    lastModified: datetime

class LcmOperationInfoTypeDef(BaseModel):
    nsLcmOpOccId: str

class GetSolNetworkOperationInputRequestTypeDef(BaseModel):
    nsLcmOpOccId: str

class GetSolNetworkOperationMetadataTypeDef(BaseModel):
    createdAt: datetime
    lastModified: datetime

class ProblemDetailsTypeDef(BaseModel):
    detail: str
    title: Optional[str] = None

class GetSolNetworkPackageContentInputRequestTypeDef(BaseModel):
    accept: Literal["application/zip"]
    nsdInfoId: str

class GetSolNetworkPackageDescriptorInputRequestTypeDef(BaseModel):
    nsdInfoId: str

class GetSolNetworkPackageInputRequestTypeDef(BaseModel):
    nsdInfoId: str

class GetSolVnfcResourceInfoMetadataTypeDef(BaseModel):
    cluster: Optional[str] = None
    helmChart: Optional[str] = None
    nodeGroup: Optional[str] = None

class InstantiateSolNetworkInstanceInputRequestTypeDef(BaseModel):
    nsInstanceId: str
    additionalParamsForNs: Optional[Mapping[str, Any]] = None
    dryRun: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None

class ListSolFunctionInstanceMetadataTypeDef(BaseModel):
    createdAt: datetime
    lastModified: datetime

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListSolFunctionInstancesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSolFunctionPackageMetadataTypeDef(BaseModel):
    createdAt: datetime
    lastModified: datetime

class ListSolFunctionPackagesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSolNetworkInstanceMetadataTypeDef(BaseModel):
    createdAt: datetime
    lastModified: datetime

class ListSolNetworkInstancesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSolNetworkOperationsMetadataTypeDef(BaseModel):
    createdAt: datetime
    lastModified: datetime

class ListSolNetworkOperationsInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSolNetworkPackageMetadataTypeDef(BaseModel):
    createdAt: datetime
    lastModified: datetime

class ListSolNetworkPackagesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class TerminateSolNetworkInstanceInputRequestTypeDef(BaseModel):
    nsInstanceId: str
    tags: Optional[Mapping[str, str]] = None

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateSolFunctionPackageInputRequestTypeDef(BaseModel):
    operationalState: OperationalStateType
    vnfPkgId: str

class UpdateSolNetworkModifyTypeDef(BaseModel):
    vnfConfigurableProperties: Mapping[str, Any]
    vnfInstanceId: str

class UpdateSolNetworkPackageInputRequestTypeDef(BaseModel):
    nsdInfoId: str
    nsdOperationalState: NsdOperationalStateType

class PutSolFunctionPackageContentInputRequestTypeDef(BaseModel):
    file: BlobTypeDef
    vnfPkgId: str
    contentType: Optional[Literal["application/zip"]] = None

class PutSolNetworkPackageContentInputRequestTypeDef(BaseModel):
    file: BlobTypeDef
    nsdInfoId: str
    contentType: Optional[Literal["application/zip"]] = None

class ValidateSolFunctionPackageContentInputRequestTypeDef(BaseModel):
    file: BlobTypeDef
    vnfPkgId: str
    contentType: Optional[Literal["application/zip"]] = None

class ValidateSolNetworkPackageContentInputRequestTypeDef(BaseModel):
    file: BlobTypeDef
    nsdInfoId: str
    contentType: Optional[Literal["application/zip"]] = None

class CreateSolFunctionPackageOutputTypeDef(BaseModel):
    arn: str
    id: str
    onboardingState: OnboardingStateType
    operationalState: OperationalStateType
    tags: Dict[str, str]
    usageState: UsageStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSolNetworkInstanceOutputTypeDef(BaseModel):
    arn: str
    id: str
    nsInstanceName: str
    nsdInfoId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSolNetworkPackageOutputTypeDef(BaseModel):
    arn: str
    id: str
    nsdOnboardingState: NsdOnboardingStateType
    nsdOperationalState: NsdOperationalStateType
    nsdUsageState: NsdUsageStateType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolFunctionPackageContentOutputTypeDef(BaseModel):
    contentType: Literal["application/zip"]
    packageContent: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolFunctionPackageDescriptorOutputTypeDef(BaseModel):
    contentType: Literal["text/plain"]
    vnfd: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolNetworkPackageContentOutputTypeDef(BaseModel):
    contentType: Literal["application/zip"]
    nsdContent: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolNetworkPackageDescriptorOutputTypeDef(BaseModel):
    contentType: Literal["text/plain"]
    nsd: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class InstantiateSolNetworkInstanceOutputTypeDef(BaseModel):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateSolNetworkInstanceOutputTypeDef(BaseModel):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSolFunctionPackageOutputTypeDef(BaseModel):
    operationalState: OperationalStateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSolNetworkInstanceOutputTypeDef(BaseModel):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSolNetworkPackageOutputTypeDef(BaseModel):
    nsdOperationalState: NsdOperationalStateType
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolNetworkOperationTaskDetailsTypeDef(BaseModel):
    taskContext: Optional[Dict[str, str]] = None
    taskEndTime: Optional[datetime] = None
    taskErrorDetails: Optional[ErrorInfoTypeDef] = None
    taskName: Optional[str] = None
    taskStartTime: Optional[datetime] = None
    taskStatus: Optional[TaskStatusType] = None

class FunctionArtifactMetaTypeDef(BaseModel):
    overrides: Optional[List[ToscaOverrideTypeDef]] = None

class NetworkArtifactMetaTypeDef(BaseModel):
    overrides: Optional[List[ToscaOverrideTypeDef]] = None

class GetSolNetworkInstanceOutputTypeDef(BaseModel):
    arn: str
    id: str
    lcmOpInfo: LcmOperationInfoTypeDef
    metadata: GetSolNetworkInstanceMetadataTypeDef
    nsInstanceDescription: str
    nsInstanceName: str
    nsState: NsStateType
    nsdId: str
    nsdInfoId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolVnfcResourceInfoTypeDef(BaseModel):
    metadata: Optional[GetSolVnfcResourceInfoMetadataTypeDef] = None

class ListSolFunctionInstanceInfoTypeDef(BaseModel):
    arn: str
    id: str
    instantiationState: VnfInstantiationStateType
    metadata: ListSolFunctionInstanceMetadataTypeDef
    nsInstanceId: str
    vnfPkgId: str
    instantiatedVnfInfo: Optional[GetSolInstantiatedVnfInfoTypeDef] = None
    vnfPkgName: Optional[str] = None

class ListSolFunctionInstancesInputListSolFunctionInstancesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSolFunctionPackagesInputListSolFunctionPackagesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSolNetworkInstancesInputListSolNetworkInstancesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSolNetworkOperationsInputListSolNetworkOperationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSolNetworkPackagesInputListSolNetworkPackagesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSolFunctionPackageInfoTypeDef(BaseModel):
    arn: str
    id: str
    onboardingState: OnboardingStateType
    operationalState: OperationalStateType
    usageState: UsageStateType
    metadata: Optional[ListSolFunctionPackageMetadataTypeDef] = None
    vnfProductName: Optional[str] = None
    vnfProvider: Optional[str] = None
    vnfdId: Optional[str] = None
    vnfdVersion: Optional[str] = None

class ListSolNetworkInstanceInfoTypeDef(BaseModel):
    arn: str
    id: str
    metadata: ListSolNetworkInstanceMetadataTypeDef
    nsInstanceDescription: str
    nsInstanceName: str
    nsState: NsStateType
    nsdId: str
    nsdInfoId: str

class ListSolNetworkOperationsInfoTypeDef(BaseModel):
    arn: str
    id: str
    lcmOperationType: LcmOperationTypeType
    nsInstanceId: str
    operationState: NsLcmOperationStateType
    error: Optional[ProblemDetailsTypeDef] = None
    metadata: Optional[ListSolNetworkOperationsMetadataTypeDef] = None

class ListSolNetworkPackageInfoTypeDef(BaseModel):
    arn: str
    id: str
    metadata: ListSolNetworkPackageMetadataTypeDef
    nsdOnboardingState: NsdOnboardingStateType
    nsdOperationalState: NsdOperationalStateType
    nsdUsageState: NsdUsageStateType
    nsdDesigner: Optional[str] = None
    nsdId: Optional[str] = None
    nsdInvariantId: Optional[str] = None
    nsdName: Optional[str] = None
    nsdVersion: Optional[str] = None
    vnfPkgIds: Optional[List[str]] = None

class UpdateSolNetworkInstanceInputRequestTypeDef(BaseModel):
    nsInstanceId: str
    updateType: Literal["MODIFY_VNF_INFORMATION"]
    modifyVnfInfoData: Optional[UpdateSolNetworkModifyTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class GetSolNetworkOperationOutputTypeDef(BaseModel):
    arn: str
    error: ProblemDetailsTypeDef
    id: str
    lcmOperationType: LcmOperationTypeType
    metadata: GetSolNetworkOperationMetadataTypeDef
    nsInstanceId: str
    operationState: NsLcmOperationStateType
    tags: Dict[str, str]
    tasks: List[GetSolNetworkOperationTaskDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolFunctionPackageMetadataTypeDef(BaseModel):
    createdAt: datetime
    lastModified: datetime
    vnfd: Optional[FunctionArtifactMetaTypeDef] = None

class PutSolFunctionPackageContentMetadataTypeDef(BaseModel):
    vnfd: Optional[FunctionArtifactMetaTypeDef] = None

class ValidateSolFunctionPackageContentMetadataTypeDef(BaseModel):
    vnfd: Optional[FunctionArtifactMetaTypeDef] = None

class GetSolNetworkPackageMetadataTypeDef(BaseModel):
    createdAt: datetime
    lastModified: datetime
    nsd: Optional[NetworkArtifactMetaTypeDef] = None

class PutSolNetworkPackageContentMetadataTypeDef(BaseModel):
    nsd: Optional[NetworkArtifactMetaTypeDef] = None

class ValidateSolNetworkPackageContentMetadataTypeDef(BaseModel):
    nsd: Optional[NetworkArtifactMetaTypeDef] = None

class GetSolVnfInfoTypeDef(BaseModel):
    vnfState: Optional[VnfOperationalStateType] = None
    vnfcResourceInfo: Optional[List[GetSolVnfcResourceInfoTypeDef]] = None

class ListSolFunctionInstancesOutputTypeDef(BaseModel):
    functionInstances: List[ListSolFunctionInstanceInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSolFunctionPackagesOutputTypeDef(BaseModel):
    functionPackages: List[ListSolFunctionPackageInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSolNetworkInstancesOutputTypeDef(BaseModel):
    networkInstances: List[ListSolNetworkInstanceInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSolNetworkOperationsOutputTypeDef(BaseModel):
    networkOperations: List[ListSolNetworkOperationsInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSolNetworkPackagesOutputTypeDef(BaseModel):
    networkPackages: List[ListSolNetworkPackageInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolFunctionPackageOutputTypeDef(BaseModel):
    arn: str
    id: str
    metadata: GetSolFunctionPackageMetadataTypeDef
    onboardingState: OnboardingStateType
    operationalState: OperationalStateType
    tags: Dict[str, str]
    usageState: UsageStateType
    vnfProductName: str
    vnfProvider: str
    vnfdId: str
    vnfdVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutSolFunctionPackageContentOutputTypeDef(BaseModel):
    id: str
    metadata: PutSolFunctionPackageContentMetadataTypeDef
    vnfProductName: str
    vnfProvider: str
    vnfdId: str
    vnfdVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ValidateSolFunctionPackageContentOutputTypeDef(BaseModel):
    id: str
    metadata: ValidateSolFunctionPackageContentMetadataTypeDef
    vnfProductName: str
    vnfProvider: str
    vnfdId: str
    vnfdVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolNetworkPackageOutputTypeDef(BaseModel):
    arn: str
    id: str
    metadata: GetSolNetworkPackageMetadataTypeDef
    nsdId: str
    nsdName: str
    nsdOnboardingState: NsdOnboardingStateType
    nsdOperationalState: NsdOperationalStateType
    nsdUsageState: NsdUsageStateType
    nsdVersion: str
    tags: Dict[str, str]
    vnfPkgIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutSolNetworkPackageContentOutputTypeDef(BaseModel):
    arn: str
    id: str
    metadata: PutSolNetworkPackageContentMetadataTypeDef
    nsdId: str
    nsdName: str
    nsdVersion: str
    vnfPkgIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ValidateSolNetworkPackageContentOutputTypeDef(BaseModel):
    arn: str
    id: str
    metadata: ValidateSolNetworkPackageContentMetadataTypeDef
    nsdId: str
    nsdName: str
    nsdVersion: str
    vnfPkgIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolFunctionInstanceOutputTypeDef(BaseModel):
    arn: str
    id: str
    instantiatedVnfInfo: GetSolVnfInfoTypeDef
    instantiationState: VnfInstantiationStateType
    metadata: GetSolFunctionInstanceMetadataTypeDef
    nsInstanceId: str
    tags: Dict[str, str]
    vnfPkgId: str
    vnfProductName: str
    vnfProvider: str
    vnfdId: str
    vnfdVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

