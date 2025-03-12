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


class CreateLandingZoneInputTypeDef(BaseValidatorModel):
    manifest: Mapping[str, Any]
    version: str
    tags: Optional[Mapping[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteLandingZoneInputTypeDef(BaseValidatorModel):
    landingZoneIdentifier: str


class DisableBaselineInputTypeDef(BaseValidatorModel):
    enabledBaselineIdentifier: str


class DisableControlInputTypeDef(BaseValidatorModel):
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
    parentIdentifiers: Optional[Sequence[str]] = None
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


class GetBaselineInputTypeDef(BaseValidatorModel):
    baselineIdentifier: str


class GetBaselineOperationInputTypeDef(BaseValidatorModel):
    operationIdentifier: str


class GetControlOperationInputTypeDef(BaseValidatorModel):
    operationIdentifier: str


class GetEnabledBaselineInputTypeDef(BaseValidatorModel):
    enabledBaselineIdentifier: str


class GetEnabledControlInputTypeDef(BaseValidatorModel):
    enabledControlIdentifier: str


class GetLandingZoneInputTypeDef(BaseValidatorModel):
    landingZoneIdentifier: str


class GetLandingZoneOperationInputTypeDef(BaseValidatorModel):
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


class ListBaselinesInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListLandingZonesInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str


class ResetEnabledBaselineInputTypeDef(BaseValidatorModel):
    enabledBaselineIdentifier: str


class ResetEnabledControlInputTypeDef(BaseValidatorModel):
    enabledControlIdentifier: str


class ResetLandingZoneInputTypeDef(BaseValidatorModel):
    landingZoneIdentifier: str


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateLandingZoneInputTypeDef(BaseValidatorModel):
    landingZoneIdentifier: str
    manifest: Mapping[str, Any]
    version: str


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListControlOperationsOutputTypeDef(BaseValidatorModel):
    controlOperations: List[ControlOperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ResetEnabledBaselineOutputTypeDef(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResetEnabledControlOutputTypeDef(BaseValidatorModel):
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


class EnableBaselineInputTypeDef(BaseValidatorModel):
    baselineIdentifier: str
    baselineVersion: str
    targetIdentifier: str
    parameters: Optional[Sequence[EnabledBaselineParameterTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateEnabledBaselineInputTypeDef(BaseValidatorModel):
    baselineVersion: str
    enabledBaselineIdentifier: str
    parameters: Optional[Sequence[EnabledBaselineParameterTypeDef]] = None


class EnableControlInputTypeDef(BaseValidatorModel):
    controlIdentifier: str
    targetIdentifier: str
    parameters: Optional[Sequence[EnabledControlParameterTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateEnabledControlInputTypeDef(BaseValidatorModel):
    enabledControlIdentifier: str
    parameters: Sequence[EnabledControlParameterTypeDef]


class EnabledBaselineDetailsTypeDef(BaseValidatorModel):
    arn: str
    baselineIdentifier: str
    statusSummary: EnablementStatusSummaryTypeDef
    targetIdentifier: str
    baselineVersion: Optional[str] = None
    parameters: Optional[List[EnabledBaselineParameterSummaryTypeDef]] = None
    parentIdentifier: Optional[str] = None


class EnabledBaselineSummaryTypeDef(BaseValidatorModel):
    arn: str
    baselineIdentifier: str
    statusSummary: EnablementStatusSummaryTypeDef
    targetIdentifier: str
    baselineVersion: Optional[str] = None
    parentIdentifier: Optional[str] = None


class EnabledControlSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    controlIdentifier: Optional[str] = None
    driftStatusSummary: Optional[DriftStatusSummaryTypeDef] = None
    statusSummary: Optional[EnablementStatusSummaryTypeDef] = None
    targetIdentifier: Optional[str] = None


class EnabledControlDetailsTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    controlIdentifier: Optional[str] = None
    driftStatusSummary: Optional[DriftStatusSummaryTypeDef] = None
    parameters: Optional[List[EnabledControlParameterSummaryTypeDef]] = None
    statusSummary: Optional[EnablementStatusSummaryTypeDef] = None
    targetIdentifier: Optional[str] = None
    targetRegions: Optional[List[RegionTypeDef]] = None


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


class ListLandingZoneOperationsOutputTypeDef(BaseValidatorModel):
    landingZoneOperations: List[LandingZoneOperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListLandingZonesOutputTypeDef(BaseValidatorModel):
    landingZones: List[LandingZoneSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListBaselinesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLandingZonesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetEnabledBaselineOutputTypeDef(BaseValidatorModel):
    enabledBaselineDetails: EnabledBaselineDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListEnabledBaselinesOutputTypeDef(BaseValidatorModel):
    enabledBaselines: List[EnabledBaselineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListEnabledControlsOutputTypeDef(BaseValidatorModel):
    enabledControls: List[EnabledControlSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetEnabledControlOutputTypeDef(BaseValidatorModel):
    enabledControlDetails: EnabledControlDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetLandingZoneOutputTypeDef(BaseValidatorModel):
    landingZone: LandingZoneDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


