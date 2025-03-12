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
from aws_resource_validator.pydantic_models.billing_constants import *

class BillingViewListElementTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    ownerAccountId: Optional[str] = None
    billingViewType: Optional[BillingViewTypeType] = None


class ResourceTagTypeDef(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteBillingViewRequestTypeDef(BaseValidatorModel):
    arn: str


class DimensionValuesOutputTypeDef(BaseValidatorModel):
    key: Literal["LINKED_ACCOUNT"]
    values: List[str]


class DimensionValuesTypeDef(BaseValidatorModel):
    key: Literal["LINKED_ACCOUNT"]
    values: Sequence[str]


class TagValuesOutputTypeDef(BaseValidatorModel):
    key: str
    values: List[str]


class TagValuesTypeDef(BaseValidatorModel):
    key: str
    values: Sequence[str]


class GetBillingViewRequestTypeDef(BaseValidatorModel):
    arn: str


class GetResourcePolicyRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListSourceViewsForBillingViewRequestTypeDef(BaseValidatorModel):
    arn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    resourceTagKeys: Sequence[str]


class TimestampTypeDef(BaseValidatorModel):
    pass


class ActiveTimeRangeTypeDef(BaseValidatorModel):
    activeAfterInclusive: TimestampTypeDef
    activeBeforeInclusive: TimestampTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    resourceTags: Sequence[ResourceTagTypeDef]


class CreateBillingViewResponseTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBillingViewResponseTypeDef(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcePolicyResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListBillingViewsResponseTypeDef(BaseValidatorModel):
    billingViews: List[BillingViewListElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSourceViewsForBillingViewResponseTypeDef(BaseValidatorModel):
    sourceViews: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    resourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBillingViewResponseTypeDef(BaseValidatorModel):
    arn: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ExpressionOutputTypeDef(BaseValidatorModel):
    dimensions: Optional[DimensionValuesOutputTypeDef] = None
    tags: Optional[TagValuesOutputTypeDef] = None


class ExpressionTypeDef(BaseValidatorModel):
    dimensions: Optional[DimensionValuesTypeDef] = None
    tags: Optional[TagValuesTypeDef] = None


class ListSourceViewsForBillingViewRequestPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBillingViewsRequestPaginateTypeDef(BaseValidatorModel):
    activeTimeRange: Optional[ActiveTimeRangeTypeDef] = None
    arns: Optional[Sequence[str]] = None
    billingViewTypes: Optional[Sequence[BillingViewTypeType]] = None
    ownerAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBillingViewsRequestTypeDef(BaseValidatorModel):
    activeTimeRange: Optional[ActiveTimeRangeTypeDef] = None
    arns: Optional[Sequence[str]] = None
    billingViewTypes: Optional[Sequence[BillingViewTypeType]] = None
    ownerAccountId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class BillingViewElementTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    billingViewType: Optional[BillingViewTypeType] = None
    ownerAccountId: Optional[str] = None
    dataFilterExpression: Optional[ExpressionOutputTypeDef] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class GetBillingViewResponseTypeDef(BaseValidatorModel):
    billingView: BillingViewElementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExpressionUnionTypeDef(BaseValidatorModel):
    pass


class CreateBillingViewRequestTypeDef(BaseValidatorModel):
    name: str
    sourceViews: Sequence[str]
    description: Optional[str] = None
    dataFilterExpression: Optional[ExpressionUnionTypeDef] = None
    clientToken: Optional[str] = None
    resourceTags: Optional[Sequence[ResourceTagTypeDef]] = None


class UpdateBillingViewRequestTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    description: Optional[str] = None
    dataFilterExpression: Optional[ExpressionUnionTypeDef] = None


