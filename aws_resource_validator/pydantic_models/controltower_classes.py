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
from aws_resource_validator.pydantic_models.controltower_constants import *

class BaselineOperationTypeDef(BaseValidatorModel):
    endTime: Optional[datetime] = None
    operationIdentifier: Optional[str] = None
    operationType: Optional[BaselineOperationTypeType] = None
    startTime: Optional[datetime] = None
    status: Optional[BaselineOperationStatusType] = None
    statusMessage: Optional[str] = None

class BaselineSummaryTypeDef(BaseValidatorModel):
    arn: str
    name: str
    description: Optional[str] = None

class ControlOperationFilterTypeDef(BaseValidatorModel):
    controlIdentifiers: Optional[Sequence[str]] = None
    controlOperationTypes: Optional[Sequence[ControlOperationTypeType]] = None
    enabledControlIdentifiers: Optional[Sequence[str]] = None
    statuses: Optional[Sequence[ControlOperationStatusType]] = None
    targetIdentifiers: Optional[Sequence[str]] = None

class ControlOperationSummaryTypeDef(BaseValidatorModel):
    controlIdentifier: Optional[str] = None
    enabledControlIdentifier: Optional[str] = None
    endTime: Optional[datetime] = None
    operationIdentifier: Optional[str] = None
    operationType: Optional[ControlOperationTypeType] = None
    startTime: Optional[datetime] = None
    status: Optional[ControlOperationStatusType] = None
    statusMessage: Optional[str] = None
    targetIdentifier: Optional[str] = None

class ControlOperationTypeDef(BaseValidatorModel):
    controlIdentifier: Optional[str] = None
    enabledControlIdentifier: Optional[str] = None
    endTime: Optional[datetime] = None
    operationIdentifier: Optional[str] = None
    operationType: Optional[ControlOperationTypeType] = None
    startTime: Optional[datetime] = None
    status: Optional[ControlOperationStatusType] = None
    statusMessage: Optional[str] = None
    targetIdentifier: Optional[str] = None

class CreateLandingZoneInputRequestTypeDef(BaseValidatorModel):
    manifest: Mapping[str, Any]
    version: str
    tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteLandingZoneInputRequestTypeDef(BaseValidatorModel):
    landingZoneIdentifier: str

class DisableBaselineInputRequestTypeDef(BaseValidatorModel):
    enabledBaselineIdentifier: str

class DisableControlInputRequestTypeDef(BaseValidatorModel):
    controlIdentifier: str
    targetIdentifier: str

class DriftStatusSummaryTypeDef(BaseValidatorModel):
    driftStatus: Optional[DriftStatusType] = None

class EnabledBaselineParameterTypeDef(BaseValidatorModel):
    key: str
    value: Mapping[str, Any]

class EnabledControlParameterTypeDef(BaseValidatorModel):
    key: str
    value: Mapping[str, Any]

class EnabledBaselineParameterSummaryTypeDef(BaseValidatorModel):
    key: str
    value: Dict[str, Any]

class EnablementStatusSummaryTypeDef(BaseValidatorModel):
    lastOperationIdentifier: Optional[str] = None
    status: Optional[EnablementStatusType] = None

class EnabledBaselineFilterTypeDef(BaseValidatorModel):
    baselineIdentifiers: Optional[Sequence[str]] = None
    targetIdentifiers: Optional[Sequence[str]] = None

class EnabledControlParameterSummaryTypeDef(BaseValidatorModel):
    key: str
    value: Dict[str, Any]

class RegionTypeDef(BaseValidatorModel):
    name: Optional[str] = None

class EnabledControlFilterTypeDef(BaseValidatorModel):
    controlIdentifiers: Optional[Sequence[str]] = None
    driftStatuses: Optional[Sequence[DriftStatusType]] = None
    statuses: Optional[Sequence[EnablementStatusType]] = None

class GetBaselineInputRequestTypeDef(BaseValidatorModel):
    baselineIdentifier: str

class GetBaselineOperationInputRequestTypeDef(BaseValidatorModel):
    operationIdentifier: str

class GetControlOperationInputRequestTypeDef(BaseValidatorModel):
    operationIdentifier: str

class GetEnabledBaselineInputRequestTypeDef(BaseValidatorModel):
    enabledBaselineIdentifier: str

class GetEnabledControlInputRequestTypeDef(BaseValidatorModel):
    enabledControlIdentifier: str

class GetLandingZoneInputRequestTypeDef(BaseValidatorModel):
    landingZoneIdentifier: str

class GetLandingZoneOperationInputRequestTypeDef(BaseValidatorModel):
    operationIdentifier: str

class LandingZoneOperationDetailTypeDef(BaseValidatorModel):
    endTime: Optional[datetime] = None
    operationIdentifier: Optional[str] = None
    operationType: Optional[LandingZoneOperationTypeType] = None
    startTime: Optional[datetime] = None
    status: Optional[LandingZoneOperationStatusType] = None
    statusMessage: Optional[str] = None

class LandingZoneDriftStatusSummaryTypeDef(BaseValidatorModel):
    status: Optional[LandingZoneDriftStatusType] = None

class LandingZoneOperationFilterTypeDef(BaseValidatorModel):
    statuses: Optional[Sequence[LandingZoneOperationStatusType]] = None
    types: Optional[Sequence[LandingZoneOperationTypeType]] = None

class LandingZoneOperationSummaryTypeDef(BaseValidatorModel):
    operationIdentifier: Optional[str] = None
    operationType: Optional[LandingZoneOperationTypeType] = None
    status: Optional[LandingZoneOperationStatusType] = None

class LandingZoneSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBaselinesInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLandingZonesInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ResetEnabledBaselineInputRequestTypeDef(BaseValidatorModel):
    enabledBaselineIdentifier: str

class ResetLandingZoneInputRequestTypeDef(BaseValidatorModel):
    landingZoneIdentifier: str

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateLandingZoneInputRequestTypeDef(BaseValidatorModel):
    landingZoneIdentifier: str
    manifest: Mapping[str, Any]
    version: str

class ListControlOperationsInputRequestTypeDef(BaseValidatorModel):
    filter: Optional[ControlOperationFilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class CreateLandingZoneOutputTypeDef(BaseValidatorModel):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLandingZoneOutputTypeDef(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableBaselineOutputTypeDef(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableControlOutputTypeDef(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableBaselineOutputTypeDef(BaseValidatorModel):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableControlOutputTypeDef(BaseValidatorModel):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBaselineOperationOutputTypeDef(BaseValidatorModel):
    baselineOperation: BaselineOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBaselineOutputTypeDef(BaseValidatorModel):
    arn: str
    description: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetControlOperationOutputTypeDef(BaseValidatorModel):
    controlOperation: ControlOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBaselinesOutputTypeDef(BaseValidatorModel):
    baselines: List[BaselineSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListControlOperationsOutputTypeDef(BaseValidatorModel):
    controlOperations: List[ControlOperationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ResetEnabledBaselineOutputTypeDef(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetLandingZoneOutputTypeDef(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnabledBaselineOutputTypeDef(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnabledControlOutputTypeDef(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLandingZoneOutputTypeDef(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableBaselineInputRequestTypeDef(BaseValidatorModel):
    baselineIdentifier: str
    baselineVersion: str
    targetIdentifier: str
    parameters: Optional[Sequence[EnabledBaselineParameterTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateEnabledBaselineInputRequestTypeDef(BaseValidatorModel):
    baselineVersion: str
    enabledBaselineIdentifier: str
    parameters: Optional[Sequence[EnabledBaselineParameterTypeDef]] = None

class EnableControlInputRequestTypeDef(BaseValidatorModel):
    controlIdentifier: str
    targetIdentifier: str
    parameters: Optional[Sequence[EnabledControlParameterTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateEnabledControlInputRequestTypeDef(BaseValidatorModel):
    enabledControlIdentifier: str
    parameters: Sequence[EnabledControlParameterTypeDef]

class EnabledBaselineDetailsTypeDef(BaseValidatorModel):
    arn: str
    baselineIdentifier: str
    statusSummary: EnablementStatusSummaryTypeDef
    targetIdentifier: str
    baselineVersion: Optional[str] = None
    parameters: Optional[List[EnabledBaselineParameterSummaryTypeDef]] = None

class EnabledBaselineSummaryTypeDef(BaseValidatorModel):
    arn: str
    baselineIdentifier: str
    statusSummary: EnablementStatusSummaryTypeDef
    targetIdentifier: str
    baselineVersion: Optional[str] = None

class EnabledControlSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    controlIdentifier: Optional[str] = None
    driftStatusSummary: Optional[DriftStatusSummaryTypeDef] = None
    statusSummary: Optional[EnablementStatusSummaryTypeDef] = None
    targetIdentifier: Optional[str] = None

class ListEnabledBaselinesInputRequestTypeDef(BaseValidatorModel):
    filter: Optional[EnabledBaselineFilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class EnabledControlDetailsTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    controlIdentifier: Optional[str] = None
    driftStatusSummary: Optional[DriftStatusSummaryTypeDef] = None
    parameters: Optional[List[EnabledControlParameterSummaryTypeDef]] = None
    statusSummary: Optional[EnablementStatusSummaryTypeDef] = None
    targetIdentifier: Optional[str] = None
    targetRegions: Optional[List[RegionTypeDef]] = None

class ListEnabledControlsInputRequestTypeDef(BaseValidatorModel):
    filter: Optional[EnabledControlFilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targetIdentifier: Optional[str] = None

class GetLandingZoneOperationOutputTypeDef(BaseValidatorModel):
    operationDetails: LandingZoneOperationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LandingZoneDetailTypeDef(BaseValidatorModel):
    manifest: Dict[str, Any]
    version: str
    arn: Optional[str] = None
    driftStatus: Optional[LandingZoneDriftStatusSummaryTypeDef] = None
    latestAvailableVersion: Optional[str] = None
    status: Optional[LandingZoneStatusType] = None

class ListLandingZoneOperationsInputRequestTypeDef(BaseValidatorModel):
    filter: Optional[LandingZoneOperationFilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLandingZoneOperationsOutputTypeDef(BaseValidatorModel):
    landingZoneOperations: List[LandingZoneOperationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLandingZonesOutputTypeDef(BaseValidatorModel):
    landingZones: List[LandingZoneSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBaselinesInputListBaselinesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListControlOperationsInputListControlOperationsPaginateTypeDef(BaseValidatorModel):
    filter: Optional[ControlOperationFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnabledBaselinesInputListEnabledBaselinesPaginateTypeDef(BaseValidatorModel):
    filter: Optional[EnabledBaselineFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnabledControlsInputListEnabledControlsPaginateTypeDef(BaseValidatorModel):
    filter: Optional[EnabledControlFilterTypeDef] = None
    targetIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLandingZoneOperationsInputListLandingZoneOperationsPaginateTypeDef(BaseValidatorModel):
    filter: Optional[LandingZoneOperationFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLandingZonesInputListLandingZonesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetEnabledBaselineOutputTypeDef(BaseValidatorModel):
    enabledBaselineDetails: EnabledBaselineDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnabledBaselinesOutputTypeDef(BaseValidatorModel):
    enabledBaselines: List[EnabledBaselineSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnabledControlsOutputTypeDef(BaseValidatorModel):
    enabledControls: List[EnabledControlSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnabledControlOutputTypeDef(BaseValidatorModel):
    enabledControlDetails: EnabledControlDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLandingZoneOutputTypeDef(BaseValidatorModel):
    landingZone: LandingZoneDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

