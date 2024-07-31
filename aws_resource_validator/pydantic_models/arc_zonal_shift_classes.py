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
from aws_resource_validator.pydantic_models.arc_zonal_shift_constants import *

class AutoshiftInResourceTypeDef(BaseModel):
    appliedStatus: AutoshiftAppliedStatusType
    awayFrom: str
    startTime: datetime

class AutoshiftSummaryTypeDef(BaseModel):
    awayFrom: str
    endTime: datetime
    startTime: datetime
    status: AutoshiftExecutionStatusType

class CancelZonalShiftRequestRequestTypeDef(BaseModel):
    zonalShiftId: str

class ControlConditionTypeDef(BaseModel):
    alarmIdentifier: str
    type: Literal["CLOUDWATCH"]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeletePracticeRunConfigurationRequestRequestTypeDef(BaseModel):
    resourceIdentifier: str

class GetManagedResourceRequestRequestTypeDef(BaseModel):
    resourceIdentifier: str

class ZonalShiftInResourceTypeDef(BaseModel):
    appliedStatus: AppliedStatusType
    awayFrom: str
    comment: str
    expiryTime: datetime
    resourceIdentifier: str
    startTime: datetime
    zonalShiftId: str
    practiceRunOutcome: Optional[PracticeRunOutcomeType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAutoshiftsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[AutoshiftExecutionStatusType] = None

class ListManagedResourcesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListZonalShiftsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceIdentifier: Optional[str] = None
    status: Optional[ZonalShiftStatusType] = None

class ZonalShiftSummaryTypeDef(BaseModel):
    awayFrom: str
    comment: str
    expiryTime: datetime
    resourceIdentifier: str
    startTime: datetime
    status: ZonalShiftStatusType
    zonalShiftId: str
    practiceRunOutcome: Optional[PracticeRunOutcomeType] = None

class StartZonalShiftRequestRequestTypeDef(BaseModel):
    awayFrom: str
    comment: str
    expiresIn: str
    resourceIdentifier: str

class UpdateZonalAutoshiftConfigurationRequestRequestTypeDef(BaseModel):
    resourceIdentifier: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType

class UpdateZonalShiftRequestRequestTypeDef(BaseModel):
    zonalShiftId: str
    comment: Optional[str] = None
    expiresIn: Optional[str] = None

class CreatePracticeRunConfigurationRequestRequestTypeDef(BaseModel):
    outcomeAlarms: Sequence[ControlConditionTypeDef]
    resourceIdentifier: str
    blockedDates: Optional[Sequence[str]] = None
    blockedWindows: Optional[Sequence[str]] = None
    blockingAlarms: Optional[Sequence[ControlConditionTypeDef]] = None

class PracticeRunConfigurationTypeDef(BaseModel):
    outcomeAlarms: List[ControlConditionTypeDef]
    blockedDates: Optional[List[str]] = None
    blockedWindows: Optional[List[str]] = None
    blockingAlarms: Optional[List[ControlConditionTypeDef]] = None

class UpdatePracticeRunConfigurationRequestRequestTypeDef(BaseModel):
    resourceIdentifier: str
    blockedDates: Optional[Sequence[str]] = None
    blockedWindows: Optional[Sequence[str]] = None
    blockingAlarms: Optional[Sequence[ControlConditionTypeDef]] = None
    outcomeAlarms: Optional[Sequence[ControlConditionTypeDef]] = None

class DeletePracticeRunConfigurationResponseTypeDef(BaseModel):
    arn: str
    name: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListAutoshiftsResponseTypeDef(BaseModel):
    items: List[AutoshiftSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateZonalAutoshiftConfigurationResponseTypeDef(BaseModel):
    resourceIdentifier: str
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ZonalShiftTypeDef(BaseModel):
    awayFrom: str
    comment: str
    expiryTime: datetime
    resourceIdentifier: str
    startTime: datetime
    status: ZonalShiftStatusType
    zonalShiftId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ManagedResourceSummaryTypeDef(BaseModel):
    availabilityZones: List[str]
    appliedWeights: Optional[Dict[str, float]] = None
    arn: Optional[str] = None
    autoshifts: Optional[List[AutoshiftInResourceTypeDef]] = None
    name: Optional[str] = None
    practiceRunStatus: Optional[ZonalAutoshiftStatusType] = None
    zonalAutoshiftStatus: Optional[ZonalAutoshiftStatusType] = None
    zonalShifts: Optional[List[ZonalShiftInResourceTypeDef]] = None

class ListAutoshiftsRequestListAutoshiftsPaginateTypeDef(BaseModel):
    status: Optional[AutoshiftExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListManagedResourcesRequestListManagedResourcesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListZonalShiftsRequestListZonalShiftsPaginateTypeDef(BaseModel):
    resourceIdentifier: Optional[str] = None
    status: Optional[ZonalShiftStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListZonalShiftsResponseTypeDef(BaseModel):
    items: List[ZonalShiftSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePracticeRunConfigurationResponseTypeDef(BaseModel):
    arn: str
    name: str
    practiceRunConfiguration: PracticeRunConfigurationTypeDef
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetManagedResourceResponseTypeDef(BaseModel):
    appliedWeights: Dict[str, float]
    arn: str
    autoshifts: List[AutoshiftInResourceTypeDef]
    name: str
    practiceRunConfiguration: PracticeRunConfigurationTypeDef
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    zonalShifts: List[ZonalShiftInResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePracticeRunConfigurationResponseTypeDef(BaseModel):
    arn: str
    name: str
    practiceRunConfiguration: PracticeRunConfigurationTypeDef
    zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListManagedResourcesResponseTypeDef(BaseModel):
    items: List[ManagedResourceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

