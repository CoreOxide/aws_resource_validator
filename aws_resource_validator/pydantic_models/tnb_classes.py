from datetime import datetime

from botocore.response import StreamingBody

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
from aws_resource_validator.pydantic_models.tnb_constants import *

class CancelSolNetworkOperationInputRequestTypeDef(BaseValidatorModel):
    nsLcmOpOccId: str

class CreateSolFunctionPackageInputRequestTypeDef(BaseValidatorModel):
    tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateSolNetworkInstanceInputRequestTypeDef(BaseValidatorModel):
    nsName: str
    nsdInfoId: str
    nsDescription: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateSolNetworkPackageInputRequestTypeDef(BaseValidatorModel):
    tags: Optional[Mapping[str, str]] = None

class DeleteSolFunctionPackageInputRequestTypeDef(BaseValidatorModel):
    vnfPkgId: str

class DeleteSolNetworkInstanceInputRequestTypeDef(BaseValidatorModel):
    nsInstanceId: str

class DeleteSolNetworkPackageInputRequestTypeDef(BaseValidatorModel):
    nsdInfoId: str

class ErrorInfoTypeDef(BaseValidatorModel):
    cause: Optional[str] = None
    details: Optional[str] = None

class ToscaOverrideTypeDef(BaseValidatorModel):
    defaultValue: Optional[str] = None
    name: Optional[str] = None

class GetSolFunctionInstanceInputRequestTypeDef(BaseValidatorModel):
    vnfInstanceId: str

class GetSolFunctionInstanceMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime

class GetSolFunctionPackageContentInputRequestTypeDef(BaseValidatorModel):
    accept: Literal["application/zip"]
    vnfPkgId: str

class GetSolFunctionPackageDescriptorInputRequestTypeDef(BaseValidatorModel):
    accept: Literal["text/plain"]
    vnfPkgId: str

class GetSolFunctionPackageInputRequestTypeDef(BaseValidatorModel):
    vnfPkgId: str

class GetSolInstantiatedVnfInfoTypeDef(BaseValidatorModel):
    vnfState: Optional[VnfOperationalStateType] = None

class GetSolNetworkInstanceInputRequestTypeDef(BaseValidatorModel):
    nsInstanceId: str

class GetSolNetworkInstanceMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime

class LcmOperationInfoTypeDef(BaseValidatorModel):
    nsLcmOpOccId: str

class GetSolNetworkOperationInputRequestTypeDef(BaseValidatorModel):
    nsLcmOpOccId: str

class GetSolNetworkOperationMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime

class ProblemDetailsTypeDef(BaseValidatorModel):
    detail: str
    title: Optional[str] = None

class GetSolNetworkPackageContentInputRequestTypeDef(BaseValidatorModel):
    accept: Literal["application/zip"]
    nsdInfoId: str

class GetSolNetworkPackageDescriptorInputRequestTypeDef(BaseValidatorModel):
    nsdInfoId: str

class GetSolNetworkPackageInputRequestTypeDef(BaseValidatorModel):
    nsdInfoId: str

class GetSolVnfcResourceInfoMetadataTypeDef(BaseValidatorModel):
    cluster: Optional[str] = None
    helmChart: Optional[str] = None
    nodeGroup: Optional[str] = None

class InstantiateSolNetworkInstanceInputRequestTypeDef(BaseValidatorModel):
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

class ListSolFunctionInstancesInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSolFunctionPackageMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime

class ListSolFunctionPackagesInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSolNetworkInstanceMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime

class ListSolNetworkInstancesInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSolNetworkOperationsMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime

class ListSolNetworkOperationsInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSolNetworkPackageMetadataTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastModified: datetime

class ListSolNetworkPackagesInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class TerminateSolNetworkInstanceInputRequestTypeDef(BaseValidatorModel):
    nsInstanceId: str
    tags: Optional[Mapping[str, str]] = None

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateSolFunctionPackageInputRequestTypeDef(BaseValidatorModel):
    operationalState: OperationalStateType
    vnfPkgId: str

class UpdateSolNetworkModifyTypeDef(BaseValidatorModel):
    vnfConfigurableProperties: Mapping[str, Any]
    vnfInstanceId: str

class UpdateSolNetworkPackageInputRequestTypeDef(BaseValidatorModel):
    nsdInfoId: str
    nsdOperationalState: NsdOperationalStateType

class PutSolFunctionPackageContentInputRequestTypeDef(BaseValidatorModel):
    file: BlobTypeDef
    vnfPkgId: str
    contentType: Optional[Literal["application/zip"]] = None

class PutSolNetworkPackageContentInputRequestTypeDef(BaseValidatorModel):
    file: BlobTypeDef
    nsdInfoId: str
    contentType: Optional[Literal["application/zip"]] = None

class ValidateSolFunctionPackageContentInputRequestTypeDef(BaseValidatorModel):
    file: BlobTypeDef
    vnfPkgId: str
    contentType: Optional[Literal["application/zip"]] = None

class ValidateSolNetworkPackageContentInputRequestTypeDef(BaseValidatorModel):
    file: BlobTypeDef
    nsdInfoId: str
    contentType: Optional[Literal["application/zip"]] = None

class CreateSolFunctionPackageOutputTypeDef(BaseValidatorModel):
    arn: str
    id: str
    onboardingState: OnboardingStateType
    operationalState: OperationalStateType
    tags: Dict[str, str]
    usageState: UsageStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSolNetworkInstanceOutputTypeDef(BaseValidatorModel):
    arn: str
    id: str
    nsInstanceName: str
    nsdInfoId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSolNetworkPackageOutputTypeDef(BaseValidatorModel):
    arn: str
    id: str
    nsdOnboardingState: NsdOnboardingStateType
    nsdOperationalState: NsdOperationalStateType
    nsdUsageState: NsdUsageStateType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

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

class GetSolNetworkInstanceOutputTypeDef(BaseValidatorModel):
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

class GetSolVnfcResourceInfoTypeDef(BaseValidatorModel):
    metadata: Optional[GetSolVnfcResourceInfoMetadataTypeDef] = None

class ListSolFunctionInstanceInfoTypeDef(BaseValidatorModel):
    arn: str
    id: str
    instantiationState: VnfInstantiationStateType
    metadata: ListSolFunctionInstanceMetadataTypeDef
    nsInstanceId: str
    vnfPkgId: str
    instantiatedVnfInfo: Optional[GetSolInstantiatedVnfInfoTypeDef] = None
    vnfPkgName: Optional[str] = None

class ListSolFunctionInstancesInputListSolFunctionInstancesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSolFunctionPackagesInputListSolFunctionPackagesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSolNetworkInstancesInputListSolNetworkInstancesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSolNetworkOperationsInputListSolNetworkOperationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSolNetworkPackagesInputListSolNetworkPackagesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSolFunctionPackageInfoTypeDef(BaseValidatorModel):
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

class ListSolNetworkInstanceInfoTypeDef(BaseValidatorModel):
    arn: str
    id: str
    metadata: ListSolNetworkInstanceMetadataTypeDef
    nsInstanceDescription: str
    nsInstanceName: str
    nsState: NsStateType
    nsdId: str
    nsdInfoId: str

class ListSolNetworkOperationsInfoTypeDef(BaseValidatorModel):
    arn: str
    id: str
    lcmOperationType: LcmOperationTypeType
    nsInstanceId: str
    operationState: NsLcmOperationStateType
    error: Optional[ProblemDetailsTypeDef] = None
    metadata: Optional[ListSolNetworkOperationsMetadataTypeDef] = None

class ListSolNetworkPackageInfoTypeDef(BaseValidatorModel):
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

class UpdateSolNetworkInstanceInputRequestTypeDef(BaseValidatorModel):
    nsInstanceId: str
    updateType: Literal["MODIFY_VNF_INFORMATION"]
    modifyVnfInfoData: Optional[UpdateSolNetworkModifyTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class GetSolNetworkOperationOutputTypeDef(BaseValidatorModel):
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

class ListSolFunctionInstancesOutputTypeDef(BaseValidatorModel):
    functionInstances: List[ListSolFunctionInstanceInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSolFunctionPackagesOutputTypeDef(BaseValidatorModel):
    functionPackages: List[ListSolFunctionPackageInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSolNetworkInstancesOutputTypeDef(BaseValidatorModel):
    networkInstances: List[ListSolNetworkInstanceInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSolNetworkOperationsOutputTypeDef(BaseValidatorModel):
    networkOperations: List[ListSolNetworkOperationsInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSolNetworkPackagesOutputTypeDef(BaseValidatorModel):
    networkPackages: List[ListSolNetworkPackageInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolFunctionPackageOutputTypeDef(BaseValidatorModel):
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

class PutSolFunctionPackageContentOutputTypeDef(BaseValidatorModel):
    id: str
    metadata: PutSolFunctionPackageContentMetadataTypeDef
    vnfProductName: str
    vnfProvider: str
    vnfdId: str
    vnfdVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ValidateSolFunctionPackageContentOutputTypeDef(BaseValidatorModel):
    id: str
    metadata: ValidateSolFunctionPackageContentMetadataTypeDef
    vnfProductName: str
    vnfProvider: str
    vnfdId: str
    vnfdVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolNetworkPackageOutputTypeDef(BaseValidatorModel):
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

class PutSolNetworkPackageContentOutputTypeDef(BaseValidatorModel):
    arn: str
    id: str
    metadata: PutSolNetworkPackageContentMetadataTypeDef
    nsdId: str
    nsdName: str
    nsdVersion: str
    vnfPkgIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ValidateSolNetworkPackageContentOutputTypeDef(BaseValidatorModel):
    arn: str
    id: str
    metadata: ValidateSolNetworkPackageContentMetadataTypeDef
    nsdId: str
    nsdName: str
    nsdVersion: str
    vnfPkgIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolFunctionInstanceOutputTypeDef(BaseValidatorModel):
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

