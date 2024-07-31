from datetime import datetime
from pydantic import BaseModel
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

class AmiProductEntityIdFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None

class AmiProductTitleFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None

class AmiProductVisibilityFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[AmiProductVisibilityStringType]] = None

class AmiProductLastModifiedDateFilterDateRangeTypeDef(BaseModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None

class AmiProductSortTypeDef(BaseModel):
    SortBy: Optional[AmiProductSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class AmiProductSummaryTypeDef(BaseModel):
    ProductTitle: Optional[str] = None
    Visibility: Optional[AmiProductVisibilityStringType] = None

class EntityRequestTypeDef(BaseModel):
    Catalog: str
    EntityId: str

class BatchDescribeErrorDetailTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class EntityDetailTypeDef(BaseModel):
    EntityType: Optional[str] = None
    EntityArn: Optional[str] = None
    EntityIdentifier: Optional[str] = None
    LastModifiedDate: Optional[str] = None
    DetailsDocument: Optional[Dict[str, Any]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CancelChangeSetRequestRequestTypeDef(BaseModel):
    Catalog: str
    ChangeSetId: str

class ChangeSetSummaryListItemTypeDef(BaseModel):
    ChangeSetId: Optional[str] = None
    ChangeSetArn: Optional[str] = None
    ChangeSetName: Optional[str] = None
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None
    Status: Optional[ChangeStatusType] = None
    EntityIdList: Optional[List[str]] = None
    FailureCode: Optional[FailureCodeType] = None

class EntityTypeDef(BaseModel):
    Type: str
    Identifier: Optional[str] = None

class ErrorDetailTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ContainerProductEntityIdFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None

class ContainerProductTitleFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None

class ContainerProductVisibilityFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[ContainerProductVisibilityStringType]] = None

class ContainerProductLastModifiedDateFilterDateRangeTypeDef(BaseModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None

class ContainerProductSortTypeDef(BaseModel):
    SortBy: Optional[ContainerProductSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ContainerProductSummaryTypeDef(BaseModel):
    ProductTitle: Optional[str] = None
    Visibility: Optional[ContainerProductVisibilityStringType] = None

class DataProductEntityIdFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None

class DataProductTitleFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None

class DataProductVisibilityFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[DataProductVisibilityStringType]] = None

class DataProductLastModifiedDateFilterDateRangeTypeDef(BaseModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None

class DataProductSortTypeDef(BaseModel):
    SortBy: Optional[DataProductSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class DataProductSummaryTypeDef(BaseModel):
    ProductTitle: Optional[str] = None
    Visibility: Optional[DataProductVisibilityStringType] = None

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DescribeChangeSetRequestRequestTypeDef(BaseModel):
    Catalog: str
    ChangeSetId: str

class DescribeEntityRequestRequestTypeDef(BaseModel):
    Catalog: str
    EntityId: str

class OfferSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    ProductId: Optional[str] = None
    ResaleAuthorizationId: Optional[str] = None
    ReleaseDate: Optional[str] = None
    AvailabilityEndDate: Optional[str] = None
    BuyerAccounts: Optional[List[str]] = None
    State: Optional[OfferStateStringType] = None
    Targeting: Optional[List[OfferTargetingStringType]] = None

class ResaleAuthorizationSummaryTypeDef(BaseModel):
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

class SaaSProductSummaryTypeDef(BaseModel):
    ProductTitle: Optional[str] = None
    Visibility: Optional[SaaSProductVisibilityStringType] = None

class OfferSortTypeDef(BaseModel):
    SortBy: Optional[OfferSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class ResaleAuthorizationSortTypeDef(BaseModel):
    SortBy: Optional[ResaleAuthorizationSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class SaaSProductSortTypeDef(BaseModel):
    SortBy: Optional[SaaSProductSortByType] = None
    SortOrder: Optional[SortOrderType] = None

class FilterTypeDef(BaseModel):
    Name: Optional[str] = None
    ValueList: Optional[Sequence[str]] = None

class GetResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class SortTypeDef(BaseModel):
    SortBy: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class OfferAvailabilityEndDateFilterDateRangeTypeDef(BaseModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None

class OfferBuyerAccountsFilterTypeDef(BaseModel):
    WildCardValue: Optional[str] = None

class OfferEntityIdFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None

class OfferNameFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None

class OfferProductIdFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None

class OfferResaleAuthorizationIdFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None

class OfferStateFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[OfferStateStringType]] = None

class OfferTargetingFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[OfferTargetingStringType]] = None

class OfferLastModifiedDateFilterDateRangeTypeDef(BaseModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None

class OfferReleaseDateFilterDateRangeTypeDef(BaseModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Policy: str

class ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef(BaseModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None

class ResaleAuthorizationCreatedDateFilterDateRangeTypeDef(BaseModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None

class ResaleAuthorizationEntityIdFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None

class ResaleAuthorizationManufacturerAccountIdFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None

class ResaleAuthorizationManufacturerLegalNameFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None

class ResaleAuthorizationNameFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None

class ResaleAuthorizationOfferExtendedStatusFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None

class ResaleAuthorizationProductIdFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None

class ResaleAuthorizationProductNameFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None

class ResaleAuthorizationResellerAccountIDFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None

class ResaleAuthorizationResellerLegalNameFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None

class ResaleAuthorizationStatusFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[ResaleAuthorizationStatusStringType]] = None

class ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef(BaseModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None

class SaaSProductEntityIdFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None

class SaaSProductTitleFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[str]] = None
    WildCardValue: Optional[str] = None

class SaaSProductVisibilityFilterTypeDef(BaseModel):
    ValueList: Optional[Sequence[SaaSProductVisibilityStringType]] = None

class SaaSProductLastModifiedDateFilterDateRangeTypeDef(BaseModel):
    AfterValue: Optional[str] = None
    BeforeValue: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class AmiProductLastModifiedDateFilterTypeDef(BaseModel):
    DateRange: Optional[AmiProductLastModifiedDateFilterDateRangeTypeDef] = None

class BatchDescribeEntitiesRequestRequestTypeDef(BaseModel):
    EntityRequestList: Sequence[EntityRequestTypeDef]

class BatchDescribeEntitiesResponseTypeDef(BaseModel):
    EntityDetails: Dict[str, EntityDetailTypeDef]
    Errors: Dict[str, BatchDescribeErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelChangeSetResponseTypeDef(BaseModel):
    ChangeSetId: str
    ChangeSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEntityResponseTypeDef(BaseModel):
    EntityType: str
    EntityIdentifier: str
    EntityArn: str
    LastModifiedDate: str
    Details: str
    DetailsDocument: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartChangeSetResponseTypeDef(BaseModel):
    ChangeSetId: str
    ChangeSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChangeSetsResponseTypeDef(BaseModel):
    ChangeSetSummaryList: List[ChangeSetSummaryListItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeSummaryTypeDef(BaseModel):
    ChangeType: Optional[str] = None
    Entity: Optional[EntityTypeDef] = None
    Details: Optional[str] = None
    DetailsDocument: Optional[Dict[str, Any]] = None
    ErrorDetailList: Optional[List[ErrorDetailTypeDef]] = None
    ChangeName: Optional[str] = None

class ChangeTypeDef(BaseModel):
    ChangeType: str
    Entity: EntityTypeDef
    EntityTags: Optional[Sequence[TagTypeDef]] = None
    Details: Optional[str] = None
    DetailsDocument: Optional[Mapping[str, Any]] = None
    ChangeName: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class ContainerProductLastModifiedDateFilterTypeDef(BaseModel):
    DateRange: Optional[ContainerProductLastModifiedDateFilterDateRangeTypeDef] = None

class DataProductLastModifiedDateFilterTypeDef(BaseModel):
    DateRange: Optional[DataProductLastModifiedDateFilterDateRangeTypeDef] = None

class EntitySummaryTypeDef(BaseModel):
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

class EntityTypeSortTypeDef(BaseModel):
    DataProductSort: Optional[DataProductSortTypeDef] = None
    SaaSProductSort: Optional[SaaSProductSortTypeDef] = None
    AmiProductSort: Optional[AmiProductSortTypeDef] = None
    OfferSort: Optional[OfferSortTypeDef] = None
    ContainerProductSort: Optional[ContainerProductSortTypeDef] = None
    ResaleAuthorizationSort: Optional[ResaleAuthorizationSortTypeDef] = None

class ListChangeSetsRequestListChangeSetsPaginateTypeDef(BaseModel):
    Catalog: str
    FilterList: Optional[Sequence[FilterTypeDef]] = None
    Sort: Optional[SortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListChangeSetsRequestRequestTypeDef(BaseModel):
    Catalog: str
    FilterList: Optional[Sequence[FilterTypeDef]] = None
    Sort: Optional[SortTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class OfferAvailabilityEndDateFilterTypeDef(BaseModel):
    DateRange: Optional[OfferAvailabilityEndDateFilterDateRangeTypeDef] = None

class OfferLastModifiedDateFilterTypeDef(BaseModel):
    DateRange: Optional[OfferLastModifiedDateFilterDateRangeTypeDef] = None

class OfferReleaseDateFilterTypeDef(BaseModel):
    DateRange: Optional[OfferReleaseDateFilterDateRangeTypeDef] = None

class ResaleAuthorizationAvailabilityEndDateFilterTypeDef(BaseModel):
    DateRange: Optional[ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef] = None
    ValueList: Optional[Sequence[str]] = None

class ResaleAuthorizationCreatedDateFilterTypeDef(BaseModel):
    DateRange: Optional[ResaleAuthorizationCreatedDateFilterDateRangeTypeDef] = None
    ValueList: Optional[Sequence[str]] = None

class ResaleAuthorizationLastModifiedDateFilterTypeDef(BaseModel):
    DateRange: Optional[ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef] = None

class SaaSProductLastModifiedDateFilterTypeDef(BaseModel):
    DateRange: Optional[SaaSProductLastModifiedDateFilterDateRangeTypeDef] = None

class AmiProductFiltersTypeDef(BaseModel):
    EntityId: Optional[AmiProductEntityIdFilterTypeDef] = None
    LastModifiedDate: Optional[AmiProductLastModifiedDateFilterTypeDef] = None
    ProductTitle: Optional[AmiProductTitleFilterTypeDef] = None
    Visibility: Optional[AmiProductVisibilityFilterTypeDef] = None

class DescribeChangeSetResponseTypeDef(BaseModel):
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

class StartChangeSetRequestRequestTypeDef(BaseModel):
    Catalog: str
    ChangeSet: Sequence[ChangeTypeDef]
    ChangeSetName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    ChangeSetTags: Optional[Sequence[TagTypeDef]] = None
    Intent: Optional[IntentType] = None

class ContainerProductFiltersTypeDef(BaseModel):
    EntityId: Optional[ContainerProductEntityIdFilterTypeDef] = None
    LastModifiedDate: Optional[ContainerProductLastModifiedDateFilterTypeDef] = None
    ProductTitle: Optional[ContainerProductTitleFilterTypeDef] = None
    Visibility: Optional[ContainerProductVisibilityFilterTypeDef] = None

class DataProductFiltersTypeDef(BaseModel):
    EntityId: Optional[DataProductEntityIdFilterTypeDef] = None
    ProductTitle: Optional[DataProductTitleFilterTypeDef] = None
    Visibility: Optional[DataProductVisibilityFilterTypeDef] = None
    LastModifiedDate: Optional[DataProductLastModifiedDateFilterTypeDef] = None

class ListEntitiesResponseTypeDef(BaseModel):
    EntitySummaryList: List[EntitySummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OfferFiltersTypeDef(BaseModel):
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

class ResaleAuthorizationFiltersTypeDef(BaseModel):
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

class SaaSProductFiltersTypeDef(BaseModel):
    EntityId: Optional[SaaSProductEntityIdFilterTypeDef] = None
    ProductTitle: Optional[SaaSProductTitleFilterTypeDef] = None
    Visibility: Optional[SaaSProductVisibilityFilterTypeDef] = None
    LastModifiedDate: Optional[SaaSProductLastModifiedDateFilterTypeDef] = None

class EntityTypeFiltersTypeDef(BaseModel):
    DataProductFilters: Optional[DataProductFiltersTypeDef] = None
    SaaSProductFilters: Optional[SaaSProductFiltersTypeDef] = None
    AmiProductFilters: Optional[AmiProductFiltersTypeDef] = None
    OfferFilters: Optional[OfferFiltersTypeDef] = None
    ContainerProductFilters: Optional[ContainerProductFiltersTypeDef] = None
    ResaleAuthorizationFilters: Optional[ResaleAuthorizationFiltersTypeDef] = None

class ListEntitiesRequestListEntitiesPaginateTypeDef(BaseModel):
    Catalog: str
    EntityType: str
    FilterList: Optional[Sequence[FilterTypeDef]] = None
    Sort: Optional[SortTypeDef] = None
    OwnershipType: Optional[OwnershipTypeType] = None
    EntityTypeFilters: Optional[EntityTypeFiltersTypeDef] = None
    EntityTypeSort: Optional[EntityTypeSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEntitiesRequestRequestTypeDef(BaseModel):
    Catalog: str
    EntityType: str
    FilterList: Optional[Sequence[FilterTypeDef]] = None
    Sort: Optional[SortTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    OwnershipType: Optional[OwnershipTypeType] = None
    EntityTypeFilters: Optional[EntityTypeFiltersTypeDef] = None
    EntityTypeSort: Optional[EntityTypeSortTypeDef] = None

