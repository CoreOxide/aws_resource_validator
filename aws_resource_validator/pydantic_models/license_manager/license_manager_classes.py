from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.license_manager.license_manager_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'accept_grant' function.
class AcceptGrantRequest(BaseValidatorModel):
    GrantArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AutomatedDiscoveryInformation(BaseValidatorModel):
    LastRunTime: Optional[datetime] = None


class BorrowConfiguration(BaseValidatorModel):
    AllowEarlyCheckIn: bool
    MaxTimeToLiveInMinutes: int


class CheckInLicenseRequest(BaseValidatorModel):
    LicenseConsumptionToken: str
    Beneficiary: Optional[str] = None


class EntitlementData(BaseValidatorModel):
    Name: str
    Unit: EntitlementDataUnitType
    Value: Optional[str] = None


class Metadata(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class ConsumedLicenseSummary(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    ConsumedLicenses: Optional[int] = None


class ProvisionalConfiguration(BaseValidatorModel):
    MaxTimeToLiveInMinutes: int


# This class is the input for the 'create_grant' function.
class CreateGrantRequest(BaseValidatorModel):
    ClientToken: str
    GrantName: str
    LicenseArn: str
    Principals: List[str]
    HomeRegion: str
    AllowedOperations: List[AllowedOperationType]


class Options(BaseValidatorModel):
    ActivationOverrideBehavior: Optional[ActivationOverrideBehaviorType] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class LicenseConversionContext(BaseValidatorModel):
    UsageOperation: Optional[str] = None


class ReportFrequency(BaseValidatorModel):
    value: Optional[int] = None
    period: Optional[ReportFrequencyTypeType] = None


class DatetimeRange(BaseValidatorModel):
    Begin: str
    End: Optional[str] = None


class Entitlement(BaseValidatorModel):
    Name: str
    Unit: EntitlementUnitType
    Value: Optional[str] = None
    MaxCount: Optional[int] = None
    Overage: Optional[bool] = None
    AllowCheckIn: Optional[bool] = None


class Issuer(BaseValidatorModel):
    Name: str
    SignKey: Optional[str] = None


# This class is the input for the 'create_token' function.
class CreateTokenRequest(BaseValidatorModel):
    LicenseArn: str
    ClientToken: str
    RoleArns: Optional[List[str]] = None
    ExpirationInDays: Optional[int] = None
    TokenProperties: Optional[List[str]] = None


# This class is the input for the 'delete_grant' function.
class DeleteGrantRequest(BaseValidatorModel):
    GrantArn: str
    Version: str
    StatusReason: Optional[str] = None


class DeleteLicenseConfigurationRequest(BaseValidatorModel):
    LicenseConfigurationArn: str


class DeleteLicenseManagerReportGeneratorRequest(BaseValidatorModel):
    LicenseManagerReportGeneratorArn: str


# This class is the input for the 'delete_license' function.
class DeleteLicenseRequest(BaseValidatorModel):
    LicenseArn: str
    SourceVersion: str


class DeleteTokenRequest(BaseValidatorModel):
    TokenId: str


class EntitlementUsage(BaseValidatorModel):
    Name: str
    ConsumedValue: str
    Unit: EntitlementDataUnitType
    MaxCount: Optional[str] = None


# This class is the input for the 'extend_license_consumption' function.
class ExtendLicenseConsumptionRequest(BaseValidatorModel):
    LicenseConsumptionToken: str
    DryRun: Optional[bool] = None


class Filter(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[List[str]] = None


# This class is the input for the 'get_access_token' function.
class GetAccessTokenRequest(BaseValidatorModel):
    Token: str
    TokenProperties: Optional[List[str]] = None


# This class is the input for the 'get_grant' function.
class GetGrantRequest(BaseValidatorModel):
    GrantArn: str
    Version: Optional[str] = None


# This class is the input for the 'get_license_configuration' function.
class GetLicenseConfigurationRequest(BaseValidatorModel):
    LicenseConfigurationArn: str


class ManagedResourceSummary(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    AssociationCount: Optional[int] = None


# This class is the input for the 'get_license_conversion_task' function.
class GetLicenseConversionTaskRequest(BaseValidatorModel):
    LicenseConversionTaskId: str


# This class is the input for the 'get_license_manager_report_generator' function.
class GetLicenseManagerReportGeneratorRequest(BaseValidatorModel):
    LicenseManagerReportGeneratorArn: str


# This class is the input for the 'get_license' function.
class GetLicenseRequest(BaseValidatorModel):
    LicenseArn: str
    Version: Optional[str] = None


# This class is the input for the 'get_license_usage' function.
class GetLicenseUsageRequest(BaseValidatorModel):
    LicenseArn: str


class OrganizationConfiguration(BaseValidatorModel):
    EnableIntegration: bool


class IssuerDetails(BaseValidatorModel):
    Name: Optional[str] = None
    SignKey: Optional[str] = None
    KeyFingerprint: Optional[str] = None


class ReceivedMetadata(BaseValidatorModel):
    ReceivedStatus: Optional[ReceivedStatusType] = None
    ReceivedStatusReason: Optional[str] = None
    AllowedOperations: Optional[List[AllowedOperationType]] = None


class InventoryFilter(BaseValidatorModel):
    Name: str
    Condition: InventoryFilterConditionType
    Value: Optional[str] = None


class LicenseConfigurationAssociation(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceOwnerId: Optional[str] = None
    AssociationTime: Optional[datetime] = None
    AmiAssociationScope: Optional[str] = None


class LicenseConfigurationUsage(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceStatus: Optional[str] = None
    ResourceOwnerId: Optional[str] = None
    AssociationTime: Optional[datetime] = None
    ConsumedLicenses: Optional[int] = None


class LicenseSpecification(BaseValidatorModel):
    LicenseConfigurationArn: str
    AmiAssociationScope: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_associations_for_license_configuration' function.
class ListAssociationsForLicenseConfigurationRequest(BaseValidatorModel):
    LicenseConfigurationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_failures_for_license_configuration_operations' function.
class ListFailuresForLicenseConfigurationOperationsRequest(BaseValidatorModel):
    LicenseConfigurationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_license_specifications_for_resource' function.
class ListLicenseSpecificationsForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_license_versions' function.
class ListLicenseVersionsRequest(BaseValidatorModel):
    LicenseArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ResourceInventory(BaseValidatorModel):
    ResourceId: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceArn: Optional[str] = None
    Platform: Optional[str] = None
    PlatformVersion: Optional[str] = None
    ResourceOwningAccountId: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class TokenData(BaseValidatorModel):
    TokenId: Optional[str] = None
    TokenType: Optional[str] = None
    LicenseArn: Optional[str] = None
    ExpirationTime: Optional[str] = None
    TokenProperties: Optional[List[str]] = None
    RoleArns: Optional[List[str]] = None
    Status: Optional[str] = None


class ProductInformationFilterOutput(BaseValidatorModel):
    ProductInformationFilterName: str
    ProductInformationFilterComparator: str
    ProductInformationFilterValue: Optional[List[str]] = None


class ProductInformationFilter(BaseValidatorModel):
    ProductInformationFilterName: str
    ProductInformationFilterComparator: str
    ProductInformationFilterValue: Optional[List[str]] = None


# This class is the input for the 'reject_grant' function.
class RejectGrantRequest(BaseValidatorModel):
    GrantArn: str


class ReportContextOutput(BaseValidatorModel):
    licenseConfigurationArns: List[str]


class ReportContext(BaseValidatorModel):
    licenseConfigurationArns: List[str]


class S3Location(BaseValidatorModel):
    bucket: Optional[str] = None
    keyPrefix: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the output for the 'accept_grant' function.
class AcceptGrantResponse(BaseValidatorModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_grant' function.
class CreateGrantResponse(BaseValidatorModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_grant_version' function.
class CreateGrantVersionResponse(BaseValidatorModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_license_configuration' function.
class CreateLicenseConfigurationResponse(BaseValidatorModel):
    LicenseConfigurationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_license_conversion_task_for_resource' function.
class CreateLicenseConversionTaskForResourceResponse(BaseValidatorModel):
    LicenseConversionTaskId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_license_manager_report_generator' function.
class CreateLicenseManagerReportGeneratorResponse(BaseValidatorModel):
    LicenseManagerReportGeneratorArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_license' function.
class CreateLicenseResponse(BaseValidatorModel):
    LicenseArn: str
    Status: LicenseStatusType
    Version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_license_version' function.
class CreateLicenseVersionResponse(BaseValidatorModel):
    LicenseArn: str
    Version: str
    Status: LicenseStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_token' function.
class CreateTokenResponse(BaseValidatorModel):
    TokenId: str
    TokenType: Literal['REFRESH_TOKEN']
    Token: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_grant' function.
class DeleteGrantResponse(BaseValidatorModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_license' function.
class DeleteLicenseResponse(BaseValidatorModel):
    Status: LicenseDeletionStatusType
    DeletionDate: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'extend_license_consumption' function.
class ExtendLicenseConsumptionResponse(BaseValidatorModel):
    LicenseConsumptionToken: str
    Expiration: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_access_token' function.
class GetAccessTokenResponse(BaseValidatorModel):
    AccessToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reject_grant' function.
class RejectGrantResponse(BaseValidatorModel):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'checkout_license' function.
class CheckoutLicenseRequest(BaseValidatorModel):
    ProductSKU: str
    CheckoutType: CheckoutTypeType
    KeyFingerprint: str
    Entitlements: List[EntitlementData]
    ClientToken: str
    Beneficiary: Optional[str] = None
    NodeId: Optional[str] = None


# This class is the output for the 'checkout_license' function.
class CheckoutLicenseResponse(BaseValidatorModel):
    CheckoutType: CheckoutTypeType
    LicenseConsumptionToken: str
    EntitlementsAllowed: List[EntitlementData]
    SignedToken: str
    NodeId: str
    IssuedAt: str
    Expiration: str
    LicenseArn: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'checkout_borrow_license' function.
class CheckoutBorrowLicenseRequest(BaseValidatorModel):
    LicenseArn: str
    Entitlements: List[EntitlementData]
    DigitalSignatureMethod: Literal['JWT_PS384']
    ClientToken: str
    NodeId: Optional[str] = None
    CheckoutMetadata: Optional[List[Metadata]] = None


# This class is the output for the 'checkout_borrow_license' function.
class CheckoutBorrowLicenseResponse(BaseValidatorModel):
    LicenseArn: str
    LicenseConsumptionToken: str
    EntitlementsAllowed: List[EntitlementData]
    NodeId: str
    SignedToken: str
    IssuedAt: str
    Expiration: str
    CheckoutMetadata: List[Metadata]
    ResponseMetadata: ResponseMetadata


class LicenseOperationFailure(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ErrorMessage: Optional[str] = None
    FailureTime: Optional[datetime] = None
    OperationName: Optional[str] = None
    ResourceOwnerId: Optional[str] = None
    OperationRequestedBy: Optional[str] = None
    MetadataList: Optional[List[Metadata]] = None


class ConsumptionConfiguration(BaseValidatorModel):
    RenewType: Optional[RenewTypeType] = None
    ProvisionalConfiguration: Optional[ProvisionalConfiguration] = None
    BorrowConfiguration: Optional[BorrowConfiguration] = None


# This class is the input for the 'create_grant_version' function.
class CreateGrantVersionRequest(BaseValidatorModel):
    ClientToken: str
    GrantArn: str
    GrantName: Optional[str] = None
    AllowedOperations: Optional[List[AllowedOperationType]] = None
    Status: Optional[GrantStatusType] = None
    StatusReason: Optional[str] = None
    SourceVersion: Optional[str] = None
    Options: Optional[Options] = None


class Grant(BaseValidatorModel):
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
    Options: Optional[Options] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


# This class is the input for the 'create_license_conversion_task_for_resource' function.
class CreateLicenseConversionTaskForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    SourceLicenseContext: LicenseConversionContext
    DestinationLicenseContext: LicenseConversionContext


# This class is the output for the 'get_license_conversion_task' function.
class GetLicenseConversionTaskResponse(BaseValidatorModel):
    LicenseConversionTaskId: str
    ResourceArn: str
    SourceLicenseContext: LicenseConversionContext
    DestinationLicenseContext: LicenseConversionContext
    StatusMessage: str
    Status: LicenseConversionTaskStatusType
    StartTime: datetime
    LicenseConversionTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadata


class LicenseConversionTask(BaseValidatorModel):
    LicenseConversionTaskId: Optional[str] = None
    ResourceArn: Optional[str] = None
    SourceLicenseContext: Optional[LicenseConversionContext] = None
    DestinationLicenseContext: Optional[LicenseConversionContext] = None
    Status: Optional[LicenseConversionTaskStatusType] = None
    StatusMessage: Optional[str] = None
    StartTime: Optional[datetime] = None
    LicenseConversionTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class LicenseUsage(BaseValidatorModel):
    EntitlementUsages: Optional[List[EntitlementUsage]] = None


# This class is the input for the 'list_distributed_grants' function.
class ListDistributedGrantsRequest(BaseValidatorModel):
    GrantArns: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_license_configurations' function.
class ListLicenseConfigurationsRequest(BaseValidatorModel):
    LicenseConfigurationArns: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'list_license_conversion_tasks' function.
class ListLicenseConversionTasksRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'list_license_manager_report_generators' function.
class ListLicenseManagerReportGeneratorsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_licenses' function.
class ListLicensesRequest(BaseValidatorModel):
    LicenseArns: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_received_grants_for_organization' function.
class ListReceivedGrantsForOrganizationRequest(BaseValidatorModel):
    LicenseArn: str
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_received_grants' function.
class ListReceivedGrantsRequest(BaseValidatorModel):
    GrantArns: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_received_licenses_for_organization' function.
class ListReceivedLicensesForOrganizationRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_received_licenses' function.
class ListReceivedLicensesRequest(BaseValidatorModel):
    LicenseArns: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tokens' function.
class ListTokensRequest(BaseValidatorModel):
    TokenIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_usage_for_license_configuration' function.
class ListUsageForLicenseConfigurationRequest(BaseValidatorModel):
    LicenseConfigurationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


class GetServiceSettingsResponse(BaseValidatorModel):
    S3BucketArn: str
    SnsTopicArn: str
    OrganizationConfiguration: OrganizationConfiguration
    EnableCrossAccountsDiscovery: bool
    LicenseManagerResourceShareArn: str
    ResponseMetadata: ResponseMetadata


class UpdateServiceSettingsRequest(BaseValidatorModel):
    S3BucketArn: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    OrganizationConfiguration: Optional[OrganizationConfiguration] = None
    EnableCrossAccountsDiscovery: Optional[bool] = None


# This class is the input for the 'list_resource_inventory' function.
class ListResourceInventoryRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[InventoryFilter]] = None


# This class is the output for the 'list_associations_for_license_configuration' function.
class ListAssociationsForLicenseConfigurationResponse(BaseValidatorModel):
    LicenseConfigurationAssociations: List[LicenseConfigurationAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_usage_for_license_configuration' function.
class ListUsageForLicenseConfigurationResponse(BaseValidatorModel):
    LicenseConfigurationUsageList: List[LicenseConfigurationUsage]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_license_specifications_for_resource' function.
class ListLicenseSpecificationsForResourceResponse(BaseValidatorModel):
    LicenseSpecifications: List[LicenseSpecification]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateLicenseSpecificationsForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    AddLicenseSpecifications: Optional[List[LicenseSpecification]] = None
    RemoveLicenseSpecifications: Optional[List[LicenseSpecification]] = None


class ListAssociationsForLicenseConfigurationRequestPaginate(BaseValidatorModel):
    LicenseConfigurationArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLicenseConfigurationsRequestPaginate(BaseValidatorModel):
    LicenseConfigurationArns: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLicenseSpecificationsForResourceRequestPaginate(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceInventoryRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[InventoryFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsageForLicenseConfigurationRequestPaginate(BaseValidatorModel):
    LicenseConfigurationArn: str
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_resource_inventory' function.
class ListResourceInventoryResponse(BaseValidatorModel):
    ResourceInventoryList: List[ResourceInventory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tokens' function.
class ListTokensResponse(BaseValidatorModel):
    Tokens: List[TokenData]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ProductInformationOutput(BaseValidatorModel):
    ResourceType: str
    ProductInformationFilterList: List[ProductInformationFilterOutput]

ProductInformationFilterUnion = Union[ProductInformationFilter, ProductInformationFilterOutput]

ReportContextUnion = Union[ReportContext, ReportContextOutput]


class ReportGenerator(BaseValidatorModel):
    ReportGeneratorName: Optional[str] = None
    ReportType: Optional[List[ReportTypeType]] = None
    ReportContext: Optional[ReportContextOutput] = None
    ReportFrequency: Optional[ReportFrequency] = None
    LicenseManagerReportGeneratorArn: Optional[str] = None
    LastRunStatus: Optional[str] = None
    LastRunFailureReason: Optional[str] = None
    LastReportGenerationTime: Optional[str] = None
    ReportCreatorAccount: Optional[str] = None
    Description: Optional[str] = None
    S3Location: Optional[S3Location] = None
    CreateTime: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_failures_for_license_configuration_operations' function.
class ListFailuresForLicenseConfigurationOperationsResponse(BaseValidatorModel):
    LicenseOperationFailureList: List[LicenseOperationFailure]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_license' function.
class CreateLicenseRequest(BaseValidatorModel):
    LicenseName: str
    ProductName: str
    ProductSKU: str
    Issuer: Issuer
    HomeRegion: str
    Validity: DatetimeRange
    Entitlements: List[Entitlement]
    Beneficiary: str
    ConsumptionConfiguration: ConsumptionConfiguration
    ClientToken: str
    LicenseMetadata: Optional[List[Metadata]] = None


# This class is the input for the 'create_license_version' function.
class CreateLicenseVersionRequest(BaseValidatorModel):
    LicenseArn: str
    LicenseName: str
    ProductName: str
    Issuer: Issuer
    HomeRegion: str
    Validity: DatetimeRange
    Entitlements: List[Entitlement]
    ConsumptionConfiguration: ConsumptionConfiguration
    Status: LicenseStatusType
    ClientToken: str
    LicenseMetadata: Optional[List[Metadata]] = None
    SourceVersion: Optional[str] = None


class GrantedLicense(BaseValidatorModel):
    LicenseArn: Optional[str] = None
    LicenseName: Optional[str] = None
    ProductName: Optional[str] = None
    ProductSKU: Optional[str] = None
    Issuer: Optional[IssuerDetails] = None
    HomeRegion: Optional[str] = None
    Status: Optional[LicenseStatusType] = None
    Validity: Optional[DatetimeRange] = None
    Beneficiary: Optional[str] = None
    Entitlements: Optional[List[Entitlement]] = None
    ConsumptionConfiguration: Optional[ConsumptionConfiguration] = None
    LicenseMetadata: Optional[List[Metadata]] = None
    CreateTime: Optional[str] = None
    Version: Optional[str] = None
    ReceivedMetadata: Optional[ReceivedMetadata] = None


class License(BaseValidatorModel):
    LicenseArn: Optional[str] = None
    LicenseName: Optional[str] = None
    ProductName: Optional[str] = None
    ProductSKU: Optional[str] = None
    Issuer: Optional[IssuerDetails] = None
    HomeRegion: Optional[str] = None
    Status: Optional[LicenseStatusType] = None
    Validity: Optional[DatetimeRange] = None
    Beneficiary: Optional[str] = None
    Entitlements: Optional[List[Entitlement]] = None
    ConsumptionConfiguration: Optional[ConsumptionConfiguration] = None
    LicenseMetadata: Optional[List[Metadata]] = None
    CreateTime: Optional[str] = None
    Version: Optional[str] = None


# This class is the output for the 'get_grant' function.
class GetGrantResponse(BaseValidatorModel):
    Grant: Grant
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_distributed_grants' function.
class ListDistributedGrantsResponse(BaseValidatorModel):
    Grants: List[Grant]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_received_grants_for_organization' function.
class ListReceivedGrantsForOrganizationResponse(BaseValidatorModel):
    Grants: List[Grant]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_received_grants' function.
class ListReceivedGrantsResponse(BaseValidatorModel):
    Grants: List[Grant]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_license_conversion_tasks' function.
class ListLicenseConversionTasksResponse(BaseValidatorModel):
    LicenseConversionTasks: List[LicenseConversionTask]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_license_usage' function.
class GetLicenseUsageResponse(BaseValidatorModel):
    LicenseUsage: LicenseUsage
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_license_configuration' function.
class GetLicenseConfigurationResponse(BaseValidatorModel):
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
    ConsumedLicenseSummaryList: List[ConsumedLicenseSummary]
    ManagedResourceSummaryList: List[ManagedResourceSummary]
    Tags: List[Tag]
    ProductInformationList: List[ProductInformationOutput]
    AutomatedDiscoveryInformation: AutomatedDiscoveryInformation
    DisassociateWhenNotFound: bool
    ResponseMetadata: ResponseMetadata


class LicenseConfiguration(BaseValidatorModel):
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
    ConsumedLicenseSummaryList: Optional[List[ConsumedLicenseSummary]] = None
    ManagedResourceSummaryList: Optional[List[ManagedResourceSummary]] = None
    ProductInformationList: Optional[List[ProductInformationOutput]] = None
    AutomatedDiscoveryInformation: Optional[AutomatedDiscoveryInformation] = None


class ProductInformation(BaseValidatorModel):
    ResourceType: str
    ProductInformationFilterList: List[ProductInformationFilterUnion]


# This class is the input for the 'create_license_manager_report_generator' function.
class CreateLicenseManagerReportGeneratorRequest(BaseValidatorModel):
    ReportGeneratorName: str
    Type: List[ReportTypeType]
    ReportContext: ReportContextUnion
    ReportFrequency: ReportFrequency
    ClientToken: str
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class UpdateLicenseManagerReportGeneratorRequest(BaseValidatorModel):
    LicenseManagerReportGeneratorArn: str
    ReportGeneratorName: str
    Type: List[ReportTypeType]
    ReportContext: ReportContextUnion
    ReportFrequency: ReportFrequency
    ClientToken: str
    Description: Optional[str] = None


# This class is the output for the 'get_license_manager_report_generator' function.
class GetLicenseManagerReportGeneratorResponse(BaseValidatorModel):
    ReportGenerator: ReportGenerator
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_license_manager_report_generators' function.
class ListLicenseManagerReportGeneratorsResponse(BaseValidatorModel):
    ReportGenerators: List[ReportGenerator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_received_licenses_for_organization' function.
class ListReceivedLicensesForOrganizationResponse(BaseValidatorModel):
    Licenses: List[GrantedLicense]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_received_licenses' function.
class ListReceivedLicensesResponse(BaseValidatorModel):
    Licenses: List[GrantedLicense]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_license' function.
class GetLicenseResponse(BaseValidatorModel):
    License: License
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_license_versions' function.
class ListLicenseVersionsResponse(BaseValidatorModel):
    Licenses: List[License]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_licenses' function.
class ListLicensesResponse(BaseValidatorModel):
    Licenses: List[License]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_license_configurations' function.
class ListLicenseConfigurationsResponse(BaseValidatorModel):
    LicenseConfigurations: List[LicenseConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

ProductInformationUnion = Union[ProductInformation, ProductInformationOutput]


# This class is the input for the 'create_license_configuration' function.
class CreateLicenseConfigurationRequest(BaseValidatorModel):
    Name: str
    LicenseCountingType: LicenseCountingTypeType
    Description: Optional[str] = None
    LicenseCount: Optional[int] = None
    LicenseCountHardLimit: Optional[bool] = None
    LicenseRules: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    DisassociateWhenNotFound: Optional[bool] = None
    ProductInformationList: Optional[List[ProductInformationUnion]] = None


class UpdateLicenseConfigurationRequest(BaseValidatorModel):
    LicenseConfigurationArn: str
    LicenseConfigurationStatus: Optional[LicenseConfigurationStatusType] = None
    LicenseRules: Optional[List[str]] = None
    LicenseCount: Optional[int] = None
    LicenseCountHardLimit: Optional[bool] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ProductInformationList: Optional[List[ProductInformationUnion]] = None
    DisassociateWhenNotFound: Optional[bool] = None