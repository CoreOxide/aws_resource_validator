from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.notificationscontacts.notificationscontacts_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ActivateEmailContactRequest(BaseValidatorModel):
    arn: str
    code: str


# This class is the input for the 'create_email_contact' function.
class CreateEmailContactRequest(BaseValidatorModel):
    name: str
    emailAddress: str
    tags: Optional[Dict[str, str]] = None


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


# This class is the input for the 'get_email_contact' function.
class GetEmailContactRequest(BaseValidatorModel):
    arn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_email_contacts' function.
class ListEmailContactsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    arn: str


class SendActivationCodeRequest(BaseValidatorModel):
    arn: str


class TagResourceRequest(BaseValidatorModel):
    arn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    arn: str
    tagKeys: List[str]


# This class is the output for the 'create_email_contact' function.
class CreateEmailContactResponse(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_email_contact' function.
class GetEmailContactResponse(BaseValidatorModel):
    emailContact: EmailContact
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_email_contacts' function.
class ListEmailContactsResponse(BaseValidatorModel):
    emailContacts: List[EmailContact]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListEmailContactsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None