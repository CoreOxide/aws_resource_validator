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


class DeletePracticeRunConfigurationRequest(BaseValidatorModel):
    resourceIdentifier: str


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


class ListAutoshiftsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[AutoshiftExecutionStatusType] = None


class ListManagedResourcesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


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


class StartZonalShiftRequest(BaseValidatorModel):
    awayFrom: str
    comment: str
    expiresIn: str
    resourceIdentifier: str


class UpdateAutoshiftObserverNotificationStatusRequest(BaseValidatorModel):
    status: AutoshiftObserverNotificationStatusType


class UpdateZonalAutoshiftConfigurationRequest(BaseValidatorModel):
    resourceIdentifier: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType


class UpdateZonalShiftRequest(BaseValidatorModel):
    zonalShiftId: str
    comment: Optional[str] = None
    expiresIn: Optional[str] = None


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


class UpdatePracticeRunConfigurationRequest(BaseValidatorModel):
    resourceIdentifier: str
    blockedDates: Optional[List[str]] = None
    blockedWindows: Optional[List[str]] = None
    blockingAlarms: Optional[List[ControlCondition]] = None
    outcomeAlarms: Optional[List[ControlCondition]] = None


class DeletePracticeRunConfigurationResponse(BaseValidatorModel):
    arn: str
    name: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadata


class GetAutoshiftObserverNotificationStatusResponse(BaseValidatorModel):
    status: AutoshiftObserverNotificationStatusType
    ResponseMetadata: ResponseMetadata


class ListAutoshiftsResponse(BaseValidatorModel):
    items: List[AutoshiftSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateAutoshiftObserverNotificationStatusResponse(BaseValidatorModel):
    status: AutoshiftObserverNotificationStatusType
    ResponseMetadata: ResponseMetadata


class UpdateZonalAutoshiftConfigurationResponse(BaseValidatorModel):
    resourceIdentifier: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadata


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


class ListZonalShiftsResponse(BaseValidatorModel):
    items: List[ZonalShiftSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreatePracticeRunConfigurationResponse(BaseValidatorModel):
    arn: str
    name: str
    practiceRunConfiguration: PracticeRunConfiguration
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadata


class GetManagedResourceResponse(BaseValidatorModel):
    appliedWeights: Dict[str, float]
    arn: str
    autoshifts: List[AutoshiftInResource]
    name: str
    practiceRunConfiguration: PracticeRunConfiguration
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    zonalShifts: List[ZonalShiftInResource]
    ResponseMetadata: ResponseMetadata


class UpdatePracticeRunConfigurationResponse(BaseValidatorModel):
    arn: str
    name: str
    practiceRunConfiguration: PracticeRunConfiguration
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadata


class ListManagedResourcesResponse(BaseValidatorModel):
    items: List[ManagedResourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None