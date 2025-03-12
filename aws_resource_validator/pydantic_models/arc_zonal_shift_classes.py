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
from aws_resource_validator.pydantic_models.arc_zonal_shift_constants import *

class AutoshiftInResourceTypeDef(BaseValidatorModel):
    appliedStatus: AutoshiftAppliedStatusType
    awayFrom: str
    startTime: datetime


class AutoshiftSummaryTypeDef(BaseValidatorModel):
    awayFrom: str
    endTime: datetime
    startTime: datetime
    status: AutoshiftExecutionStatusType


class CancelZonalShiftRequestTypeDef(BaseValidatorModel):
    zonalShiftId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeletePracticeRunConfigurationRequestTypeDef(BaseValidatorModel):
    resourceIdentifier: str


class GetManagedResourceRequestTypeDef(BaseValidatorModel):
    resourceIdentifier: str


class ZonalShiftInResourceTypeDef(BaseValidatorModel):
    appliedStatus: AppliedStatusType
    awayFrom: str
    comment: str
    expiryTime: datetime
    resourceIdentifier: str
    startTime: datetime
    zonalShiftId: str
    practiceRunOutcome: Optional[PracticeRunOutcomeType] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAutoshiftsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[AutoshiftExecutionStatusType] = None


class ListManagedResourcesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListZonalShiftsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceIdentifier: Optional[str] = None
    status: Optional[ZonalShiftStatusType] = None


class ZonalShiftSummaryTypeDef(BaseValidatorModel):
    awayFrom: str
    comment: str
    expiryTime: datetime
    resourceIdentifier: str
    startTime: datetime
    status: ZonalShiftStatusType
    zonalShiftId: str
    practiceRunOutcome: Optional[PracticeRunOutcomeType] = None


class StartZonalShiftRequestTypeDef(BaseValidatorModel):
    awayFrom: str
    comment: str
    expiresIn: str
    resourceIdentifier: str


class UpdateAutoshiftObserverNotificationStatusRequestTypeDef(BaseValidatorModel):
    status: AutoshiftObserverNotificationStatusType


class UpdateZonalAutoshiftConfigurationRequestTypeDef(BaseValidatorModel):
    resourceIdentifier: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType


class UpdateZonalShiftRequestTypeDef(BaseValidatorModel):
    zonalShiftId: str
    comment: Optional[str] = None
    expiresIn: Optional[str] = None


class ControlConditionTypeDef(BaseValidatorModel):
    pass


class CreatePracticeRunConfigurationRequestTypeDef(BaseValidatorModel):
    outcomeAlarms: Sequence[ControlConditionTypeDef]
    resourceIdentifier: str
    blockedDates: Optional[Sequence[str]] = None
    blockedWindows: Optional[Sequence[str]] = None
    blockingAlarms: Optional[Sequence[ControlConditionTypeDef]] = None


class PracticeRunConfigurationTypeDef(BaseValidatorModel):
    outcomeAlarms: List[ControlConditionTypeDef]
    blockedDates: Optional[List[str]] = None
    blockedWindows: Optional[List[str]] = None
    blockingAlarms: Optional[List[ControlConditionTypeDef]] = None


class UpdatePracticeRunConfigurationRequestTypeDef(BaseValidatorModel):
    resourceIdentifier: str
    blockedDates: Optional[Sequence[str]] = None
    blockedWindows: Optional[Sequence[str]] = None
    blockingAlarms: Optional[Sequence[ControlConditionTypeDef]] = None
    outcomeAlarms: Optional[Sequence[ControlConditionTypeDef]] = None


class DeletePracticeRunConfigurationResponseTypeDef(BaseValidatorModel):
    arn: str
    name: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetAutoshiftObserverNotificationStatusResponseTypeDef(BaseValidatorModel):
    status: AutoshiftObserverNotificationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListAutoshiftsResponseTypeDef(BaseValidatorModel):
    items: List[AutoshiftSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateAutoshiftObserverNotificationStatusResponseTypeDef(BaseValidatorModel):
    status: AutoshiftObserverNotificationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateZonalAutoshiftConfigurationResponseTypeDef(BaseValidatorModel):
    resourceIdentifier: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ZonalShiftTypeDef(BaseValidatorModel):
    awayFrom: str
    comment: str
    expiryTime: datetime
    resourceIdentifier: str
    startTime: datetime
    status: ZonalShiftStatusType
    zonalShiftId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ManagedResourceSummaryTypeDef(BaseValidatorModel):
    availabilityZones: List[str]
    appliedWeights: Optional[Dict[str, float]] = None
    arn: Optional[str] = None
    autoshifts: Optional[List[AutoshiftInResourceTypeDef]] = None
    name: Optional[str] = None
    practiceRunStatus: Optional[ZonalAutoshiftStatusType] = None
    zonalAutoshiftStatus: Optional[ZonalAutoshiftStatusType] = None
    zonalShifts: Optional[List[ZonalShiftInResourceTypeDef]] = None


class ListAutoshiftsRequestPaginateTypeDef(BaseValidatorModel):
    status: Optional[AutoshiftExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedResourcesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListZonalShiftsRequestPaginateTypeDef(BaseValidatorModel):
    resourceIdentifier: Optional[str] = None
    status: Optional[ZonalShiftStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListZonalShiftsResponseTypeDef(BaseValidatorModel):
    items: List[ZonalShiftSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreatePracticeRunConfigurationResponseTypeDef(BaseValidatorModel):
    arn: str
    name: str
    practiceRunConfiguration: PracticeRunConfigurationTypeDef
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetManagedResourceResponseTypeDef(BaseValidatorModel):
    appliedWeights: Dict[str, float]
    arn: str
    autoshifts: List[AutoshiftInResourceTypeDef]
    name: str
    practiceRunConfiguration: PracticeRunConfigurationTypeDef
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    zonalShifts: List[ZonalShiftInResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePracticeRunConfigurationResponseTypeDef(BaseValidatorModel):
    arn: str
    name: str
    practiceRunConfiguration: PracticeRunConfigurationTypeDef
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListManagedResourcesResponseTypeDef(BaseValidatorModel):
    items: List[ManagedResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


