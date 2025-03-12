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
from aws_resource_validator.pydantic_models.marketplace_catalog_constants import *

class AmiProductEntityIdFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None


class AmiProductTitleFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None


class AmiProductVisibilityFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[AmiProductVisibilityStringType]] = None


class AmiProductLastModifiedDateFilterDateRangeTypeDef(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class AmiProductSortTypeDef(BaseValidatorModel):
    SortBy: Optional[AmiProductSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class AmiProductSummaryTypeDef(BaseValidatorModel):
    ProductTitle: Optional[str] = None
    Visibility: Optional[AmiProductVisibilityStringType] = None


class EntityRequestTypeDef(BaseValidatorModel):
    Catalog: str
    EntityId: str


class BatchDescribeErrorDetailTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class EntityDetailTypeDef(BaseValidatorModel):
    EntityType: Optional[str] = None
    EntityArn: Optional[str] = None
    EntityIdentifier: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    DetailsDocument: Optional[Dict[str, Any]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelChangeSetRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ChangeSetId: str


class ChangeSetSummaryListItemTypeDef(BaseValidatorModel):
    ChangeSetId: Optional[str] = None
    ChangeSetArn: Optional[str] = None
    ChangeSetName: Optional[str] = None
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None
    Status: Optional[ChangeStatusType] = None
    EntityIdList: Optional[List[str]] = None
    FailureCode: Optional[FailureCodeType] = None


class ErrorDetailTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ContainerProductEntityIdFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None


class ContainerProductTitleFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None


class ContainerProductVisibilityFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[ContainerProductVisibilityStringType]] = None


class ContainerProductLastModifiedDateFilterDateRangeTypeDef(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class ContainerProductSortTypeDef(BaseValidatorModel):
    SortBy: Optional[ContainerProductSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class ContainerProductSummaryTypeDef(BaseValidatorModel):
    ProductTitle: Optional[str] = None
    Visibility: Optional[ContainerProductVisibilityStringType] = None


class DataProductEntityIdFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None


class DataProductTitleFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None


class DataProductVisibilityFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[DataProductVisibilityStringType]] = None


class DataProductLastModifiedDateFilterDateRangeTypeDef(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class DataProductSortTypeDef(BaseValidatorModel):
    SortBy: Optional[DataProductSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class DataProductSummaryTypeDef(BaseValidatorModel):
    ProductTitle: Optional[str] = None
    Visibility: Optional[DataProductVisibilityStringType] = None


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class DescribeChangeSetRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ChangeSetId: str


class DescribeEntityRequestTypeDef(BaseValidatorModel):
    Catalog: str
    EntityId: str


class OfferSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ProductId: Optional[str] = None
    ResaleAuthorizationId: Optional[str] = None
    ReleaseDate: Optional[str] = None
    AvailabilityEndDate: Optional[str] = None
    BuyerAccounts: Optional[List[str]] = None
    State: Optional[OfferStateStringType] = None
    Targeting: Optional[List[OfferTargetingStringType]] = None


class ResaleAuthorizationSummaryTypeDef(BaseValidatorModel):
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


class SaaSProductSummaryTypeDef(BaseValidatorModel):
    ProductTitle: Optional[str] = None
    Visibility: Optional[SaaSProductVisibilityStringType] = None


class OfferSortTypeDef(BaseValidatorModel):
    SortBy: Optional[OfferSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class ResaleAuthorizationSortTypeDef(BaseValidatorModel):
    SortBy: Optional[ResaleAuthorizationSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class SaaSProductSortTypeDef(BaseValidatorModel):
    SortBy: Optional[SaaSProductSortByType] = None
    SortOrder: Optional[SortOrderType] = None


class FilterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ValueList: Optional[Sequence[str]] = None


class GetResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class SortTypeDef(BaseValidatorModel):
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class OfferAvailabilityEndDateFilterDateRangeTypeDef(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class OfferBuyerAccountsFilterTypeDef(BaseValidatorModel):
    WildCardValue: Optional[str] = None


class OfferEntityIdFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None


class OfferNameFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None


class OfferProductIdFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None


class OfferResaleAuthorizationIdFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None


class OfferStateFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[OfferStateStringType]] = None


class OfferTargetingFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[OfferTargetingStringType]] = None


class OfferLastModifiedDateFilterDateRangeTypeDef(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class OfferReleaseDateFilterDateRangeTypeDef(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str


class ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class ResaleAuthorizationCreatedDateFilterDateRangeTypeDef(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class ResaleAuthorizationEntityIdFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None


class ResaleAuthorizationManufacturerAccountIdFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None


class ResaleAuthorizationManufacturerLegalNameFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None


class ResaleAuthorizationNameFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None


class ResaleAuthorizationOfferExtendedStatusFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None


class ResaleAuthorizationProductIdFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None


class ResaleAuthorizationProductNameFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None


class ResaleAuthorizationResellerAccountIDFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None


class ResaleAuthorizationResellerLegalNameFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None


class ResaleAuthorizationStatusFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[ResaleAuthorizationStatusStringType]] = None


class ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class SaaSProductEntityIdFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None


class SaaSProductTitleFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None


class SaaSProductVisibilityFilterTypeDef(BaseValidatorModel):
    ValueList: Optional[Sequence[SaaSProductVisibilityStringType]] = None


class SaaSProductLastModifiedDateFilterDateRangeTypeDef(BaseValidatorModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class AmiProductLastModifiedDateFilterTypeDef(BaseValidatorModel):
    DateRange: Optional[AmiProductLastModifiedDateFilterDateRangeTypeDef] = None


class BatchDescribeEntitiesRequestTypeDef(BaseValidatorModel):
    EntityRequestList: Sequence[EntityRequestTypeDef]


class BatchDescribeEntitiesResponseTypeDef(BaseValidatorModel):
    EntityDetails: Dict[str, EntityDetailTypeDef]
    Errors: Dict[str, BatchDescribeErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CancelChangeSetResponseTypeDef(BaseValidatorModel):
    ChangeSetId: str
    ChangeSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEntityResponseTypeDef(BaseValidatorModel):
    EntityType: str
    EntityIdentifier: str
    EntityArn: str
    LastModifiedDate: str
    Details: str
    DetailsDocument: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcePolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartChangeSetResponseTypeDef(BaseValidatorModel):
    ChangeSetId: str
    ChangeSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListChangeSetsResponseTypeDef(BaseValidatorModel):
    ChangeSetSummaryList: List[ChangeSetSummaryListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class EntityTypeDef(BaseValidatorModel):
    pass


class ChangeSummaryTypeDef(BaseValidatorModel):
    ChangeType: Optional[str] = None
    Entity: Optional[EntityTypeDef] = None
    Details: Optional[str] = None
    DetailsDocument: Optional[Dict[str, Any]] = None
    ErrorDetailList: Optional[List[ErrorDetailTypeDef]] = None
    ChangeName: Optional[str] = None


class ChangeTypeDef(BaseValidatorModel):
    ChangeType: str
    Entity: EntityTypeDef
    EntityTags: Optional[Sequence[TagTypeDef]] = None
    Details: Optional[str] = None
    DetailsDocument: Optional[Mapping[str, Any]] = None
    ChangeName: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class ContainerProductLastModifiedDateFilterTypeDef(BaseValidatorModel):
    DateRange: Optional[ContainerProductLastModifiedDateFilterDateRangeTypeDef] = None


class DataProductLastModifiedDateFilterTypeDef(BaseValidatorModel):
    DateRange: Optional[DataProductLastModifiedDateFilterDateRangeTypeDef] = None


class EntitySummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    EntityType: Optional[str] = None
    EntityId: Optional[str] = None
    EntityArn: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    Visibility: Optional[str] = None
    AmiProductSummary: Optional[AmiProductSummaryTypeDef] = None
    ContainerProductSummary: Optional[ContainerProductSummaryTypeDef] = None
    DataProductSummary: Optional[DataProductSummaryTypeDef] = None
    SaaSProductSummary: Optional[SaaSProductSummaryTypeDef] = None
    OfferSummary: Optional[OfferSummaryTypeDef] = None
    ResaleAuthorizationSummary: Optional[ResaleAuthorizationSummaryTypeDef] = None


class EntityTypeSortTypeDef(BaseValidatorModel):
    DataProductSort: Optional[DataProductSortTypeDef] = None
    SaaSProductSort: Optional[SaaSProductSortTypeDef] = None
    AmiProductSort: Optional[AmiProductSortTypeDef] = None
    OfferSort: Optional[OfferSortTypeDef] = None
    ContainerProductSort: Optional[ContainerProductSortTypeDef] = None
    ResaleAuthorizationSort: Optional[ResaleAuthorizationSortTypeDef] = None


class ListChangeSetsRequestPaginateTypeDef(BaseValidatorModel):
    Catalog: str
    FilterList: Optional[Sequence[FilterTypeDef]] = None
    Sort: Optional[SortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListChangeSetsRequestTypeDef(BaseValidatorModel):
    Catalog: str
    FilterList: Optional[Sequence[FilterTypeDef]] = None
    Sort: Optional[SortTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class OfferAvailabilityEndDateFilterTypeDef(BaseValidatorModel):
    DateRange: Optional[OfferAvailabilityEndDateFilterDateRangeTypeDef] = None


class OfferLastModifiedDateFilterTypeDef(BaseValidatorModel):
    DateRange: Optional[OfferLastModifiedDateFilterDateRangeTypeDef] = None


class OfferReleaseDateFilterTypeDef(BaseValidatorModel):
    DateRange: Optional[OfferReleaseDateFilterDateRangeTypeDef] = None


class ResaleAuthorizationAvailabilityEndDateFilterTypeDef(BaseValidatorModel):
    DateRange: Optional[ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef] = None
    ValueList: Optional[Sequence[str]] = None


class ResaleAuthorizationCreatedDateFilterTypeDef(BaseValidatorModel):
    DateRange: Optional[ResaleAuthorizationCreatedDateFilterDateRangeTypeDef] = None
    ValueList: Optional[Sequence[str]] = None


class ResaleAuthorizationLastModifiedDateFilterTypeDef(BaseValidatorModel):
    DateRange: Optional[ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef] = None


class SaaSProductLastModifiedDateFilterTypeDef(BaseValidatorModel):
    DateRange: Optional[SaaSProductLastModifiedDateFilterDateRangeTypeDef] = None


class AmiProductFiltersTypeDef(BaseValidatorModel):
    EntityId: Optional[AmiProductEntityIdFilterTypeDef] = None
    LastModifiedDate: Optional[AmiProductLastModifiedDateFilterTypeDef] = None
    ProductTitle: Optional[AmiProductTitleFilterTypeDef] = None
    Visibility: Optional[AmiProductVisibilityFilterTypeDef] = None


class DescribeChangeSetResponseTypeDef(BaseValidatorModel):
    ChangeSetId: str
    ChangeSetArn: str
    ChangeSetName: str
    Intent: IntentType
    StartTime: str
    EndTime: str
    Status: ChangeStatusType
    FailureCode: FailureCodeType
    FailureDescription: str
    ChangeSet: List[ChangeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartChangeSetRequestTypeDef(BaseValidatorModel):
    Catalog: str
    ChangeSet: Sequence[ChangeTypeDef]
    ChangeSetName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    ChangeSetTags: Optional[Sequence[TagTypeDef]] = None
    Intent: Optional[IntentType] = None


class ContainerProductFiltersTypeDef(BaseValidatorModel):
    EntityId: Optional[ContainerProductEntityIdFilterTypeDef] = None
    LastModifiedDate: Optional[ContainerProductLastModifiedDateFilterTypeDef] = None
    ProductTitle: Optional[ContainerProductTitleFilterTypeDef] = None
    Visibility: Optional[ContainerProductVisibilityFilterTypeDef] = None


class DataProductFiltersTypeDef(BaseValidatorModel):
    EntityId: Optional[DataProductEntityIdFilterTypeDef] = None
    ProductTitle: Optional[DataProductTitleFilterTypeDef] = None
    Visibility: Optional[DataProductVisibilityFilterTypeDef] = None
    LastModifiedDate: Optional[DataProductLastModifiedDateFilterTypeDef] = None


class ListEntitiesResponseTypeDef(BaseValidatorModel):
    EntitySummaryList: List[EntitySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class OfferFiltersTypeDef(BaseValidatorModel):
    EntityId: Optional[OfferEntityIdFilterTypeDef] = None
    Name: Optional[OfferNameFilterTypeDef] = None
    ProductId: Optional[OfferProductIdFilterTypeDef] = None
    ResaleAuthorizationId: Optional[OfferResaleAuthorizationIdFilterTypeDef] = None
    ReleaseDate: Optional[OfferReleaseDateFilterTypeDef] = None
    AvailabilityEndDate: Optional[OfferAvailabilityEndDateFilterTypeDef] = None
    BuyerAccounts: Optional[OfferBuyerAccountsFilterTypeDef] = None
    State: Optional[OfferStateFilterTypeDef] = None
    Targeting: Optional[OfferTargetingFilterTypeDef] = None
    LastModifiedDate: Optional[OfferLastModifiedDateFilterTypeDef] = None


class ResaleAuthorizationFiltersTypeDef(BaseValidatorModel):
    EntityId: Optional[ResaleAuthorizationEntityIdFilterTypeDef] = None
    Name: Optional[ResaleAuthorizationNameFilterTypeDef] = None
    ProductId: Optional[ResaleAuthorizationProductIdFilterTypeDef] = None
    CreatedDate: Optional[ResaleAuthorizationCreatedDateFilterTypeDef] = None
    AvailabilityEndDate: Optional[ResaleAuthorizationAvailabilityEndDateFilterTypeDef] = None
    ManufacturerAccountId: Optional[ResaleAuthorizationManufacturerAccountIdFilterTypeDef] = None
    ProductName: Optional[ResaleAuthorizationProductNameFilterTypeDef] = None
    ManufacturerLegalName: Optional[ResaleAuthorizationManufacturerLegalNameFilterTypeDef] = None
    ResellerAccountID: Optional[ResaleAuthorizationResellerAccountIDFilterTypeDef] = None
    ResellerLegalName: Optional[ResaleAuthorizationResellerLegalNameFilterTypeDef] = None
    Status: Optional[ResaleAuthorizationStatusFilterTypeDef] = None
    OfferExtendedStatus: Optional[ResaleAuthorizationOfferExtendedStatusFilterTypeDef] = None
    LastModifiedDate: Optional[ResaleAuthorizationLastModifiedDateFilterTypeDef] = None


class SaaSProductFiltersTypeDef(BaseValidatorModel):
    EntityId: Optional[SaaSProductEntityIdFilterTypeDef] = None
    ProductTitle: Optional[SaaSProductTitleFilterTypeDef] = None
    Visibility: Optional[SaaSProductVisibilityFilterTypeDef] = None
    LastModifiedDate: Optional[SaaSProductLastModifiedDateFilterTypeDef] = None


class EntityTypeFiltersTypeDef(BaseValidatorModel):
    DataProductFilters: Optional[DataProductFiltersTypeDef] = None
    SaaSProductFilters: Optional[SaaSProductFiltersTypeDef] = None
    AmiProductFilters: Optional[AmiProductFiltersTypeDef] = None
    OfferFilters: Optional[OfferFiltersTypeDef] = None
    ContainerProductFilters: Optional[ContainerProductFiltersTypeDef] = None
    ResaleAuthorizationFilters: Optional[ResaleAuthorizationFiltersTypeDef] = None


class ListEntitiesRequestPaginateTypeDef(BaseValidatorModel):
    Catalog: str
    EntityType: str
    FilterList: Optional[Sequence[FilterTypeDef]] = None
    Sort: Optional[SortTypeDef] = None
    OwnershipType: Optional[OwnershipTypeType] = None
    EntityTypeFilters: Optional[EntityTypeFiltersTypeDef] = None
    EntityTypeSort: Optional[EntityTypeSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEntitiesRequestTypeDef(BaseValidatorModel):
    Catalog: str
    EntityType: str
    FilterList: Optional[Sequence[FilterTypeDef]] = None
    Sort: Optional[SortTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    OwnershipType: Optional[OwnershipTypeType] = None
    EntityTypeFilters: Optional[EntityTypeFiltersTypeDef] = None
    EntityTypeSort: Optional[EntityTypeSortTypeDef] = None


