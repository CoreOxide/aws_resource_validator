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
from aws_resource_validator.pydantic_models.supplychain_constants import *

class BillOfMaterialsImportJobTypeDef(BaseValidatorModel):
    instanceId: str
    jobId: str
    status: ConfigurationJobStatusType
    s3uri: str
    message: Optional[str] = None

class CreateBillOfMaterialsImportJobRequestRequestTypeDef(BaseValidatorModel):
    instanceId: str
    s3uri: str
    clientToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class GetBillOfMaterialsImportJobRequestRequestTypeDef(BaseValidatorModel):
    instanceId: str
    jobId: str

class CreateBillOfMaterialsImportJobResponseTypeDef(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBillOfMaterialsImportJobResponseTypeDef(BaseValidatorModel):
    job: BillOfMaterialsImportJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SendDataIntegrationEventResponseTypeDef(BaseValidatorModel):
    eventId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendDataIntegrationEventRequestRequestTypeDef(BaseValidatorModel):
    instanceId: str
    eventType: DataIntegrationEventTypeType
    data: str
    eventGroupId: str
    eventTimestamp: Optional[TimestampTypeDef] = None
    clientToken: Optional[str] = None

