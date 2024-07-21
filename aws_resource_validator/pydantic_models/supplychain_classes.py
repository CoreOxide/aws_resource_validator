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
from aws_resource_validator.pydantic_models.supplychain_constants import *

class BillOfMaterialsImportJobTypeDef(BaseModel):
    instanceId: str
    jobId: str
    status: ConfigurationJobStatusType
    s3uri: str
    message: Optional[str] = None

class CreateBillOfMaterialsImportJobRequestRequestTypeDef(BaseModel):
    instanceId: str
    s3uri: str
    clientToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class GetBillOfMaterialsImportJobRequestRequestTypeDef(BaseModel):
    instanceId: str
    jobId: str

class CreateBillOfMaterialsImportJobResponseTypeDef(BaseModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBillOfMaterialsImportJobResponseTypeDef(BaseModel):
    job: BillOfMaterialsImportJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SendDataIntegrationEventResponseTypeDef(BaseModel):
    eventId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendDataIntegrationEventRequestRequestTypeDef(BaseModel):
    instanceId: str
    eventType: DataIntegrationEventTypeType
    data: str
    eventGroupId: str
    eventTimestamp: Optional[TimestampTypeDef] = None
    clientToken: Optional[str] = None

