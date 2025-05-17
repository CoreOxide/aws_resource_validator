from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.arc_zonal_shift.arc_zonal_shift_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AutoshiftInResource(BaseValidatorModel):
    appliedStatus: AutoshiftAppliedStatusType
    awayFrom: str
    startTime: datetime


class AutoshiftSummary(BaseValidatorModel):
    awayFrom: str
    endTime: datetime
    startTime: datetime
    status: AutoshiftExecutionStatusType


# This class is the input for the 'cancel_zonal_shift' function.
class CancelZonalShiftRequest(BaseValidatorModel):
    zonalShiftId: str


class ControlCondition(BaseValidatorModel):
    alarmIdentifier: str
    type: Literal['CLOUDWATCH']


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'delete_practice_run_configuration' function.
class DeletePracticeRunConfigurationRequest(BaseValidatorModel):
    resourceIdentifier: str


# This class is the input for the 'get_managed_resource' function.
class GetManagedResourceRequest(BaseValidatorModel):
    resourceIdentifier: str


class ZonalShiftInResource(BaseValidatorModel):
    appliedStatus: AppliedStatusType
    awayFrom: str
    comment: str
    expiryTime: datetime
    resourceIdentifier: str
    startTime: datetime
    zonalShiftId: str
    practiceRunOutcome: Optional[PracticeRunOutcomeType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_autoshifts' function.
class ListAutoshiftsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[AutoshiftExecutionStatusType] = None


# This class is the input for the 'list_managed_resources' function.
class ListManagedResourcesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_zonal_shifts' function.
class ListZonalShiftsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceIdentifier: Optional[str] = None
    status: Optional[ZonalShiftStatusType] = None


class ZonalShiftSummary(BaseValidatorModel):
    awayFrom: str
    comment: str
    expiryTime: datetime
    resourceIdentifier: str
    startTime: datetime
    status: ZonalShiftStatusType
    zonalShiftId: str
    practiceRunOutcome: Optional[PracticeRunOutcomeType] = None


# This class is the input for the 'start_zonal_shift' function.
class StartZonalShiftRequest(BaseValidatorModel):
    awayFrom: str
    comment: str
    expiresIn: str
    resourceIdentifier: str


# This class is the input for the 'update_autoshift_observer_notification_status' function.
class UpdateAutoshiftObserverNotificationStatusRequest(BaseValidatorModel):
    status: AutoshiftObserverNotificationStatusType


# This class is the input for the 'update_zonal_autoshift_configuration' function.
class UpdateZonalAutoshiftConfigurationRequest(BaseValidatorModel):
    resourceIdentifier: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType


# This class is the input for the 'update_zonal_shift' function.
class UpdateZonalShiftRequest(BaseValidatorModel):
    zonalShiftId: str
    comment: Optional[str] = None
    expiresIn: Optional[str] = None


# This class is the input for the 'create_practice_run_configuration' function.
class CreatePracticeRunConfigurationRequest(BaseValidatorModel):
    outcomeAlarms: List[ControlCondition]
    resourceIdentifier: str
    blockedDates: Optional[List[str]] = None
    blockedWindows: Optional[List[str]] = None
    blockingAlarms: Optional[List[ControlCondition]] = None


class PracticeRunConfiguration(BaseValidatorModel):
    outcomeAlarms: List[ControlCondition]
    blockedDates: Optional[List[str]] = None
    blockedWindows: Optional[List[str]] = None
    blockingAlarms: Optional[List[ControlCondition]] = None


# This class is the input for the 'update_practice_run_configuration' function.
class UpdatePracticeRunConfigurationRequest(BaseValidatorModel):
    resourceIdentifier: str
    blockedDates: Optional[List[str]] = None
    blockedWindows: Optional[List[str]] = None
    blockingAlarms: Optional[List[ControlCondition]] = None
    outcomeAlarms: Optional[List[ControlCondition]] = None


# This class is the output for the 'delete_practice_run_configuration' function.
class DeletePracticeRunConfigurationResponse(BaseValidatorModel):
    arn: str
    name: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadata


class GetAutoshiftObserverNotificationStatusResponse(BaseValidatorModel):
    status: AutoshiftObserverNotificationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_autoshifts' function.
class ListAutoshiftsResponse(BaseValidatorModel):
    items: List[AutoshiftSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_autoshift_observer_notification_status' function.
class UpdateAutoshiftObserverNotificationStatusResponse(BaseValidatorModel):
    status: AutoshiftObserverNotificationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_zonal_autoshift_configuration' function.
class UpdateZonalAutoshiftConfigurationResponse(BaseValidatorModel):
    resourceIdentifier: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_zonal_shift' function.
class ZonalShift(BaseValidatorModel):
    awayFrom: str
    comment: str
    expiryTime: datetime
    resourceIdentifier: str
    startTime: datetime
    status: ZonalShiftStatusType
    zonalShiftId: str
    ResponseMetadata: ResponseMetadata


class ManagedResourceSummary(BaseValidatorModel):
    availabilityZones: List[str]
    appliedWeights: Optional[Dict[str, float]] = None
    arn: Optional[str] = None
    autoshifts: Optional[List[AutoshiftInResource]] = None
    name: Optional[str] = None
    practiceRunStatus: Optional[ZonalAutoshiftStatusType] = None
    zonalAutoshiftStatus: Optional[ZonalAutoshiftStatusType] = None
    zonalShifts: Optional[List[ZonalShiftInResource]] = None


class ListAutoshiftsRequestPaginate(BaseValidatorModel):
    status: Optional[AutoshiftExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListManagedResourcesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListZonalShiftsRequestPaginate(BaseValidatorModel):
    resourceIdentifier: Optional[str] = None
    status: Optional[ZonalShiftStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_zonal_shifts' function.
class ListZonalShiftsResponse(BaseValidatorModel):
    items: List[ZonalShiftSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_practice_run_configuration' function.
class CreatePracticeRunConfigurationResponse(BaseValidatorModel):
    arn: str
    name: str
    practiceRunConfiguration: PracticeRunConfiguration
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_managed_resource' function.
class GetManagedResourceResponse(BaseValidatorModel):
    appliedWeights: Dict[str, float]
    arn: str
    autoshifts: List[AutoshiftInResource]
    name: str
    practiceRunConfiguration: PracticeRunConfiguration
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    zonalShifts: List[ZonalShiftInResource]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_practice_run_configuration' function.
class UpdatePracticeRunConfigurationResponse(BaseValidatorModel):
    arn: str
    name: str
    practiceRunConfiguration: PracticeRunConfiguration
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_managed_resources' function.
class ListManagedResourcesResponse(BaseValidatorModel):
    items: List[ManagedResourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None