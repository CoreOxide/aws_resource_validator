from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.marketplace_catalog.marketplace_catalog_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AmiProductEntityIdFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None


class AmiProductTitleFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None
    WildCardValue: Optional[str] = None


class AmiProductVisibilityFilter(BaseValidatorModel):
    ValueList: Optional[List[AmiProductVisibilityStringType]] = None


class AmiProductLastModifiedDateFilterDateRange(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class AmiProductSort(BaseValidatorModel):
    SortBy: Optional[AmiProductSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class AmiProductSummary(BaseValidatorModel):
    ProductTitle: Optional[str] = None
    Visibility: Optional[AmiProductVisibilityStringType] = None


class EntityRequest(BaseValidatorModel):
    Catalog: str
    EntityId: str


class BatchDescribeErrorDetail(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class EntityDetail(BaseValidatorModel):
    EntityType: Optional[str] = None
    EntityArn: Optional[str] = None
    EntityIdentifier: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    DetailsDocument: Optional[Dict[str, Any]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'cancel_change_set' function.
class CancelChangeSetRequest(BaseValidatorModel):
    Catalog: str
    ChangeSetId: str


class ChangeSetSummaryListItem(BaseValidatorModel):
    ChangeSetId: Optional[str] = None
    ChangeSetArn: Optional[str] = None
    ChangeSetName: Optional[str] = None
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None
    Status: Optional[ChangeStatusType] = None
    EntityIdList: Optional[List[str]] = None
    FailureCode: Optional[FailureCodeType] = None


class Entity(BaseValidatorModel):
    Type: str
    Identifier: Optional[str] = None


class ErrorDetail(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ContainerProductEntityIdFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None


class ContainerProductTitleFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None
    WildCardValue: Optional[str] = None


class ContainerProductVisibilityFilter(BaseValidatorModel):
    ValueList: Optional[List[ContainerProductVisibilityStringType]] = None


class ContainerProductLastModifiedDateFilterDateRange(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class ContainerProductSort(BaseValidatorModel):
    SortBy: Optional[ContainerProductSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class ContainerProductSummary(BaseValidatorModel):
    ProductTitle: Optional[str] = None
    Visibility: Optional[ContainerProductVisibilityStringType] = None


class DataProductEntityIdFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None


class DataProductTitleFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None
    WildCardValue: Optional[str] = None


class DataProductVisibilityFilter(BaseValidatorModel):
    ValueList: Optional[List[DataProductVisibilityStringType]] = None


class DataProductLastModifiedDateFilterDateRange(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class DataProductSort(BaseValidatorModel):
    SortBy: Optional[DataProductSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class DataProductSummary(BaseValidatorModel):
    ProductTitle: Optional[str] = None
    Visibility: Optional[DataProductVisibilityStringType] = None


class DeleteResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'describe_change_set' function.
class DescribeChangeSetRequest(BaseValidatorModel):
    Catalog: str
    ChangeSetId: str


# This class is the input for the 'describe_entity' function.
class DescribeEntityRequest(BaseValidatorModel):
    Catalog: str
    EntityId: str


class OfferSummary(BaseValidatorModel):
    Name: Optional[str] = None
    ProductId: Optional[str] = None
    ResaleAuthorizationId: Optional[str] = None
    ReleaseDate: Optional[str] = None
    AvailabilityEndDate: Optional[str] = None
    BuyerAccounts: Optional[List[str]] = None
    State: Optional[OfferStateStringType] = None
    Targeting: Optional[List[OfferTargetingStringType]] = None


class ResaleAuthorizationSummary(BaseValidatorModel):
    Name: Optional[str] = None
    ProductId: Optional[str] = None
    ProductName: Optional[str] = None
    ManufacturerAccountId: Optional[str] = None
    ManufacturerLegalName: Optional[str] = None
    ResellerAccountID: Optional[str] = None
    ResellerLegalName: Optional[str] = None
    Status: Optional[ResaleAuthorizationStatusStringType] = None
    OfferExtendedStatus: Optional[str] = None
    CreatedDate: Optional[str] = None
    AvailabilityEndDate: Optional[str] = None


class SaaSProductSummary(BaseValidatorModel):
    ProductTitle: Optional[str] = None
    Visibility: Optional[SaaSProductVisibilityStringType] = None


class OfferSort(BaseValidatorModel):
    SortBy: Optional[OfferSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class ResaleAuthorizationSort(BaseValidatorModel):
    SortBy: Optional[ResaleAuthorizationSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class SaaSProductSort(BaseValidatorModel):
    SortBy: Optional[SaaSProductSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class Filter(BaseValidatorModel):
    Name: Optional[str] = None
    ValueList: Optional[List[str]] = None


# This class is the input for the 'get_resource_policy' function.
class GetResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class Sort(BaseValidatorModel):
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class OfferAvailabilityEndDateFilterDateRange(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class OfferBuyerAccountsFilter(BaseValidatorModel):
    WildCardValue: Optional[str] = None


class OfferEntityIdFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None


class OfferNameFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None
    WildCardValue: Optional[str] = None


class OfferProductIdFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None


class OfferResaleAuthorizationIdFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None


class OfferStateFilter(BaseValidatorModel):
    ValueList: Optional[List[OfferStateStringType]] = None


class OfferTargetingFilter(BaseValidatorModel):
    ValueList: Optional[List[OfferTargetingStringType]] = None


class OfferLastModifiedDateFilterDateRange(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class OfferReleaseDateFilterDateRange(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class PutResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str
    Policy: str


class ResaleAuthorizationAvailabilityEndDateFilterDateRange(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class ResaleAuthorizationCreatedDateFilterDateRange(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class ResaleAuthorizationEntityIdFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None


class ResaleAuthorizationManufacturerAccountIdFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None
    WildCardValue: Optional[str] = None


class ResaleAuthorizationManufacturerLegalNameFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None
    WildCardValue: Optional[str] = None


class ResaleAuthorizationNameFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None
    WildCardValue: Optional[str] = None


class ResaleAuthorizationOfferExtendedStatusFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None


class ResaleAuthorizationProductIdFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None
    WildCardValue: Optional[str] = None


class ResaleAuthorizationProductNameFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None
    WildCardValue: Optional[str] = None


class ResaleAuthorizationResellerAccountIDFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None
    WildCardValue: Optional[str] = None


class ResaleAuthorizationResellerLegalNameFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None
    WildCardValue: Optional[str] = None


class ResaleAuthorizationStatusFilter(BaseValidatorModel):
    ValueList: Optional[List[ResaleAuthorizationStatusStringType]] = None


class ResaleAuthorizationLastModifiedDateFilterDateRange(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class SaaSProductEntityIdFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None


class SaaSProductTitleFilter(BaseValidatorModel):
    ValueList: Optional[List[str]] = None
    WildCardValue: Optional[str] = None


class SaaSProductVisibilityFilter(BaseValidatorModel):
    ValueList: Optional[List[SaaSProductVisibilityStringType]] = None


class SaaSProductLastModifiedDateFilterDateRange(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class AmiProductLastModifiedDateFilter(BaseValidatorModel):
    DateRange: Optional[AmiProductLastModifiedDateFilterDateRange] = None


# This class is the input for the 'batch_describe_entities' function.
class BatchDescribeEntitiesRequest(BaseValidatorModel):
    EntityRequestList: List[EntityRequest]


# This class is the output for the 'batch_describe_entities' function.
class BatchDescribeEntitiesResponse(BaseValidatorModel):
    EntityDetails: Dict[str, EntityDetail]
    Errors: Dict[str, BatchDescribeErrorDetail]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_change_set' function.
class CancelChangeSetResponse(BaseValidatorModel):
    ChangeSetId: str
    ChangeSetArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_entity' function.
class DescribeEntityResponse(BaseValidatorModel):
    EntityType: str
    EntityIdentifier: str
    EntityArn: str
    LastModifiedDate: str
    Details: str
    DetailsDocument: Dict[str, Any]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyResponse(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_change_set' function.
class StartChangeSetResponse(BaseValidatorModel):
    ChangeSetId: str
    ChangeSetArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_change_sets' function.
class ListChangeSetsResponse(BaseValidatorModel):
    ChangeSetSummaryList: List[ChangeSetSummaryListItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ChangeSummary(BaseValidatorModel):
    ChangeType: Optional[str] = None
    Entity: Optional[Entity] = None
    Details: Optional[str] = None
    DetailsDocument: Optional[Dict[str, Any]] = None
    ErrorDetailList: Optional[List[ErrorDetail]] = None
    ChangeName: Optional[str] = None


class Change(BaseValidatorModel):
    ChangeType: str
    Entity: Entity
    EntityTags: Optional[List[Tag]] = None
    Details: Optional[str] = None
    DetailsDocument: Optional[Dict[str, Any]] = None
    ChangeName: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class ContainerProductLastModifiedDateFilter(BaseValidatorModel):
    DateRange: Optional[ContainerProductLastModifiedDateFilterDateRange] = None


class DataProductLastModifiedDateFilter(BaseValidatorModel):
    DateRange: Optional[DataProductLastModifiedDateFilterDateRange] = None


class EntitySummary(BaseValidatorModel):
    Name: Optional[str] = None
    EntityType: Optional[str] = None
    EntityId: Optional[str] = None
    EntityArn: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Visibility: Optional[str] = None
    AmiProductSummary: Optional[AmiProductSummary] = None
    ContainerProductSummary: Optional[ContainerProductSummary] = None
    DataProductSummary: Optional[DataProductSummary] = None
    SaaSProductSummary: Optional[SaaSProductSummary] = None
    OfferSummary: Optional[OfferSummary] = None
    ResaleAuthorizationSummary: Optional[ResaleAuthorizationSummary] = None


class EntityTypeSort(BaseValidatorModel):
    DataProductSort: Optional[DataProductSort] = None
    SaaSProductSort: Optional[SaaSProductSort] = None
    AmiProductSort: Optional[AmiProductSort] = None
    OfferSort: Optional[OfferSort] = None
    ContainerProductSort: Optional[ContainerProductSort] = None
    ResaleAuthorizationSort: Optional[ResaleAuthorizationSort] = None


class ListChangeSetsRequestPaginate(BaseValidatorModel):
    Catalog: str
    FilterList: Optional[List[Filter]] = None
    Sort: Optional[Sort] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_change_sets' function.
class ListChangeSetsRequest(BaseValidatorModel):
    Catalog: str
    FilterList: Optional[List[Filter]] = None
    Sort: Optional[Sort] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class OfferAvailabilityEndDateFilter(BaseValidatorModel):
    DateRange: Optional[OfferAvailabilityEndDateFilterDateRange] = None


class OfferLastModifiedDateFilter(BaseValidatorModel):
    DateRange: Optional[OfferLastModifiedDateFilterDateRange] = None


class OfferReleaseDateFilter(BaseValidatorModel):
    DateRange: Optional[OfferReleaseDateFilterDateRange] = None


class ResaleAuthorizationAvailabilityEndDateFilter(BaseValidatorModel):
    DateRange: Optional[ResaleAuthorizationAvailabilityEndDateFilterDateRange] = None
    ValueList: Optional[List[str]] = None


class ResaleAuthorizationCreatedDateFilter(BaseValidatorModel):
    DateRange: Optional[ResaleAuthorizationCreatedDateFilterDateRange] = None
    ValueList: Optional[List[str]] = None


class ResaleAuthorizationLastModifiedDateFilter(BaseValidatorModel):
    DateRange: Optional[ResaleAuthorizationLastModifiedDateFilterDateRange] = None


class SaaSProductLastModifiedDateFilter(BaseValidatorModel):
    DateRange: Optional[SaaSProductLastModifiedDateFilterDateRange] = None


class AmiProductFilters(BaseValidatorModel):
    EntityId: Optional[AmiProductEntityIdFilter] = None
    LastModifiedDate: Optional[AmiProductLastModifiedDateFilter] = None
    ProductTitle: Optional[AmiProductTitleFilter] = None
    Visibility: Optional[AmiProductVisibilityFilter] = None


# This class is the output for the 'describe_change_set' function.
class DescribeChangeSetResponse(BaseValidatorModel):
    ChangeSetId: str
    ChangeSetArn: str
    ChangeSetName: str
    Intent: IntentType
    StartTime: str
    EndTime: str
    Status: ChangeStatusType
    FailureCode: FailureCodeType
    FailureDescription: str
    ChangeSet: List[ChangeSummary]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_change_set' function.
class StartChangeSetRequest(BaseValidatorModel):
    Catalog: str
    ChangeSet: List[Change]
    ChangeSetName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    ChangeSetTags: Optional[List[Tag]] = None
    Intent: Optional[IntentType] = None


class ContainerProductFilters(BaseValidatorModel):
    EntityId: Optional[ContainerProductEntityIdFilter] = None
    LastModifiedDate: Optional[ContainerProductLastModifiedDateFilter] = None
    ProductTitle: Optional[ContainerProductTitleFilter] = None
    Visibility: Optional[ContainerProductVisibilityFilter] = None


class DataProductFilters(BaseValidatorModel):
    EntityId: Optional[DataProductEntityIdFilter] = None
    ProductTitle: Optional[DataProductTitleFilter] = None
    Visibility: Optional[DataProductVisibilityFilter] = None
    LastModifiedDate: Optional[DataProductLastModifiedDateFilter] = None


# This class is the output for the 'list_entities' function.
class ListEntitiesResponse(BaseValidatorModel):
    EntitySummaryList: List[EntitySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class OfferFilters(BaseValidatorModel):
    EntityId: Optional[OfferEntityIdFilter] = None
    Name: Optional[OfferNameFilter] = None
    ProductId: Optional[OfferProductIdFilter] = None
    ResaleAuthorizationId: Optional[OfferResaleAuthorizationIdFilter] = None
    ReleaseDate: Optional[OfferReleaseDateFilter] = None
    AvailabilityEndDate: Optional[OfferAvailabilityEndDateFilter] = None
    BuyerAccounts: Optional[OfferBuyerAccountsFilter] = None
    State: Optional[OfferStateFilter] = None
    Targeting: Optional[OfferTargetingFilter] = None
    LastModifiedDate: Optional[OfferLastModifiedDateFilter] = None


class ResaleAuthorizationFilters(BaseValidatorModel):
    EntityId: Optional[ResaleAuthorizationEntityIdFilter] = None
    Name: Optional[ResaleAuthorizationNameFilter] = None
    ProductId: Optional[ResaleAuthorizationProductIdFilter] = None
    CreatedDate: Optional[ResaleAuthorizationCreatedDateFilter] = None
    AvailabilityEndDate: Optional[ResaleAuthorizationAvailabilityEndDateFilter] = None
    ManufacturerAccountId: Optional[ResaleAuthorizationManufacturerAccountIdFilter] = None
    ProductName: Optional[ResaleAuthorizationProductNameFilter] = None
    ManufacturerLegalName: Optional[ResaleAuthorizationManufacturerLegalNameFilter] = None
    ResellerAccountID: Optional[ResaleAuthorizationResellerAccountIDFilter] = None
    ResellerLegalName: Optional[ResaleAuthorizationResellerLegalNameFilter] = None
    Status: Optional[ResaleAuthorizationStatusFilter] = None
    OfferExtendedStatus: Optional[ResaleAuthorizationOfferExtendedStatusFilter] = None
    LastModifiedDate: Optional[ResaleAuthorizationLastModifiedDateFilter] = None


class SaaSProductFilters(BaseValidatorModel):
    EntityId: Optional[SaaSProductEntityIdFilter] = None
    ProductTitle: Optional[SaaSProductTitleFilter] = None
    Visibility: Optional[SaaSProductVisibilityFilter] = None
    LastModifiedDate: Optional[SaaSProductLastModifiedDateFilter] = None


class EntityTypeFilters(BaseValidatorModel):
    DataProductFilters: Optional[DataProductFilters] = None
    SaaSProductFilters: Optional[SaaSProductFilters] = None
    AmiProductFilters: Optional[AmiProductFilters] = None
    OfferFilters: Optional[OfferFilters] = None
    ContainerProductFilters: Optional[ContainerProductFilters] = None
    ResaleAuthorizationFilters: Optional[ResaleAuthorizationFilters] = None


class ListEntitiesRequestPaginate(BaseValidatorModel):
    Catalog: str
    EntityType: str
    FilterList: Optional[List[Filter]] = None
    Sort: Optional[Sort] = None
    OwnershipType: Optional[OwnershipTypeType] = None
    EntityTypeFilters: Optional[EntityTypeFilters] = None
    EntityTypeSort: Optional[EntityTypeSort] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_entities' function.
class ListEntitiesRequest(BaseValidatorModel):
    Catalog: str
    EntityType: str
    FilterList: Optional[List[Filter]] = None
    Sort: Optional[Sort] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    OwnershipType: Optional[OwnershipTypeType] = None
    EntityTypeFilters: Optional[EntityTypeFilters] = None
    EntityTypeSort: Optional[EntityTypeSort] = None