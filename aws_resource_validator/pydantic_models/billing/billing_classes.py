from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.billing.billing_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Timestamp = Union[datetime, str]


class BillingViewListElement(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    ownerAccountId: Optional[str] = None
    billingViewType: Optional[BillingViewTypeType] = None


class ResourceTag(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'delete_billing_view' function.
class DeleteBillingViewRequest(BaseValidatorModel):
    arn: str


class DimensionValuesOutput(BaseValidatorModel):
    key: Literal['LINKED_ACCOUNT']
    values: List[str]


class DimensionValues(BaseValidatorModel):
    key: Literal['LINKED_ACCOUNT']
    values: List[str]


class TagValuesOutput(BaseValidatorModel):
    key: str
    values: List[str]


class TagValues(BaseValidatorModel):
    key: str
    values: List[str]


# This class is the input for the 'get_billing_view' function.
class GetBillingViewRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'get_resource_policy' function.
class GetResourcePolicyRequest(BaseValidatorModel):
    resourceArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_source_views_for_billing_view' function.
class ListSourceViewsForBillingViewRequest(BaseValidatorModel):
    arn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    resourceTagKeys: List[str]


class ActiveTimeRange(BaseValidatorModel):
    activeAfterInclusive: Timestamp
    activeBeforeInclusive: Timestamp


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    resourceTags: List[ResourceTag]


# This class is the output for the 'create_billing_view' function.
class CreateBillingViewResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_billing_view' function.
class DeleteBillingViewResponse(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyResponse(BaseValidatorModel):
    resourceArn: str
    policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_billing_views' function.
class ListBillingViewsResponse(BaseValidatorModel):
    billingViews: List[BillingViewListElement]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_source_views_for_billing_view' function.
class ListSourceViewsForBillingViewResponse(BaseValidatorModel):
    sourceViews: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    resourceTags: List[ResourceTag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_billing_view' function.
class UpdateBillingViewResponse(BaseValidatorModel):
    arn: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class ExpressionOutput(BaseValidatorModel):
    dimensions: Optional[DimensionValuesOutput] = None
    tags: Optional[TagValuesOutput] = None


class Expression(BaseValidatorModel):
    dimensions: Optional[DimensionValues] = None
    tags: Optional[TagValues] = None


class ListSourceViewsForBillingViewRequestPaginate(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBillingViewsRequestPaginate(BaseValidatorModel):
    activeTimeRange: Optional[ActiveTimeRange] = None
    arns: Optional[List[str]] = None
    billingViewTypes: Optional[List[BillingViewTypeType]] = None
    ownerAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_billing_views' function.
class ListBillingViewsRequest(BaseValidatorModel):
    activeTimeRange: Optional[ActiveTimeRange] = None
    arns: Optional[List[str]] = None
    billingViewTypes: Optional[List[BillingViewTypeType]] = None
    ownerAccountId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class BillingViewElement(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    billingViewType: Optional[BillingViewTypeType] = None
    ownerAccountId: Optional[str] = None
    dataFilterExpression: Optional[ExpressionOutput] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

ExpressionUnion = Union[Expression, ExpressionOutput]


# This class is the output for the 'get_billing_view' function.
class GetBillingViewResponse(BaseValidatorModel):
    billingView: BillingViewElement
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_billing_view' function.
class CreateBillingViewRequest(BaseValidatorModel):
    name: str
    sourceViews: List[str]
    description: Optional[str] = None
    dataFilterExpression: Optional[ExpressionUnion] = None
    clientToken: Optional[str] = None
    resourceTags: Optional[List[ResourceTag]] = None


# This class is the input for the 'update_billing_view' function.
class UpdateBillingViewRequest(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    description: Optional[str] = None
    dataFilterExpression: Optional[ExpressionUnion] = None