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
from aws_resource_validator.pydantic_models.meteringmarketplace_constants import *

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class RegisterUsageRequestRequestTypeDef(BaseModel):
    ProductCode: str
    PublicKeyVersion: int
    Nonce: Optional[str] = None

class ResolveCustomerRequestRequestTypeDef(BaseModel):
    RegistrationToken: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class MeterUsageResultTypeDef(BaseModel):
    MeteringRecordId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterUsageResultTypeDef(BaseModel):
    PublicKeyRotationTimestamp: datetime
    Signature: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResolveCustomerResultTypeDef(BaseModel):
    CustomerIdentifier: str
    ProductCode: str
    CustomerAWSAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UsageAllocationTypeDef(BaseModel):
    AllocatedUsageQuantity: int
    Tags: Optional[Sequence[TagTypeDef]] = None

class MeterUsageRequestRequestTypeDef(BaseModel):
    ProductCode: str
    Timestamp: TimestampTypeDef
    UsageDimension: str
    UsageQuantity: Optional[int] = None
    DryRun: Optional[bool] = None
    UsageAllocations: Optional[Sequence[UsageAllocationTypeDef]] = None

class UsageRecordTypeDef(BaseModel):
    Timestamp: TimestampTypeDef
    CustomerIdentifier: str
    Dimension: str
    Quantity: Optional[int] = None
    UsageAllocations: Optional[Sequence[UsageAllocationTypeDef]] = None

class BatchMeterUsageRequestRequestTypeDef(BaseModel):
    UsageRecords: Sequence[UsageRecordTypeDef]
    ProductCode: str

class UsageRecordResultTypeDef(BaseModel):
    UsageRecord: Optional[UsageRecordTypeDef] = None
    MeteringRecordId: Optional[str] = None
    Status: Optional[UsageRecordResultStatusType] = None

class BatchMeterUsageResultTypeDef(BaseModel):
    Results: List[UsageRecordResultTypeDef]
    UnprocessedRecords: List[UsageRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

