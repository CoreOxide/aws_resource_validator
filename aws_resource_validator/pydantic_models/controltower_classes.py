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
from aws_resource_validator.pydantic_models.controltower_constants import *

class BaselineOperationTypeDef(BaseModel):
    endTime: Optional[datetime] = None
    operationIdentifier: Optional[str] = None
    operationType: Optional[BaselineOperationTypeType] = None
    startTime: Optional[datetime] = None
    status: Optional[BaselineOperationStatusType] = None
    statusMessage: Optional[str] = None

class BaselineSummaryTypeDef(BaseModel):
    arn: str
    name: str
    description: Optional[str] = None

class ControlOperationFilterTypeDef(BaseModel):
    controlIdentifiers: Optional[Sequence[str]] = None
    controlOperationTypes: Optional[Sequence[ControlOperationTypeType]] = None
    enabledControlIdentifiers: Optional[Sequence[str]] = None
    statuses: Optional[Sequence[ControlOperationStatusType]] = None
    targetIdentifiers: Optional[Sequence[str]] = None

class ControlOperationSummaryTypeDef(BaseModel):
    controlIdentifier: Optional[str] = None
    enabledControlIdentifier: Optional[str] = None
    endTime: Optional[datetime] = None
    operationIdentifier: Optional[str] = None
    operationType: Optional[ControlOperationTypeType] = None
    startTime: Optional[datetime] = None
    status: Optional[ControlOperationStatusType] = None
    statusMessage: Optional[str] = None
    targetIdentifier: Optional[str] = None

class ControlOperationTypeDef(BaseModel):
    controlIdentifier: Optional[str] = None
    enabledControlIdentifier: Optional[str] = None
    endTime: Optional[datetime] = None
    operationIdentifier: Optional[str] = None
    operationType: Optional[ControlOperationTypeType] = None
    startTime: Optional[datetime] = None
    status: Optional[ControlOperationStatusType] = None
    statusMessage: Optional[str] = None
    targetIdentifier: Optional[str] = None

class CreateLandingZoneInputRequestTypeDef(BaseModel):
    manifest: Mapping[str, Any]
    version: str
    tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteLandingZoneInputRequestTypeDef(BaseModel):
    landingZoneIdentifier: str

class DisableBaselineInputRequestTypeDef(BaseModel):
    enabledBaselineIdentifier: str

class DisableControlInputRequestTypeDef(BaseModel):
    controlIdentifier: str
    targetIdentifier: str

class DriftStatusSummaryTypeDef(BaseModel):
    driftStatus: Optional[DriftStatusType] = None

class EnabledBaselineParameterTypeDef(BaseModel):
    key: str
    value: Mapping[str, Any]

class EnabledControlParameterTypeDef(BaseModel):
    key: str
    value: Mapping[str, Any]

class EnabledBaselineParameterSummaryTypeDef(BaseModel):
    key: str
    value: Dict[str, Any]

class EnablementStatusSummaryTypeDef(BaseModel):
    lastOperationIdentifier: Optional[str] = None
    status: Optional[EnablementStatusType] = None

class EnabledBaselineFilterTypeDef(BaseModel):
    baselineIdentifiers: Optional[Sequence[str]] = None
    targetIdentifiers: Optional[Sequence[str]] = None

class EnabledControlParameterSummaryTypeDef(BaseModel):
    key: str
    value: Dict[str, Any]

class RegionTypeDef(BaseModel):
    name: Optional[str] = None

class EnabledControlFilterTypeDef(BaseModel):
    controlIdentifiers: Optional[Sequence[str]] = None
    driftStatuses: Optional[Sequence[DriftStatusType]] = None
    statuses: Optional[Sequence[EnablementStatusType]] = None

class GetBaselineInputRequestTypeDef(BaseModel):
    baselineIdentifier: str

class GetBaselineOperationInputRequestTypeDef(BaseModel):
    operationIdentifier: str

class GetControlOperationInputRequestTypeDef(BaseModel):
    operationIdentifier: str

class GetEnabledBaselineInputRequestTypeDef(BaseModel):
    enabledBaselineIdentifier: str

class GetEnabledControlInputRequestTypeDef(BaseModel):
    enabledControlIdentifier: str

class GetLandingZoneInputRequestTypeDef(BaseModel):
    landingZoneIdentifier: str

class GetLandingZoneOperationInputRequestTypeDef(BaseModel):
    operationIdentifier: str

class LandingZoneOperationDetailTypeDef(BaseModel):
    endTime: Optional[datetime] = None
    operationIdentifier: Optional[str] = None
    operationType: Optional[LandingZoneOperationTypeType] = None
    startTime: Optional[datetime] = None
    status: Optional[LandingZoneOperationStatusType] = None
    statusMessage: Optional[str] = None

class LandingZoneDriftStatusSummaryTypeDef(BaseModel):
    status: Optional[LandingZoneDriftStatusType] = None

class LandingZoneOperationFilterTypeDef(BaseModel):
    statuses: Optional[Sequence[LandingZoneOperationStatusType]] = None
    types: Optional[Sequence[LandingZoneOperationTypeType]] = None

class LandingZoneOperationSummaryTypeDef(BaseModel):
    operationIdentifier: Optional[str] = None
    operationType: Optional[LandingZoneOperationTypeType] = None
    status: Optional[LandingZoneOperationStatusType] = None

class LandingZoneSummaryTypeDef(BaseModel):
    arn: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBaselinesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLandingZonesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str

class ResetEnabledBaselineInputRequestTypeDef(BaseModel):
    enabledBaselineIdentifier: str

class ResetLandingZoneInputRequestTypeDef(BaseModel):
    landingZoneIdentifier: str

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateLandingZoneInputRequestTypeDef(BaseModel):
    landingZoneIdentifier: str
    manifest: Mapping[str, Any]
    version: str

class ListControlOperationsInputRequestTypeDef(BaseModel):
    filter: Optional[ControlOperationFilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class CreateLandingZoneOutputTypeDef(BaseModel):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLandingZoneOutputTypeDef(BaseModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableBaselineOutputTypeDef(BaseModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableControlOutputTypeDef(BaseModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableBaselineOutputTypeDef(BaseModel):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableControlOutputTypeDef(BaseModel):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBaselineOperationOutputTypeDef(BaseModel):
    baselineOperation: BaselineOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBaselineOutputTypeDef(BaseModel):
    arn: str
    description: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetControlOperationOutputTypeDef(BaseModel):
    controlOperation: ControlOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBaselinesOutputTypeDef(BaseModel):
    baselines: List[BaselineSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListControlOperationsOutputTypeDef(BaseModel):
    controlOperations: List[ControlOperationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ResetEnabledBaselineOutputTypeDef(BaseModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetLandingZoneOutputTypeDef(BaseModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnabledBaselineOutputTypeDef(BaseModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnabledControlOutputTypeDef(BaseModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLandingZoneOutputTypeDef(BaseModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableBaselineInputRequestTypeDef(BaseModel):
    baselineIdentifier: str
    baselineVersion: str
    targetIdentifier: str
    parameters: Optional[Sequence[EnabledBaselineParameterTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateEnabledBaselineInputRequestTypeDef(BaseModel):
    baselineVersion: str
    enabledBaselineIdentifier: str
    parameters: Optional[Sequence[EnabledBaselineParameterTypeDef]] = None

class EnableControlInputRequestTypeDef(BaseModel):
    controlIdentifier: str
    targetIdentifier: str
    parameters: Optional[Sequence[EnabledControlParameterTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateEnabledControlInputRequestTypeDef(BaseModel):
    enabledControlIdentifier: str
    parameters: Sequence[EnabledControlParameterTypeDef]

class EnabledBaselineDetailsTypeDef(BaseModel):
    arn: str
    baselineIdentifier: str
    statusSummary: EnablementStatusSummaryTypeDef
    targetIdentifier: str
    baselineVersion: Optional[str] = None
    parameters: Optional[List[EnabledBaselineParameterSummaryTypeDef]] = None

class EnabledBaselineSummaryTypeDef(BaseModel):
    arn: str
    baselineIdentifier: str
    statusSummary: EnablementStatusSummaryTypeDef
    targetIdentifier: str
    baselineVersion: Optional[str] = None

class EnabledControlSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    controlIdentifier: Optional[str] = None
    driftStatusSummary: Optional[DriftStatusSummaryTypeDef] = None
    statusSummary: Optional[EnablementStatusSummaryTypeDef] = None
    targetIdentifier: Optional[str] = None

class ListEnabledBaselinesInputRequestTypeDef(BaseModel):
    filter: Optional[EnabledBaselineFilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class EnabledControlDetailsTypeDef(BaseModel):
    arn: Optional[str] = None
    controlIdentifier: Optional[str] = None
    driftStatusSummary: Optional[DriftStatusSummaryTypeDef] = None
    parameters: Optional[List[EnabledControlParameterSummaryTypeDef]] = None
    statusSummary: Optional[EnablementStatusSummaryTypeDef] = None
    targetIdentifier: Optional[str] = None
    targetRegions: Optional[List[RegionTypeDef]] = None

class ListEnabledControlsInputRequestTypeDef(BaseModel):
    filter: Optional[EnabledControlFilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targetIdentifier: Optional[str] = None

class GetLandingZoneOperationOutputTypeDef(BaseModel):
    operationDetails: LandingZoneOperationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LandingZoneDetailTypeDef(BaseModel):
    manifest: Dict[str, Any]
    version: str
    arn: Optional[str] = None
    driftStatus: Optional[LandingZoneDriftStatusSummaryTypeDef] = None
    latestAvailableVersion: Optional[str] = None
    status: Optional[LandingZoneStatusType] = None

class ListLandingZoneOperationsInputRequestTypeDef(BaseModel):
    filter: Optional[LandingZoneOperationFilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLandingZoneOperationsOutputTypeDef(BaseModel):
    landingZoneOperations: List[LandingZoneOperationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLandingZonesOutputTypeDef(BaseModel):
    landingZones: List[LandingZoneSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBaselinesInputListBaselinesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListControlOperationsInputListControlOperationsPaginateTypeDef(BaseModel):
    filter: Optional[ControlOperationFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnabledBaselinesInputListEnabledBaselinesPaginateTypeDef(BaseModel):
    filter: Optional[EnabledBaselineFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnabledControlsInputListEnabledControlsPaginateTypeDef(BaseModel):
    filter: Optional[EnabledControlFilterTypeDef] = None
    targetIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLandingZoneOperationsInputListLandingZoneOperationsPaginateTypeDef(BaseModel):
    filter: Optional[LandingZoneOperationFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLandingZonesInputListLandingZonesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetEnabledBaselineOutputTypeDef(BaseModel):
    enabledBaselineDetails: EnabledBaselineDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnabledBaselinesOutputTypeDef(BaseModel):
    enabledBaselines: List[EnabledBaselineSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnabledControlsOutputTypeDef(BaseModel):
    enabledControls: List[EnabledControlSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnabledControlOutputTypeDef(BaseModel):
    enabledControlDetails: EnabledControlDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLandingZoneOutputTypeDef(BaseModel):
    landingZone: LandingZoneDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

