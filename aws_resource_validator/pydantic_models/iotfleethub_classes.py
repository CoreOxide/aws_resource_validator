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
from aws_resource_validator.pydantic_models.iotfleethub_constants import *

class ApplicationSummary(BaseValidatorModel):
    applicationId: str
    applicationName: str
    applicationUrl: str
    applicationDescription: Optional[str] = None
    applicationCreationDate: Optional[int] = None
    applicationLastUpdateDate: Optional[int] = None
    applicationState: Optional[ApplicationStateType] = None


class CreateApplicationRequest(BaseValidatorModel):
    applicationName: str
    roleArn: str
    applicationDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteApplicationRequest(BaseValidatorModel):
    applicationId: str
    clientToken: Optional[str] = None


class DescribeApplicationRequest(BaseValidatorModel):
    applicationId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateApplicationRequest(BaseValidatorModel):
    applicationId: str
    applicationName: Optional[str] = None
    applicationDescription: Optional[str] = None
    clientToken: Optional[str] = None


class CreateApplicationResponse(BaseValidatorModel):
    applicationId: str
    applicationArn: str
    ResponseMetadata: ResponseMetadata


class DescribeApplicationResponse(BaseValidatorModel):
    applicationId: str
    applicationArn: str
    applicationName: str
    applicationDescription: str
    applicationUrl: str
    applicationState: ApplicationStateType
    applicationCreationDate: int
    applicationLastUpdateDate: int
    roleArn: str
    ssoClientId: str
    errorMessage: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListApplicationsResponse(BaseValidatorModel):
    applicationSummaries: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListApplicationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


