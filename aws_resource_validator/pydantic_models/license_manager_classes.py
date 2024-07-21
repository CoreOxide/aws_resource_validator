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
from aws_resource_validator.pydantic_models.license_manager_constants import *

class AcceptGrantRequestRequestTypeDef(BaseModel):
    GrantArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AutomatedDiscoveryInformationTypeDef(BaseModel):
    LastRunTime: Optional[datetime] = None

class BorrowConfigurationTypeDef(BaseModel):
    AllowEarlyCheckIn: bool
    MaxTimeToLiveInMinutes: int

class CheckInLicenseRequestRequestTypeDef(BaseModel):
    LicenseConsumptionToken: str
    Beneficiary: Optional[str] = None

class EntitlementDataTypeDef(BaseModel):
    Name: str
    Unit: EntitlementDataUnitType
    Value: Optional[str] = None

class MetadataTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class ConsumedLicenseSummaryTypeDef(BaseModel):
    ResourceType: Optional[ResourceTypeType] = None
    ConsumedLicenses: Optional[int] = None

class ProvisionalConfigurationTypeDef(BaseModel):
    MaxTimeToLiveInMinutes: int

class CreateGrantRequestRequestTypeDef(BaseModel):
    ClientToken: str
    GrantName: str
    LicenseArn: str
    Principals: Sequence[str]
    HomeRegion: str
    AllowedOperations: Sequence[AllowedOperationType]

class OptionsTypeDef(BaseModel):
    ActivationOverrideBehavior: Optional[ActivationOverrideBehaviorType] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class LicenseConversionContextTypeDef(BaseModel):
    UsageOperation: Optional[str] = None

class ReportContextTypeDef(BaseModel):
    licenseConfigurationArns: Sequence[str]

class ReportFrequencyTypeDef(BaseModel):
    value: Optional[int] = None
    period: Optional[ReportFrequencyTypeType] = None

class DatetimeRangeTypeDef(BaseModel):
    Begin: str
    End: Optional[str] = None

class EntitlementTypeDef(BaseModel):
    Name: str
    Unit: EntitlementUnitType
    Value: Optional[str] = None
    MaxCount: Optional[int] = None
    Overage: Optional[bool] = None
    AllowCheckIn: Optional[bool] = None

class IssuerTypeDef(BaseModel):
    Name: str
    SignKey: Optional[str] = None

class CreateTokenRequestRequestTypeDef(BaseModel):
    LicenseArn: str
    ClientToken: str
    RoleArns: Optional[Sequence[str]] = None
    ExpirationInDays: Optional[int] = None
    TokenProperties: Optional[Sequence[str]] = None

class DeleteGrantRequestRequestTypeDef(BaseModel):
    GrantArn: str
    Version: str
    StatusReason: Optional[str] = None

class DeleteLicenseConfigurationRequestRequestTypeDef(BaseModel):
    LicenseConfigurationArn: str

class DeleteLicenseManagerReportGeneratorRequestRequestTypeDef(BaseModel):
    LicenseManagerReportGeneratorArn: str

class DeleteLicenseRequestRequestTypeDef(BaseModel):
    LicenseArn: str
    SourceVersion: str

class DeleteTokenRequestRequestTypeDef(BaseModel):
    TokenId: str

class EntitlementUsageTypeDef(BaseModel):
    Name: str
    ConsumedValue: str
    Unit: EntitlementDataUnitType
    MaxCount: Optional[str] = None

class ExtendLicenseConsumptionRequestRequestTypeDef(BaseModel):
    LicenseConsumptionToken: str
    DryRun: Optional[bool] = None

class FilterTypeDef(BaseModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class GetAccessTokenRequestRequestTypeDef(BaseModel):
    Token: str
    TokenProperties: Optional[Sequence[str]] = None

class GetGrantRequestRequestTypeDef(BaseModel):
    GrantArn: str
    Version: Optional[str] = None

class GetLicenseConfigurationRequestRequestTypeDef(BaseModel):
    LicenseConfigurationArn: str

class ManagedResourceSummaryTypeDef(BaseModel):
    ResourceType: Optional[ResourceTypeType] = None
    AssociationCount: Optional[int] = None

class GetLicenseConversionTaskRequestRequestTypeDef(BaseModel):
    LicenseConversionTaskId: str

class GetLicenseManagerReportGeneratorRequestRequestTypeDef(BaseModel):
    LicenseManagerReportGeneratorArn: str

class GetLicenseRequestRequestTypeDef(BaseModel):
    LicenseArn: str
    Version: Optional[str] = None

class GetLicenseUsageRequestRequestTypeDef(BaseModel):
    LicenseArn: str

class OrganizationConfigurationTypeDef(BaseModel):
    EnableIntegration: bool

class IssuerDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    SignKey: Optional[str] = None
    KeyFingerprint: Optional[str] = None

class ReceivedMetadataTypeDef(BaseModel):
    ReceivedStatus: Optional[ReceivedStatusType] = None
    ReceivedStatusReason: Optional[str] = None
    AllowedOperations: Optional[List[AllowedOperationType]] = None

class InventoryFilterTypeDef(BaseModel):
    Name: str
    Condition: InventoryFilterConditionType
    Value: Optional[str] = None

class LicenseConfigurationAssociationTypeDef(BaseModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceOwnerId: Optional[str] = None
    AssociationTime: Optional[datetime] = None
    AmiAssociationScope: Optional[str] = None

class LicenseConfigurationUsageTypeDef(BaseModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceStatus: Optional[str] = None
    ResourceOwnerId: Optional[str] = None
    AssociationTime: Optional[datetime] = None
    ConsumedLicenses: Optional[int] = None

class LicenseSpecificationTypeDef(BaseModel):
    LicenseConfigurationArn: str
    AmiAssociationScope: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAssociationsForLicenseConfigurationRequestRequestTypeDef(BaseModel):
    LicenseConfigurationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef(BaseModel):
    LicenseConfigurationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListLicenseSpecificationsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListLicenseVersionsRequestRequestTypeDef(BaseModel):
    LicenseArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ResourceInventoryTypeDef(BaseModel):
    ResourceId: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceArn: Optional[str] = None
    Platform: Optional[str] = None
    PlatformVersion: Optional[str] = None
    ResourceOwningAccountId: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class TokenDataTypeDef(BaseModel):
    TokenId: Optional[str] = None
    TokenType: Optional[str] = None
    LicenseArn: Optional[str] = None
    ExpirationTime: Optional[str] = None
    TokenProperties: Optional[List[str]] = None
    RoleArns: Optional[List[str]] = None
    Status: Optional[str] = None

class ProductInformationFilterPaginatorTypeDef(BaseModel):
    ProductInformationFilterName: str
    ProductInformationFilterComparator: str
    ProductInformationFilterValue: Optional[List[str]] = None

class ProductInformationFilterTypeDef(BaseModel):
    ProductInformationFilterName: str
    ProductInformationFilterComparator: str
    ProductInformationFilterValue: Optional[Sequence[str]] = None

class RejectGrantRequestRequestTypeDef(BaseModel):
    GrantArn: str

class S3LocationTypeDef(BaseModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class AcceptGrantResponseTypeDef(BaseModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGrantResponseTypeDef(BaseModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGrantVersionResponseTypeDef(BaseModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseConfigurationResponseTypeDef(BaseModel):
    LicenseConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseConversionTaskForResourceResponseTypeDef(BaseModel):
    LicenseConversionTaskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseManagerReportGeneratorResponseTypeDef(BaseModel):
    LicenseManagerReportGeneratorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseResponseTypeDef(BaseModel):
    LicenseArn: str
    Status: LicenseStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseVersionResponseTypeDef(BaseModel):
    LicenseArn: str
    Version: str
    Status: LicenseStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTokenResponseTypeDef(BaseModel):
    TokenId: str
    TokenType: Literal["REFRESH_TOKEN"]
    Token: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGrantResponseTypeDef(BaseModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLicenseResponseTypeDef(BaseModel):
    Status: LicenseDeletionStatusType
    DeletionDate: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExtendLicenseConsumptionResponseTypeDef(BaseModel):
    LicenseConsumptionToken: str
    Expiration: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessTokenResponseTypeDef(BaseModel):
    AccessToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RejectGrantResponseTypeDef(BaseModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CheckoutLicenseRequestRequestTypeDef(BaseModel):
    ProductSKU: str
    CheckoutType: CheckoutTypeType
    KeyFingerprint: str
    Entitlements: Sequence[EntitlementDataTypeDef]
    ClientToken: str
    Beneficiary: Optional[str] = None
    NodeId: Optional[str] = None

class CheckoutLicenseResponseTypeDef(BaseModel):
    CheckoutType: CheckoutTypeType
    LicenseConsumptionToken: str
    EntitlementsAllowed: List[EntitlementDataTypeDef]
    SignedToken: str
    NodeId: str
    IssuedAt: str
    Expiration: str
    LicenseArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CheckoutBorrowLicenseRequestRequestTypeDef(BaseModel):
    LicenseArn: str
    Entitlements: Sequence[EntitlementDataTypeDef]
    DigitalSignatureMethod: Literal["JWT_PS384"]
    ClientToken: str
    NodeId: Optional[str] = None
    CheckoutMetadata: Optional[Sequence[MetadataTypeDef]] = None

class CheckoutBorrowLicenseResponseTypeDef(BaseModel):
    LicenseArn: str
    LicenseConsumptionToken: str
    EntitlementsAllowed: List[EntitlementDataTypeDef]
    NodeId: str
    SignedToken: str
    IssuedAt: str
    Expiration: str
    CheckoutMetadata: List[MetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LicenseOperationFailureTypeDef(BaseModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ErrorMessage: Optional[str] = None
    FailureTime: Optional[datetime] = None
    OperationName: Optional[str] = None
    ResourceOwnerId: Optional[str] = None
    OperationRequestedBy: Optional[str] = None
    MetadataList: Optional[List[MetadataTypeDef]] = None

class ConsumptionConfigurationTypeDef(BaseModel):
    RenewType: Optional[RenewTypeType] = None
    ProvisionalConfiguration: Optional[ProvisionalConfigurationTypeDef] = None
    BorrowConfiguration: Optional[BorrowConfigurationTypeDef] = None

class CreateGrantVersionRequestRequestTypeDef(BaseModel):
    ClientToken: str
    GrantArn: str
    GrantName: Optional[str] = None
    AllowedOperations: Optional[Sequence[AllowedOperationType]] = None
    Status: Optional[GrantStatusType] = None
    StatusReason: Optional[str] = None
    SourceVersion: Optional[str] = None
    Options: Optional[OptionsTypeDef] = None

class GrantTypeDef(BaseModel):
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

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateLicenseConversionTaskForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    SourceLicenseContext: LicenseConversionContextTypeDef
    DestinationLicenseContext: LicenseConversionContextTypeDef

class GetLicenseConversionTaskResponseTypeDef(BaseModel):
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

class LicenseConversionTaskTypeDef(BaseModel):
    LicenseConversionTaskId: Optional[str] = None
    ResourceArn: Optional[str] = None
    SourceLicenseContext: Optional[LicenseConversionContextTypeDef] = None
    DestinationLicenseContext: Optional[LicenseConversionContextTypeDef] = None
    Status: Optional[LicenseConversionTaskStatusType] = None
    StatusMessage: Optional[str] = None
    StartTime: Optional[datetime] = None
    LicenseConversionTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class CreateLicenseManagerReportGeneratorRequestRequestTypeDef(BaseModel):
    ReportGeneratorName: str
    Type: Sequence[ReportTypeType]
    ReportContext: ReportContextTypeDef
    ReportFrequency: ReportFrequencyTypeDef
    ClientToken: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateLicenseManagerReportGeneratorRequestRequestTypeDef(BaseModel):
    LicenseManagerReportGeneratorArn: str
    ReportGeneratorName: str
    Type: Sequence[ReportTypeType]
    ReportContext: ReportContextTypeDef
    ReportFrequency: ReportFrequencyTypeDef
    ClientToken: str
    Description: Optional[str] = None

class LicenseUsageTypeDef(BaseModel):
    EntitlementUsages: Optional[List[EntitlementUsageTypeDef]] = None

class ListDistributedGrantsRequestRequestTypeDef(BaseModel):
    GrantArns: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListLicenseConfigurationsRequestRequestTypeDef(BaseModel):
    LicenseConfigurationArns: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListLicenseConversionTasksRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListLicenseManagerReportGeneratorsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListLicensesRequestRequestTypeDef(BaseModel):
    LicenseArns: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListReceivedGrantsForOrganizationRequestRequestTypeDef(BaseModel):
    LicenseArn: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListReceivedGrantsRequestRequestTypeDef(BaseModel):
    GrantArns: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListReceivedLicensesForOrganizationRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListReceivedLicensesRequestRequestTypeDef(BaseModel):
    LicenseArns: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTokensRequestRequestTypeDef(BaseModel):
    TokenIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListUsageForLicenseConfigurationRequestRequestTypeDef(BaseModel):
    LicenseConfigurationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class GetServiceSettingsResponseTypeDef(BaseModel):
    S3BucketArn: str
    SnsTopicArn: str
    OrganizationConfiguration: OrganizationConfigurationTypeDef
    EnableCrossAccountsDiscovery: bool
    LicenseManagerResourceShareArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceSettingsRequestRequestTypeDef(BaseModel):
    S3BucketArn: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    OrganizationConfiguration: Optional[OrganizationConfigurationTypeDef] = None
    EnableCrossAccountsDiscovery: Optional[bool] = None

class ListResourceInventoryRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[InventoryFilterTypeDef]] = None

class ListAssociationsForLicenseConfigurationResponseTypeDef(BaseModel):
    LicenseConfigurationAssociations: List[LicenseConfigurationAssociationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsageForLicenseConfigurationResponseTypeDef(BaseModel):
    LicenseConfigurationUsageList: List[LicenseConfigurationUsageTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicenseSpecificationsForResourceResponseTypeDef(BaseModel):
    LicenseSpecifications: List[LicenseSpecificationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLicenseSpecificationsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    AddLicenseSpecifications: Optional[Sequence[LicenseSpecificationTypeDef]] = None
    RemoveLicenseSpecifications: Optional[Sequence[LicenseSpecificationTypeDef]] = None

class ListAssociationsForLicenseConfigurationRequestListAssociationsForLicenseConfigurationPaginateTypeDef(BaseModel):
    LicenseConfigurationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLicenseConfigurationsRequestListLicenseConfigurationsPaginateTypeDef(BaseModel):
    LicenseConfigurationArns: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLicenseSpecificationsForResourceRequestListLicenseSpecificationsForResourcePaginateTypeDef(BaseModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceInventoryRequestListResourceInventoryPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[InventoryFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsageForLicenseConfigurationRequestListUsageForLicenseConfigurationPaginateTypeDef(BaseModel):
    LicenseConfigurationArn: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceInventoryResponseTypeDef(BaseModel):
    ResourceInventoryList: List[ResourceInventoryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTokensResponseTypeDef(BaseModel):
    Tokens: List[TokenDataTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ProductInformationPaginatorTypeDef(BaseModel):
    ResourceType: str
    ProductInformationFilterList: List[ProductInformationFilterPaginatorTypeDef]

class ProductInformationTypeDef(BaseModel):
    ResourceType: str
    ProductInformationFilterList: Sequence[ProductInformationFilterTypeDef]

class ReportGeneratorTypeDef(BaseModel):
    ReportGeneratorName: Optional[str] = None
    ReportType: Optional[List[ReportTypeType]] = None
    ReportContext: Optional[ReportContextTypeDef] = None
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

class ListFailuresForLicenseConfigurationOperationsResponseTypeDef(BaseModel):
    LicenseOperationFailureList: List[LicenseOperationFailureTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseRequestRequestTypeDef(BaseModel):
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

class CreateLicenseVersionRequestRequestTypeDef(BaseModel):
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

class GrantedLicenseTypeDef(BaseModel):
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

class LicenseTypeDef(BaseModel):
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

class GetGrantResponseTypeDef(BaseModel):
    Grant: GrantTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributedGrantsResponseTypeDef(BaseModel):
    Grants: List[GrantTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListReceivedGrantsForOrganizationResponseTypeDef(BaseModel):
    Grants: List[GrantTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListReceivedGrantsResponseTypeDef(BaseModel):
    Grants: List[GrantTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicenseConversionTasksResponseTypeDef(BaseModel):
    LicenseConversionTasks: List[LicenseConversionTaskTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLicenseUsageResponseTypeDef(BaseModel):
    LicenseUsage: LicenseUsageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LicenseConfigurationPaginatorTypeDef(BaseModel):
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
    ProductInformationList: Optional[List[ProductInformationPaginatorTypeDef]] = None
    AutomatedDiscoveryInformation: Optional[AutomatedDiscoveryInformationTypeDef] = None

class CreateLicenseConfigurationRequestRequestTypeDef(BaseModel):
    Name: str
    LicenseCountingType: LicenseCountingTypeType
    Description: Optional[str] = None
    LicenseCount: Optional[int] = None
    LicenseCountHardLimit: Optional[bool] = None
    LicenseRules: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DisassociateWhenNotFound: Optional[bool] = None
    ProductInformationList: Optional[Sequence[ProductInformationTypeDef]] = None

class GetLicenseConfigurationResponseTypeDef(BaseModel):
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
    ProductInformationList: List[ProductInformationTypeDef]
    AutomatedDiscoveryInformation: AutomatedDiscoveryInformationTypeDef
    DisassociateWhenNotFound: bool
    ResponseMetadata: ResponseMetadataTypeDef

class LicenseConfigurationTypeDef(BaseModel):
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
    ProductInformationList: Optional[List[ProductInformationTypeDef]] = None
    AutomatedDiscoveryInformation: Optional[AutomatedDiscoveryInformationTypeDef] = None

class UpdateLicenseConfigurationRequestRequestTypeDef(BaseModel):
    LicenseConfigurationArn: str
    LicenseConfigurationStatus: Optional[LicenseConfigurationStatusType] = None
    LicenseRules: Optional[Sequence[str]] = None
    LicenseCount: Optional[int] = None
    LicenseCountHardLimit: Optional[bool] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ProductInformationList: Optional[Sequence[ProductInformationTypeDef]] = None
    DisassociateWhenNotFound: Optional[bool] = None

class GetLicenseManagerReportGeneratorResponseTypeDef(BaseModel):
    ReportGenerator: ReportGeneratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicenseManagerReportGeneratorsResponseTypeDef(BaseModel):
    ReportGenerators: List[ReportGeneratorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListReceivedLicensesForOrganizationResponseTypeDef(BaseModel):
    Licenses: List[GrantedLicenseTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListReceivedLicensesResponseTypeDef(BaseModel):
    Licenses: List[GrantedLicenseTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLicenseResponseTypeDef(BaseModel):
    License: LicenseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicenseVersionsResponseTypeDef(BaseModel):
    Licenses: List[LicenseTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicensesResponseTypeDef(BaseModel):
    Licenses: List[LicenseTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicenseConfigurationsResponsePaginatorTypeDef(BaseModel):
    LicenseConfigurations: List[LicenseConfigurationPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicenseConfigurationsResponseTypeDef(BaseModel):
    LicenseConfigurations: List[LicenseConfigurationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

