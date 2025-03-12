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
from aws_resource_validator.pydantic_models.marketplace_reporting_constants import *

class GetBuyerDashboardInputTypeDef(BaseValidatorModel):
    dashboardIdentifier: str
    embeddingDomains: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetBuyerDashboardOutputTypeDef(BaseValidatorModel):
    embedUrl: str
    dashboardIdentifier: str
    embeddingDomains: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


