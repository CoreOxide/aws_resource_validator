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
from aws_resource_validator.pydantic_models.notificationscontacts_constants import *

class ActivateEmailContactRequest(BaseValidatorModel):
    arn: str
    code: str


class CreateEmailContactRequest(BaseValidatorModel):
    name: str
    emailAddress: str
    tags: Optional[Mapping[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteEmailContactRequest(BaseValidatorModel):
    arn: str


class EmailContact(BaseValidatorModel):
    arn: str
    name: str
    address: str
    status: EmailContactStatusType
    creationTime: datetime
    updateTime: datetime


class GetEmailContactRequest(BaseValidatorModel):
    arn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListEmailContactsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    arn: str


class SendActivationCodeRequest(BaseValidatorModel):
    arn: str


class TagResourceRequest(BaseValidatorModel):
    arn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    arn: str
    tagKeys: Sequence[str]


class CreateEmailContactResponse(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetEmailContactResponse(BaseValidatorModel):
    emailContact: EmailContact
    ResponseMetadata: ResponseMetadata


class ListEmailContactsResponse(BaseValidatorModel):
    emailContacts: List[EmailContact]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListEmailContactsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


