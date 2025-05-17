from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.controltower.controltower_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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
    controlIdentifiers: Optional[List[str]] = None
    controlOperationTypes: Optional[List[ControlOperationTypeType]] = None
    enabledControlIdentifiers: Optional[List[str]] = None
    statuses: Optional[List[ControlOperationStatusType]] = None
    targetIdentifiers: Optional[List[str]] = None


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


# This class is the input for the 'create_landing_zone' function.
class CreateLandingZoneInput(BaseValidatorModel):
    manifest: Dict[str, Any]
    version: str
    tags: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'delete_landing_zone' function.
class DeleteLandingZoneInput(BaseValidatorModel):
    landingZoneIdentifier: str


# This class is the input for the 'disable_baseline' function.
class DisableBaselineInput(BaseValidatorModel):
    enabledBaselineIdentifier: str


# This class is the input for the 'disable_control' function.
class DisableControlInput(BaseValidatorModel):
    controlIdentifier: str
    targetIdentifier: str


class DriftStatusSummary(BaseValidatorModel):
    driftStatus: Optional[DriftStatusType] = None


class EnabledBaselineParameter(BaseValidatorModel):
    key: str
    value: Dict[str, Any]


class EnabledControlParameter(BaseValidatorModel):
    key: str
    value: Dict[str, Any]


class EnabledBaselineParameterSummary(BaseValidatorModel):
    key: str
    value: Dict[str, Any]


class EnablementStatusSummary(BaseValidatorModel):
    lastOperationIdentifier: Optional[str] = None
    status: Optional[EnablementStatusType] = None


class EnabledBaselineFilter(BaseValidatorModel):
    baselineIdentifiers: Optional[List[str]] = None
    parentIdentifiers: Optional[List[str]] = None
    targetIdentifiers: Optional[List[str]] = None


class EnabledControlParameterSummary(BaseValidatorModel):
    key: str
    value: Dict[str, Any]


class Region(BaseValidatorModel):
    name: Optional[str] = None


class EnabledControlFilter(BaseValidatorModel):
    controlIdentifiers: Optional[List[str]] = None
    driftStatuses: Optional[List[DriftStatusType]] = None
    statuses: Optional[List[EnablementStatusType]] = None


# This class is the input for the 'get_baseline' function.
class GetBaselineInput(BaseValidatorModel):
    baselineIdentifier: str


# This class is the input for the 'get_baseline_operation' function.
class GetBaselineOperationInput(BaseValidatorModel):
    operationIdentifier: str


# This class is the input for the 'get_control_operation' function.
class GetControlOperationInput(BaseValidatorModel):
    operationIdentifier: str


# This class is the input for the 'get_enabled_baseline' function.
class GetEnabledBaselineInput(BaseValidatorModel):
    enabledBaselineIdentifier: str


# This class is the input for the 'get_enabled_control' function.
class GetEnabledControlInput(BaseValidatorModel):
    enabledControlIdentifier: str


# This class is the input for the 'get_landing_zone' function.
class GetLandingZoneInput(BaseValidatorModel):
    landingZoneIdentifier: str


# This class is the input for the 'get_landing_zone_operation' function.
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


class LandingZoneOperationFilter(BaseValidatorModel):
    statuses: Optional[List[LandingZoneOperationStatusType]] = None
    types: Optional[List[LandingZoneOperationTypeType]] = None


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


# This class is the input for the 'list_baselines' function.
class ListBaselinesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_landing_zones' function.
class ListLandingZonesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'reset_enabled_baseline' function.
class ResetEnabledBaselineInput(BaseValidatorModel):
    enabledBaselineIdentifier: str


# This class is the input for the 'reset_enabled_control' function.
class ResetEnabledControlInput(BaseValidatorModel):
    enabledControlIdentifier: str


# This class is the input for the 'reset_landing_zone' function.
class ResetLandingZoneInput(BaseValidatorModel):
    landingZoneIdentifier: str


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_landing_zone' function.
class UpdateLandingZoneInput(BaseValidatorModel):
    landingZoneIdentifier: str
    manifest: Dict[str, Any]
    version: str


# This class is the input for the 'list_control_operations' function.
class ListControlOperationsInput(BaseValidatorModel):
    filter: Optional[ControlOperationFilter] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'create_landing_zone' function.
class CreateLandingZoneOutput(BaseValidatorModel):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_landing_zone' function.
class DeleteLandingZoneOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_baseline' function.
class DisableBaselineOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_control' function.
class DisableControlOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_baseline' function.
class EnableBaselineOutput(BaseValidatorModel):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_control' function.
class EnableControlOutput(BaseValidatorModel):
    arn: str
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_baseline_operation' function.
class GetBaselineOperationOutput(BaseValidatorModel):
    baselineOperation: BaselineOperation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_baseline' function.
class GetBaselineOutput(BaseValidatorModel):
    arn: str
    description: str
    name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_control_operation' function.
class GetControlOperationOutput(BaseValidatorModel):
    controlOperation: ControlOperation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_baselines' function.
class ListBaselinesOutput(BaseValidatorModel):
    baselines: List[BaselineSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_control_operations' function.
class ListControlOperationsOutput(BaseValidatorModel):
    controlOperations: List[ControlOperationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_enabled_baseline' function.
class ResetEnabledBaselineOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_enabled_control' function.
class ResetEnabledControlOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_landing_zone' function.
class ResetLandingZoneOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_enabled_baseline' function.
class UpdateEnabledBaselineOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_enabled_control' function.
class UpdateEnabledControlOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_landing_zone' function.
class UpdateLandingZoneOutput(BaseValidatorModel):
    operationIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'enable_baseline' function.
class EnableBaselineInput(BaseValidatorModel):
    baselineIdentifier: str
    baselineVersion: str
    targetIdentifier: str
    parameters: Optional[List[EnabledBaselineParameter]] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_enabled_baseline' function.
class UpdateEnabledBaselineInput(BaseValidatorModel):
    baselineVersion: str
    enabledBaselineIdentifier: str
    parameters: Optional[List[EnabledBaselineParameter]] = None


# This class is the input for the 'enable_control' function.
class EnableControlInput(BaseValidatorModel):
    controlIdentifier: str
    targetIdentifier: str
    parameters: Optional[List[EnabledControlParameter]] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_enabled_control' function.
class UpdateEnabledControlInput(BaseValidatorModel):
    enabledControlIdentifier: str
    parameters: List[EnabledControlParameter]


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


# This class is the input for the 'list_enabled_baselines' function.
class ListEnabledBaselinesInput(BaseValidatorModel):
    filter: Optional[EnabledBaselineFilter] = None
    includeChildren: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class EnabledControlDetails(BaseValidatorModel):
    arn: Optional[str] = None
    controlIdentifier: Optional[str] = None
    driftStatusSummary: Optional[DriftStatusSummary] = None
    parameters: Optional[List[EnabledControlParameterSummary]] = None
    statusSummary: Optional[EnablementStatusSummary] = None
    targetIdentifier: Optional[str] = None
    targetRegions: Optional[List[Region]] = None


# This class is the input for the 'list_enabled_controls' function.
class ListEnabledControlsInput(BaseValidatorModel):
    filter: Optional[EnabledControlFilter] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targetIdentifier: Optional[str] = None


# This class is the output for the 'get_landing_zone_operation' function.
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


# This class is the input for the 'list_landing_zone_operations' function.
class ListLandingZoneOperationsInput(BaseValidatorModel):
    filter: Optional[LandingZoneOperationFilter] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_landing_zone_operations' function.
class ListLandingZoneOperationsOutput(BaseValidatorModel):
    landingZoneOperations: List[LandingZoneOperationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_landing_zones' function.
class ListLandingZonesOutput(BaseValidatorModel):
    landingZones: List[LandingZoneSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListBaselinesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListControlOperationsInputPaginate(BaseValidatorModel):
    filter: Optional[ControlOperationFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnabledBaselinesInputPaginate(BaseValidatorModel):
    filter: Optional[EnabledBaselineFilter] = None
    includeChildren: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnabledControlsInputPaginate(BaseValidatorModel):
    filter: Optional[EnabledControlFilter] = None
    targetIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLandingZoneOperationsInputPaginate(BaseValidatorModel):
    filter: Optional[LandingZoneOperationFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLandingZonesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'get_enabled_baseline' function.
class GetEnabledBaselineOutput(BaseValidatorModel):
    enabledBaselineDetails: EnabledBaselineDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_enabled_baselines' function.
class ListEnabledBaselinesOutput(BaseValidatorModel):
    enabledBaselines: List[EnabledBaselineSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_enabled_controls' function.
class ListEnabledControlsOutput(BaseValidatorModel):
    enabledControls: List[EnabledControlSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_enabled_control' function.
class GetEnabledControlOutput(BaseValidatorModel):
    enabledControlDetails: EnabledControlDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_landing_zone' function.
class GetLandingZoneOutput(BaseValidatorModel):
    landingZone: LandingZoneDetail
    ResponseMetadata: ResponseMetadata