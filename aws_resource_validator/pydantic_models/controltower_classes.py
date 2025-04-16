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

class BaselineOperation(BaseValidatorModel):
    endTime: Optional[datetime] = None
    operationIdentifier: Optional[str] = None
    operationType: Optional[BaselineOperationTypeType] = None
    startTime: Optional[datetime] = None
    status: Optional[BaselineOperationStatusType] = None
    statusMessage: Optional[str] = None


class BaselineSummary(BaseValidatorModel):
    arn: str
    name: str
    description: Optional[str] = None


class ControlOperationFilter(BaseValidatorModel):
    controlIdentifiers: Optional[Sequence[str]] = None
    controlOperationTypes: Optional[Sequence[ControlOperationTypeType]] = None
    enabledControlIdentifiers: Optional[Sequence[str]] = None
    statuses: Optional[Sequence[ControlOperationStatusType]] = None
    targetIdentifiers: Optional[Sequence[str]] = None


class ControlOperationSummary(BaseValidatorModel):
    controlIdentifier: Optional[str] = None
    enabledControlIdentifier: Optional[str] = None
    endTime: Optional[datetime] = None
    operationIdentifier: Optional[str] = None
    operationType: Optional[ControlOperationTypeType] = None
    startTime: Optional[datetime] = None
    status: Optional[ControlOperationStatusType] = None
    statusMessage: Optional[str] = None
    targetIdentifier: Optional[str] = None


class ControlOperation(BaseValidatorModel):
    controlIdentifier: Optional[str] = None
    enabledControlIdentifier: Optional[str] = None
    endTime: Optional[datetime] = None
    operationIdentifier: Optional[str] = None
    operationType: Optional[ControlOperationTypeType] = None
    startTime: Optional[datetime] = None
    status: Optional[ControlOperationStatusType] = None
    statusMessage: Optional[str] = None
    targetIdentifier: Optional[str] = None


class CreateLandingZoneInput(BaseValidatorModel):
    manifest: Mapping[str, Any]
    version: str
    tags: Optional[Mapping[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteLandingZoneInput(BaseValidatorModel):
    landingZoneIdentifier: str


class DisableBaselineInput(BaseValidatorModel):
    enabledBaselineIdentifier: str


class DisableControlInput(BaseValidatorModel):
    controlIdentifier: str
    targetIdentifier: str


class DriftStatusSummary(BaseValidatorModel):
    driftStatus: Optional[DriftStatusType] = None


class EnabledBaselineParameter(BaseValidatorModel):
    key: str
    value: Mapping[str, Any]


class EnabledControlParameter(BaseValidatorModel):
    key: str
    value: Mapping[str, Any]


class EnabledBaselineParameterSummary(BaseValidatorModel):
    key: str
    value: Dict[str, Any]


class EnablementStatusSummary(BaseValidatorModel):
    lastOperationIdentifier: Optional[str] = None
    status: Optional[EnablementStatusType] = None


class EnabledBaselineFilter(BaseValidatorModel):
    baselineIdentifiers: Optional[Sequence[str]] = None
    parentIdentifiers: Optional[Sequence[str]] = None
    targetIdentifiers: Optional[Sequence[str]] = None


class EnabledControlParameterSummary(BaseValidatorModel):
    key: str
    value: Dict[str, Any]


class Region(BaseValidatorModel):
    name: Optional[str] = None


class EnabledControlFilter(BaseValidatorModel):
    controlIdentifiers: Optional[Sequence[str]] = None
    driftStatuses: Optional[Sequence[DriftStatusType]] = None
    statuses: Optional[Sequence[EnablementStatusType]] = None


class GetBaselineInput(BaseValidatorModel):
    baselineIdentifier: str


class GetBaselineOperationInput(BaseValidatorModel):
    operationIdentifier: str


class GetControlOperationInput(BaseValidatorModel):
    operationIdentifier: str


class GetEnabledBaselineInput(BaseValidatorModel):
    enabledBaselineIdentifier: str


class GetEnabledControlInput(BaseValidatorModel):
    enabledControlIdentifier: str


class GetLandingZoneInput(BaseValidatorModel):
    landingZoneIdentifier: str


class GetLandingZoneOperationInput(BaseValidatorModel):
    operationIdentifier: str


class LandingZoneOperationDetail(BaseValidatorModel):
    endTime: Optional[datetime] = None
    operationIdentifier: Optional[str] = None
    operationType: Optional[LandingZoneOperationTypeType] = None
    startTime: Optional[datetime] = None
    status: Optional[LandingZoneOperationStatusType] = None
    statusMessage: Optional[str] = None


class LandingZoneDriftStatusSummary(BaseValidatorModel):
    status: Optional[LandingZoneDriftStatusType] = None


class LandingZoneOperationSummary(BaseValidatorModel):
    operationIdentifier: Optional[str] = None
    operationType: Optional[LandingZoneOperationTypeType] = None
    status: Optional[LandingZoneOperationStatusType] = None


class LandingZoneSummary(BaseValidatorModel):
    arn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBaselinesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListLandingZonesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class ResetEnabledBaselineInput(BaseValidatorModel):
    enabledBaselineIdentifier: str


class ResetEnabledControlInput(BaseValidatorModel):
    enabledControlIdentifier: str


class ResetLandingZoneInput(BaseValidatorModel):
    landingZoneIdentifier: str


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateLandingZoneInput(BaseValidatorModel):
    landingZoneIdentifier: str
    manifest: Mapping[str, Any]
    version: str


class CreateLandingZoneOutput(BaseValidatorModel):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


class DeleteLandingZoneOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


class DisableBaselineOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


class DisableControlOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


class EnableBaselineOutput(BaseValidatorModel):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


class EnableControlOutput(BaseValidatorModel):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


class GetBaselineOperationOutput(BaseValidatorModel):
    baselineOperation: BaselineOperation
    ResponseMetadata: ResponseMetadata


class GetBaselineOutput(BaseValidatorModel):
    arn: str
    description: str
    name: str
    ResponseMetadata: ResponseMetadata


class GetControlOperationOutput(BaseValidatorModel):
    controlOperation: ControlOperation
    ResponseMetadata: ResponseMetadata


class ListBaselinesOutput(BaseValidatorModel):
    baselines: List[BaselineSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListControlOperationsOutput(BaseValidatorModel):
    controlOperations: List[ControlOperationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ResetEnabledBaselineOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


class ResetEnabledControlOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


class ResetLandingZoneOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


class UpdateEnabledBaselineOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


class UpdateEnabledControlOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


class UpdateLandingZoneOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


class EnableBaselineInput(BaseValidatorModel):
    baselineIdentifier: str
    baselineVersion: str
    targetIdentifier: str
    parameters: Optional[Sequence[EnabledBaselineParameter]] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateEnabledBaselineInput(BaseValidatorModel):
    baselineVersion: str
    enabledBaselineIdentifier: str
    parameters: Optional[Sequence[EnabledBaselineParameter]] = None


class EnableControlInput(BaseValidatorModel):
    controlIdentifier: str
    targetIdentifier: str
    parameters: Optional[Sequence[EnabledControlParameter]] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateEnabledControlInput(BaseValidatorModel):
    enabledControlIdentifier: str
    parameters: Sequence[EnabledControlParameter]


class EnabledBaselineDetails(BaseValidatorModel):
    arn: str
    baselineIdentifier: str
    statusSummary: EnablementStatusSummary
    targetIdentifier: str
    baselineVersion: Optional[str] = None
    parameters: Optional[List[EnabledBaselineParameterSummary]] = None
    parentIdentifier: Optional[str] = None


class EnabledBaselineSummary(BaseValidatorModel):
    arn: str
    baselineIdentifier: str
    statusSummary: EnablementStatusSummary
    targetIdentifier: str
    baselineVersion: Optional[str] = None
    parentIdentifier: Optional[str] = None


class EnabledControlSummary(BaseValidatorModel):
    arn: Optional[str] = None
    controlIdentifier: Optional[str] = None
    driftStatusSummary: Optional[DriftStatusSummary] = None
    statusSummary: Optional[EnablementStatusSummary] = None
    targetIdentifier: Optional[str] = None


class EnabledControlDetails(BaseValidatorModel):
    arn: Optional[str] = None
    controlIdentifier: Optional[str] = None
    driftStatusSummary: Optional[DriftStatusSummary] = None
    parameters: Optional[List[EnabledControlParameterSummary]] = None
    statusSummary: Optional[EnablementStatusSummary] = None
    targetIdentifier: Optional[str] = None
    targetRegions: Optional[List[Region]] = None


class GetLandingZoneOperationOutput(BaseValidatorModel):
    operationDetails: LandingZoneOperationDetail
    ResponseMetadata: ResponseMetadata


class LandingZoneDetail(BaseValidatorModel):
    manifest: Dict[str, Any]
    version: str
    arn: Optional[str] = None
    driftStatus: Optional[LandingZoneDriftStatusSummary] = None
    latestAvailableVersion: Optional[str] = None
    status: Optional[LandingZoneStatusType] = None


class ListLandingZoneOperationsOutput(BaseValidatorModel):
    landingZoneOperations: List[LandingZoneOperationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListLandingZonesOutput(BaseValidatorModel):
    landingZones: List[LandingZoneSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListBaselinesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLandingZonesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetEnabledBaselineOutput(BaseValidatorModel):
    enabledBaselineDetails: EnabledBaselineDetails
    ResponseMetadata: ResponseMetadata


class ListEnabledBaselinesOutput(BaseValidatorModel):
    enabledBaselines: List[EnabledBaselineSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListEnabledControlsOutput(BaseValidatorModel):
    enabledControls: List[EnabledControlSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetEnabledControlOutput(BaseValidatorModel):
    enabledControlDetails: EnabledControlDetails
    ResponseMetadata: ResponseMetadata


class GetLandingZoneOutput(BaseValidatorModel):
    landingZone: LandingZoneDetail
    ResponseMetadata: ResponseMetadata


