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

class CancelZonalShiftRequestRequestTypeDef(BaseValidatorModel):
    zonalShiftId: str

class ControlConditionTypeDef(BaseValidatorModel):
    alarmIdentifier: str
    type: Literal["CLOUDWATCH"]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeletePracticeRunConfigurationRequestRequestTypeDef(BaseValidatorModel):
    resourceIdentifier: str

class GetManagedResourceRequestRequestTypeDef(BaseValidatorModel):
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

class ListAutoshiftsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[AutoshiftExecutionStatusType] = None

class ListManagedResourcesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListZonalShiftsRequestRequestTypeDef(BaseValidatorModel):
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

class StartZonalShiftRequestRequestTypeDef(BaseValidatorModel):
    awayFrom: str
    comment: str
    expiresIn: str
    resourceIdentifier: str

class UpdateZonalAutoshiftConfigurationRequestRequestTypeDef(BaseValidatorModel):
    resourceIdentifier: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType

class UpdateZonalShiftRequestRequestTypeDef(BaseValidatorModel):
    zonalShiftId: str
    comment: Optional[str] = None
    expiresIn: Optional[str] = None

class CreatePracticeRunConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class UpdatePracticeRunConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class ListAutoshiftsResponseTypeDef(BaseValidatorModel):
    items: List[AutoshiftSummaryTypeDef]
    nextToken: str
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

class ListAutoshiftsRequestListAutoshiftsPaginateTypeDef(BaseValidatorModel):
    status: Optional[AutoshiftExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListManagedResourcesRequestListManagedResourcesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListZonalShiftsRequestListZonalShiftsPaginateTypeDef(BaseValidatorModel):
    resourceIdentifier: Optional[str] = None
    status: Optional[ZonalShiftStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListZonalShiftsResponseTypeDef(BaseValidatorModel):
    items: List[ZonalShiftSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

