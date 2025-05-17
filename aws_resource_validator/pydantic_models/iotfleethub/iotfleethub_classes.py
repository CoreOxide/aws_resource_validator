from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.iotfleethub.iotfleethub_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ApplicationSummary(BaseValidatorModel):
    applicationId: str
    applicationName: str
    applicationUrl: str
    applicationDescription: Optional[str] = None
    applicationCreationDate: Optional[int] = None
    applicationLastUpdateDate: Optional[int] = None
    applicationState: Optional[ApplicationStateType] = None


# This class is the input for the 'create_application' function.
class CreateApplicationRequest(BaseValidatorModel):
    applicationName: str
    roleArn: str
    applicationDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteApplicationRequest(BaseValidatorModel):
    applicationId: str
    clientToken: Optional[str] = None


# This class is the input for the 'describe_application' function.
class DescribeApplicationRequest(BaseValidatorModel):
    applicationId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_applications' function.
class ListApplicationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateApplicationRequest(BaseValidatorModel):
    applicationId: str
    applicationName: Optional[str] = None
    applicationDescription: Optional[str] = None
    clientToken: Optional[str] = None


# This class is the output for the 'create_application' function.
class CreateApplicationResponse(BaseValidatorModel):
    applicationId: str
    applicationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_application' function.
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


# This class is the output for the 'list_applications' function.
class ListApplicationsResponse(BaseValidatorModel):
    applicationSummaries: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListApplicationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None