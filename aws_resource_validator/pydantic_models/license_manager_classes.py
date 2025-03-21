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
from aws_resource_validator.pydantic_models.license_manager_constants import *

class AcceptGrantRequestTypeDef(BaseValidatorModel):
    GrantArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AutomatedDiscoveryInformationTypeDef(BaseValidatorModel):
    LastRunTime: Optional[datetime] = None


class BorrowConfigurationTypeDef(BaseValidatorModel):
    AllowEarlyCheckIn: bool
    MaxTimeToLiveInMinutes: int


class CheckInLicenseRequestTypeDef(BaseValidatorModel):
    LicenseConsumptionToken: str
    Beneficiary: Optional[str] = None


class EntitlementDataTypeDef(BaseValidatorModel):
    Name: str
    Unit: EntitlementDataUnitType
    Value: Optional[str] = None


class MetadataTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class ConsumedLicenseSummaryTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    ConsumedLicenses: Optional[int] = None


class ProvisionalConfigurationTypeDef(BaseValidatorModel):
    MaxTimeToLiveInMinutes: int


class CreateGrantRequestTypeDef(BaseValidatorModel):
    ClientToken: str
    GrantName: str
    LicenseArn: str
    Principals: Sequence[str]
    HomeRegion: str
    AllowedOperations: Sequence[AllowedOperationType]


class OptionsTypeDef(BaseValidatorModel):
    ActivationOverrideBehavior: Optional[ActivationOverrideBehaviorType] = None


class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class LicenseConversionContextTypeDef(BaseValidatorModel):
    UsageOperation: Optional[str] = None


class ReportFrequencyTypeDef(BaseValidatorModel):
    value: Optional[int] = None
    period: Optional[ReportFrequencyTypeType] = None


class DatetimeRangeTypeDef(BaseValidatorModel):
    Begin: str
    End: Optional[str] = None


class EntitlementTypeDef(BaseValidatorModel):
    Name: str
    Unit: EntitlementUnitType
    Value: Optional[str] = None
    MaxCount: Optional[int] = None
    Overage: Optional[bool] = None
    AllowCheckIn: Optional[bool] = None


class IssuerTypeDef(BaseValidatorModel):
    Name: str
    SignKey: Optional[str] = None


class CreateTokenRequestTypeDef(BaseValidatorModel):
    LicenseArn: str
    ClientToken: str
    RoleArns: Optional[Sequence[str]] = None
    ExpirationInDays: Optional[int] = None
    TokenProperties: Optional[Sequence[str]] = None


class DeleteGrantRequestTypeDef(BaseValidatorModel):
    GrantArn: str
    Version: str
    StatusReason: Optional[str] = None


class DeleteLicenseConfigurationRequestTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: str


class DeleteLicenseManagerReportGeneratorRequestTypeDef(BaseValidatorModel):
    LicenseManagerReportGeneratorArn: str


class DeleteLicenseRequestTypeDef(BaseValidatorModel):
    LicenseArn: str
    SourceVersion: str


class DeleteTokenRequestTypeDef(BaseValidatorModel):
    TokenId: str


class EntitlementUsageTypeDef(BaseValidatorModel):
    Name: str
    ConsumedValue: str
    Unit: EntitlementDataUnitType
    MaxCount: Optional[str] = None


class ExtendLicenseConsumptionRequestTypeDef(BaseValidatorModel):
    LicenseConsumptionToken: str
    DryRun: Optional[bool] = None


class FilterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class GetAccessTokenRequestTypeDef(BaseValidatorModel):
    Token: str
    TokenProperties: Optional[Sequence[str]] = None


class GetGrantRequestTypeDef(BaseValidatorModel):
    GrantArn: str
    Version: Optional[str] = None


class GetLicenseConfigurationRequestTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: str


class ManagedResourceSummaryTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    AssociationCount: Optional[int] = None


class GetLicenseConversionTaskRequestTypeDef(BaseValidatorModel):
    LicenseConversionTaskId: str


class GetLicenseManagerReportGeneratorRequestTypeDef(BaseValidatorModel):
    LicenseManagerReportGeneratorArn: str


class GetLicenseRequestTypeDef(BaseValidatorModel):
    LicenseArn: str
    Version: Optional[str] = None


class GetLicenseUsageRequestTypeDef(BaseValidatorModel):
    LicenseArn: str


class OrganizationConfigurationTypeDef(BaseValidatorModel):
    EnableIntegration: bool


class IssuerDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    SignKey: Optional[str] = None
    KeyFingerprint: Optional[str] = None


class ReceivedMetadataTypeDef(BaseValidatorModel):
    ReceivedStatus: Optional[ReceivedStatusType] = None
    ReceivedStatusReason: Optional[str] = None
    AllowedOperations: Optional[List[AllowedOperationType]] = None


class InventoryFilterTypeDef(BaseValidatorModel):
    Name: str
    Condition: InventoryFilterConditionType
    Value: Optional[str] = None


class LicenseConfigurationAssociationTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceOwnerId: Optional[str] = None
    AssociationTime: Optional[datetime] = None
    AmiAssociationScope: Optional[str] = None


class LicenseConfigurationUsageTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceStatus: Optional[str] = None
    ResourceOwnerId: Optional[str] = None
    AssociationTime: Optional[datetime] = None
    ConsumedLicenses: Optional[int] = None


class LicenseSpecificationTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: str
    AmiAssociationScope: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAssociationsForLicenseConfigurationRequestTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFailuresForLicenseConfigurationOperationsRequestTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLicenseSpecificationsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLicenseVersionsRequestTypeDef(BaseValidatorModel):
    LicenseArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ResourceInventoryTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceArn: Optional[str] = None
    Platform: Optional[str] = None
    PlatformVersion: Optional[str] = None
    ResourceOwningAccountId: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class TokenDataTypeDef(BaseValidatorModel):
    TokenId: Optional[str] = None
    TokenType: Optional[str] = None
    LicenseArn: Optional[str] = None
    ExpirationTime: Optional[str] = None
    TokenProperties: Optional[List[str]] = None
    RoleArns: Optional[List[str]] = None
    Status: Optional[str] = None


class ProductInformationFilterOutputTypeDef(BaseValidatorModel):
    ProductInformationFilterName: str
    ProductInformationFilterComparator: str
    ProductInformationFilterValue: Optional[List[str]] = None


class ProductInformationFilterTypeDef(BaseValidatorModel):
    ProductInformationFilterName: str
    ProductInformationFilterComparator: str
    ProductInformationFilterValue: Optional[Sequence[str]] = None


class RejectGrantRequestTypeDef(BaseValidatorModel):
    GrantArn: str


class ReportContextOutputTypeDef(BaseValidatorModel):
    licenseConfigurationArns: List[str]


class ReportContextTypeDef(BaseValidatorModel):
    licenseConfigurationArns: Sequence[str]


class S3LocationTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class AcceptGrantResponseTypeDef(BaseValidatorModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateGrantResponseTypeDef(BaseValidatorModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateGrantVersionResponseTypeDef(BaseValidatorModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLicenseConfigurationResponseTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLicenseConversionTaskForResourceResponseTypeDef(BaseValidatorModel):
    LicenseConversionTaskId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLicenseManagerReportGeneratorResponseTypeDef(BaseValidatorModel):
    LicenseManagerReportGeneratorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLicenseResponseTypeDef(BaseValidatorModel):
    LicenseArn: str
    Status: LicenseStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLicenseVersionResponseTypeDef(BaseValidatorModel):
    LicenseArn: str
    Version: str
    Status: LicenseStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTokenResponseTypeDef(BaseValidatorModel):
    TokenId: str
    TokenType: Literal["REFRESH_TOKEN"]
    Token: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteGrantResponseTypeDef(BaseValidatorModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteLicenseResponseTypeDef(BaseValidatorModel):
    Status: LicenseDeletionStatusType
    DeletionDate: str
    ResponseMetadata: ResponseMetadataTypeDef


class ExtendLicenseConsumptionResponseTypeDef(BaseValidatorModel):
    LicenseConsumptionToken: str
    Expiration: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccessTokenResponseTypeDef(BaseValidatorModel):
    AccessToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class RejectGrantResponseTypeDef(BaseValidatorModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef


class CheckoutLicenseRequestTypeDef(BaseValidatorModel):
    ProductSKU: str
    CheckoutType: CheckoutTypeType
    KeyFingerprint: str
    Entitlements: Sequence[EntitlementDataTypeDef]
    ClientToken: str
    Beneficiary: Optional[str] = None
    NodeId: Optional[str] = None


class CheckoutLicenseResponseTypeDef(BaseValidatorModel):
    CheckoutType: CheckoutTypeType
    LicenseConsumptionToken: str
    EntitlementsAllowed: List[EntitlementDataTypeDef]
    SignedToken: str
    NodeId: str
    IssuedAt: str
    Expiration: str
    LicenseArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CheckoutBorrowLicenseRequestTypeDef(BaseValidatorModel):
    LicenseArn: str
    Entitlements: Sequence[EntitlementDataTypeDef]
    DigitalSignatureMethod: Literal["JWT_PS384"]
    ClientToken: str
    NodeId: Optional[str] = None
    CheckoutMetadata: Optional[Sequence[MetadataTypeDef]] = None


class CheckoutBorrowLicenseResponseTypeDef(BaseValidatorModel):
    LicenseArn: str
    LicenseConsumptionToken: str
    EntitlementsAllowed: List[EntitlementDataTypeDef]
    NodeId: str
    SignedToken: str
    IssuedAt: str
    Expiration: str
    CheckoutMetadata: List[MetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class LicenseOperationFailureTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ErrorMessage: Optional[str] = None
    FailureTime: Optional[datetime] = None
    OperationName: Optional[str] = None
    ResourceOwnerId: Optional[str] = None
    OperationRequestedBy: Optional[str] = None
    MetadataList: Optional[List[MetadataTypeDef]] = None


class ConsumptionConfigurationTypeDef(BaseValidatorModel):
    RenewType: Optional[RenewTypeType] = None
    ProvisionalConfiguration: Optional[ProvisionalConfigurationTypeDef] = None
    BorrowConfiguration: Optional[BorrowConfigurationTypeDef] = None


class CreateGrantVersionRequestTypeDef(BaseValidatorModel):
    ClientToken: str
    GrantArn: str
    GrantName: Optional[str] = None
    AllowedOperations: Optional[Sequence[AllowedOperationType]] = None
    Status: Optional[GrantStatusType] = None
    StatusReason: Optional[str] = None
    SourceVersion: Optional[str] = None
    Options: Optional[OptionsTypeDef] = None


class GrantTypeDef(BaseValidatorModel):
    GrantArn: str
    GrantName: str
    ParentArn: str
    LicenseArn: str
    GranteePrincipalArn: str
    HomeRegion: str
    GrantStatus: GrantStatusType
    Version: str
    GrantedOperations: List[AllowedOperationType]
    StatusReason: Optional[str] = None
    Options: Optional[OptionsTypeDef] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CreateLicenseConversionTaskForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    SourceLicenseContext: LicenseConversionContextTypeDef
    DestinationLicenseContext: LicenseConversionContextTypeDef


class GetLicenseConversionTaskResponseTypeDef(BaseValidatorModel):
    LicenseConversionTaskId: str
    ResourceArn: str
    SourceLicenseContext: LicenseConversionContextTypeDef
    DestinationLicenseContext: LicenseConversionContextTypeDef
    StatusMessage: str
    Status: LicenseConversionTaskStatusType
    StartTime: datetime
    LicenseConversionTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class LicenseConversionTaskTypeDef(BaseValidatorModel):
    LicenseConversionTaskId: Optional[str] = None
    ResourceArn: Optional[str] = None
    SourceLicenseContext: Optional[LicenseConversionContextTypeDef] = None
    DestinationLicenseContext: Optional[LicenseConversionContextTypeDef] = None
    Status: Optional[LicenseConversionTaskStatusType] = None
    StatusMessage: Optional[str] = None
    StartTime: Optional[datetime] = None
    LicenseConversionTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class LicenseUsageTypeDef(BaseValidatorModel):
    EntitlementUsages: Optional[List[EntitlementUsageTypeDef]] = None


class ListDistributedGrantsRequestTypeDef(BaseValidatorModel):
    GrantArns: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListLicenseConfigurationsRequestTypeDef(BaseValidatorModel):
    LicenseConfigurationArns: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListLicenseConversionTasksRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class ListLicenseManagerReportGeneratorsRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListLicensesRequestTypeDef(BaseValidatorModel):
    LicenseArns: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListReceivedGrantsForOrganizationRequestTypeDef(BaseValidatorModel):
    LicenseArn: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListReceivedGrantsRequestTypeDef(BaseValidatorModel):
    GrantArns: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListReceivedLicensesForOrganizationRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListReceivedLicensesRequestTypeDef(BaseValidatorModel):
    LicenseArns: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTokensRequestTypeDef(BaseValidatorModel):
    TokenIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListUsageForLicenseConfigurationRequestTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class GetServiceSettingsResponseTypeDef(BaseValidatorModel):
    S3BucketArn: str
    SnsTopicArn: str
    OrganizationConfiguration: OrganizationConfigurationTypeDef
    EnableCrossAccountsDiscovery: bool
    LicenseManagerResourceShareArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateServiceSettingsRequestTypeDef(BaseValidatorModel):
    S3BucketArn: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    OrganizationConfiguration: Optional[OrganizationConfigurationTypeDef] = None
    EnableCrossAccountsDiscovery: Optional[bool] = None


class ListResourceInventoryRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[InventoryFilterTypeDef]] = None


class ListAssociationsForLicenseConfigurationResponseTypeDef(BaseValidatorModel):
    LicenseConfigurationAssociations: List[LicenseConfigurationAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListUsageForLicenseConfigurationResponseTypeDef(BaseValidatorModel):
    LicenseConfigurationUsageList: List[LicenseConfigurationUsageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListLicenseSpecificationsForResourceResponseTypeDef(BaseValidatorModel):
    LicenseSpecifications: List[LicenseSpecificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateLicenseSpecificationsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    AddLicenseSpecifications: Optional[Sequence[LicenseSpecificationTypeDef]] = None
    RemoveLicenseSpecifications: Optional[Sequence[LicenseSpecificationTypeDef]] = None


class ListAssociationsForLicenseConfigurationRequestPaginateTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLicenseConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    LicenseConfigurationArns: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLicenseSpecificationsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceInventoryRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[InventoryFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsageForLicenseConfigurationRequestPaginateTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceInventoryResponseTypeDef(BaseValidatorModel):
    ResourceInventoryList: List[ResourceInventoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTokensResponseTypeDef(BaseValidatorModel):
    Tokens: List[TokenDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ProductInformationOutputTypeDef(BaseValidatorModel):
    ResourceType: str
    ProductInformationFilterList: List[ProductInformationFilterOutputTypeDef]


class ReportGeneratorTypeDef(BaseValidatorModel):
    ReportGeneratorName: Optional[str] = None
    ReportType: Optional[List[ReportTypeType]] = None
    ReportContext: Optional[ReportContextOutputTypeDef] = None
    ReportFrequency: Optional[ReportFrequencyTypeDef] = None
    LicenseManagerReportGeneratorArn: Optional[str] = None
    LastRunStatus: Optional[str] = None
    LastRunFailureReason: Optional[str] = None
    LastReportGenerationTime: Optional[str] = None
    ReportCreatorAccount: Optional[str] = None
    Description: Optional[str] = None
    S3Location: Optional[S3LocationTypeDef] = None
    CreateTime: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None


class ListFailuresForLicenseConfigurationOperationsResponseTypeDef(BaseValidatorModel):
    LicenseOperationFailureList: List[LicenseOperationFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateLicenseRequestTypeDef(BaseValidatorModel):
    LicenseName: str
    ProductName: str
    ProductSKU: str
    Issuer: IssuerTypeDef
    HomeRegion: str
    Validity: DatetimeRangeTypeDef
    Entitlements: Sequence[EntitlementTypeDef]
    Beneficiary: str
    ConsumptionConfiguration: ConsumptionConfigurationTypeDef
    ClientToken: str
    LicenseMetadata: Optional[Sequence[MetadataTypeDef]] = None


class CreateLicenseVersionRequestTypeDef(BaseValidatorModel):
    LicenseArn: str
    LicenseName: str
    ProductName: str
    Issuer: IssuerTypeDef
    HomeRegion: str
    Validity: DatetimeRangeTypeDef
    Entitlements: Sequence[EntitlementTypeDef]
    ConsumptionConfiguration: ConsumptionConfigurationTypeDef
    Status: LicenseStatusType
    ClientToken: str
    LicenseMetadata: Optional[Sequence[MetadataTypeDef]] = None
    SourceVersion: Optional[str] = None


class GrantedLicenseTypeDef(BaseValidatorModel):
    LicenseArn: Optional[str] = None
    LicenseName: Optional[str] = None
    ProductName: Optional[str] = None
    ProductSKU: Optional[str] = None
    Issuer: Optional[IssuerDetailsTypeDef] = None
    HomeRegion: Optional[str] = None
    Status: Optional[LicenseStatusType] = None
    Validity: Optional[DatetimeRangeTypeDef] = None
    Beneficiary: Optional[str] = None
    Entitlements: Optional[List[EntitlementTypeDef]] = None
    ConsumptionConfiguration: Optional[ConsumptionConfigurationTypeDef] = None
    LicenseMetadata: Optional[List[MetadataTypeDef]] = None
    CreateTime: Optional[str] = None
    Version: Optional[str] = None
    ReceivedMetadata: Optional[ReceivedMetadataTypeDef] = None


class LicenseTypeDef(BaseValidatorModel):
    LicenseArn: Optional[str] = None
    LicenseName: Optional[str] = None
    ProductName: Optional[str] = None
    ProductSKU: Optional[str] = None
    Issuer: Optional[IssuerDetailsTypeDef] = None
    HomeRegion: Optional[str] = None
    Status: Optional[LicenseStatusType] = None
    Validity: Optional[DatetimeRangeTypeDef] = None
    Beneficiary: Optional[str] = None
    Entitlements: Optional[List[EntitlementTypeDef]] = None
    ConsumptionConfiguration: Optional[ConsumptionConfigurationTypeDef] = None
    LicenseMetadata: Optional[List[MetadataTypeDef]] = None
    CreateTime: Optional[str] = None
    Version: Optional[str] = None


class GetGrantResponseTypeDef(BaseValidatorModel):
    Grant: GrantTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDistributedGrantsResponseTypeDef(BaseValidatorModel):
    Grants: List[GrantTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListReceivedGrantsForOrganizationResponseTypeDef(BaseValidatorModel):
    Grants: List[GrantTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListReceivedGrantsResponseTypeDef(BaseValidatorModel):
    Grants: List[GrantTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListLicenseConversionTasksResponseTypeDef(BaseValidatorModel):
    LicenseConversionTasks: List[LicenseConversionTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetLicenseUsageResponseTypeDef(BaseValidatorModel):
    LicenseUsage: LicenseUsageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetLicenseConfigurationResponseTypeDef(BaseValidatorModel):
    LicenseConfigurationId: str
    LicenseConfigurationArn: str
    Name: str
    Description: str
    LicenseCountingType: LicenseCountingTypeType
    LicenseRules: List[str]
    LicenseCount: int
    LicenseCountHardLimit: bool
    ConsumedLicenses: int
    Status: str
    OwnerAccountId: str
    ConsumedLicenseSummaryList: List[ConsumedLicenseSummaryTypeDef]
    ManagedResourceSummaryList: List[ManagedResourceSummaryTypeDef]
    Tags: List[TagTypeDef]
    ProductInformationList: List[ProductInformationOutputTypeDef]
    AutomatedDiscoveryInformation: AutomatedDiscoveryInformationTypeDef
    DisassociateWhenNotFound: bool
    ResponseMetadata: ResponseMetadataTypeDef


class LicenseConfigurationTypeDef(BaseValidatorModel):
    LicenseConfigurationId: Optional[str] = None
    LicenseConfigurationArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    LicenseCountingType: Optional[LicenseCountingTypeType] = None
    LicenseRules: Optional[List[str]] = None
    LicenseCount: Optional[int] = None
    LicenseCountHardLimit: Optional[bool] = None
    DisassociateWhenNotFound: Optional[bool] = None
    ConsumedLicenses: Optional[int] = None
    Status: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    ConsumedLicenseSummaryList: Optional[List[ConsumedLicenseSummaryTypeDef]] = None
    ManagedResourceSummaryList: Optional[List[ManagedResourceSummaryTypeDef]] = None
    ProductInformationList: Optional[List[ProductInformationOutputTypeDef]] = None
    AutomatedDiscoveryInformation: Optional[AutomatedDiscoveryInformationTypeDef] = None


class ProductInformationFilterUnionTypeDef(BaseValidatorModel):
    pass


class ProductInformationTypeDef(BaseValidatorModel):
    ResourceType: str
    ProductInformationFilterList: Sequence[ProductInformationFilterUnionTypeDef]


class GetLicenseManagerReportGeneratorResponseTypeDef(BaseValidatorModel):
    ReportGenerator: ReportGeneratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListLicenseManagerReportGeneratorsResponseTypeDef(BaseValidatorModel):
    ReportGenerators: List[ReportGeneratorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListReceivedLicensesForOrganizationResponseTypeDef(BaseValidatorModel):
    Licenses: List[GrantedLicenseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListReceivedLicensesResponseTypeDef(BaseValidatorModel):
    Licenses: List[GrantedLicenseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetLicenseResponseTypeDef(BaseValidatorModel):
    License: LicenseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListLicenseVersionsResponseTypeDef(BaseValidatorModel):
    Licenses: List[LicenseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListLicensesResponseTypeDef(BaseValidatorModel):
    Licenses: List[LicenseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListLicenseConfigurationsResponseTypeDef(BaseValidatorModel):
    LicenseConfigurations: List[LicenseConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ProductInformationUnionTypeDef(BaseValidatorModel):
    pass


class CreateLicenseConfigurationRequestTypeDef(BaseValidatorModel):
    Name: str
    LicenseCountingType: LicenseCountingTypeType
    Description: Optional[str] = None
    LicenseCount: Optional[int] = None
    LicenseCountHardLimit: Optional[bool] = None
    LicenseRules: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DisassociateWhenNotFound: Optional[bool] = None
    ProductInformationList: Optional[Sequence[ProductInformationUnionTypeDef]] = None


class UpdateLicenseConfigurationRequestTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: str
    LicenseConfigurationStatus: Optional[LicenseConfigurationStatusType] = None
    LicenseRules: Optional[Sequence[str]] = None
    LicenseCount: Optional[int] = None
    LicenseCountHardLimit: Optional[bool] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ProductInformationList: Optional[Sequence[ProductInformationUnionTypeDef]] = None
    DisassociateWhenNotFound: Optional[bool] = None


