from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.marketplace_reporting.marketplace_reporting_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'get_buyer_dashboard' function.
class GetBuyerDashboardInput(BaseValidatorModel):
    dashboardIdentifier: str
    embeddingDomains: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the output for the 'get_buyer_dashboard' function.
class GetBuyerDashboardOutput(BaseValidatorModel):
    embedUrl: str
    dashboardIdentifier: str
    embeddingDomains: List[str]
    ResponseMetadata: ResponseMetadata