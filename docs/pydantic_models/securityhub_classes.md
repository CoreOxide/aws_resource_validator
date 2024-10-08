# Pydantic Models in securityhub_classes

# AcceptAdministratorInvitationRequestRequestTypeDef

### AdministratorId
- **Type**: <class 'str'>
- **Required**: Yes

### InvitationId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptInvitationRequestRequestTypeDef

### MasterId
- **Type**: <class 'str'>
- **Required**: Yes

### InvitationId
- **Type**: <class 'str'>
- **Required**: Yes


# AccountDetailsTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: typing.Optional[str]


# ActionExtraOutputTypeDef

### ActionType
- **Type**: typing.Optional[str]

### NetworkConnectionAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkConnectionActionTypeDef]

### AwsApiCallAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiCallActionExtraOutputTypeDef]

### DnsRequestAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.DnsRequestActionTypeDef]

### PortProbeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PortProbeActionExtraOutputTypeDef]


# ActionLocalIpDetailsTypeDef

### IpAddressV4
- **Type**: typing.Optional[str]


# ActionLocalPortDetailsTypeDef

### Port
- **Type**: typing.Optional[int]

### PortName
- **Type**: typing.Optional[str]


# ActionOutputTypeDef

### ActionType
- **Type**: typing.Optional[str]

### NetworkConnectionAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkConnectionActionTypeDef]

### AwsApiCallAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiCallActionOutputTypeDef]

### DnsRequestAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.DnsRequestActionTypeDef]

### PortProbeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PortProbeActionOutputTypeDef]


# ActionRemoteIpDetailsTypeDef

### IpAddressV4
- **Type**: typing.Optional[str]

### Organization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.IpOrganizationDetailsTypeDef]

### Country
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.CountryTypeDef]

### City
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.CityTypeDef]

### GeoLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.GeoLocationTypeDef]


# ActionRemotePortDetailsTypeDef

### Port
- **Type**: typing.Optional[int]

### PortName
- **Type**: typing.Optional[str]


# ActionTargetTypeDef

### ActionTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# ActionTypeDef

### ActionType
- **Type**: typing.Optional[str]

### NetworkConnectionAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkConnectionActionTypeDef]

### AwsApiCallAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiCallActionTypeDef]

### DnsRequestAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.DnsRequestActionTypeDef]

### PortProbeAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PortProbeActionTypeDef]


# AdjustmentTypeDef

### Metric
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]


# AdminAccountTypeDef

### AccountId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLE_IN_PROGRESS', 'ENABLED']]


# AssociatedStandardTypeDef

### StandardsId
- **Type**: typing.Optional[str]


# AssociationFiltersTypeDef

### ConfigurationPolicyId
- **Type**: typing.Optional[str]

### AssociationType
- **Type**: typing.Optional[typing.Literal['APPLIED', 'INHERITED']]

### AssociationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCESS']]


# AssociationSetDetailsTypeDef

### AssociationState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AssociationStateDetailsTypeDef]

### GatewayId
- **Type**: typing.Optional[str]

### Main
- **Type**: typing.Optional[bool]

### RouteTableAssociationId
- **Type**: typing.Optional[str]

### RouteTableId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]


# AssociationStateDetailsTypeDef

### State
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# AutomationRulesActionOutputTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['FINDING_FIELDS_UPDATE']]

### FindingFieldsUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesFindingFieldsUpdateOutputTypeDef]


# AutomationRulesActionTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['FINDING_FIELDS_UPDATE']]

### FindingFieldsUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesFindingFieldsUpdateTypeDef]


# AutomationRulesConfigTypeDef

### RuleArn
- **Type**: typing.Optional[str]

### RuleStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RuleOrder
- **Type**: typing.Optional[int]

### RuleName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IsTerminal
- **Type**: typing.Optional[bool]

### Criteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesFindingFiltersOutputTypeDef]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesActionOutputTypeDef]]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[str]


# AutomationRulesFindingFieldsUpdateOutputTypeDef

### Note
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NoteUpdateTypeDef]

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SeverityUpdateTypeDef]

### VerificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### Types
- **Type**: typing.Optional[typing.List[str]]

### UserDefinedFields
- **Type**: typing.Optional[typing.Dict[str, str]]

### Workflow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WorkflowUpdateTypeDef]

### RelatedFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFindingTypeDef]]


# AutomationRulesFindingFieldsUpdateTypeDef

### Note
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NoteUpdateTypeDef]

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SeverityUpdateTypeDef]

### VerificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### Types
- **Type**: typing.Optional[typing.Sequence[str]]

### UserDefinedFields
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Workflow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WorkflowUpdateTypeDef]

### RelatedFindings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFindingTypeDef]]


# AutomationRulesFindingFiltersOutputTypeDef

### ProductArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### AwsAccountId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Id
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### GeneratorId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Type
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FirstObservedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### LastObservedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### CreatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### UpdatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### Confidence
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### Criticality
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### Title
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Description
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### SourceUrl
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ProductName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### CompanyName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### SeverityLabel
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourcePartition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceRegion
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ResourceDetailsOther
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ComplianceStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ComplianceSecurityControlId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ComplianceAssociatedStandardsId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### VerificationState
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### WorkflowStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RecordState
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RelatedFindingsProductArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RelatedFindingsId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NoteText
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NoteUpdatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### NoteUpdatedBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### UserDefinedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ResourceApplicationArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceApplicationName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### AwsAccountName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]


# AutomationRulesFindingFiltersTypeDef

### ProductArn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### AwsAccountId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Id
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### GeneratorId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Type
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FirstObservedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### LastObservedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### CreatedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### UpdatedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### Confidence
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### Criticality
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### Title
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Description
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### SourceUrl
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ProductName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### CompanyName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### SeverityLabel
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourcePartition
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceRegion
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ResourceDetailsOther
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ComplianceStatus
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ComplianceSecurityControlId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ComplianceAssociatedStandardsId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### VerificationState
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### WorkflowStatus
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RecordState
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RelatedFindingsProductArn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RelatedFindingsId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NoteText
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NoteUpdatedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### NoteUpdatedBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### UserDefinedFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ResourceApplicationArn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceApplicationName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### AwsAccountName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]


# AutomationRulesMetadataTypeDef

### RuleArn
- **Type**: typing.Optional[str]

### RuleStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RuleOrder
- **Type**: typing.Optional[int]

### RuleName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IsTerminal
- **Type**: typing.Optional[bool]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[str]


# AvailabilityZoneTypeDef

### ZoneName
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]


# AwsAmazonMqBrokerDetailsExtraOutputTypeDef

### AuthenticationStrategy
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### BrokerArn
- **Type**: typing.Optional[str]

### BrokerName
- **Type**: typing.Optional[str]

### DeploymentMode
- **Type**: typing.Optional[str]

### EncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef]

### EngineType
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### HostInstanceType
- **Type**: typing.Optional[str]

### BrokerId
- **Type**: typing.Optional[str]

### LdapServerMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerLdapServerMetadataDetailsExtraOutputTypeDef]

### Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerLogsDetailsTypeDef]

### MaintenanceWindowStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### StorageType
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### Users
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerUsersDetailsTypeDef]]


# AwsAmazonMqBrokerDetailsOutputTypeDef

### AuthenticationStrategy
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### BrokerArn
- **Type**: typing.Optional[str]

### BrokerName
- **Type**: typing.Optional[str]

### DeploymentMode
- **Type**: typing.Optional[str]

### EncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef]

### EngineType
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### HostInstanceType
- **Type**: typing.Optional[str]

### BrokerId
- **Type**: typing.Optional[str]

### LdapServerMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef]

### Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerLogsDetailsTypeDef]

### MaintenanceWindowStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### StorageType
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### Users
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerUsersDetailsTypeDef]]


# AwsAmazonMqBrokerDetailsTypeDef

### AuthenticationStrategy
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### BrokerArn
- **Type**: typing.Optional[str]

### BrokerName
- **Type**: typing.Optional[str]

### DeploymentMode
- **Type**: typing.Optional[str]

### EncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef]

### EngineType
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### HostInstanceType
- **Type**: typing.Optional[str]

### BrokerId
- **Type**: typing.Optional[str]

### LdapServerMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef]

### Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerLogsDetailsTypeDef]

### MaintenanceWindowStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### StorageType
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Users
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerUsersDetailsTypeDef]]


# AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef

### KmsKeyId
- **Type**: typing.Optional[str]

### UseAwsOwnedKey
- **Type**: typing.Optional[bool]


# AwsAmazonMqBrokerLdapServerMetadataDetailsExtraOutputTypeDef

### Hosts
- **Type**: typing.Optional[typing.List[str]]

### RoleBase
- **Type**: typing.Optional[str]

### RoleName
- **Type**: typing.Optional[str]

### RoleSearchMatching
- **Type**: typing.Optional[str]

### RoleSearchSubtree
- **Type**: typing.Optional[bool]

### ServiceAccountUsername
- **Type**: typing.Optional[str]

### UserBase
- **Type**: typing.Optional[str]

### UserRoleName
- **Type**: typing.Optional[str]

### UserSearchMatching
- **Type**: typing.Optional[str]

### UserSearchSubtree
- **Type**: typing.Optional[bool]


# AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef

### Hosts
- **Type**: typing.Optional[typing.List[str]]

### RoleBase
- **Type**: typing.Optional[str]

### RoleName
- **Type**: typing.Optional[str]

### RoleSearchMatching
- **Type**: typing.Optional[str]

### RoleSearchSubtree
- **Type**: typing.Optional[bool]

### ServiceAccountUsername
- **Type**: typing.Optional[str]

### UserBase
- **Type**: typing.Optional[str]

### UserRoleName
- **Type**: typing.Optional[str]

### UserSearchMatching
- **Type**: typing.Optional[str]

### UserSearchSubtree
- **Type**: typing.Optional[bool]


# AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef

### Hosts
- **Type**: typing.Optional[typing.Sequence[str]]

### RoleBase
- **Type**: typing.Optional[str]

### RoleName
- **Type**: typing.Optional[str]

### RoleSearchMatching
- **Type**: typing.Optional[str]

### RoleSearchSubtree
- **Type**: typing.Optional[bool]

### ServiceAccountUsername
- **Type**: typing.Optional[str]

### UserBase
- **Type**: typing.Optional[str]

### UserRoleName
- **Type**: typing.Optional[str]

### UserSearchMatching
- **Type**: typing.Optional[str]

### UserSearchSubtree
- **Type**: typing.Optional[bool]


# AwsAmazonMqBrokerLogsDetailsTypeDef

### Audit
- **Type**: typing.Optional[bool]

### General
- **Type**: typing.Optional[bool]

### AuditLogGroup
- **Type**: typing.Optional[str]

### GeneralLogGroup
- **Type**: typing.Optional[str]

### Pending
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerLogsPendingDetailsTypeDef]


# AwsAmazonMqBrokerLogsPendingDetailsTypeDef

### Audit
- **Type**: typing.Optional[bool]

### General
- **Type**: typing.Optional[bool]


# AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef

### DayOfWeek
- **Type**: typing.Optional[str]

### TimeOfDay
- **Type**: typing.Optional[str]

### TimeZone
- **Type**: typing.Optional[str]


# AwsAmazonMqBrokerUsersDetailsTypeDef

### PendingChange
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# AwsApiCallActionDomainDetailsTypeDef

### Domain
- **Type**: typing.Optional[str]


# AwsApiCallActionExtraOutputTypeDef

### Api
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### CallerType
- **Type**: typing.Optional[str]

### RemoteIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionRemoteIpDetailsTypeDef]

### DomainDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiCallActionDomainDetailsTypeDef]

### AffectedResources
- **Type**: typing.Optional[typing.Dict[str, str]]

### FirstSeen
- **Type**: typing.Optional[str]

### LastSeen
- **Type**: typing.Optional[str]


# AwsApiCallActionOutputTypeDef

### Api
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### CallerType
- **Type**: typing.Optional[str]

### RemoteIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionRemoteIpDetailsTypeDef]

### DomainDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiCallActionDomainDetailsTypeDef]

### AffectedResources
- **Type**: typing.Optional[typing.Dict[str, str]]

### FirstSeen
- **Type**: typing.Optional[str]

### LastSeen
- **Type**: typing.Optional[str]


# AwsApiCallActionTypeDef

### Api
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### CallerType
- **Type**: typing.Optional[str]

### RemoteIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionRemoteIpDetailsTypeDef]

### DomainDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiCallActionDomainDetailsTypeDef]

### AffectedResources
- **Type**: typing.Optional[typing.Mapping[str, str]]

### FirstSeen
- **Type**: typing.Optional[str]

### LastSeen
- **Type**: typing.Optional[str]


# AwsApiGatewayAccessLogSettingsTypeDef

### Format
- **Type**: typing.Optional[str]

### DestinationArn
- **Type**: typing.Optional[str]


# AwsApiGatewayCanarySettingsExtraOutputTypeDef

### PercentTraffic
- **Type**: typing.Optional[float]

### DeploymentId
- **Type**: typing.Optional[str]

### StageVariableOverrides
- **Type**: typing.Optional[typing.Dict[str, str]]

### UseStageCache
- **Type**: typing.Optional[bool]


# AwsApiGatewayCanarySettingsOutputTypeDef

### PercentTraffic
- **Type**: typing.Optional[float]

### DeploymentId
- **Type**: typing.Optional[str]

### StageVariableOverrides
- **Type**: typing.Optional[typing.Dict[str, str]]

### UseStageCache
- **Type**: typing.Optional[bool]


# AwsApiGatewayCanarySettingsTypeDef

### PercentTraffic
- **Type**: typing.Optional[float]

### DeploymentId
- **Type**: typing.Optional[str]

### StageVariableOverrides
- **Type**: typing.Optional[typing.Mapping[str, str]]

### UseStageCache
- **Type**: typing.Optional[bool]


# AwsApiGatewayEndpointConfigurationExtraOutputTypeDef

### Types
- **Type**: typing.Optional[typing.List[str]]


# AwsApiGatewayEndpointConfigurationOutputTypeDef

### Types
- **Type**: typing.Optional[typing.List[str]]


# AwsApiGatewayEndpointConfigurationTypeDef

### Types
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsApiGatewayMethodSettingsTypeDef

### MetricsEnabled
- **Type**: typing.Optional[bool]

### LoggingLevel
- **Type**: typing.Optional[str]

### DataTraceEnabled
- **Type**: typing.Optional[bool]

### ThrottlingBurstLimit
- **Type**: typing.Optional[int]

### ThrottlingRateLimit
- **Type**: typing.Optional[float]

### CachingEnabled
- **Type**: typing.Optional[bool]

### CacheTtlInSeconds
- **Type**: typing.Optional[int]

### CacheDataEncrypted
- **Type**: typing.Optional[bool]

### RequireAuthorizationForCacheControl
- **Type**: typing.Optional[bool]

### UnauthorizedCacheControlHeaderStrategy
- **Type**: typing.Optional[str]

### HttpMethod
- **Type**: typing.Optional[str]

### ResourcePath
- **Type**: typing.Optional[str]


# AwsApiGatewayRestApiDetailsExtraOutputTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### BinaryMediaTypes
- **Type**: typing.Optional[typing.List[str]]

### MinimumCompressionSize
- **Type**: typing.Optional[int]

### ApiKeySource
- **Type**: typing.Optional[str]

### EndpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayEndpointConfigurationExtraOutputTypeDef]


# AwsApiGatewayRestApiDetailsOutputTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### BinaryMediaTypes
- **Type**: typing.Optional[typing.List[str]]

### MinimumCompressionSize
- **Type**: typing.Optional[int]

### ApiKeySource
- **Type**: typing.Optional[str]

### EndpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayEndpointConfigurationOutputTypeDef]


# AwsApiGatewayRestApiDetailsTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### BinaryMediaTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### MinimumCompressionSize
- **Type**: typing.Optional[int]

### ApiKeySource
- **Type**: typing.Optional[str]

### EndpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayEndpointConfigurationTypeDef]


# AwsApiGatewayStageDetailsExtraOutputTypeDef

### DeploymentId
- **Type**: typing.Optional[str]

### ClientCertificateId
- **Type**: typing.Optional[str]

### StageName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CacheClusterEnabled
- **Type**: typing.Optional[bool]

### CacheClusterSize
- **Type**: typing.Optional[str]

### CacheClusterStatus
- **Type**: typing.Optional[str]

### MethodSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayMethodSettingsTypeDef]]

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]

### DocumentationVersion
- **Type**: typing.Optional[str]

### AccessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayAccessLogSettingsTypeDef]

### CanarySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayCanarySettingsExtraOutputTypeDef]

### TracingEnabled
- **Type**: typing.Optional[bool]

### CreatedDate
- **Type**: typing.Optional[str]

### LastUpdatedDate
- **Type**: typing.Optional[str]

### WebAclArn
- **Type**: typing.Optional[str]


# AwsApiGatewayStageDetailsOutputTypeDef

### DeploymentId
- **Type**: typing.Optional[str]

### ClientCertificateId
- **Type**: typing.Optional[str]

### StageName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CacheClusterEnabled
- **Type**: typing.Optional[bool]

### CacheClusterSize
- **Type**: typing.Optional[str]

### CacheClusterStatus
- **Type**: typing.Optional[str]

### MethodSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayMethodSettingsTypeDef]]

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]

### DocumentationVersion
- **Type**: typing.Optional[str]

### AccessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayAccessLogSettingsTypeDef]

### CanarySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayCanarySettingsOutputTypeDef]

### TracingEnabled
- **Type**: typing.Optional[bool]

### CreatedDate
- **Type**: typing.Optional[str]

### LastUpdatedDate
- **Type**: typing.Optional[str]

### WebAclArn
- **Type**: typing.Optional[str]


# AwsApiGatewayStageDetailsTypeDef

### DeploymentId
- **Type**: typing.Optional[str]

### ClientCertificateId
- **Type**: typing.Optional[str]

### StageName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CacheClusterEnabled
- **Type**: typing.Optional[bool]

### CacheClusterSize
- **Type**: typing.Optional[str]

### CacheClusterStatus
- **Type**: typing.Optional[str]

### MethodSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayMethodSettingsTypeDef]]

### Variables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DocumentationVersion
- **Type**: typing.Optional[str]

### AccessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayAccessLogSettingsTypeDef]

### CanarySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayCanarySettingsTypeDef]

### TracingEnabled
- **Type**: typing.Optional[bool]

### CreatedDate
- **Type**: typing.Optional[str]

### LastUpdatedDate
- **Type**: typing.Optional[str]

### WebAclArn
- **Type**: typing.Optional[str]


# AwsApiGatewayV2ApiDetailsExtraOutputTypeDef

### ApiEndpoint
- **Type**: typing.Optional[str]

### ApiId
- **Type**: typing.Optional[str]

### ApiKeySelectionExpression
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ProtocolType
- **Type**: typing.Optional[str]

### RouteSelectionExpression
- **Type**: typing.Optional[str]

### CorsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCorsConfigurationExtraOutputTypeDef]


# AwsApiGatewayV2ApiDetailsOutputTypeDef

### ApiEndpoint
- **Type**: typing.Optional[str]

### ApiId
- **Type**: typing.Optional[str]

### ApiKeySelectionExpression
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ProtocolType
- **Type**: typing.Optional[str]

### RouteSelectionExpression
- **Type**: typing.Optional[str]

### CorsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCorsConfigurationOutputTypeDef]


# AwsApiGatewayV2ApiDetailsTypeDef

### ApiEndpoint
- **Type**: typing.Optional[str]

### ApiId
- **Type**: typing.Optional[str]

### ApiKeySelectionExpression
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ProtocolType
- **Type**: typing.Optional[str]

### RouteSelectionExpression
- **Type**: typing.Optional[str]

### CorsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCorsConfigurationTypeDef]


# AwsApiGatewayV2RouteSettingsTypeDef

### DetailedMetricsEnabled
- **Type**: typing.Optional[bool]

### LoggingLevel
- **Type**: typing.Optional[str]

### DataTraceEnabled
- **Type**: typing.Optional[bool]

### ThrottlingBurstLimit
- **Type**: typing.Optional[int]

### ThrottlingRateLimit
- **Type**: typing.Optional[float]


# AwsApiGatewayV2StageDetailsExtraOutputTypeDef

### ClientCertificateId
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefaultRouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2RouteSettingsTypeDef]

### DeploymentId
- **Type**: typing.Optional[str]

### LastUpdatedDate
- **Type**: typing.Optional[str]

### RouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2RouteSettingsTypeDef]

### StageName
- **Type**: typing.Optional[str]

### StageVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### AccessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayAccessLogSettingsTypeDef]

### AutoDeploy
- **Type**: typing.Optional[bool]

### LastDeploymentStatusMessage
- **Type**: typing.Optional[str]

### ApiGatewayManaged
- **Type**: typing.Optional[bool]


# AwsApiGatewayV2StageDetailsOutputTypeDef

### ClientCertificateId
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefaultRouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2RouteSettingsTypeDef]

### DeploymentId
- **Type**: typing.Optional[str]

### LastUpdatedDate
- **Type**: typing.Optional[str]

### RouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2RouteSettingsTypeDef]

### StageName
- **Type**: typing.Optional[str]

### StageVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### AccessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayAccessLogSettingsTypeDef]

### AutoDeploy
- **Type**: typing.Optional[bool]

### LastDeploymentStatusMessage
- **Type**: typing.Optional[str]

### ApiGatewayManaged
- **Type**: typing.Optional[bool]


# AwsApiGatewayV2StageDetailsTypeDef

### ClientCertificateId
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefaultRouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2RouteSettingsTypeDef]

### DeploymentId
- **Type**: typing.Optional[str]

### LastUpdatedDate
- **Type**: typing.Optional[str]

### RouteSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2RouteSettingsTypeDef]

### StageName
- **Type**: typing.Optional[str]

### StageVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AccessLogSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayAccessLogSettingsTypeDef]

### AutoDeploy
- **Type**: typing.Optional[bool]

### LastDeploymentStatusMessage
- **Type**: typing.Optional[str]

### ApiGatewayManaged
- **Type**: typing.Optional[bool]


# AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef

### AuthenticationType
- **Type**: typing.Optional[str]

### LambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef]

### OpenIdConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef]

### UserPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef]


# AwsAppSyncGraphQlApiDetailsExtraOutputTypeDef

### ApiId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### OpenIdConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef]

### Name
- **Type**: typing.Optional[str]

### LambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef]

### XrayEnabled
- **Type**: typing.Optional[bool]

### Arn
- **Type**: typing.Optional[str]

### UserPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef]

### AuthenticationType
- **Type**: typing.Optional[str]

### LogConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiLogConfigDetailsTypeDef]

### AdditionalAuthenticationProviders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]]

### WafWebAclArn
- **Type**: typing.Optional[str]


# AwsAppSyncGraphQlApiDetailsOutputTypeDef

### ApiId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### OpenIdConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef]

### Name
- **Type**: typing.Optional[str]

### LambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef]

### XrayEnabled
- **Type**: typing.Optional[bool]

### Arn
- **Type**: typing.Optional[str]

### UserPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef]

### AuthenticationType
- **Type**: typing.Optional[str]

### LogConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiLogConfigDetailsTypeDef]

### AdditionalAuthenticationProviders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]]

### WafWebAclArn
- **Type**: typing.Optional[str]


# AwsAppSyncGraphQlApiDetailsTypeDef

### ApiId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### OpenIdConnectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef]

### Name
- **Type**: typing.Optional[str]

### LambdaAuthorizerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef]

### XrayEnabled
- **Type**: typing.Optional[bool]

### Arn
- **Type**: typing.Optional[str]

### UserPoolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef]

### AuthenticationType
- **Type**: typing.Optional[str]

### LogConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiLogConfigDetailsTypeDef]

### AdditionalAuthenticationProviders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]]

### WafWebAclArn
- **Type**: typing.Optional[str]


# AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef

### AuthorizerResultTtlInSeconds
- **Type**: typing.Optional[int]

### AuthorizerUri
- **Type**: typing.Optional[str]

### IdentityValidationExpression
- **Type**: typing.Optional[str]


# AwsAppSyncGraphQlApiLogConfigDetailsTypeDef

### CloudWatchLogsRoleArn
- **Type**: typing.Optional[str]

### ExcludeVerboseContent
- **Type**: typing.Optional[bool]

### FieldLogLevel
- **Type**: typing.Optional[str]


# AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef

### AuthTtL
- **Type**: typing.Optional[int]

### ClientId
- **Type**: typing.Optional[str]

### IatTtL
- **Type**: typing.Optional[int]

### Issuer
- **Type**: typing.Optional[str]


# AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef

### AppIdClientRegex
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### DefaultAction
- **Type**: typing.Optional[str]

### UserPoolId
- **Type**: typing.Optional[str]


# AwsAthenaWorkGroupConfigurationDetailsTypeDef

### ResultConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef]


# AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef]


# AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef

### EncryptionOption
- **Type**: typing.Optional[str]

### KmsKey
- **Type**: typing.Optional[str]


# AwsAthenaWorkGroupDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAthenaWorkGroupConfigurationDetailsTypeDef]


# AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef

### Value
- **Type**: typing.Optional[str]


# AwsAutoScalingAutoScalingGroupDetailsExtraOutputTypeDef

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### LoadBalancerNames
- **Type**: typing.Optional[typing.List[str]]

### HealthCheckType
- **Type**: typing.Optional[str]

### HealthCheckGracePeriod
- **Type**: typing.Optional[int]

### CreatedTime
- **Type**: typing.Optional[str]

### MixedInstancesPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsExtraOutputTypeDef]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef]

### CapacityRebalance
- **Type**: typing.Optional[bool]


# AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### LoadBalancerNames
- **Type**: typing.Optional[typing.List[str]]

### HealthCheckType
- **Type**: typing.Optional[str]

### HealthCheckGracePeriod
- **Type**: typing.Optional[int]

### CreatedTime
- **Type**: typing.Optional[str]

### MixedInstancesPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef]

### CapacityRebalance
- **Type**: typing.Optional[bool]


# AwsAutoScalingAutoScalingGroupDetailsTypeDef

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### LoadBalancerNames
- **Type**: typing.Optional[typing.Sequence[str]]

### HealthCheckType
- **Type**: typing.Optional[str]

### HealthCheckGracePeriod
- **Type**: typing.Optional[int]

### CreatedTime
- **Type**: typing.Optional[str]

### MixedInstancesPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef]

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef]

### CapacityRebalance
- **Type**: typing.Optional[bool]


# AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef

### LaunchTemplateId
- **Type**: typing.Optional[str]

### LaunchTemplateName
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsExtraOutputTypeDef

### InstancesDistribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsExtraOutputTypeDef]


# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef

### InstancesDistribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef]


# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef

### InstancesDistribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef]

### LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef]


# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef

### OnDemandAllocationStrategy
- **Type**: typing.Optional[str]

### OnDemandBaseCapacity
- **Type**: typing.Optional[int]

### OnDemandPercentageAboveBaseCapacity
- **Type**: typing.Optional[int]

### SpotAllocationStrategy
- **Type**: typing.Optional[str]

### SpotInstancePools
- **Type**: typing.Optional[int]

### SpotMaxPrice
- **Type**: typing.Optional[str]


# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsExtraOutputTypeDef

### LaunchTemplateSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef]

### Overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef]]


# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef

### LaunchTemplateSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef]

### Overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef]]


# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef

### LaunchTemplateSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef]

### Overrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef]]


# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef

### LaunchTemplateId
- **Type**: typing.Optional[str]

### LaunchTemplateName
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef

### InstanceType
- **Type**: typing.Optional[str]

### WeightedCapacity
- **Type**: typing.Optional[str]


# AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef

### DeviceName
- **Type**: typing.Optional[str]

### Ebs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef]

### NoDevice
- **Type**: typing.Optional[bool]

### VirtualName
- **Type**: typing.Optional[str]


# AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef

### DeleteOnTermination
- **Type**: typing.Optional[bool]

### Encrypted
- **Type**: typing.Optional[bool]

### Iops
- **Type**: typing.Optional[int]

### SnapshotId
- **Type**: typing.Optional[str]

### VolumeSize
- **Type**: typing.Optional[int]

### VolumeType
- **Type**: typing.Optional[str]


# AwsAutoScalingLaunchConfigurationDetailsExtraOutputTypeDef

### AssociatePublicIpAddress
- **Type**: typing.Optional[bool]

### BlockDeviceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]]

### ClassicLinkVpcId
- **Type**: typing.Optional[str]

### ClassicLinkVpcSecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### CreatedTime
- **Type**: typing.Optional[str]

### EbsOptimized
- **Type**: typing.Optional[bool]

### IamInstanceProfile
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### InstanceMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef]

### InstanceType
- **Type**: typing.Optional[str]

### KernelId
- **Type**: typing.Optional[str]

### KeyName
- **Type**: typing.Optional[str]

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### PlacementTenancy
- **Type**: typing.Optional[str]

### RamdiskId
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### SpotPrice
- **Type**: typing.Optional[str]

### UserData
- **Type**: typing.Optional[str]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef]


# AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef

### AssociatePublicIpAddress
- **Type**: typing.Optional[bool]

### BlockDeviceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]]

### ClassicLinkVpcId
- **Type**: typing.Optional[str]

### ClassicLinkVpcSecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### CreatedTime
- **Type**: typing.Optional[str]

### EbsOptimized
- **Type**: typing.Optional[bool]

### IamInstanceProfile
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### InstanceMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef]

### InstanceType
- **Type**: typing.Optional[str]

### KernelId
- **Type**: typing.Optional[str]

### KeyName
- **Type**: typing.Optional[str]

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### PlacementTenancy
- **Type**: typing.Optional[str]

### RamdiskId
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### SpotPrice
- **Type**: typing.Optional[str]

### UserData
- **Type**: typing.Optional[str]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef]


# AwsAutoScalingLaunchConfigurationDetailsTypeDef

### AssociatePublicIpAddress
- **Type**: typing.Optional[bool]

### BlockDeviceMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]]

### ClassicLinkVpcId
- **Type**: typing.Optional[str]

### ClassicLinkVpcSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### CreatedTime
- **Type**: typing.Optional[str]

### EbsOptimized
- **Type**: typing.Optional[bool]

### IamInstanceProfile
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### InstanceMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef]

### InstanceType
- **Type**: typing.Optional[str]

### KernelId
- **Type**: typing.Optional[str]

### KeyName
- **Type**: typing.Optional[str]

### LaunchConfigurationName
- **Type**: typing.Optional[str]

### PlacementTenancy
- **Type**: typing.Optional[str]

### RamdiskId
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### SpotPrice
- **Type**: typing.Optional[str]

### UserData
- **Type**: typing.Optional[str]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef]


# AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef

### HttpEndpoint
- **Type**: typing.Optional[str]

### HttpPutResponseHopLimit
- **Type**: typing.Optional[int]

### HttpTokens
- **Type**: typing.Optional[str]


# AwsBackupBackupPlanAdvancedBackupSettingsDetailsExtraOutputTypeDef

### BackupOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResourceType
- **Type**: typing.Optional[str]


# AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef

### BackupOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### ResourceType
- **Type**: typing.Optional[str]


# AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef

### BackupOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ResourceType
- **Type**: typing.Optional[str]


# AwsBackupBackupPlanBackupPlanDetailsExtraOutputTypeDef

### BackupPlanName
- **Type**: typing.Optional[str]

### AdvancedBackupSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanAdvancedBackupSettingsDetailsExtraOutputTypeDef]]

### BackupPlanRule
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanRuleDetailsExtraOutputTypeDef]]


# AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef

### BackupPlanName
- **Type**: typing.Optional[str]

### AdvancedBackupSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef]]

### BackupPlanRule
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanRuleDetailsOutputTypeDef]]


# AwsBackupBackupPlanBackupPlanDetailsTypeDef

### BackupPlanName
- **Type**: typing.Optional[str]

### AdvancedBackupSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef]]

### BackupPlanRule
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanRuleDetailsTypeDef]]


# AwsBackupBackupPlanDetailsExtraOutputTypeDef

### BackupPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanBackupPlanDetailsExtraOutputTypeDef]

### BackupPlanArn
- **Type**: typing.Optional[str]

### BackupPlanId
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]


# AwsBackupBackupPlanDetailsOutputTypeDef

### BackupPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef]

### BackupPlanArn
- **Type**: typing.Optional[str]

### BackupPlanId
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]


# AwsBackupBackupPlanDetailsTypeDef

### BackupPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanBackupPlanDetailsTypeDef]

### BackupPlanArn
- **Type**: typing.Optional[str]

### BackupPlanId
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]


# AwsBackupBackupPlanLifecycleDetailsTypeDef

### DeleteAfterDays
- **Type**: typing.Optional[int]

### MoveToColdStorageAfterDays
- **Type**: typing.Optional[int]


# AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef

### DestinationBackupVaultArn
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanLifecycleDetailsTypeDef]


# AwsBackupBackupPlanRuleDetailsExtraOutputTypeDef

### TargetBackupVault
- **Type**: typing.Optional[str]

### StartWindowMinutes
- **Type**: typing.Optional[int]

### ScheduleExpression
- **Type**: typing.Optional[str]

### RuleName
- **Type**: typing.Optional[str]

### RuleId
- **Type**: typing.Optional[str]

### EnableContinuousBackup
- **Type**: typing.Optional[bool]

### CompletionWindowMinutes
- **Type**: typing.Optional[int]

### CopyActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]]

### Lifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanLifecycleDetailsTypeDef]


# AwsBackupBackupPlanRuleDetailsOutputTypeDef

### TargetBackupVault
- **Type**: typing.Optional[str]

### StartWindowMinutes
- **Type**: typing.Optional[int]

### ScheduleExpression
- **Type**: typing.Optional[str]

### RuleName
- **Type**: typing.Optional[str]

### RuleId
- **Type**: typing.Optional[str]

### EnableContinuousBackup
- **Type**: typing.Optional[bool]

### CompletionWindowMinutes
- **Type**: typing.Optional[int]

### CopyActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]]

### Lifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanLifecycleDetailsTypeDef]


# AwsBackupBackupPlanRuleDetailsTypeDef

### TargetBackupVault
- **Type**: typing.Optional[str]

### StartWindowMinutes
- **Type**: typing.Optional[int]

### ScheduleExpression
- **Type**: typing.Optional[str]

### RuleName
- **Type**: typing.Optional[str]

### RuleId
- **Type**: typing.Optional[str]

### EnableContinuousBackup
- **Type**: typing.Optional[bool]

### CompletionWindowMinutes
- **Type**: typing.Optional[int]

### CopyActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]]

### Lifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanLifecycleDetailsTypeDef]


# AwsBackupBackupVaultDetailsExtraOutputTypeDef

### BackupVaultArn
- **Type**: typing.Optional[str]

### BackupVaultName
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### Notifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupVaultNotificationsDetailsExtraOutputTypeDef]

### AccessPolicy
- **Type**: typing.Optional[str]


# AwsBackupBackupVaultDetailsOutputTypeDef

### BackupVaultArn
- **Type**: typing.Optional[str]

### BackupVaultName
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### Notifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupVaultNotificationsDetailsOutputTypeDef]

### AccessPolicy
- **Type**: typing.Optional[str]


# AwsBackupBackupVaultDetailsTypeDef

### BackupVaultArn
- **Type**: typing.Optional[str]

### BackupVaultName
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### Notifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupVaultNotificationsDetailsTypeDef]

### AccessPolicy
- **Type**: typing.Optional[str]


# AwsBackupBackupVaultNotificationsDetailsExtraOutputTypeDef

### BackupVaultEvents
- **Type**: typing.Optional[typing.List[str]]

### SnsTopicArn
- **Type**: typing.Optional[str]


# AwsBackupBackupVaultNotificationsDetailsOutputTypeDef

### BackupVaultEvents
- **Type**: typing.Optional[typing.List[str]]

### SnsTopicArn
- **Type**: typing.Optional[str]


# AwsBackupBackupVaultNotificationsDetailsTypeDef

### BackupVaultEvents
- **Type**: typing.Optional[typing.Sequence[str]]

### SnsTopicArn
- **Type**: typing.Optional[str]


# AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef

### DeleteAt
- **Type**: typing.Optional[str]

### MoveToColdStorageAt
- **Type**: typing.Optional[str]


# AwsBackupRecoveryPointCreatedByDetailsTypeDef

### BackupPlanArn
- **Type**: typing.Optional[str]

### BackupPlanId
- **Type**: typing.Optional[str]

### BackupPlanVersion
- **Type**: typing.Optional[str]

### BackupRuleId
- **Type**: typing.Optional[str]


# AwsBackupRecoveryPointDetailsTypeDef

### BackupSizeInBytes
- **Type**: typing.Optional[int]

### BackupVaultArn
- **Type**: typing.Optional[str]

### BackupVaultName
- **Type**: typing.Optional[str]

### CalculatedLifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef]

### CompletionDate
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupRecoveryPointCreatedByDetailsTypeDef]

### CreationDate
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]

### IsEncrypted
- **Type**: typing.Optional[bool]

### LastRestoreTime
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupRecoveryPointLifecycleDetailsTypeDef]

### RecoveryPointArn
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### SourceBackupVaultArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]

### StorageClass
- **Type**: typing.Optional[str]


# AwsBackupRecoveryPointLifecycleDetailsTypeDef

### DeleteAfterDays
- **Type**: typing.Optional[int]

### MoveToColdStorageAfterDays
- **Type**: typing.Optional[int]


# AwsCertificateManagerCertificateDetailsExtraOutputTypeDef

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### DomainValidationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateDomainValidationOptionExtraOutputTypeDef]]

### ExtendedKeyUsages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]]

### FailureReason
- **Type**: typing.Optional[str]

### ImportedAt
- **Type**: typing.Optional[str]

### InUseBy
- **Type**: typing.Optional[typing.List[str]]

### IssuedAt
- **Type**: typing.Optional[str]

### Issuer
- **Type**: typing.Optional[str]

### KeyAlgorithm
- **Type**: typing.Optional[str]

### KeyUsages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateKeyUsageTypeDef]]

### NotAfter
- **Type**: typing.Optional[str]

### NotBefore
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateOptionsTypeDef]

### RenewalEligibility
- **Type**: typing.Optional[str]

### RenewalSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateRenewalSummaryExtraOutputTypeDef]

### Serial
- **Type**: typing.Optional[str]

### SignatureAlgorithm
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### SubjectAlternativeNames
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateDetailsOutputTypeDef

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### DomainValidationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef]]

### ExtendedKeyUsages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]]

### FailureReason
- **Type**: typing.Optional[str]

### ImportedAt
- **Type**: typing.Optional[str]

### InUseBy
- **Type**: typing.Optional[typing.List[str]]

### IssuedAt
- **Type**: typing.Optional[str]

### Issuer
- **Type**: typing.Optional[str]

### KeyAlgorithm
- **Type**: typing.Optional[str]

### KeyUsages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateKeyUsageTypeDef]]

### NotAfter
- **Type**: typing.Optional[str]

### NotBefore
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateOptionsTypeDef]

### RenewalEligibility
- **Type**: typing.Optional[str]

### RenewalSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef]

### Serial
- **Type**: typing.Optional[str]

### SignatureAlgorithm
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### SubjectAlternativeNames
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateDetailsTypeDef

### CertificateAuthorityArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### DomainValidationOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateDomainValidationOptionTypeDef]]

### ExtendedKeyUsages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]]

### FailureReason
- **Type**: typing.Optional[str]

### ImportedAt
- **Type**: typing.Optional[str]

### InUseBy
- **Type**: typing.Optional[typing.Sequence[str]]

### IssuedAt
- **Type**: typing.Optional[str]

### Issuer
- **Type**: typing.Optional[str]

### KeyAlgorithm
- **Type**: typing.Optional[str]

### KeyUsages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateKeyUsageTypeDef]]

### NotAfter
- **Type**: typing.Optional[str]

### NotBefore
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateOptionsTypeDef]

### RenewalEligibility
- **Type**: typing.Optional[str]

### RenewalSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateRenewalSummaryTypeDef]

### Serial
- **Type**: typing.Optional[str]

### SignatureAlgorithm
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### SubjectAlternativeNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Type
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateDomainValidationOptionExtraOutputTypeDef

### DomainName
- **Type**: typing.Optional[str]

### ResourceRecord
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateResourceRecordTypeDef]

### ValidationDomain
- **Type**: typing.Optional[str]

### ValidationEmails
- **Type**: typing.Optional[typing.List[str]]

### ValidationMethod
- **Type**: typing.Optional[str]

### ValidationStatus
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef

### DomainName
- **Type**: typing.Optional[str]

### ResourceRecord
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateResourceRecordTypeDef]

### ValidationDomain
- **Type**: typing.Optional[str]

### ValidationEmails
- **Type**: typing.Optional[typing.List[str]]

### ValidationMethod
- **Type**: typing.Optional[str]

### ValidationStatus
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateDomainValidationOptionTypeDef

### DomainName
- **Type**: typing.Optional[str]

### ResourceRecord
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateResourceRecordTypeDef]

### ValidationDomain
- **Type**: typing.Optional[str]

### ValidationEmails
- **Type**: typing.Optional[typing.Sequence[str]]

### ValidationMethod
- **Type**: typing.Optional[str]

### ValidationStatus
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateExtendedKeyUsageTypeDef

### Name
- **Type**: typing.Optional[str]

### OId
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateKeyUsageTypeDef

### Name
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateOptionsTypeDef

### CertificateTransparencyLoggingPreference
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateRenewalSummaryExtraOutputTypeDef

### DomainValidationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateDomainValidationOptionExtraOutputTypeDef]]

### RenewalStatus
- **Type**: typing.Optional[str]

### RenewalStatusReason
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef

### DomainValidationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef]]

### RenewalStatus
- **Type**: typing.Optional[str]

### RenewalStatusReason
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateRenewalSummaryTypeDef

### DomainValidationOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateDomainValidationOptionTypeDef]]

### RenewalStatus
- **Type**: typing.Optional[str]

### RenewalStatusReason
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[str]


# AwsCertificateManagerCertificateResourceRecordTypeDef

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsCloudFormationStackDetailsExtraOutputTypeDef

### Capabilities
- **Type**: typing.Optional[typing.List[str]]

### CreationTime
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DisableRollback
- **Type**: typing.Optional[bool]

### DriftInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFormationStackDriftInformationDetailsTypeDef]

### EnableTerminationProtection
- **Type**: typing.Optional[bool]

### LastUpdatedTime
- **Type**: typing.Optional[str]

### NotificationArns
- **Type**: typing.Optional[typing.List[str]]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFormationStackOutputsDetailsTypeDef]]

### RoleArn
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### StackName
- **Type**: typing.Optional[str]

### StackStatus
- **Type**: typing.Optional[str]

### StackStatusReason
- **Type**: typing.Optional[str]

### TimeoutInMinutes
- **Type**: typing.Optional[int]


# AwsCloudFormationStackDetailsOutputTypeDef

### Capabilities
- **Type**: typing.Optional[typing.List[str]]

### CreationTime
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DisableRollback
- **Type**: typing.Optional[bool]

### DriftInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFormationStackDriftInformationDetailsTypeDef]

### EnableTerminationProtection
- **Type**: typing.Optional[bool]

### LastUpdatedTime
- **Type**: typing.Optional[str]

### NotificationArns
- **Type**: typing.Optional[typing.List[str]]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFormationStackOutputsDetailsTypeDef]]

### RoleArn
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### StackName
- **Type**: typing.Optional[str]

### StackStatus
- **Type**: typing.Optional[str]

### StackStatusReason
- **Type**: typing.Optional[str]

### TimeoutInMinutes
- **Type**: typing.Optional[int]


# AwsCloudFormationStackDetailsTypeDef

### Capabilities
- **Type**: typing.Optional[typing.Sequence[str]]

### CreationTime
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DisableRollback
- **Type**: typing.Optional[bool]

### DriftInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFormationStackDriftInformationDetailsTypeDef]

### EnableTerminationProtection
- **Type**: typing.Optional[bool]

### LastUpdatedTime
- **Type**: typing.Optional[str]

### NotificationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFormationStackOutputsDetailsTypeDef]]

### RoleArn
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### StackName
- **Type**: typing.Optional[str]

### StackStatus
- **Type**: typing.Optional[str]

### StackStatusReason
- **Type**: typing.Optional[str]

### TimeoutInMinutes
- **Type**: typing.Optional[int]


# AwsCloudFormationStackDriftInformationDetailsTypeDef

### StackDriftStatus
- **Type**: typing.Optional[str]


# AwsCloudFormationStackOutputsDetailsTypeDef

### Description
- **Type**: typing.Optional[str]

### OutputKey
- **Type**: typing.Optional[str]

### OutputValue
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionCacheBehaviorTypeDef

### ViewerProtocolPolicy
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionCacheBehaviorsExtraOutputTypeDef

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionCacheBehaviorTypeDef]]


# AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionCacheBehaviorTypeDef]]


# AwsCloudFrontDistributionCacheBehaviorsTypeDef

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionCacheBehaviorTypeDef]]


# AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef

### ViewerProtocolPolicy
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionDetailsExtraOutputTypeDef

### CacheBehaviors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionCacheBehaviorsExtraOutputTypeDef]

### DefaultCacheBehavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef]

### DefaultRootObject
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### ETag
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[str]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionLoggingTypeDef]

### Origins
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginsExtraOutputTypeDef]

### OriginGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupsExtraOutputTypeDef]

### ViewerCertificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionViewerCertificateTypeDef]

### Status
- **Type**: typing.Optional[str]

### WebAclId
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionDetailsOutputTypeDef

### CacheBehaviors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef]

### DefaultCacheBehavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef]

### DefaultRootObject
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### ETag
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[str]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionLoggingTypeDef]

### Origins
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginsOutputTypeDef]

### OriginGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupsOutputTypeDef]

### ViewerCertificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionViewerCertificateTypeDef]

### Status
- **Type**: typing.Optional[str]

### WebAclId
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionDetailsTypeDef

### CacheBehaviors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionCacheBehaviorsTypeDef]

### DefaultCacheBehavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef]

### DefaultRootObject
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### ETag
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[str]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionLoggingTypeDef]

### Origins
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginsTypeDef]

### OriginGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupsTypeDef]

### ViewerCertificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionViewerCertificateTypeDef]

### Status
- **Type**: typing.Optional[str]

### WebAclId
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionLoggingTypeDef

### Bucket
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### IncludeCookies
- **Type**: typing.Optional[bool]

### Prefix
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionOriginCustomOriginConfigExtraOutputTypeDef

### HttpPort
- **Type**: typing.Optional[int]

### HttpsPort
- **Type**: typing.Optional[int]

### OriginKeepaliveTimeout
- **Type**: typing.Optional[int]

### OriginProtocolPolicy
- **Type**: typing.Optional[str]

### OriginReadTimeout
- **Type**: typing.Optional[int]

### OriginSslProtocols
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginSslProtocolsExtraOutputTypeDef]


# AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef

### HttpPort
- **Type**: typing.Optional[int]

### HttpsPort
- **Type**: typing.Optional[int]

### OriginKeepaliveTimeout
- **Type**: typing.Optional[int]

### OriginProtocolPolicy
- **Type**: typing.Optional[str]

### OriginReadTimeout
- **Type**: typing.Optional[int]

### OriginSslProtocols
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef]


# AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef

### HttpPort
- **Type**: typing.Optional[int]

### HttpsPort
- **Type**: typing.Optional[int]

### OriginKeepaliveTimeout
- **Type**: typing.Optional[int]

### OriginProtocolPolicy
- **Type**: typing.Optional[str]

### OriginReadTimeout
- **Type**: typing.Optional[int]

### OriginSslProtocols
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginSslProtocolsTypeDef]


# AwsCloudFrontDistributionOriginGroupExtraOutputTypeDef

### FailoverCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupFailoverExtraOutputTypeDef]


# AwsCloudFrontDistributionOriginGroupFailoverExtraOutputTypeDef

### StatusCodes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupFailoverStatusCodesExtraOutputTypeDef]


# AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef

### StatusCodes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef]


# AwsCloudFrontDistributionOriginGroupFailoverStatusCodesExtraOutputTypeDef

### Items
- **Type**: typing.Optional[typing.List[int]]

### Quantity
- **Type**: typing.Optional[int]


# AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef

### Items
- **Type**: typing.Optional[typing.List[int]]

### Quantity
- **Type**: typing.Optional[int]


# AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef

### Items
- **Type**: typing.Optional[typing.Sequence[int]]

### Quantity
- **Type**: typing.Optional[int]


# AwsCloudFrontDistributionOriginGroupFailoverTypeDef

### StatusCodes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef]


# AwsCloudFrontDistributionOriginGroupOutputTypeDef

### FailoverCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef]


# AwsCloudFrontDistributionOriginGroupTypeDef

### FailoverCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupFailoverTypeDef]


# AwsCloudFrontDistributionOriginGroupsExtraOutputTypeDef

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupExtraOutputTypeDef]]


# AwsCloudFrontDistributionOriginGroupsOutputTypeDef

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupOutputTypeDef]]


# AwsCloudFrontDistributionOriginGroupsTypeDef

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginGroupTypeDef]]


# AwsCloudFrontDistributionOriginItemExtraOutputTypeDef

### DomainName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### OriginPath
- **Type**: typing.Optional[str]

### S3OriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginS3OriginConfigTypeDef]

### CustomOriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginCustomOriginConfigExtraOutputTypeDef]


# AwsCloudFrontDistributionOriginItemOutputTypeDef

### DomainName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### OriginPath
- **Type**: typing.Optional[str]

### S3OriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginS3OriginConfigTypeDef]

### CustomOriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef]


# AwsCloudFrontDistributionOriginItemTypeDef

### DomainName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### OriginPath
- **Type**: typing.Optional[str]

### S3OriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginS3OriginConfigTypeDef]

### CustomOriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef]


# AwsCloudFrontDistributionOriginS3OriginConfigTypeDef

### OriginAccessIdentity
- **Type**: typing.Optional[str]


# AwsCloudFrontDistributionOriginSslProtocolsExtraOutputTypeDef

### Items
- **Type**: typing.Optional[typing.List[str]]

### Quantity
- **Type**: typing.Optional[int]


# AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef

### Items
- **Type**: typing.Optional[typing.List[str]]

### Quantity
- **Type**: typing.Optional[int]


# AwsCloudFrontDistributionOriginSslProtocolsTypeDef

### Items
- **Type**: typing.Optional[typing.Sequence[str]]

### Quantity
- **Type**: typing.Optional[int]


# AwsCloudFrontDistributionOriginsExtraOutputTypeDef

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginItemExtraOutputTypeDef]]


# AwsCloudFrontDistributionOriginsOutputTypeDef

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginItemOutputTypeDef]]


# AwsCloudFrontDistributionOriginsTypeDef

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionOriginItemTypeDef]]


# AwsCloudFrontDistributionViewerCertificateTypeDef

### AcmCertificateArn
- **Type**: typing.Optional[str]

### Certificate
- **Type**: typing.Optional[str]

### CertificateSource
- **Type**: typing.Optional[str]

### CloudFrontDefaultCertificate
- **Type**: typing.Optional[bool]

### IamCertificateId
- **Type**: typing.Optional[str]

### MinimumProtocolVersion
- **Type**: typing.Optional[str]

### SslSupportMethod
- **Type**: typing.Optional[str]


# AwsCloudTrailTrailDetailsTypeDef

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### CloudWatchLogsRoleArn
- **Type**: typing.Optional[str]

### HasCustomEventSelectors
- **Type**: typing.Optional[bool]

### HomeRegion
- **Type**: typing.Optional[str]

### IncludeGlobalServiceEvents
- **Type**: typing.Optional[bool]

### IsMultiRegionTrail
- **Type**: typing.Optional[bool]

### IsOrganizationTrail
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### LogFileValidationEnabled
- **Type**: typing.Optional[bool]

### Name
- **Type**: typing.Optional[str]

### S3BucketName
- **Type**: typing.Optional[str]

### S3KeyPrefix
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### SnsTopicName
- **Type**: typing.Optional[str]

### TrailArn
- **Type**: typing.Optional[str]


# AwsCloudWatchAlarmDetailsExtraOutputTypeDef

### ActionsEnabled
- **Type**: typing.Optional[bool]

### AlarmActions
- **Type**: typing.Optional[typing.List[str]]

### AlarmArn
- **Type**: typing.Optional[str]

### AlarmConfigurationUpdatedTimestamp
- **Type**: typing.Optional[str]

### AlarmDescription
- **Type**: typing.Optional[str]

### AlarmName
- **Type**: typing.Optional[str]

### ComparisonOperator
- **Type**: typing.Optional[str]

### DatapointsToAlarm
- **Type**: typing.Optional[int]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudWatchAlarmDimensionsDetailsTypeDef]]

### EvaluateLowSampleCountPercentile
- **Type**: typing.Optional[str]

### EvaluationPeriods
- **Type**: typing.Optional[int]

### ExtendedStatistic
- **Type**: typing.Optional[str]

### InsufficientDataActions
- **Type**: typing.Optional[typing.List[str]]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### OkActions
- **Type**: typing.Optional[typing.List[str]]

### Period
- **Type**: typing.Optional[int]

### Statistic
- **Type**: typing.Optional[str]

### Threshold
- **Type**: typing.Optional[float]

### ThresholdMetricId
- **Type**: typing.Optional[str]

### TreatMissingData
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]


# AwsCloudWatchAlarmDetailsOutputTypeDef

### ActionsEnabled
- **Type**: typing.Optional[bool]

### AlarmActions
- **Type**: typing.Optional[typing.List[str]]

### AlarmArn
- **Type**: typing.Optional[str]

### AlarmConfigurationUpdatedTimestamp
- **Type**: typing.Optional[str]

### AlarmDescription
- **Type**: typing.Optional[str]

### AlarmName
- **Type**: typing.Optional[str]

### ComparisonOperator
- **Type**: typing.Optional[str]

### DatapointsToAlarm
- **Type**: typing.Optional[int]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudWatchAlarmDimensionsDetailsTypeDef]]

### EvaluateLowSampleCountPercentile
- **Type**: typing.Optional[str]

### EvaluationPeriods
- **Type**: typing.Optional[int]

### ExtendedStatistic
- **Type**: typing.Optional[str]

### InsufficientDataActions
- **Type**: typing.Optional[typing.List[str]]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### OkActions
- **Type**: typing.Optional[typing.List[str]]

### Period
- **Type**: typing.Optional[int]

### Statistic
- **Type**: typing.Optional[str]

### Threshold
- **Type**: typing.Optional[float]

### ThresholdMetricId
- **Type**: typing.Optional[str]

### TreatMissingData
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]


# AwsCloudWatchAlarmDetailsTypeDef

### ActionsEnabled
- **Type**: typing.Optional[bool]

### AlarmActions
- **Type**: typing.Optional[typing.Sequence[str]]

### AlarmArn
- **Type**: typing.Optional[str]

### AlarmConfigurationUpdatedTimestamp
- **Type**: typing.Optional[str]

### AlarmDescription
- **Type**: typing.Optional[str]

### AlarmName
- **Type**: typing.Optional[str]

### ComparisonOperator
- **Type**: typing.Optional[str]

### DatapointsToAlarm
- **Type**: typing.Optional[int]

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudWatchAlarmDimensionsDetailsTypeDef]]

### EvaluateLowSampleCountPercentile
- **Type**: typing.Optional[str]

### EvaluationPeriods
- **Type**: typing.Optional[int]

### ExtendedStatistic
- **Type**: typing.Optional[str]

### InsufficientDataActions
- **Type**: typing.Optional[typing.Sequence[str]]

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### OkActions
- **Type**: typing.Optional[typing.Sequence[str]]

### Period
- **Type**: typing.Optional[int]

### Statistic
- **Type**: typing.Optional[str]

### Threshold
- **Type**: typing.Optional[float]

### ThresholdMetricId
- **Type**: typing.Optional[str]

### TreatMissingData
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]


# AwsCloudWatchAlarmDimensionsDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsCodeBuildProjectArtifactsDetailsTypeDef

### ArtifactIdentifier
- **Type**: typing.Optional[str]

### EncryptionDisabled
- **Type**: typing.Optional[bool]

### Location
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### NamespaceType
- **Type**: typing.Optional[str]

### OverrideArtifactName
- **Type**: typing.Optional[bool]

### Packaging
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsCodeBuildProjectDetailsExtraOutputTypeDef

### EncryptionKey
- **Type**: typing.Optional[str]

### Artifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectArtifactsDetailsTypeDef]]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectEnvironmentExtraOutputTypeDef]

### Name
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectSourceTypeDef]

### ServiceRole
- **Type**: typing.Optional[str]

### LogsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectLogsConfigDetailsTypeDef]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectVpcConfigExtraOutputTypeDef]

### SecondaryArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectArtifactsDetailsTypeDef]]


# AwsCodeBuildProjectDetailsOutputTypeDef

### EncryptionKey
- **Type**: typing.Optional[str]

### Artifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectArtifactsDetailsTypeDef]]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectEnvironmentOutputTypeDef]

### Name
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectSourceTypeDef]

### ServiceRole
- **Type**: typing.Optional[str]

### LogsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectLogsConfigDetailsTypeDef]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectVpcConfigOutputTypeDef]

### SecondaryArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectArtifactsDetailsTypeDef]]


# AwsCodeBuildProjectDetailsTypeDef

### EncryptionKey
- **Type**: typing.Optional[str]

### Artifacts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectArtifactsDetailsTypeDef]]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectEnvironmentTypeDef]

### Name
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectSourceTypeDef]

### ServiceRole
- **Type**: typing.Optional[str]

### LogsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectLogsConfigDetailsTypeDef]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectVpcConfigTypeDef]

### SecondaryArtifacts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectArtifactsDetailsTypeDef]]


# AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsCodeBuildProjectEnvironmentExtraOutputTypeDef

### Certificate
- **Type**: typing.Optional[str]

### EnvironmentVariables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]]

### PrivilegedMode
- **Type**: typing.Optional[bool]

### ImagePullCredentialsType
- **Type**: typing.Optional[str]

### RegistryCredential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef]

### Type
- **Type**: typing.Optional[str]


# AwsCodeBuildProjectEnvironmentOutputTypeDef

### Certificate
- **Type**: typing.Optional[str]

### EnvironmentVariables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]]

### PrivilegedMode
- **Type**: typing.Optional[bool]

### ImagePullCredentialsType
- **Type**: typing.Optional[str]

### RegistryCredential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef]

### Type
- **Type**: typing.Optional[str]


# AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef

### Credential
- **Type**: typing.Optional[str]

### CredentialProvider
- **Type**: typing.Optional[str]


# AwsCodeBuildProjectEnvironmentTypeDef

### Certificate
- **Type**: typing.Optional[str]

### EnvironmentVariables
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]]

### PrivilegedMode
- **Type**: typing.Optional[bool]

### ImagePullCredentialsType
- **Type**: typing.Optional[str]

### RegistryCredential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef]

### Type
- **Type**: typing.Optional[str]


# AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef

### GroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### StreamName
- **Type**: typing.Optional[str]


# AwsCodeBuildProjectLogsConfigDetailsTypeDef

### CloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef]

### S3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef]


# AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef

### EncryptionDisabled
- **Type**: typing.Optional[bool]

### Location
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsCodeBuildProjectSourceTypeDef

### Type
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]

### GitCloneDepth
- **Type**: typing.Optional[int]

### InsecureSsl
- **Type**: typing.Optional[bool]


# AwsCodeBuildProjectVpcConfigExtraOutputTypeDef

### VpcId
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# AwsCodeBuildProjectVpcConfigOutputTypeDef

### VpcId
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# AwsCodeBuildProjectVpcConfigTypeDef

### VpcId
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsCorsConfigurationExtraOutputTypeDef

### AllowOrigins
- **Type**: typing.Optional[typing.List[str]]

### AllowCredentials
- **Type**: typing.Optional[bool]

### ExposeHeaders
- **Type**: typing.Optional[typing.List[str]]

### MaxAge
- **Type**: typing.Optional[int]

### AllowMethods
- **Type**: typing.Optional[typing.List[str]]

### AllowHeaders
- **Type**: typing.Optional[typing.List[str]]


# AwsCorsConfigurationOutputTypeDef

### AllowOrigins
- **Type**: typing.Optional[typing.List[str]]

### AllowCredentials
- **Type**: typing.Optional[bool]

### ExposeHeaders
- **Type**: typing.Optional[typing.List[str]]

### MaxAge
- **Type**: typing.Optional[int]

### AllowMethods
- **Type**: typing.Optional[typing.List[str]]

### AllowHeaders
- **Type**: typing.Optional[typing.List[str]]


# AwsCorsConfigurationTypeDef

### AllowOrigins
- **Type**: typing.Optional[typing.Sequence[str]]

### AllowCredentials
- **Type**: typing.Optional[bool]

### ExposeHeaders
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxAge
- **Type**: typing.Optional[int]

### AllowMethods
- **Type**: typing.Optional[typing.Sequence[str]]

### AllowHeaders
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsDmsEndpointDetailsTypeDef

### CertificateArn
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### EndpointArn
- **Type**: typing.Optional[str]

### EndpointIdentifier
- **Type**: typing.Optional[str]

### EndpointType
- **Type**: typing.Optional[str]

### EngineName
- **Type**: typing.Optional[str]

### ExternalId
- **Type**: typing.Optional[str]

### ExtraConnectionAttributes
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ServerName
- **Type**: typing.Optional[str]

### SslMode
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# AwsDmsReplicationInstanceDetailsExtraOutputTypeDef

### AllocatedStorage
- **Type**: typing.Optional[int]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### AvailabilityZone
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### ReplicationInstanceClass
- **Type**: typing.Optional[str]

### ReplicationInstanceIdentifier
- **Type**: typing.Optional[str]

### ReplicationSubnetGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]]


# AwsDmsReplicationInstanceDetailsOutputTypeDef

### AllocatedStorage
- **Type**: typing.Optional[int]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### AvailabilityZone
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### ReplicationInstanceClass
- **Type**: typing.Optional[str]

### ReplicationInstanceIdentifier
- **Type**: typing.Optional[str]

### ReplicationSubnetGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]]


# AwsDmsReplicationInstanceDetailsTypeDef

### AllocatedStorage
- **Type**: typing.Optional[int]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### AvailabilityZone
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### MultiAZ
- **Type**: typing.Optional[bool]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### ReplicationInstanceClass
- **Type**: typing.Optional[str]

### ReplicationInstanceIdentifier
- **Type**: typing.Optional[str]

### ReplicationSubnetGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]]


# AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef

### ReplicationSubnetGroupIdentifier
- **Type**: typing.Optional[str]


# AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef

### VpcSecurityGroupId
- **Type**: typing.Optional[str]


# AwsDmsReplicationTaskDetailsTypeDef

### CdcStartPosition
- **Type**: typing.Optional[str]

### CdcStartTime
- **Type**: typing.Optional[str]

### CdcStopPosition
- **Type**: typing.Optional[str]

### MigrationType
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ReplicationInstanceArn
- **Type**: typing.Optional[str]

### ReplicationTaskIdentifier
- **Type**: typing.Optional[str]

### ReplicationTaskSettings
- **Type**: typing.Optional[str]

### SourceEndpointArn
- **Type**: typing.Optional[str]

### TableMappings
- **Type**: typing.Optional[str]

### TargetEndpointArn
- **Type**: typing.Optional[str]

### TaskData
- **Type**: typing.Optional[str]


# AwsDynamoDbTableAttributeDefinitionTypeDef

### AttributeName
- **Type**: typing.Optional[str]

### AttributeType
- **Type**: typing.Optional[str]


# AwsDynamoDbTableBillingModeSummaryTypeDef

### BillingMode
- **Type**: typing.Optional[str]

### LastUpdateToPayPerRequestDateTime
- **Type**: typing.Optional[str]


# AwsDynamoDbTableDetailsExtraOutputTypeDef

### AttributeDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableAttributeDefinitionTypeDef]]

### BillingModeSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableBillingModeSummaryTypeDef]

### CreationDateTime
- **Type**: typing.Optional[str]

### GlobalSecondaryIndexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableGlobalSecondaryIndexExtraOutputTypeDef]]

### GlobalTableVersion
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### KeySchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchemaTypeDef]]

### LatestStreamArn
- **Type**: typing.Optional[str]

### LatestStreamLabel
- **Type**: typing.Optional[str]

### LocalSecondaryIndexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableLocalSecondaryIndexExtraOutputTypeDef]]

### ProvisionedThroughput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughputTypeDef]

### Replicas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableReplicaExtraOutputTypeDef]]

### RestoreSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableRestoreSummaryTypeDef]

### SseDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableSseDescriptionTypeDef]

### StreamSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableStreamSpecificationTypeDef]

### TableId
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### TableSizeBytes
- **Type**: typing.Optional[int]

### TableStatus
- **Type**: typing.Optional[str]

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]


# AwsDynamoDbTableDetailsOutputTypeDef

### AttributeDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableAttributeDefinitionTypeDef]]

### BillingModeSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableBillingModeSummaryTypeDef]

### CreationDateTime
- **Type**: typing.Optional[str]

### GlobalSecondaryIndexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef]]

### GlobalTableVersion
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### KeySchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchemaTypeDef]]

### LatestStreamArn
- **Type**: typing.Optional[str]

### LatestStreamLabel
- **Type**: typing.Optional[str]

### LocalSecondaryIndexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef]]

### ProvisionedThroughput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughputTypeDef]

### Replicas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableReplicaOutputTypeDef]]

### RestoreSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableRestoreSummaryTypeDef]

### SseDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableSseDescriptionTypeDef]

### StreamSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableStreamSpecificationTypeDef]

### TableId
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### TableSizeBytes
- **Type**: typing.Optional[int]

### TableStatus
- **Type**: typing.Optional[str]

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]


# AwsDynamoDbTableDetailsTypeDef

### AttributeDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableAttributeDefinitionTypeDef]]

### BillingModeSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableBillingModeSummaryTypeDef]

### CreationDateTime
- **Type**: typing.Optional[str]

### GlobalSecondaryIndexes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableGlobalSecondaryIndexTypeDef]]

### GlobalTableVersion
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### KeySchema
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchemaTypeDef]]

### LatestStreamArn
- **Type**: typing.Optional[str]

### LatestStreamLabel
- **Type**: typing.Optional[str]

### LocalSecondaryIndexes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableLocalSecondaryIndexTypeDef]]

### ProvisionedThroughput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughputTypeDef]

### Replicas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableReplicaTypeDef]]

### RestoreSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableRestoreSummaryTypeDef]

### SseDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableSseDescriptionTypeDef]

### StreamSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableStreamSpecificationTypeDef]

### TableId
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### TableSizeBytes
- **Type**: typing.Optional[int]

### TableStatus
- **Type**: typing.Optional[str]

### DeletionProtectionEnabled
- **Type**: typing.Optional[bool]


# AwsDynamoDbTableGlobalSecondaryIndexExtraOutputTypeDef

### Backfilling
- **Type**: typing.Optional[bool]

### IndexArn
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### IndexSizeBytes
- **Type**: typing.Optional[int]

### IndexStatus
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### KeySchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchemaTypeDef]]

### Projection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProjectionExtraOutputTypeDef]

### ProvisionedThroughput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughputTypeDef]


# AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef

### Backfilling
- **Type**: typing.Optional[bool]

### IndexArn
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### IndexSizeBytes
- **Type**: typing.Optional[int]

### IndexStatus
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### KeySchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchemaTypeDef]]

### Projection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProjectionOutputTypeDef]

### ProvisionedThroughput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughputTypeDef]


# AwsDynamoDbTableGlobalSecondaryIndexTypeDef

### Backfilling
- **Type**: typing.Optional[bool]

### IndexArn
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### IndexSizeBytes
- **Type**: typing.Optional[int]

### IndexStatus
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### KeySchema
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchemaTypeDef]]

### Projection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProjectionTypeDef]

### ProvisionedThroughput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughputTypeDef]


# AwsDynamoDbTableKeySchemaTypeDef

### AttributeName
- **Type**: typing.Optional[str]

### KeyType
- **Type**: typing.Optional[str]


# AwsDynamoDbTableLocalSecondaryIndexExtraOutputTypeDef

### IndexArn
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### KeySchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchemaTypeDef]]

### Projection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProjectionExtraOutputTypeDef]


# AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef

### IndexArn
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### KeySchema
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchemaTypeDef]]

### Projection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProjectionOutputTypeDef]


# AwsDynamoDbTableLocalSecondaryIndexTypeDef

### IndexArn
- **Type**: typing.Optional[str]

### IndexName
- **Type**: typing.Optional[str]

### KeySchema
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableKeySchemaTypeDef]]

### Projection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProjectionTypeDef]


# AwsDynamoDbTableProjectionExtraOutputTypeDef

### NonKeyAttributes
- **Type**: typing.Optional[typing.List[str]]

### ProjectionType
- **Type**: typing.Optional[str]


# AwsDynamoDbTableProjectionOutputTypeDef

### NonKeyAttributes
- **Type**: typing.Optional[typing.List[str]]

### ProjectionType
- **Type**: typing.Optional[str]


# AwsDynamoDbTableProjectionTypeDef

### NonKeyAttributes
- **Type**: typing.Optional[typing.Sequence[str]]

### ProjectionType
- **Type**: typing.Optional[str]


# AwsDynamoDbTableProvisionedThroughputOverrideTypeDef

### ReadCapacityUnits
- **Type**: typing.Optional[int]


# AwsDynamoDbTableProvisionedThroughputTypeDef

### LastDecreaseDateTime
- **Type**: typing.Optional[str]

### LastIncreaseDateTime
- **Type**: typing.Optional[str]

### NumberOfDecreasesToday
- **Type**: typing.Optional[int]

### ReadCapacityUnits
- **Type**: typing.Optional[int]

### WriteCapacityUnits
- **Type**: typing.Optional[int]


# AwsDynamoDbTableReplicaExtraOutputTypeDef

### GlobalSecondaryIndexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]]

### KmsMasterKeyId
- **Type**: typing.Optional[str]

### ProvisionedThroughputOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughputOverrideTypeDef]

### RegionName
- **Type**: typing.Optional[str]

### ReplicaStatus
- **Type**: typing.Optional[str]

### ReplicaStatusDescription
- **Type**: typing.Optional[str]


# AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef

### IndexName
- **Type**: typing.Optional[str]

### ProvisionedThroughputOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughputOverrideTypeDef]


# AwsDynamoDbTableReplicaOutputTypeDef

### GlobalSecondaryIndexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]]

### KmsMasterKeyId
- **Type**: typing.Optional[str]

### ProvisionedThroughputOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughputOverrideTypeDef]

### RegionName
- **Type**: typing.Optional[str]

### ReplicaStatus
- **Type**: typing.Optional[str]

### ReplicaStatusDescription
- **Type**: typing.Optional[str]


# AwsDynamoDbTableReplicaTypeDef

### GlobalSecondaryIndexes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]]

### KmsMasterKeyId
- **Type**: typing.Optional[str]

### ProvisionedThroughputOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableProvisionedThroughputOverrideTypeDef]

### RegionName
- **Type**: typing.Optional[str]

### ReplicaStatus
- **Type**: typing.Optional[str]

### ReplicaStatusDescription
- **Type**: typing.Optional[str]


# AwsDynamoDbTableRestoreSummaryTypeDef

### SourceBackupArn
- **Type**: typing.Optional[str]

### SourceTableArn
- **Type**: typing.Optional[str]

### RestoreDateTime
- **Type**: typing.Optional[str]

### RestoreInProgress
- **Type**: typing.Optional[bool]


# AwsDynamoDbTableSseDescriptionTypeDef

### InaccessibleEncryptionDateTime
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### SseType
- **Type**: typing.Optional[str]

### KmsMasterKeyArn
- **Type**: typing.Optional[str]


# AwsDynamoDbTableStreamSpecificationTypeDef

### StreamEnabled
- **Type**: typing.Optional[bool]

### StreamViewType
- **Type**: typing.Optional[str]


# AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef

### DirectoryId
- **Type**: typing.Optional[str]


# AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef

### Type
- **Type**: typing.Optional[str]

### ActiveDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef]

### MutualAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef]

### FederatedAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef]


# AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef

### SamlProviderArn
- **Type**: typing.Optional[str]

### SelfServiceSamlProviderArn
- **Type**: typing.Optional[str]


# AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef

### ClientRootCertificateChain
- **Type**: typing.Optional[str]


# AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### LambdaFunctionArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef]


# AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### BannerText
- **Type**: typing.Optional[str]


# AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### CloudwatchLogGroup
- **Type**: typing.Optional[str]

### CloudwatchLogStream
- **Type**: typing.Optional[str]


# AwsEc2ClientVpnEndpointDetailsExtraOutputTypeDef

### ClientVpnEndpointId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientCidrBlock
- **Type**: typing.Optional[str]

### DnsServer
- **Type**: typing.Optional[typing.List[str]]

### SplitTunnel
- **Type**: typing.Optional[bool]

### TransportProtocol
- **Type**: typing.Optional[str]

### VpnPort
- **Type**: typing.Optional[int]

### ServerCertificateArn
- **Type**: typing.Optional[str]

### AuthenticationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]]

### ConnectionLogOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef]

### SecurityGroupIdSet
- **Type**: typing.Optional[typing.List[str]]

### VpcId
- **Type**: typing.Optional[str]

### SelfServicePortalUrl
- **Type**: typing.Optional[str]

### ClientConnectOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef]

### SessionTimeoutHours
- **Type**: typing.Optional[int]

### ClientLoginBannerOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef]


# AwsEc2ClientVpnEndpointDetailsOutputTypeDef

### ClientVpnEndpointId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientCidrBlock
- **Type**: typing.Optional[str]

### DnsServer
- **Type**: typing.Optional[typing.List[str]]

### SplitTunnel
- **Type**: typing.Optional[bool]

### TransportProtocol
- **Type**: typing.Optional[str]

### VpnPort
- **Type**: typing.Optional[int]

### ServerCertificateArn
- **Type**: typing.Optional[str]

### AuthenticationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]]

### ConnectionLogOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef]

### SecurityGroupIdSet
- **Type**: typing.Optional[typing.List[str]]

### VpcId
- **Type**: typing.Optional[str]

### SelfServicePortalUrl
- **Type**: typing.Optional[str]

### ClientConnectOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef]

### SessionTimeoutHours
- **Type**: typing.Optional[int]

### ClientLoginBannerOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef]


# AwsEc2ClientVpnEndpointDetailsTypeDef

### ClientVpnEndpointId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientCidrBlock
- **Type**: typing.Optional[str]

### DnsServer
- **Type**: typing.Optional[typing.Sequence[str]]

### SplitTunnel
- **Type**: typing.Optional[bool]

### TransportProtocol
- **Type**: typing.Optional[str]

### VpnPort
- **Type**: typing.Optional[int]

### ServerCertificateArn
- **Type**: typing.Optional[str]

### AuthenticationOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]]

### ConnectionLogOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef]

### SecurityGroupIdSet
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcId
- **Type**: typing.Optional[str]

### SelfServicePortalUrl
- **Type**: typing.Optional[str]

### ClientConnectOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef]

### SessionTimeoutHours
- **Type**: typing.Optional[int]

### ClientLoginBannerOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef]


# AwsEc2EipDetailsTypeDef

### InstanceId
- **Type**: typing.Optional[str]

### PublicIp
- **Type**: typing.Optional[str]

### AllocationId
- **Type**: typing.Optional[str]

### AssociationId
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### PublicIpv4Pool
- **Type**: typing.Optional[str]

### NetworkBorderGroup
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### NetworkInterfaceOwnerId
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]


# AwsEc2InstanceDetailsExtraOutputTypeDef

### Type
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### IpV4Addresses
- **Type**: typing.Optional[typing.List[str]]

### IpV6Addresses
- **Type**: typing.Optional[typing.List[str]]

### KeyName
- **Type**: typing.Optional[str]

### IamInstanceProfileArn
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### LaunchedAt
- **Type**: typing.Optional[str]

### NetworkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2InstanceNetworkInterfacesDetailsTypeDef]]

### VirtualizationType
- **Type**: typing.Optional[str]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2InstanceMetadataOptionsTypeDef]

### Monitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2InstanceMonitoringDetailsTypeDef]


# AwsEc2InstanceDetailsOutputTypeDef

### Type
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### IpV4Addresses
- **Type**: typing.Optional[typing.List[str]]

### IpV6Addresses
- **Type**: typing.Optional[typing.List[str]]

### KeyName
- **Type**: typing.Optional[str]

### IamInstanceProfileArn
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### LaunchedAt
- **Type**: typing.Optional[str]

### NetworkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2InstanceNetworkInterfacesDetailsTypeDef]]

### VirtualizationType
- **Type**: typing.Optional[str]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2InstanceMetadataOptionsTypeDef]

### Monitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2InstanceMonitoringDetailsTypeDef]


# AwsEc2InstanceDetailsTypeDef

### Type
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### IpV4Addresses
- **Type**: typing.Optional[typing.Sequence[str]]

### IpV6Addresses
- **Type**: typing.Optional[typing.Sequence[str]]

### KeyName
- **Type**: typing.Optional[str]

### IamInstanceProfileArn
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### LaunchedAt
- **Type**: typing.Optional[str]

### NetworkInterfaces
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2InstanceNetworkInterfacesDetailsTypeDef]]

### VirtualizationType
- **Type**: typing.Optional[str]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2InstanceMetadataOptionsTypeDef]

### Monitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2InstanceMonitoringDetailsTypeDef]


# AwsEc2InstanceMetadataOptionsTypeDef

### HttpEndpoint
- **Type**: typing.Optional[str]

### HttpProtocolIpv6
- **Type**: typing.Optional[str]

### HttpPutResponseHopLimit
- **Type**: typing.Optional[int]

### HttpTokens
- **Type**: typing.Optional[str]

### InstanceMetadataTags
- **Type**: typing.Optional[str]


# AwsEc2InstanceMonitoringDetailsTypeDef

### State
- **Type**: typing.Optional[str]


# AwsEc2InstanceNetworkInterfacesDetailsTypeDef

### NetworkInterfaceId
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef

### DeviceName
- **Type**: typing.Optional[str]

### Ebs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef]

### NoDevice
- **Type**: typing.Optional[str]

### VirtualName
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef

### DeleteOnTermination
- **Type**: typing.Optional[bool]

### Encrypted
- **Type**: typing.Optional[bool]

### Iops
- **Type**: typing.Optional[int]

### KmsKeyId
- **Type**: typing.Optional[str]

### SnapshotId
- **Type**: typing.Optional[str]

### Throughput
- **Type**: typing.Optional[int]

### VolumeSize
- **Type**: typing.Optional[int]

### VolumeType
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef

### CapacityReservationId
- **Type**: typing.Optional[str]

### CapacityReservationResourceGroupArn
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef

### CapacityReservationPreference
- **Type**: typing.Optional[str]

### CapacityReservationTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef]


# AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef

### CoreCount
- **Type**: typing.Optional[int]

### ThreadsPerCore
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef

### CpuCredits
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataDetailsExtraOutputTypeDef

### BlockDeviceMappingSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]]

### CapacityReservationSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef]

### CpuOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef]

### CreditSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef]

### DisableApiStop
- **Type**: typing.Optional[bool]

### DisableApiTermination
- **Type**: typing.Optional[bool]

### EbsOptimized
- **Type**: typing.Optional[bool]

### ElasticGpuSpecificationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]]

### ElasticInferenceAcceleratorSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]]

### EnclaveOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef]

### HibernationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef]

### IamInstanceProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef]

### ImageId
- **Type**: typing.Optional[str]

### InstanceInitiatedShutdownBehavior
- **Type**: typing.Optional[str]

### InstanceMarketOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef]

### InstanceRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsDetailsExtraOutputTypeDef]

### InstanceType
- **Type**: typing.Optional[str]

### KernelId
- **Type**: typing.Optional[str]

### KeyName
- **Type**: typing.Optional[str]

### LicenseSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]]

### MaintenanceOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef]

### Monitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef]

### NetworkInterfaceSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsExtraOutputTypeDef]]

### Placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataPlacementDetailsTypeDef]

### PrivateDnsNameOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef]

### RamDiskId
- **Type**: typing.Optional[str]

### SecurityGroupIdSet
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupSet
- **Type**: typing.Optional[typing.List[str]]

### UserData
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataDetailsOutputTypeDef

### BlockDeviceMappingSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]]

### CapacityReservationSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef]

### CpuOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef]

### CreditSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef]

### DisableApiStop
- **Type**: typing.Optional[bool]

### DisableApiTermination
- **Type**: typing.Optional[bool]

### EbsOptimized
- **Type**: typing.Optional[bool]

### ElasticGpuSpecificationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]]

### ElasticInferenceAcceleratorSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]]

### EnclaveOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef]

### HibernationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef]

### IamInstanceProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef]

### ImageId
- **Type**: typing.Optional[str]

### InstanceInitiatedShutdownBehavior
- **Type**: typing.Optional[str]

### InstanceMarketOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef]

### InstanceRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef]

### InstanceType
- **Type**: typing.Optional[str]

### KernelId
- **Type**: typing.Optional[str]

### KeyName
- **Type**: typing.Optional[str]

### LicenseSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]]

### MaintenanceOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef]

### Monitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef]

### NetworkInterfaceSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef]]

### Placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataPlacementDetailsTypeDef]

### PrivateDnsNameOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef]

### RamDiskId
- **Type**: typing.Optional[str]

### SecurityGroupIdSet
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupSet
- **Type**: typing.Optional[typing.List[str]]

### UserData
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataDetailsTypeDef

### BlockDeviceMappingSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]]

### CapacityReservationSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef]

### CpuOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef]

### CreditSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef]

### DisableApiStop
- **Type**: typing.Optional[bool]

### DisableApiTermination
- **Type**: typing.Optional[bool]

### EbsOptimized
- **Type**: typing.Optional[bool]

### ElasticGpuSpecificationSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]]

### ElasticInferenceAcceleratorSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]]

### EnclaveOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef]

### HibernationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef]

### IamInstanceProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef]

### ImageId
- **Type**: typing.Optional[str]

### InstanceInitiatedShutdownBehavior
- **Type**: typing.Optional[str]

### InstanceMarketOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef]

### InstanceRequirements
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef]

### InstanceType
- **Type**: typing.Optional[str]

### KernelId
- **Type**: typing.Optional[str]

### KeyName
- **Type**: typing.Optional[str]

### LicenseSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]]

### MaintenanceOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef]

### MetadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef]

### Monitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef]

### NetworkInterfaceSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef]]

### Placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataPlacementDetailsTypeDef]

### PrivateDnsNameOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef]

### RamDiskId
- **Type**: typing.Optional[str]

### SecurityGroupIdSet
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupSet
- **Type**: typing.Optional[typing.Sequence[str]]

### UserData
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef

### Type
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef

### Count
- **Type**: typing.Optional[int]

### Type
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef

### Configured
- **Type**: typing.Optional[bool]


# AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef

### MarketType
- **Type**: typing.Optional[str]

### SpotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef]


# AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef

### BlockDurationMinutes
- **Type**: typing.Optional[int]

### InstanceInterruptionBehavior
- **Type**: typing.Optional[str]

### MaxPrice
- **Type**: typing.Optional[str]

### SpotInstanceType
- **Type**: typing.Optional[str]

### ValidUntil
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef

### Max
- **Type**: typing.Optional[int]

### Min
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef

### Max
- **Type**: typing.Optional[int]

### Min
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef

### Max
- **Type**: typing.Optional[int]

### Min
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDataInstanceRequirementsDetailsExtraOutputTypeDef

### AcceleratorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef]

### AcceleratorManufacturers
- **Type**: typing.Optional[typing.List[str]]

### AcceleratorNames
- **Type**: typing.Optional[typing.List[str]]

### AcceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef]

### AcceleratorTypes
- **Type**: typing.Optional[typing.List[str]]

### BareMetal
- **Type**: typing.Optional[str]

### BaselineEbsBandwidthMbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef]

### BurstablePerformance
- **Type**: typing.Optional[str]

### CpuManufacturers
- **Type**: typing.Optional[typing.List[str]]

### ExcludedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### InstanceGenerations
- **Type**: typing.Optional[typing.List[str]]

### LocalStorage
- **Type**: typing.Optional[str]

### LocalStorageTypes
- **Type**: typing.Optional[typing.List[str]]

### MemoryGiBPerVCpu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef]

### MemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef]

### NetworkInterfaceCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef]

### OnDemandMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### RequireHibernateSupport
- **Type**: typing.Optional[bool]

### SpotMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### TotalLocalStorageGB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef]

### VCpuCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef]


# AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef

### AcceleratorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef]

### AcceleratorManufacturers
- **Type**: typing.Optional[typing.List[str]]

### AcceleratorNames
- **Type**: typing.Optional[typing.List[str]]

### AcceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef]

### AcceleratorTypes
- **Type**: typing.Optional[typing.List[str]]

### BareMetal
- **Type**: typing.Optional[str]

### BaselineEbsBandwidthMbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef]

### BurstablePerformance
- **Type**: typing.Optional[str]

### CpuManufacturers
- **Type**: typing.Optional[typing.List[str]]

### ExcludedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### InstanceGenerations
- **Type**: typing.Optional[typing.List[str]]

### LocalStorage
- **Type**: typing.Optional[str]

### LocalStorageTypes
- **Type**: typing.Optional[typing.List[str]]

### MemoryGiBPerVCpu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef]

### MemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef]

### NetworkInterfaceCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef]

### OnDemandMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### RequireHibernateSupport
- **Type**: typing.Optional[bool]

### SpotMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### TotalLocalStorageGB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef]

### VCpuCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef]


# AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef

### AcceleratorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef]

### AcceleratorManufacturers
- **Type**: typing.Optional[typing.Sequence[str]]

### AcceleratorNames
- **Type**: typing.Optional[typing.Sequence[str]]

### AcceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef]

### AcceleratorTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### BareMetal
- **Type**: typing.Optional[str]

### BaselineEbsBandwidthMbps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef]

### BurstablePerformance
- **Type**: typing.Optional[str]

### CpuManufacturers
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludedInstanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### InstanceGenerations
- **Type**: typing.Optional[typing.Sequence[str]]

### LocalStorage
- **Type**: typing.Optional[str]

### LocalStorageTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### MemoryGiBPerVCpu
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef]

### MemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef]

### NetworkInterfaceCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef]

### OnDemandMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### RequireHibernateSupport
- **Type**: typing.Optional[bool]

### SpotMaxPricePercentageOverLowestPrice
- **Type**: typing.Optional[int]

### TotalLocalStorageGB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef]

### VCpuCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef]


# AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef

### Max
- **Type**: typing.Optional[float]

### Min
- **Type**: typing.Optional[float]


# AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef

### Max
- **Type**: typing.Optional[int]

### Min
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef

### Max
- **Type**: typing.Optional[int]

### Min
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef

### Max
- **Type**: typing.Optional[float]

### Min
- **Type**: typing.Optional[float]


# AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef

### Max
- **Type**: typing.Optional[int]

### Min
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef

### LicenseConfigurationArn
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef

### AutoRecovery
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef

### HttpEndpoint
- **Type**: typing.Optional[str]

### HttpProtocolIpv6
- **Type**: typing.Optional[str]

### HttpTokens
- **Type**: typing.Optional[str]

### HttpPutResponseHopLimit
- **Type**: typing.Optional[int]

### InstanceMetadataTags
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsExtraOutputTypeDef

### AssociateCarrierIpAddress
- **Type**: typing.Optional[bool]

### AssociatePublicIpAddress
- **Type**: typing.Optional[bool]

### DeleteOnTermination
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### DeviceIndex
- **Type**: typing.Optional[int]

### Groups
- **Type**: typing.Optional[typing.List[str]]

### InterfaceType
- **Type**: typing.Optional[str]

### Ipv4PrefixCount
- **Type**: typing.Optional[int]

### Ipv4Prefixes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]]

### Ipv6AddressCount
- **Type**: typing.Optional[int]

### Ipv6Addresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]]

### Ipv6PrefixCount
- **Type**: typing.Optional[int]

### Ipv6Prefixes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]]

### NetworkCardIndex
- **Type**: typing.Optional[int]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]

### PrivateIpAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]]

### SecondaryPrivateIpAddressCount
- **Type**: typing.Optional[int]

### SubnetId
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef

### AssociateCarrierIpAddress
- **Type**: typing.Optional[bool]

### AssociatePublicIpAddress
- **Type**: typing.Optional[bool]

### DeleteOnTermination
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### DeviceIndex
- **Type**: typing.Optional[int]

### Groups
- **Type**: typing.Optional[typing.List[str]]

### InterfaceType
- **Type**: typing.Optional[str]

### Ipv4PrefixCount
- **Type**: typing.Optional[int]

### Ipv4Prefixes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]]

### Ipv6AddressCount
- **Type**: typing.Optional[int]

### Ipv6Addresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]]

### Ipv6PrefixCount
- **Type**: typing.Optional[int]

### Ipv6Prefixes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]]

### NetworkCardIndex
- **Type**: typing.Optional[int]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]

### PrivateIpAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]]

### SecondaryPrivateIpAddressCount
- **Type**: typing.Optional[int]

### SubnetId
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef

### AssociateCarrierIpAddress
- **Type**: typing.Optional[bool]

### AssociatePublicIpAddress
- **Type**: typing.Optional[bool]

### DeleteOnTermination
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### DeviceIndex
- **Type**: typing.Optional[int]

### Groups
- **Type**: typing.Optional[typing.Sequence[str]]

### InterfaceType
- **Type**: typing.Optional[str]

### Ipv4PrefixCount
- **Type**: typing.Optional[int]

### Ipv4Prefixes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]]

### Ipv6AddressCount
- **Type**: typing.Optional[int]

### Ipv6Addresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]]

### Ipv6PrefixCount
- **Type**: typing.Optional[int]

### Ipv6Prefixes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]]

### NetworkCardIndex
- **Type**: typing.Optional[int]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]

### PrivateIpAddresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]]

### SecondaryPrivateIpAddressCount
- **Type**: typing.Optional[int]

### SubnetId
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef

### Ipv4Prefix
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef

### Ipv6Address
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef

### Ipv6Prefix
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef

### Primary
- **Type**: typing.Optional[bool]

### PrivateIpAddress
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataPlacementDetailsTypeDef

### Affinity
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### HostId
- **Type**: typing.Optional[str]

### HostResourceGroupArn
- **Type**: typing.Optional[str]

### PartitionNumber
- **Type**: typing.Optional[int]

### SpreadDomain
- **Type**: typing.Optional[str]

### Tenancy
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef

### EnableResourceNameDnsAAAARecord
- **Type**: typing.Optional[bool]

### EnableResourceNameDnsARecord
- **Type**: typing.Optional[bool]

### HostnameType
- **Type**: typing.Optional[str]


# AwsEc2LaunchTemplateDetailsExtraOutputTypeDef

### LaunchTemplateName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### LaunchTemplateData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataDetailsExtraOutputTypeDef]

### DefaultVersionNumber
- **Type**: typing.Optional[int]

### LatestVersionNumber
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDetailsOutputTypeDef

### LaunchTemplateName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### LaunchTemplateData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataDetailsOutputTypeDef]

### DefaultVersionNumber
- **Type**: typing.Optional[int]

### LatestVersionNumber
- **Type**: typing.Optional[int]


# AwsEc2LaunchTemplateDetailsTypeDef

### LaunchTemplateName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### LaunchTemplateData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDataDetailsTypeDef]

### DefaultVersionNumber
- **Type**: typing.Optional[int]

### LatestVersionNumber
- **Type**: typing.Optional[int]


# AwsEc2NetworkAclAssociationTypeDef

### NetworkAclAssociationId
- **Type**: typing.Optional[str]

### NetworkAclId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]


# AwsEc2NetworkAclDetailsExtraOutputTypeDef

### IsDefault
- **Type**: typing.Optional[bool]

### NetworkAclId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Associations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkAclAssociationTypeDef]]

### Entries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkAclEntryTypeDef]]


# AwsEc2NetworkAclDetailsOutputTypeDef

### IsDefault
- **Type**: typing.Optional[bool]

### NetworkAclId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Associations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkAclAssociationTypeDef]]

### Entries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkAclEntryTypeDef]]


# AwsEc2NetworkAclDetailsTypeDef

### IsDefault
- **Type**: typing.Optional[bool]

### NetworkAclId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Associations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkAclAssociationTypeDef]]

### Entries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkAclEntryTypeDef]]


# AwsEc2NetworkAclEntryTypeDef

### CidrBlock
- **Type**: typing.Optional[str]

### Egress
- **Type**: typing.Optional[bool]

### IcmpTypeCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.IcmpTypeCodeTypeDef]

### Ipv6CidrBlock
- **Type**: typing.Optional[str]

### PortRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PortRangeFromToTypeDef]

### Protocol
- **Type**: typing.Optional[str]

### RuleAction
- **Type**: typing.Optional[str]

### RuleNumber
- **Type**: typing.Optional[int]


# AwsEc2NetworkInterfaceAttachmentTypeDef

### AttachTime
- **Type**: typing.Optional[str]

### AttachmentId
- **Type**: typing.Optional[str]

### DeleteOnTermination
- **Type**: typing.Optional[bool]

### DeviceIndex
- **Type**: typing.Optional[int]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceOwnerId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsEc2NetworkInterfaceDetailsExtraOutputTypeDef

### Attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceAttachmentTypeDef]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceSecurityGroupTypeDef]]

### SourceDestCheck
- **Type**: typing.Optional[bool]

### IpV6Addresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]]

### PrivateIpAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]]

### PublicDnsName
- **Type**: typing.Optional[str]

### PublicIp
- **Type**: typing.Optional[str]


# AwsEc2NetworkInterfaceDetailsOutputTypeDef

### Attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceAttachmentTypeDef]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceSecurityGroupTypeDef]]

### SourceDestCheck
- **Type**: typing.Optional[bool]

### IpV6Addresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]]

### PrivateIpAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]]

### PublicDnsName
- **Type**: typing.Optional[str]

### PublicIp
- **Type**: typing.Optional[str]


# AwsEc2NetworkInterfaceDetailsTypeDef

### Attachment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceAttachmentTypeDef]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceSecurityGroupTypeDef]]

### SourceDestCheck
- **Type**: typing.Optional[bool]

### IpV6Addresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]]

### PrivateIpAddresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]]

### PublicDnsName
- **Type**: typing.Optional[str]

### PublicIp
- **Type**: typing.Optional[str]


# AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef

### IpV6Address
- **Type**: typing.Optional[str]


# AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef

### PrivateIpAddress
- **Type**: typing.Optional[str]

### PrivateDnsName
- **Type**: typing.Optional[str]


# AwsEc2NetworkInterfaceSecurityGroupTypeDef

### GroupName
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]


# AwsEc2RouteTableDetailsExtraOutputTypeDef

### AssociationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AssociationSetDetailsTypeDef]]

### OwnerId
- **Type**: typing.Optional[str]

### PropagatingVgwSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.PropagatingVgwSetDetailsTypeDef]]

### RouteTableId
- **Type**: typing.Optional[str]

### RouteSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RouteSetDetailsTypeDef]]

### VpcId
- **Type**: typing.Optional[str]


# AwsEc2RouteTableDetailsOutputTypeDef

### AssociationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AssociationSetDetailsTypeDef]]

### OwnerId
- **Type**: typing.Optional[str]

### PropagatingVgwSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.PropagatingVgwSetDetailsTypeDef]]

### RouteTableId
- **Type**: typing.Optional[str]

### RouteSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RouteSetDetailsTypeDef]]

### VpcId
- **Type**: typing.Optional[str]


# AwsEc2RouteTableDetailsTypeDef

### AssociationSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AssociationSetDetailsTypeDef]]

### OwnerId
- **Type**: typing.Optional[str]

### PropagatingVgwSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.PropagatingVgwSetDetailsTypeDef]]

### RouteTableId
- **Type**: typing.Optional[str]

### RouteSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RouteSetDetailsTypeDef]]

### VpcId
- **Type**: typing.Optional[str]


# AwsEc2SecurityGroupDetailsExtraOutputTypeDef

### GroupName
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### IpPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpPermissionExtraOutputTypeDef]]

### IpPermissionsEgress
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpPermissionExtraOutputTypeDef]]


# AwsEc2SecurityGroupDetailsOutputTypeDef

### GroupName
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### IpPermissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpPermissionOutputTypeDef]]

### IpPermissionsEgress
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpPermissionOutputTypeDef]]


# AwsEc2SecurityGroupDetailsTypeDef

### GroupName
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### IpPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpPermissionTypeDef]]

### IpPermissionsEgress
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpPermissionTypeDef]]


# AwsEc2SecurityGroupIpPermissionExtraOutputTypeDef

### IpProtocol
- **Type**: typing.Optional[str]

### FromPort
- **Type**: typing.Optional[int]

### ToPort
- **Type**: typing.Optional[int]

### UserIdGroupPairs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupUserIdGroupPairTypeDef]]

### IpRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpRangeTypeDef]]

### Ipv6Ranges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpv6RangeTypeDef]]

### PrefixListIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupPrefixListIdTypeDef]]


# AwsEc2SecurityGroupIpPermissionOutputTypeDef

### IpProtocol
- **Type**: typing.Optional[str]

### FromPort
- **Type**: typing.Optional[int]

### ToPort
- **Type**: typing.Optional[int]

### UserIdGroupPairs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupUserIdGroupPairTypeDef]]

### IpRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpRangeTypeDef]]

### Ipv6Ranges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpv6RangeTypeDef]]

### PrefixListIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupPrefixListIdTypeDef]]


# AwsEc2SecurityGroupIpPermissionTypeDef

### IpProtocol
- **Type**: typing.Optional[str]

### FromPort
- **Type**: typing.Optional[int]

### ToPort
- **Type**: typing.Optional[int]

### UserIdGroupPairs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupUserIdGroupPairTypeDef]]

### IpRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpRangeTypeDef]]

### Ipv6Ranges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupIpv6RangeTypeDef]]

### PrefixListIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupPrefixListIdTypeDef]]


# AwsEc2SecurityGroupIpRangeTypeDef

### CidrIp
- **Type**: typing.Optional[str]


# AwsEc2SecurityGroupIpv6RangeTypeDef

### CidrIpv6
- **Type**: typing.Optional[str]


# AwsEc2SecurityGroupPrefixListIdTypeDef

### PrefixListId
- **Type**: typing.Optional[str]


# AwsEc2SecurityGroupUserIdGroupPairTypeDef

### GroupId
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### PeeringStatus
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### VpcPeeringConnectionId
- **Type**: typing.Optional[str]


# AwsEc2SubnetDetailsExtraOutputTypeDef

### AssignIpv6AddressOnCreation
- **Type**: typing.Optional[bool]

### AvailabilityZone
- **Type**: typing.Optional[str]

### AvailabilityZoneId
- **Type**: typing.Optional[str]

### AvailableIpAddressCount
- **Type**: typing.Optional[int]

### CidrBlock
- **Type**: typing.Optional[str]

### DefaultForAz
- **Type**: typing.Optional[bool]

### MapPublicIpOnLaunch
- **Type**: typing.Optional[bool]

### OwnerId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### SubnetArn
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Ipv6CidrBlockAssociationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Ipv6CidrBlockAssociationTypeDef]]


# AwsEc2SubnetDetailsOutputTypeDef

### AssignIpv6AddressOnCreation
- **Type**: typing.Optional[bool]

### AvailabilityZone
- **Type**: typing.Optional[str]

### AvailabilityZoneId
- **Type**: typing.Optional[str]

### AvailableIpAddressCount
- **Type**: typing.Optional[int]

### CidrBlock
- **Type**: typing.Optional[str]

### DefaultForAz
- **Type**: typing.Optional[bool]

### MapPublicIpOnLaunch
- **Type**: typing.Optional[bool]

### OwnerId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### SubnetArn
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Ipv6CidrBlockAssociationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Ipv6CidrBlockAssociationTypeDef]]


# AwsEc2SubnetDetailsTypeDef

### AssignIpv6AddressOnCreation
- **Type**: typing.Optional[bool]

### AvailabilityZone
- **Type**: typing.Optional[str]

### AvailabilityZoneId
- **Type**: typing.Optional[str]

### AvailableIpAddressCount
- **Type**: typing.Optional[int]

### CidrBlock
- **Type**: typing.Optional[str]

### DefaultForAz
- **Type**: typing.Optional[bool]

### MapPublicIpOnLaunch
- **Type**: typing.Optional[bool]

### OwnerId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### SubnetArn
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Ipv6CidrBlockAssociationSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.Ipv6CidrBlockAssociationTypeDef]]


# AwsEc2TransitGatewayDetailsExtraOutputTypeDef

### Id
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefaultRouteTablePropagation
- **Type**: typing.Optional[str]

### AutoAcceptSharedAttachments
- **Type**: typing.Optional[str]

### DefaultRouteTableAssociation
- **Type**: typing.Optional[str]

### TransitGatewayCidrBlocks
- **Type**: typing.Optional[typing.List[str]]

### AssociationDefaultRouteTableId
- **Type**: typing.Optional[str]

### PropagationDefaultRouteTableId
- **Type**: typing.Optional[str]

### VpnEcmpSupport
- **Type**: typing.Optional[str]

### DnsSupport
- **Type**: typing.Optional[str]

### MulticastSupport
- **Type**: typing.Optional[str]

### AmazonSideAsn
- **Type**: typing.Optional[int]


# AwsEc2TransitGatewayDetailsOutputTypeDef

### Id
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefaultRouteTablePropagation
- **Type**: typing.Optional[str]

### AutoAcceptSharedAttachments
- **Type**: typing.Optional[str]

### DefaultRouteTableAssociation
- **Type**: typing.Optional[str]

### TransitGatewayCidrBlocks
- **Type**: typing.Optional[typing.List[str]]

### AssociationDefaultRouteTableId
- **Type**: typing.Optional[str]

### PropagationDefaultRouteTableId
- **Type**: typing.Optional[str]

### VpnEcmpSupport
- **Type**: typing.Optional[str]

### DnsSupport
- **Type**: typing.Optional[str]

### MulticastSupport
- **Type**: typing.Optional[str]

### AmazonSideAsn
- **Type**: typing.Optional[int]


# AwsEc2TransitGatewayDetailsTypeDef

### Id
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefaultRouteTablePropagation
- **Type**: typing.Optional[str]

### AutoAcceptSharedAttachments
- **Type**: typing.Optional[str]

### DefaultRouteTableAssociation
- **Type**: typing.Optional[str]

### TransitGatewayCidrBlocks
- **Type**: typing.Optional[typing.Sequence[str]]

### AssociationDefaultRouteTableId
- **Type**: typing.Optional[str]

### PropagationDefaultRouteTableId
- **Type**: typing.Optional[str]

### VpnEcmpSupport
- **Type**: typing.Optional[str]

### DnsSupport
- **Type**: typing.Optional[str]

### MulticastSupport
- **Type**: typing.Optional[str]

### AmazonSideAsn
- **Type**: typing.Optional[int]


# AwsEc2VolumeAttachmentTypeDef

### AttachTime
- **Type**: typing.Optional[str]

### DeleteOnTermination
- **Type**: typing.Optional[bool]

### InstanceId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsEc2VolumeDetailsExtraOutputTypeDef

### CreateTime
- **Type**: typing.Optional[str]

### DeviceName
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### Size
- **Type**: typing.Optional[int]

### SnapshotId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VolumeAttachmentTypeDef]]

### VolumeId
- **Type**: typing.Optional[str]

### VolumeType
- **Type**: typing.Optional[str]

### VolumeScanStatus
- **Type**: typing.Optional[str]


# AwsEc2VolumeDetailsOutputTypeDef

### CreateTime
- **Type**: typing.Optional[str]

### DeviceName
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### Size
- **Type**: typing.Optional[int]

### SnapshotId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VolumeAttachmentTypeDef]]

### VolumeId
- **Type**: typing.Optional[str]

### VolumeType
- **Type**: typing.Optional[str]

### VolumeScanStatus
- **Type**: typing.Optional[str]


# AwsEc2VolumeDetailsTypeDef

### CreateTime
- **Type**: typing.Optional[str]

### DeviceName
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### Size
- **Type**: typing.Optional[int]

### SnapshotId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Attachments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VolumeAttachmentTypeDef]]

### VolumeId
- **Type**: typing.Optional[str]

### VolumeType
- **Type**: typing.Optional[str]

### VolumeScanStatus
- **Type**: typing.Optional[str]


# AwsEc2VpcDetailsExtraOutputTypeDef

### CidrBlockAssociationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.CidrBlockAssociationTypeDef]]

### Ipv6CidrBlockAssociationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Ipv6CidrBlockAssociationTypeDef]]

### DhcpOptionsId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# AwsEc2VpcDetailsOutputTypeDef

### CidrBlockAssociationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.CidrBlockAssociationTypeDef]]

### Ipv6CidrBlockAssociationSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.Ipv6CidrBlockAssociationTypeDef]]

### DhcpOptionsId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# AwsEc2VpcDetailsTypeDef

### CidrBlockAssociationSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.CidrBlockAssociationTypeDef]]

### Ipv6CidrBlockAssociationSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.Ipv6CidrBlockAssociationTypeDef]]

### DhcpOptionsId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# AwsEc2VpcEndpointServiceDetailsExtraOutputTypeDef

### AcceptanceRequired
- **Type**: typing.Optional[bool]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### BaseEndpointDnsNames
- **Type**: typing.Optional[typing.List[str]]

### ManagesVpcEndpoints
- **Type**: typing.Optional[bool]

### GatewayLoadBalancerArns
- **Type**: typing.Optional[typing.List[str]]

### NetworkLoadBalancerArns
- **Type**: typing.Optional[typing.List[str]]

### PrivateDnsName
- **Type**: typing.Optional[str]

### ServiceId
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### ServiceState
- **Type**: typing.Optional[str]

### ServiceType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]]


# AwsEc2VpcEndpointServiceDetailsOutputTypeDef

### AcceptanceRequired
- **Type**: typing.Optional[bool]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### BaseEndpointDnsNames
- **Type**: typing.Optional[typing.List[str]]

### ManagesVpcEndpoints
- **Type**: typing.Optional[bool]

### GatewayLoadBalancerArns
- **Type**: typing.Optional[typing.List[str]]

### NetworkLoadBalancerArns
- **Type**: typing.Optional[typing.List[str]]

### PrivateDnsName
- **Type**: typing.Optional[str]

### ServiceId
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### ServiceState
- **Type**: typing.Optional[str]

### ServiceType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]]


# AwsEc2VpcEndpointServiceDetailsTypeDef

### AcceptanceRequired
- **Type**: typing.Optional[bool]

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### BaseEndpointDnsNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ManagesVpcEndpoints
- **Type**: typing.Optional[bool]

### GatewayLoadBalancerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### NetworkLoadBalancerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PrivateDnsName
- **Type**: typing.Optional[str]

### ServiceId
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### ServiceState
- **Type**: typing.Optional[str]

### ServiceType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]]


# AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef

### ServiceType
- **Type**: typing.Optional[str]


# AwsEc2VpcPeeringConnectionDetailsExtraOutputTypeDef

### AccepterVpcInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionVpcInfoDetailsExtraOutputTypeDef]

### ExpirationTime
- **Type**: typing.Optional[str]

### RequesterVpcInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionVpcInfoDetailsExtraOutputTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionStatusDetailsTypeDef]

### VpcPeeringConnectionId
- **Type**: typing.Optional[str]


# AwsEc2VpcPeeringConnectionDetailsOutputTypeDef

### AccepterVpcInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef]

### ExpirationTime
- **Type**: typing.Optional[str]

### RequesterVpcInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionStatusDetailsTypeDef]

### VpcPeeringConnectionId
- **Type**: typing.Optional[str]


# AwsEc2VpcPeeringConnectionDetailsTypeDef

### AccepterVpcInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef]

### ExpirationTime
- **Type**: typing.Optional[str]

### RequesterVpcInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionStatusDetailsTypeDef]

### VpcPeeringConnectionId
- **Type**: typing.Optional[str]


# AwsEc2VpcPeeringConnectionStatusDetailsTypeDef

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# AwsEc2VpcPeeringConnectionVpcInfoDetailsExtraOutputTypeDef

### CidrBlock
- **Type**: typing.Optional[str]

### CidrBlockSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoCidrBlockSetDetailsTypeDef]]

### Ipv6CidrBlockSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoIpv6CidrBlockSetDetailsTypeDef]]

### OwnerId
- **Type**: typing.Optional[str]

### PeeringOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoPeeringOptionsDetailsTypeDef]

### Region
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef

### CidrBlock
- **Type**: typing.Optional[str]

### CidrBlockSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoCidrBlockSetDetailsTypeDef]]

### Ipv6CidrBlockSet
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoIpv6CidrBlockSetDetailsTypeDef]]

### OwnerId
- **Type**: typing.Optional[str]

### PeeringOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoPeeringOptionsDetailsTypeDef]

### Region
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef

### CidrBlock
- **Type**: typing.Optional[str]

### CidrBlockSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoCidrBlockSetDetailsTypeDef]]

### Ipv6CidrBlockSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoIpv6CidrBlockSetDetailsTypeDef]]

### OwnerId
- **Type**: typing.Optional[str]

### PeeringOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.VpcInfoPeeringOptionsDetailsTypeDef]

### Region
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# AwsEc2VpnConnectionDetailsExtraOutputTypeDef

### VpnConnectionId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### CustomerGatewayId
- **Type**: typing.Optional[str]

### CustomerGatewayConfiguration
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### VpnGatewayId
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[str]

### VgwTelemetry
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionOptionsDetailsExtraOutputTypeDef]

### Routes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionRoutesDetailsTypeDef]]

### TransitGatewayId
- **Type**: typing.Optional[str]


# AwsEc2VpnConnectionDetailsOutputTypeDef

### VpnConnectionId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### CustomerGatewayId
- **Type**: typing.Optional[str]

### CustomerGatewayConfiguration
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### VpnGatewayId
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[str]

### VgwTelemetry
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionOptionsDetailsOutputTypeDef]

### Routes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionRoutesDetailsTypeDef]]

### TransitGatewayId
- **Type**: typing.Optional[str]


# AwsEc2VpnConnectionDetailsTypeDef

### VpnConnectionId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### CustomerGatewayId
- **Type**: typing.Optional[str]

### CustomerGatewayConfiguration
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### VpnGatewayId
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[str]

### VgwTelemetry
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]]

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionOptionsDetailsTypeDef]

### Routes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionRoutesDetailsTypeDef]]

### TransitGatewayId
- **Type**: typing.Optional[str]


# AwsEc2VpnConnectionOptionsDetailsExtraOutputTypeDef

### StaticRoutesOnly
- **Type**: typing.Optional[bool]

### TunnelOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionOptionsTunnelOptionsDetailsExtraOutputTypeDef]]


# AwsEc2VpnConnectionOptionsDetailsOutputTypeDef

### StaticRoutesOnly
- **Type**: typing.Optional[bool]

### TunnelOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef]]


# AwsEc2VpnConnectionOptionsDetailsTypeDef

### StaticRoutesOnly
- **Type**: typing.Optional[bool]

### TunnelOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef]]


# AwsEc2VpnConnectionOptionsTunnelOptionsDetailsExtraOutputTypeDef

### DpdTimeoutSeconds
- **Type**: typing.Optional[int]

### IkeVersions
- **Type**: typing.Optional[typing.List[str]]

### OutsideIpAddress
- **Type**: typing.Optional[str]

### Phase1DhGroupNumbers
- **Type**: typing.Optional[typing.List[int]]

### Phase1EncryptionAlgorithms
- **Type**: typing.Optional[typing.List[str]]

### Phase1IntegrityAlgorithms
- **Type**: typing.Optional[typing.List[str]]

### Phase1LifetimeSeconds
- **Type**: typing.Optional[int]

### Phase2DhGroupNumbers
- **Type**: typing.Optional[typing.List[int]]

### Phase2EncryptionAlgorithms
- **Type**: typing.Optional[typing.List[str]]

### Phase2IntegrityAlgorithms
- **Type**: typing.Optional[typing.List[str]]

### Phase2LifetimeSeconds
- **Type**: typing.Optional[int]

### PreSharedKey
- **Type**: typing.Optional[str]

### RekeyFuzzPercentage
- **Type**: typing.Optional[int]

### RekeyMarginTimeSeconds
- **Type**: typing.Optional[int]

### ReplayWindowSize
- **Type**: typing.Optional[int]

### TunnelInsideCidr
- **Type**: typing.Optional[str]


# AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef

### DpdTimeoutSeconds
- **Type**: typing.Optional[int]

### IkeVersions
- **Type**: typing.Optional[typing.List[str]]

### OutsideIpAddress
- **Type**: typing.Optional[str]

### Phase1DhGroupNumbers
- **Type**: typing.Optional[typing.List[int]]

### Phase1EncryptionAlgorithms
- **Type**: typing.Optional[typing.List[str]]

### Phase1IntegrityAlgorithms
- **Type**: typing.Optional[typing.List[str]]

### Phase1LifetimeSeconds
- **Type**: typing.Optional[int]

### Phase2DhGroupNumbers
- **Type**: typing.Optional[typing.List[int]]

### Phase2EncryptionAlgorithms
- **Type**: typing.Optional[typing.List[str]]

### Phase2IntegrityAlgorithms
- **Type**: typing.Optional[typing.List[str]]

### Phase2LifetimeSeconds
- **Type**: typing.Optional[int]

### PreSharedKey
- **Type**: typing.Optional[str]

### RekeyFuzzPercentage
- **Type**: typing.Optional[int]

### RekeyMarginTimeSeconds
- **Type**: typing.Optional[int]

### ReplayWindowSize
- **Type**: typing.Optional[int]

### TunnelInsideCidr
- **Type**: typing.Optional[str]


# AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef

### DpdTimeoutSeconds
- **Type**: typing.Optional[int]

### IkeVersions
- **Type**: typing.Optional[typing.Sequence[str]]

### OutsideIpAddress
- **Type**: typing.Optional[str]

### Phase1DhGroupNumbers
- **Type**: typing.Optional[typing.Sequence[int]]

### Phase1EncryptionAlgorithms
- **Type**: typing.Optional[typing.Sequence[str]]

### Phase1IntegrityAlgorithms
- **Type**: typing.Optional[typing.Sequence[str]]

### Phase1LifetimeSeconds
- **Type**: typing.Optional[int]

### Phase2DhGroupNumbers
- **Type**: typing.Optional[typing.Sequence[int]]

### Phase2EncryptionAlgorithms
- **Type**: typing.Optional[typing.Sequence[str]]

### Phase2IntegrityAlgorithms
- **Type**: typing.Optional[typing.Sequence[str]]

### Phase2LifetimeSeconds
- **Type**: typing.Optional[int]

### PreSharedKey
- **Type**: typing.Optional[str]

### RekeyFuzzPercentage
- **Type**: typing.Optional[int]

### RekeyMarginTimeSeconds
- **Type**: typing.Optional[int]

### ReplayWindowSize
- **Type**: typing.Optional[int]

### TunnelInsideCidr
- **Type**: typing.Optional[str]


# AwsEc2VpnConnectionRoutesDetailsTypeDef

### DestinationCidrBlock
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef

### AcceptedRouteCount
- **Type**: typing.Optional[int]

### CertificateArn
- **Type**: typing.Optional[str]

### LastStatusChange
- **Type**: typing.Optional[str]

### OutsideIpAddress
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# AwsEcrContainerImageDetailsExtraOutputTypeDef

### RegistryId
- **Type**: typing.Optional[str]

### RepositoryName
- **Type**: typing.Optional[str]

### Architecture
- **Type**: typing.Optional[str]

### ImageDigest
- **Type**: typing.Optional[str]

### ImageTags
- **Type**: typing.Optional[typing.List[str]]

### ImagePublishedAt
- **Type**: typing.Optional[str]


# AwsEcrContainerImageDetailsOutputTypeDef

### RegistryId
- **Type**: typing.Optional[str]

### RepositoryName
- **Type**: typing.Optional[str]

### Architecture
- **Type**: typing.Optional[str]

### ImageDigest
- **Type**: typing.Optional[str]

### ImageTags
- **Type**: typing.Optional[typing.List[str]]

### ImagePublishedAt
- **Type**: typing.Optional[str]


# AwsEcrContainerImageDetailsTypeDef

### RegistryId
- **Type**: typing.Optional[str]

### RepositoryName
- **Type**: typing.Optional[str]

### Architecture
- **Type**: typing.Optional[str]

### ImageDigest
- **Type**: typing.Optional[str]

### ImageTags
- **Type**: typing.Optional[typing.Sequence[str]]

### ImagePublishedAt
- **Type**: typing.Optional[str]


# AwsEcrRepositoryDetailsTypeDef

### Arn
- **Type**: typing.Optional[str]

### ImageScanningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef]

### ImageTagMutability
- **Type**: typing.Optional[str]

### LifecyclePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcrRepositoryLifecyclePolicyDetailsTypeDef]

### RepositoryName
- **Type**: typing.Optional[str]

### RepositoryPolicyText
- **Type**: typing.Optional[str]


# AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef

### ScanOnPush
- **Type**: typing.Optional[bool]


# AwsEcrRepositoryLifecyclePolicyDetailsTypeDef

### LifecyclePolicyText
- **Type**: typing.Optional[str]

### RegistryId
- **Type**: typing.Optional[str]


# AwsEcsClusterClusterSettingsDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsEcsClusterConfigurationDetailsTypeDef

### ExecuteCommandConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef]


# AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef

### KmsKeyId
- **Type**: typing.Optional[str]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef]

### Logging
- **Type**: typing.Optional[str]


# AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef

### CloudWatchEncryptionEnabled
- **Type**: typing.Optional[bool]

### CloudWatchLogGroupName
- **Type**: typing.Optional[str]

### S3BucketName
- **Type**: typing.Optional[str]

### S3EncryptionEnabled
- **Type**: typing.Optional[bool]

### S3KeyPrefix
- **Type**: typing.Optional[str]


# AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef

### Base
- **Type**: typing.Optional[int]

### CapacityProvider
- **Type**: typing.Optional[str]

### Weight
- **Type**: typing.Optional[int]


# AwsEcsClusterDetailsExtraOutputTypeDef

### ClusterArn
- **Type**: typing.Optional[str]

### ActiveServicesCount
- **Type**: typing.Optional[int]

### CapacityProviders
- **Type**: typing.Optional[typing.List[str]]

### ClusterSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterClusterSettingsDetailsTypeDef]]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterConfigurationDetailsTypeDef]

### DefaultCapacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]]

### ClusterName
- **Type**: typing.Optional[str]

### RegisteredContainerInstancesCount
- **Type**: typing.Optional[int]

### RunningTasksCount
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]


# AwsEcsClusterDetailsOutputTypeDef

### ClusterArn
- **Type**: typing.Optional[str]

### ActiveServicesCount
- **Type**: typing.Optional[int]

### CapacityProviders
- **Type**: typing.Optional[typing.List[str]]

### ClusterSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterClusterSettingsDetailsTypeDef]]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterConfigurationDetailsTypeDef]

### DefaultCapacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]]

### ClusterName
- **Type**: typing.Optional[str]

### RegisteredContainerInstancesCount
- **Type**: typing.Optional[int]

### RunningTasksCount
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]


# AwsEcsClusterDetailsTypeDef

### ClusterArn
- **Type**: typing.Optional[str]

### ActiveServicesCount
- **Type**: typing.Optional[int]

### CapacityProviders
- **Type**: typing.Optional[typing.Sequence[str]]

### ClusterSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterClusterSettingsDetailsTypeDef]]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterConfigurationDetailsTypeDef]

### DefaultCapacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]]

### ClusterName
- **Type**: typing.Optional[str]

### RegisteredContainerInstancesCount
- **Type**: typing.Optional[int]

### RunningTasksCount
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]


# AwsEcsContainerDetailsExtraOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### MountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsMountPointTypeDef]]

### Privileged
- **Type**: typing.Optional[bool]


# AwsEcsContainerDetailsOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### MountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsMountPointTypeDef]]

### Privileged
- **Type**: typing.Optional[bool]


# AwsEcsContainerDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### MountPoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsMountPointTypeDef]]

### Privileged
- **Type**: typing.Optional[bool]


# AwsEcsServiceCapacityProviderStrategyDetailsTypeDef

### Base
- **Type**: typing.Optional[int]

### CapacityProvider
- **Type**: typing.Optional[str]

### Weight
- **Type**: typing.Optional[int]


# AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef

### Enable
- **Type**: typing.Optional[bool]

### Rollback
- **Type**: typing.Optional[bool]


# AwsEcsServiceDeploymentConfigurationDetailsTypeDef

### DeploymentCircuitBreaker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef]

### MaximumPercent
- **Type**: typing.Optional[int]

### MinimumHealthyPercent
- **Type**: typing.Optional[int]


# AwsEcsServiceDeploymentControllerDetailsTypeDef

### Type
- **Type**: typing.Optional[str]


# AwsEcsServiceDetailsExtraOutputTypeDef

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]]

### Cluster
- **Type**: typing.Optional[str]

### DeploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceDeploymentConfigurationDetailsTypeDef]

### DeploymentController
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceDeploymentControllerDetailsTypeDef]

### DesiredCount
- **Type**: typing.Optional[int]

### EnableEcsManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### HealthCheckGracePeriodSeconds
- **Type**: typing.Optional[int]

### LaunchType
- **Type**: typing.Optional[str]

### LoadBalancers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceLoadBalancersDetailsTypeDef]]

### Name
- **Type**: typing.Optional[str]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceNetworkConfigurationDetailsExtraOutputTypeDef]

### PlacementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServicePlacementConstraintsDetailsTypeDef]]

### PlacementStrategies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServicePlacementStrategiesDetailsTypeDef]]

### PlatformVersion
- **Type**: typing.Optional[str]

### PropagateTags
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### SchedulingStrategy
- **Type**: typing.Optional[str]

### ServiceArn
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### ServiceRegistries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceServiceRegistriesDetailsTypeDef]]

### TaskDefinition
- **Type**: typing.Optional[str]


# AwsEcsServiceDetailsOutputTypeDef

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]]

### Cluster
- **Type**: typing.Optional[str]

### DeploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceDeploymentConfigurationDetailsTypeDef]

### DeploymentController
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceDeploymentControllerDetailsTypeDef]

### DesiredCount
- **Type**: typing.Optional[int]

### EnableEcsManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### HealthCheckGracePeriodSeconds
- **Type**: typing.Optional[int]

### LaunchType
- **Type**: typing.Optional[str]

### LoadBalancers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceLoadBalancersDetailsTypeDef]]

### Name
- **Type**: typing.Optional[str]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef]

### PlacementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServicePlacementConstraintsDetailsTypeDef]]

### PlacementStrategies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServicePlacementStrategiesDetailsTypeDef]]

### PlatformVersion
- **Type**: typing.Optional[str]

### PropagateTags
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### SchedulingStrategy
- **Type**: typing.Optional[str]

### ServiceArn
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### ServiceRegistries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceServiceRegistriesDetailsTypeDef]]

### TaskDefinition
- **Type**: typing.Optional[str]


# AwsEcsServiceDetailsTypeDef

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]]

### Cluster
- **Type**: typing.Optional[str]

### DeploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceDeploymentConfigurationDetailsTypeDef]

### DeploymentController
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceDeploymentControllerDetailsTypeDef]

### DesiredCount
- **Type**: typing.Optional[int]

### EnableEcsManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### HealthCheckGracePeriodSeconds
- **Type**: typing.Optional[int]

### LaunchType
- **Type**: typing.Optional[str]

### LoadBalancers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceLoadBalancersDetailsTypeDef]]

### Name
- **Type**: typing.Optional[str]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceNetworkConfigurationDetailsTypeDef]

### PlacementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServicePlacementConstraintsDetailsTypeDef]]

### PlacementStrategies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServicePlacementStrategiesDetailsTypeDef]]

### PlatformVersion
- **Type**: typing.Optional[str]

### PropagateTags
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### SchedulingStrategy
- **Type**: typing.Optional[str]

### ServiceArn
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### ServiceRegistries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceServiceRegistriesDetailsTypeDef]]

### TaskDefinition
- **Type**: typing.Optional[str]


# AwsEcsServiceLoadBalancersDetailsTypeDef

### ContainerName
- **Type**: typing.Optional[str]

### ContainerPort
- **Type**: typing.Optional[int]

### LoadBalancerName
- **Type**: typing.Optional[str]

### TargetGroupArn
- **Type**: typing.Optional[str]


# AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsExtraOutputTypeDef

### AssignPublicIp
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### Subnets
- **Type**: typing.Optional[typing.List[str]]


# AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef

### AssignPublicIp
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### Subnets
- **Type**: typing.Optional[typing.List[str]]


# AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef

### AssignPublicIp
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### Subnets
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsEcsServiceNetworkConfigurationDetailsExtraOutputTypeDef

### AwsVpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsExtraOutputTypeDef]


# AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef

### AwsVpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef]


# AwsEcsServiceNetworkConfigurationDetailsTypeDef

### AwsVpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef]


# AwsEcsServicePlacementConstraintsDetailsTypeDef

### Expression
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsEcsServicePlacementStrategiesDetailsTypeDef

### Field
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsEcsServiceServiceRegistriesDetailsTypeDef

### ContainerName
- **Type**: typing.Optional[str]

### ContainerPort
- **Type**: typing.Optional[int]

### Port
- **Type**: typing.Optional[int]

### RegistryArn
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef

### Condition
- **Type**: typing.Optional[str]

### ContainerName
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsDetailsExtraOutputTypeDef

### Command
- **Type**: typing.Optional[typing.List[str]]

### Cpu
- **Type**: typing.Optional[int]

### DependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]]

### DisableNetworking
- **Type**: typing.Optional[bool]

### DnsSearchDomains
- **Type**: typing.Optional[typing.List[str]]

### DnsServers
- **Type**: typing.Optional[typing.List[str]]

### DockerLabels
- **Type**: typing.Optional[typing.Dict[str, str]]

### DockerSecurityOptions
- **Type**: typing.Optional[typing.List[str]]

### EntryPoint
- **Type**: typing.Optional[typing.List[str]]

### Environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]]

### EnvironmentFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]]

### Essential
- **Type**: typing.Optional[bool]

### ExtraHosts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]]

### FirelensConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsExtraOutputTypeDef]

### HealthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsExtraOutputTypeDef]

### Hostname
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### Interactive
- **Type**: typing.Optional[bool]

### Links
- **Type**: typing.Optional[typing.List[str]]

### LinuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsExtraOutputTypeDef]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsExtraOutputTypeDef]

### Memory
- **Type**: typing.Optional[int]

### MemoryReservation
- **Type**: typing.Optional[int]

### MountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]]

### Name
- **Type**: typing.Optional[str]

### PortMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]]

### Privileged
- **Type**: typing.Optional[bool]

### PseudoTerminal
- **Type**: typing.Optional[bool]

### ReadonlyRootFilesystem
- **Type**: typing.Optional[bool]

### RepositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef]

### ResourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]]

### Secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]]

### StartTimeout
- **Type**: typing.Optional[int]

### StopTimeout
- **Type**: typing.Optional[int]

### SystemControls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]]

### Ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]]

### User
- **Type**: typing.Optional[str]

### VolumesFrom
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]]

### WorkingDirectory
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef

### Command
- **Type**: typing.Optional[typing.List[str]]

### Cpu
- **Type**: typing.Optional[int]

### DependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]]

### DisableNetworking
- **Type**: typing.Optional[bool]

### DnsSearchDomains
- **Type**: typing.Optional[typing.List[str]]

### DnsServers
- **Type**: typing.Optional[typing.List[str]]

### DockerLabels
- **Type**: typing.Optional[typing.Dict[str, str]]

### DockerSecurityOptions
- **Type**: typing.Optional[typing.List[str]]

### EntryPoint
- **Type**: typing.Optional[typing.List[str]]

### Environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]]

### EnvironmentFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]]

### Essential
- **Type**: typing.Optional[bool]

### ExtraHosts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]]

### FirelensConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef]

### HealthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef]

### Hostname
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### Interactive
- **Type**: typing.Optional[bool]

### Links
- **Type**: typing.Optional[typing.List[str]]

### LinuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef]

### Memory
- **Type**: typing.Optional[int]

### MemoryReservation
- **Type**: typing.Optional[int]

### MountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]]

### Name
- **Type**: typing.Optional[str]

### PortMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]]

### Privileged
- **Type**: typing.Optional[bool]

### PseudoTerminal
- **Type**: typing.Optional[bool]

### ReadonlyRootFilesystem
- **Type**: typing.Optional[bool]

### RepositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef]

### ResourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]]

### Secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]]

### StartTimeout
- **Type**: typing.Optional[int]

### StopTimeout
- **Type**: typing.Optional[int]

### SystemControls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]]

### Ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]]

### User
- **Type**: typing.Optional[str]

### VolumesFrom
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]]

### WorkingDirectory
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef

### Command
- **Type**: typing.Optional[typing.Sequence[str]]

### Cpu
- **Type**: typing.Optional[int]

### DependsOn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]]

### DisableNetworking
- **Type**: typing.Optional[bool]

### DnsSearchDomains
- **Type**: typing.Optional[typing.Sequence[str]]

### DnsServers
- **Type**: typing.Optional[typing.Sequence[str]]

### DockerLabels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DockerSecurityOptions
- **Type**: typing.Optional[typing.Sequence[str]]

### EntryPoint
- **Type**: typing.Optional[typing.Sequence[str]]

### Environment
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]]

### EnvironmentFiles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]]

### Essential
- **Type**: typing.Optional[bool]

### ExtraHosts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]]

### FirelensConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef]

### HealthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef]

### Hostname
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### Interactive
- **Type**: typing.Optional[bool]

### Links
- **Type**: typing.Optional[typing.Sequence[str]]

### LinuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef]

### Memory
- **Type**: typing.Optional[int]

### MemoryReservation
- **Type**: typing.Optional[int]

### MountPoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]]

### Name
- **Type**: typing.Optional[str]

### PortMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]]

### Privileged
- **Type**: typing.Optional[bool]

### PseudoTerminal
- **Type**: typing.Optional[bool]

### ReadonlyRootFilesystem
- **Type**: typing.Optional[bool]

### RepositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef]

### ResourceRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]]

### Secrets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]]

### StartTimeout
- **Type**: typing.Optional[int]

### StopTimeout
- **Type**: typing.Optional[int]

### SystemControls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]]

### Ulimits
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]]

### User
- **Type**: typing.Optional[str]

### VolumesFrom
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]]

### WorkingDirectory
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef

### Type
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef

### Hostname
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsExtraOutputTypeDef

### Options
- **Type**: typing.Optional[typing.Dict[str, str]]

### Type
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef

### Options
- **Type**: typing.Optional[typing.Dict[str, str]]

### Type
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef

### Options
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Type
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsExtraOutputTypeDef

### Command
- **Type**: typing.Optional[typing.List[str]]

### Interval
- **Type**: typing.Optional[int]

### Retries
- **Type**: typing.Optional[int]

### StartPeriod
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]


# AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef

### Command
- **Type**: typing.Optional[typing.List[str]]

### Interval
- **Type**: typing.Optional[int]

### Retries
- **Type**: typing.Optional[int]

### StartPeriod
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]


# AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef

### Command
- **Type**: typing.Optional[typing.Sequence[str]]

### Interval
- **Type**: typing.Optional[int]

### Retries
- **Type**: typing.Optional[int]

### StartPeriod
- **Type**: typing.Optional[int]

### Timeout
- **Type**: typing.Optional[int]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsExtraOutputTypeDef

### Add
- **Type**: typing.Optional[typing.List[str]]

### Drop
- **Type**: typing.Optional[typing.List[str]]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef

### Add
- **Type**: typing.Optional[typing.List[str]]

### Drop
- **Type**: typing.Optional[typing.List[str]]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef

### Add
- **Type**: typing.Optional[typing.Sequence[str]]

### Drop
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsExtraOutputTypeDef

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsExtraOutputTypeDef]

### Devices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsExtraOutputTypeDef]]

### InitProcessEnabled
- **Type**: typing.Optional[bool]

### MaxSwap
- **Type**: typing.Optional[int]

### SharedMemorySize
- **Type**: typing.Optional[int]

### Swappiness
- **Type**: typing.Optional[int]

### Tmpfs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsExtraOutputTypeDef]]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef]

### Devices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef]]

### InitProcessEnabled
- **Type**: typing.Optional[bool]

### MaxSwap
- **Type**: typing.Optional[int]

### SharedMemorySize
- **Type**: typing.Optional[int]

### Swappiness
- **Type**: typing.Optional[int]

### Tmpfs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef]]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef]

### Devices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef]]

### InitProcessEnabled
- **Type**: typing.Optional[bool]

### MaxSwap
- **Type**: typing.Optional[int]

### SharedMemorySize
- **Type**: typing.Optional[int]

### Swappiness
- **Type**: typing.Optional[int]

### Tmpfs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef]]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsExtraOutputTypeDef

### ContainerPath
- **Type**: typing.Optional[str]

### HostPath
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.List[str]]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef

### ContainerPath
- **Type**: typing.Optional[str]

### HostPath
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.List[str]]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef

### ContainerPath
- **Type**: typing.Optional[str]

### HostPath
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsExtraOutputTypeDef

### ContainerPath
- **Type**: typing.Optional[str]

### MountOptions
- **Type**: typing.Optional[typing.List[str]]

### Size
- **Type**: typing.Optional[int]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef

### ContainerPath
- **Type**: typing.Optional[str]

### MountOptions
- **Type**: typing.Optional[typing.List[str]]

### Size
- **Type**: typing.Optional[int]


# AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef

### ContainerPath
- **Type**: typing.Optional[str]

### MountOptions
- **Type**: typing.Optional[typing.Sequence[str]]

### Size
- **Type**: typing.Optional[int]


# AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsExtraOutputTypeDef

### LogDriver
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[typing.Dict[str, str]]

### SecretOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef]]


# AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef

### LogDriver
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[typing.Dict[str, str]]

### SecretOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef]]


# AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef

### LogDriver
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[typing.Mapping[str, str]]

### SecretOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef]]


# AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### ValueFrom
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef

### ContainerPath
- **Type**: typing.Optional[str]

### ReadOnly
- **Type**: typing.Optional[bool]

### SourceVolume
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef

### ContainerPort
- **Type**: typing.Optional[int]

### HostPort
- **Type**: typing.Optional[int]

### Protocol
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef

### CredentialsParameter
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef

### Type
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### ValueFrom
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef

### Namespace
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef

### HardLimit
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[str]

### SoftLimit
- **Type**: typing.Optional[int]


# AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef

### ReadOnly
- **Type**: typing.Optional[bool]

### SourceContainer
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionDetailsExtraOutputTypeDef

### ContainerDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsDetailsExtraOutputTypeDef]]

### Cpu
- **Type**: typing.Optional[str]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### Family
- **Type**: typing.Optional[str]

### InferenceAccelerators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]]

### IpcMode
- **Type**: typing.Optional[str]

### Memory
- **Type**: typing.Optional[str]

### NetworkMode
- **Type**: typing.Optional[str]

### PidMode
- **Type**: typing.Optional[str]

### PlacementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]]

### ProxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionProxyConfigurationDetailsExtraOutputTypeDef]

### RequiresCompatibilities
- **Type**: typing.Optional[typing.List[str]]

### TaskRoleArn
- **Type**: typing.Optional[str]

### Volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesDetailsExtraOutputTypeDef]]

### Status
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionDetailsOutputTypeDef

### ContainerDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef]]

### Cpu
- **Type**: typing.Optional[str]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### Family
- **Type**: typing.Optional[str]

### InferenceAccelerators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]]

### IpcMode
- **Type**: typing.Optional[str]

### Memory
- **Type**: typing.Optional[str]

### NetworkMode
- **Type**: typing.Optional[str]

### PidMode
- **Type**: typing.Optional[str]

### PlacementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]]

### ProxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef]

### RequiresCompatibilities
- **Type**: typing.Optional[typing.List[str]]

### TaskRoleArn
- **Type**: typing.Optional[str]

### Volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef]]

### Status
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionDetailsTypeDef

### ContainerDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef]]

### Cpu
- **Type**: typing.Optional[str]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### Family
- **Type**: typing.Optional[str]

### InferenceAccelerators
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]]

### IpcMode
- **Type**: typing.Optional[str]

### Memory
- **Type**: typing.Optional[str]

### NetworkMode
- **Type**: typing.Optional[str]

### PidMode
- **Type**: typing.Optional[str]

### PlacementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]]

### ProxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef]

### RequiresCompatibilities
- **Type**: typing.Optional[typing.Sequence[str]]

### TaskRoleArn
- **Type**: typing.Optional[str]

### Volumes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesDetailsTypeDef]]

### Status
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef

### DeviceName
- **Type**: typing.Optional[str]

### DeviceType
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef

### Expression
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionProxyConfigurationDetailsExtraOutputTypeDef

### ContainerName
- **Type**: typing.Optional[str]

### ProxyConfigurationProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef]]

### Type
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef

### ContainerName
- **Type**: typing.Optional[str]

### ProxyConfigurationProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef]]

### Type
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef

### ContainerName
- **Type**: typing.Optional[str]

### ProxyConfigurationProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef]]

### Type
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionVolumesDetailsExtraOutputTypeDef

### DockerVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsExtraOutputTypeDef]

### EfsVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef]

### Host
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesHostDetailsTypeDef]

### Name
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef

### DockerVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef]

### EfsVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef]

### Host
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesHostDetailsTypeDef]

### Name
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionVolumesDetailsTypeDef

### DockerVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef]

### EfsVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef]

### Host
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesHostDetailsTypeDef]

### Name
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsExtraOutputTypeDef

### Autoprovision
- **Type**: typing.Optional[bool]

### Driver
- **Type**: typing.Optional[str]

### DriverOpts
- **Type**: typing.Optional[typing.Dict[str, str]]

### Labels
- **Type**: typing.Optional[typing.Dict[str, str]]

### Scope
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef

### Autoprovision
- **Type**: typing.Optional[bool]

### Driver
- **Type**: typing.Optional[str]

### DriverOpts
- **Type**: typing.Optional[typing.Dict[str, str]]

### Labels
- **Type**: typing.Optional[typing.Dict[str, str]]

### Scope
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef

### Autoprovision
- **Type**: typing.Optional[bool]

### Driver
- **Type**: typing.Optional[str]

### DriverOpts
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Labels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Scope
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef

### AccessPointId
- **Type**: typing.Optional[str]

### Iam
- **Type**: typing.Optional[str]


# AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef

### AuthorizationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef]

### FilesystemId
- **Type**: typing.Optional[str]

### RootDirectory
- **Type**: typing.Optional[str]

### TransitEncryption
- **Type**: typing.Optional[str]

### TransitEncryptionPort
- **Type**: typing.Optional[int]


# AwsEcsTaskDefinitionVolumesHostDetailsTypeDef

### SourcePath
- **Type**: typing.Optional[str]


# AwsEcsTaskDetailsExtraOutputTypeDef

### ClusterArn
- **Type**: typing.Optional[str]

### TaskDefinitionArn
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### StartedAt
- **Type**: typing.Optional[str]

### StartedBy
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### Volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskVolumeDetailsTypeDef]]

### Containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsContainerDetailsExtraOutputTypeDef]]


# AwsEcsTaskDetailsOutputTypeDef

### ClusterArn
- **Type**: typing.Optional[str]

### TaskDefinitionArn
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### StartedAt
- **Type**: typing.Optional[str]

### StartedBy
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### Volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskVolumeDetailsTypeDef]]

### Containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsContainerDetailsOutputTypeDef]]


# AwsEcsTaskDetailsTypeDef

### ClusterArn
- **Type**: typing.Optional[str]

### TaskDefinitionArn
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### StartedAt
- **Type**: typing.Optional[str]

### StartedBy
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### Volumes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskVolumeDetailsTypeDef]]

### Containers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsContainerDetailsTypeDef]]


# AwsEcsTaskVolumeDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Host
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskVolumeHostDetailsTypeDef]


# AwsEcsTaskVolumeHostDetailsTypeDef

### SourcePath
- **Type**: typing.Optional[str]


# AwsEfsAccessPointDetailsExtraOutputTypeDef

### AccessPointId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### PosixUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointPosixUserDetailsExtraOutputTypeDef]

### RootDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointRootDirectoryDetailsTypeDef]


# AwsEfsAccessPointDetailsOutputTypeDef

### AccessPointId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### PosixUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointPosixUserDetailsOutputTypeDef]

### RootDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointRootDirectoryDetailsTypeDef]


# AwsEfsAccessPointDetailsTypeDef

### AccessPointId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### PosixUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointPosixUserDetailsTypeDef]

### RootDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointRootDirectoryDetailsTypeDef]


# AwsEfsAccessPointPosixUserDetailsExtraOutputTypeDef

### Gid
- **Type**: typing.Optional[str]

### SecondaryGids
- **Type**: typing.Optional[typing.List[str]]

### Uid
- **Type**: typing.Optional[str]


# AwsEfsAccessPointPosixUserDetailsOutputTypeDef

### Gid
- **Type**: typing.Optional[str]

### SecondaryGids
- **Type**: typing.Optional[typing.List[str]]

### Uid
- **Type**: typing.Optional[str]


# AwsEfsAccessPointPosixUserDetailsTypeDef

### Gid
- **Type**: typing.Optional[str]

### SecondaryGids
- **Type**: typing.Optional[typing.Sequence[str]]

### Uid
- **Type**: typing.Optional[str]


# AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef

### OwnerGid
- **Type**: typing.Optional[str]

### OwnerUid
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[str]


# AwsEfsAccessPointRootDirectoryDetailsTypeDef

### CreationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef]

### Path
- **Type**: typing.Optional[str]


# AwsEksClusterDetailsExtraOutputTypeDef

### Arn
- **Type**: typing.Optional[str]

### CertificateAuthorityData
- **Type**: typing.Optional[str]

### ClusterStatus
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ResourcesVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterResourcesVpcConfigDetailsExtraOutputTypeDef]

### RoleArn
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterLoggingDetailsExtraOutputTypeDef]


# AwsEksClusterDetailsOutputTypeDef

### Arn
- **Type**: typing.Optional[str]

### CertificateAuthorityData
- **Type**: typing.Optional[str]

### ClusterStatus
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ResourcesVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef]

### RoleArn
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterLoggingDetailsOutputTypeDef]


# AwsEksClusterDetailsTypeDef

### Arn
- **Type**: typing.Optional[str]

### CertificateAuthorityData
- **Type**: typing.Optional[str]

### ClusterStatus
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ResourcesVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterResourcesVpcConfigDetailsTypeDef]

### RoleArn
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterLoggingDetailsTypeDef]


# AwsEksClusterLoggingClusterLoggingDetailsExtraOutputTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### Types
- **Type**: typing.Optional[typing.List[str]]


# AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### Types
- **Type**: typing.Optional[typing.List[str]]


# AwsEksClusterLoggingClusterLoggingDetailsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### Types
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsEksClusterLoggingDetailsExtraOutputTypeDef

### ClusterLogging
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterLoggingClusterLoggingDetailsExtraOutputTypeDef]]


# AwsEksClusterLoggingDetailsOutputTypeDef

### ClusterLogging
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef]]


# AwsEksClusterLoggingDetailsTypeDef

### ClusterLogging
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterLoggingClusterLoggingDetailsTypeDef]]


# AwsEksClusterResourcesVpcConfigDetailsExtraOutputTypeDef

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### EndpointPublicAccess
- **Type**: typing.Optional[bool]


# AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### EndpointPublicAccess
- **Type**: typing.Optional[bool]


# AwsEksClusterResourcesVpcConfigDetailsTypeDef

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### EndpointPublicAccess
- **Type**: typing.Optional[bool]


# AwsElasticBeanstalkEnvironmentDetailsExtraOutputTypeDef

### ApplicationName
- **Type**: typing.Optional[str]

### Cname
- **Type**: typing.Optional[str]

### DateCreated
- **Type**: typing.Optional[str]

### DateUpdated
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndpointUrl
- **Type**: typing.Optional[str]

### EnvironmentArn
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentLinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]]

### EnvironmentName
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]]

### PlatformArn
- **Type**: typing.Optional[str]

### SolutionStackName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Tier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentTierTypeDef]

### VersionLabel
- **Type**: typing.Optional[str]


# AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef

### ApplicationName
- **Type**: typing.Optional[str]

### Cname
- **Type**: typing.Optional[str]

### DateCreated
- **Type**: typing.Optional[str]

### DateUpdated
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndpointUrl
- **Type**: typing.Optional[str]

### EnvironmentArn
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentLinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]]

### EnvironmentName
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]]

### PlatformArn
- **Type**: typing.Optional[str]

### SolutionStackName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Tier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentTierTypeDef]

### VersionLabel
- **Type**: typing.Optional[str]


# AwsElasticBeanstalkEnvironmentDetailsTypeDef

### ApplicationName
- **Type**: typing.Optional[str]

### Cname
- **Type**: typing.Optional[str]

### DateCreated
- **Type**: typing.Optional[str]

### DateUpdated
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndpointUrl
- **Type**: typing.Optional[str]

### EnvironmentArn
- **Type**: typing.Optional[str]

### EnvironmentId
- **Type**: typing.Optional[str]

### EnvironmentLinks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]]

### EnvironmentName
- **Type**: typing.Optional[str]

### OptionSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]]

### PlatformArn
- **Type**: typing.Optional[str]

### SolutionStackName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Tier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentTierTypeDef]

### VersionLabel
- **Type**: typing.Optional[str]


# AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef

### EnvironmentName
- **Type**: typing.Optional[str]

### LinkName
- **Type**: typing.Optional[str]


# AwsElasticBeanstalkEnvironmentOptionSettingTypeDef

### Namespace
- **Type**: typing.Optional[str]

### OptionName
- **Type**: typing.Optional[str]

### ResourceName
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsElasticBeanstalkEnvironmentTierTypeDef

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# AwsElasticsearchDomainDetailsExtraOutputTypeDef

### AccessPolicies
- **Type**: typing.Optional[str]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainDomainEndpointOptionsTypeDef]

### DomainId
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.Dict[str, str]]

### ElasticsearchVersion
- **Type**: typing.Optional[str]

### ElasticsearchClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainLogPublishingOptionsTypeDef]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef]

### ServiceSoftwareOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainServiceSoftwareOptionsTypeDef]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainVPCOptionsExtraOutputTypeDef]


# AwsElasticsearchDomainDetailsOutputTypeDef

### AccessPolicies
- **Type**: typing.Optional[str]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainDomainEndpointOptionsTypeDef]

### DomainId
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.Dict[str, str]]

### ElasticsearchVersion
- **Type**: typing.Optional[str]

### ElasticsearchClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainLogPublishingOptionsTypeDef]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef]

### ServiceSoftwareOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainServiceSoftwareOptionsTypeDef]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainVPCOptionsOutputTypeDef]


# AwsElasticsearchDomainDetailsTypeDef

### AccessPolicies
- **Type**: typing.Optional[str]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainDomainEndpointOptionsTypeDef]

### DomainId
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ElasticsearchVersion
- **Type**: typing.Optional[str]

### ElasticsearchClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainLogPublishingOptionsTypeDef]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef]

### ServiceSoftwareOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainServiceSoftwareOptionsTypeDef]

### VPCOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainVPCOptionsTypeDef]


# AwsElasticsearchDomainDomainEndpointOptionsTypeDef

### EnforceHTTPS
- **Type**: typing.Optional[bool]

### TLSSecurityPolicy
- **Type**: typing.Optional[str]


# AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef

### DedicatedMasterCount
- **Type**: typing.Optional[int]

### DedicatedMasterEnabled
- **Type**: typing.Optional[bool]

### DedicatedMasterType
- **Type**: typing.Optional[str]

### InstanceCount
- **Type**: typing.Optional[int]

### InstanceType
- **Type**: typing.Optional[str]

### ZoneAwarenessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef]

### ZoneAwarenessEnabled
- **Type**: typing.Optional[bool]


# AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef

### AvailabilityZoneCount
- **Type**: typing.Optional[int]


# AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]


# AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]


# AwsElasticsearchDomainLogPublishingOptionsTypeDef

### IndexSlowLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef]

### SearchSlowLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef]

### AuditLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef]


# AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# AwsElasticsearchDomainServiceSoftwareOptionsTypeDef

### AutomatedUpdateDate
- **Type**: typing.Optional[str]

### Cancellable
- **Type**: typing.Optional[bool]

### CurrentVersion
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### NewVersion
- **Type**: typing.Optional[str]

### UpdateAvailable
- **Type**: typing.Optional[bool]

### UpdateStatus
- **Type**: typing.Optional[str]


# AwsElasticsearchDomainVPCOptionsExtraOutputTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### VPCId
- **Type**: typing.Optional[str]


# AwsElasticsearchDomainVPCOptionsOutputTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### VPCId
- **Type**: typing.Optional[str]


# AwsElasticsearchDomainVPCOptionsTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### VPCId
- **Type**: typing.Optional[str]


# AwsElbAppCookieStickinessPolicyTypeDef

### CookieName
- **Type**: typing.Optional[str]

### PolicyName
- **Type**: typing.Optional[str]


# AwsElbLbCookieStickinessPolicyTypeDef

### CookieExpirationPeriod
- **Type**: typing.Optional[int]

### PolicyName
- **Type**: typing.Optional[str]


# AwsElbLoadBalancerAccessLogTypeDef

### EmitInterval
- **Type**: typing.Optional[int]

### Enabled
- **Type**: typing.Optional[bool]

### S3BucketName
- **Type**: typing.Optional[str]

### S3BucketPrefix
- **Type**: typing.Optional[str]


# AwsElbLoadBalancerAdditionalAttributeTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsElbLoadBalancerAttributesExtraOutputTypeDef

### AccessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAccessLogTypeDef]

### ConnectionDraining
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerConnectionDrainingTypeDef]

### ConnectionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerConnectionSettingsTypeDef]

### CrossZoneLoadBalancing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef]

### AdditionalAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAdditionalAttributeTypeDef]]


# AwsElbLoadBalancerAttributesOutputTypeDef

### AccessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAccessLogTypeDef]

### ConnectionDraining
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerConnectionDrainingTypeDef]

### ConnectionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerConnectionSettingsTypeDef]

### CrossZoneLoadBalancing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef]

### AdditionalAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAdditionalAttributeTypeDef]]


# AwsElbLoadBalancerAttributesTypeDef

### AccessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAccessLogTypeDef]

### ConnectionDraining
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerConnectionDrainingTypeDef]

### ConnectionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerConnectionSettingsTypeDef]

### CrossZoneLoadBalancing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef]

### AdditionalAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAdditionalAttributeTypeDef]]


# AwsElbLoadBalancerBackendServerDescriptionExtraOutputTypeDef

### InstancePort
- **Type**: typing.Optional[int]

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]


# AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef

### InstancePort
- **Type**: typing.Optional[int]

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]


# AwsElbLoadBalancerBackendServerDescriptionTypeDef

### InstancePort
- **Type**: typing.Optional[int]

### PolicyNames
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsElbLoadBalancerConnectionDrainingTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### Timeout
- **Type**: typing.Optional[int]


# AwsElbLoadBalancerConnectionSettingsTypeDef

### IdleTimeout
- **Type**: typing.Optional[int]


# AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# AwsElbLoadBalancerDetailsExtraOutputTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### BackendServerDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerBackendServerDescriptionExtraOutputTypeDef]]

### CanonicalHostedZoneName
- **Type**: typing.Optional[str]

### CanonicalHostedZoneNameID
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### HealthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerHealthCheckTypeDef]

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerInstanceTypeDef]]

### ListenerDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerListenerDescriptionExtraOutputTypeDef]]

### LoadBalancerAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAttributesExtraOutputTypeDef]

### LoadBalancerName
- **Type**: typing.Optional[str]

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerPoliciesExtraOutputTypeDef]

### Scheme
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### SourceSecurityGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerSourceSecurityGroupTypeDef]

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### VpcId
- **Type**: typing.Optional[str]


# AwsElbLoadBalancerDetailsOutputTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### BackendServerDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef]]

### CanonicalHostedZoneName
- **Type**: typing.Optional[str]

### CanonicalHostedZoneNameID
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### HealthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerHealthCheckTypeDef]

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerInstanceTypeDef]]

### ListenerDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerListenerDescriptionOutputTypeDef]]

### LoadBalancerAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAttributesOutputTypeDef]

### LoadBalancerName
- **Type**: typing.Optional[str]

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerPoliciesOutputTypeDef]

### Scheme
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### SourceSecurityGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerSourceSecurityGroupTypeDef]

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### VpcId
- **Type**: typing.Optional[str]


# AwsElbLoadBalancerDetailsTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### BackendServerDescriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerBackendServerDescriptionTypeDef]]

### CanonicalHostedZoneName
- **Type**: typing.Optional[str]

### CanonicalHostedZoneNameID
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### HealthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerHealthCheckTypeDef]

### Instances
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerInstanceTypeDef]]

### ListenerDescriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerListenerDescriptionTypeDef]]

### LoadBalancerAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerAttributesTypeDef]

### LoadBalancerName
- **Type**: typing.Optional[str]

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerPoliciesTypeDef]

### Scheme
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### SourceSecurityGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerSourceSecurityGroupTypeDef]

### Subnets
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcId
- **Type**: typing.Optional[str]


# AwsElbLoadBalancerHealthCheckTypeDef

### HealthyThreshold
- **Type**: typing.Optional[int]

### Interval
- **Type**: typing.Optional[int]

### Target
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### UnhealthyThreshold
- **Type**: typing.Optional[int]


# AwsElbLoadBalancerInstanceTypeDef

### InstanceId
- **Type**: typing.Optional[str]


# AwsElbLoadBalancerListenerDescriptionExtraOutputTypeDef

### Listener
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerListenerTypeDef]

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]


# AwsElbLoadBalancerListenerDescriptionOutputTypeDef

### Listener
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerListenerTypeDef]

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]


# AwsElbLoadBalancerListenerDescriptionTypeDef

### Listener
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerListenerTypeDef]

### PolicyNames
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsElbLoadBalancerListenerTypeDef

### InstancePort
- **Type**: typing.Optional[int]

### InstanceProtocol
- **Type**: typing.Optional[str]

### LoadBalancerPort
- **Type**: typing.Optional[int]

### Protocol
- **Type**: typing.Optional[str]

### SslCertificateId
- **Type**: typing.Optional[str]


# AwsElbLoadBalancerPoliciesExtraOutputTypeDef

### AppCookieStickinessPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbAppCookieStickinessPolicyTypeDef]]

### LbCookieStickinessPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLbCookieStickinessPolicyTypeDef]]

### OtherPolicies
- **Type**: typing.Optional[typing.List[str]]


# AwsElbLoadBalancerPoliciesOutputTypeDef

### AppCookieStickinessPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbAppCookieStickinessPolicyTypeDef]]

### LbCookieStickinessPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLbCookieStickinessPolicyTypeDef]]

### OtherPolicies
- **Type**: typing.Optional[typing.List[str]]


# AwsElbLoadBalancerPoliciesTypeDef

### AppCookieStickinessPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbAppCookieStickinessPolicyTypeDef]]

### LbCookieStickinessPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLbCookieStickinessPolicyTypeDef]]

### OtherPolicies
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsElbLoadBalancerSourceSecurityGroupTypeDef

### GroupName
- **Type**: typing.Optional[str]

### OwnerAlias
- **Type**: typing.Optional[str]


# AwsElbv2LoadBalancerAttributeTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsElbv2LoadBalancerDetailsExtraOutputTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AvailabilityZoneTypeDef]]

### CanonicalHostedZoneId
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[str]

### DNSName
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[str]

### Scheme
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.LoadBalancerStateTypeDef]

### Type
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### LoadBalancerAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbv2LoadBalancerAttributeTypeDef]]


# AwsElbv2LoadBalancerDetailsOutputTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AvailabilityZoneTypeDef]]

### CanonicalHostedZoneId
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[str]

### DNSName
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[str]

### Scheme
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.LoadBalancerStateTypeDef]

### Type
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### LoadBalancerAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbv2LoadBalancerAttributeTypeDef]]


# AwsElbv2LoadBalancerDetailsTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AvailabilityZoneTypeDef]]

### CanonicalHostedZoneId
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[str]

### DNSName
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[str]

### Scheme
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.LoadBalancerStateTypeDef]

### Type
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### LoadBalancerAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbv2LoadBalancerAttributeTypeDef]]


# AwsEventSchemasRegistryDetailsTypeDef

### Description
- **Type**: typing.Optional[str]

### RegistryArn
- **Type**: typing.Optional[str]

### RegistryName
- **Type**: typing.Optional[str]


# AwsEventsEndpointDetailsExtraOutputTypeDef

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]

### EndpointUrl
- **Type**: typing.Optional[str]

### EventBuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointEventBusesDetailsTypeDef]]

### Name
- **Type**: typing.Optional[str]

### ReplicationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointReplicationConfigDetailsTypeDef]

### RoleArn
- **Type**: typing.Optional[str]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointRoutingConfigDetailsTypeDef]

### State
- **Type**: typing.Optional[str]

### StateReason
- **Type**: typing.Optional[str]


# AwsEventsEndpointDetailsOutputTypeDef

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]

### EndpointUrl
- **Type**: typing.Optional[str]

### EventBuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointEventBusesDetailsTypeDef]]

### Name
- **Type**: typing.Optional[str]

### ReplicationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointReplicationConfigDetailsTypeDef]

### RoleArn
- **Type**: typing.Optional[str]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointRoutingConfigDetailsTypeDef]

### State
- **Type**: typing.Optional[str]

### StateReason
- **Type**: typing.Optional[str]


# AwsEventsEndpointDetailsTypeDef

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]

### EndpointUrl
- **Type**: typing.Optional[str]

### EventBuses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointEventBusesDetailsTypeDef]]

### Name
- **Type**: typing.Optional[str]

### ReplicationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointReplicationConfigDetailsTypeDef]

### RoleArn
- **Type**: typing.Optional[str]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointRoutingConfigDetailsTypeDef]

### State
- **Type**: typing.Optional[str]

### StateReason
- **Type**: typing.Optional[str]


# AwsEventsEndpointEventBusesDetailsTypeDef

### EventBusArn
- **Type**: typing.Optional[str]


# AwsEventsEndpointReplicationConfigDetailsTypeDef

### State
- **Type**: typing.Optional[str]


# AwsEventsEndpointRoutingConfigDetailsTypeDef

### FailoverConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef]


# AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef

### Primary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef]

### Secondary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef]


# AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef

### HealthCheck
- **Type**: typing.Optional[str]


# AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef

### Route
- **Type**: typing.Optional[str]


# AwsEventsEventbusDetailsTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Policy
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDataSourcesDetailsTypeDef

### CloudTrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef]

### DnsLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef]

### FlowLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef]

### Kubernetes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef]

### MalwareProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef]

### S3Logs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef]


# AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef

### AuditLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef]


# AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef

### ScanEc2InstanceWithFindings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef]

### ServiceRole
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef

### EbsVolumes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef]


# AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef

### Reason
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDetailsExtraOutputTypeDef

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesDetailsTypeDef]

### Features
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorFeaturesDetailsTypeDef]]

### FindingPublishingFrequency
- **Type**: typing.Optional[str]

### ServiceRole
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDetailsOutputTypeDef

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesDetailsTypeDef]

### Features
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorFeaturesDetailsTypeDef]]

### FindingPublishingFrequency
- **Type**: typing.Optional[str]

### ServiceRole
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorDetailsTypeDef

### DataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDataSourcesDetailsTypeDef]

### Features
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorFeaturesDetailsTypeDef]]

### FindingPublishingFrequency
- **Type**: typing.Optional[str]

### ServiceRole
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsGuardDutyDetectorFeaturesDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsIamAccessKeyDetailsTypeDef

### UserName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### CreatedAt
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### PrincipalType
- **Type**: typing.Optional[str]

### PrincipalName
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### AccessKeyId
- **Type**: typing.Optional[str]

### SessionContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAccessKeySessionContextTypeDef]


# AwsIamAccessKeySessionContextAttributesTypeDef

### MfaAuthenticated
- **Type**: typing.Optional[bool]

### CreationDate
- **Type**: typing.Optional[str]


# AwsIamAccessKeySessionContextSessionIssuerTypeDef

### Type
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]


# AwsIamAccessKeySessionContextTypeDef

### Attributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAccessKeySessionContextAttributesTypeDef]

### SessionIssuer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAccessKeySessionContextSessionIssuerTypeDef]


# AwsIamAttachedManagedPolicyTypeDef

### PolicyName
- **Type**: typing.Optional[str]

### PolicyArn
- **Type**: typing.Optional[str]


# AwsIamGroupDetailsExtraOutputTypeDef

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicyTypeDef]]

### CreateDate
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### GroupPolicyList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamGroupPolicyTypeDef]]

### Path
- **Type**: typing.Optional[str]


# AwsIamGroupDetailsOutputTypeDef

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicyTypeDef]]

### CreateDate
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### GroupPolicyList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamGroupPolicyTypeDef]]

### Path
- **Type**: typing.Optional[str]


# AwsIamGroupDetailsTypeDef

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicyTypeDef]]

### CreateDate
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### GroupPolicyList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamGroupPolicyTypeDef]]

### Path
- **Type**: typing.Optional[str]


# AwsIamGroupPolicyTypeDef

### PolicyName
- **Type**: typing.Optional[str]


# AwsIamInstanceProfileExtraOutputTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[str]

### InstanceProfileId
- **Type**: typing.Optional[str]

### InstanceProfileName
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Roles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamInstanceProfileRoleTypeDef]]


# AwsIamInstanceProfileOutputTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[str]

### InstanceProfileId
- **Type**: typing.Optional[str]

### InstanceProfileName
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Roles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamInstanceProfileRoleTypeDef]]


# AwsIamInstanceProfileRoleTypeDef

### Arn
- **Type**: typing.Optional[str]

### AssumeRolePolicyDocument
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### RoleId
- **Type**: typing.Optional[str]

### RoleName
- **Type**: typing.Optional[str]


# AwsIamInstanceProfileTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[str]

### InstanceProfileId
- **Type**: typing.Optional[str]

### InstanceProfileName
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Roles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamInstanceProfileRoleTypeDef]]


# AwsIamPermissionsBoundaryTypeDef

### PermissionsBoundaryArn
- **Type**: typing.Optional[str]

### PermissionsBoundaryType
- **Type**: typing.Optional[str]


# AwsIamPolicyDetailsExtraOutputTypeDef

### AttachmentCount
- **Type**: typing.Optional[int]

### CreateDate
- **Type**: typing.Optional[str]

### DefaultVersionId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IsAttachable
- **Type**: typing.Optional[bool]

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundaryUsageCount
- **Type**: typing.Optional[int]

### PolicyId
- **Type**: typing.Optional[str]

### PolicyName
- **Type**: typing.Optional[str]

### PolicyVersionList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPolicyVersionTypeDef]]

### UpdateDate
- **Type**: typing.Optional[str]


# AwsIamPolicyDetailsOutputTypeDef

### AttachmentCount
- **Type**: typing.Optional[int]

### CreateDate
- **Type**: typing.Optional[str]

### DefaultVersionId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IsAttachable
- **Type**: typing.Optional[bool]

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundaryUsageCount
- **Type**: typing.Optional[int]

### PolicyId
- **Type**: typing.Optional[str]

### PolicyName
- **Type**: typing.Optional[str]

### PolicyVersionList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPolicyVersionTypeDef]]

### UpdateDate
- **Type**: typing.Optional[str]


# AwsIamPolicyDetailsTypeDef

### AttachmentCount
- **Type**: typing.Optional[int]

### CreateDate
- **Type**: typing.Optional[str]

### DefaultVersionId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### IsAttachable
- **Type**: typing.Optional[bool]

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundaryUsageCount
- **Type**: typing.Optional[int]

### PolicyId
- **Type**: typing.Optional[str]

### PolicyName
- **Type**: typing.Optional[str]

### PolicyVersionList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPolicyVersionTypeDef]]

### UpdateDate
- **Type**: typing.Optional[str]


# AwsIamPolicyVersionTypeDef

### VersionId
- **Type**: typing.Optional[str]

### IsDefaultVersion
- **Type**: typing.Optional[bool]

### CreateDate
- **Type**: typing.Optional[str]


# AwsIamRoleDetailsExtraOutputTypeDef

### AssumeRolePolicyDocument
- **Type**: typing.Optional[str]

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicyTypeDef]]

### CreateDate
- **Type**: typing.Optional[str]

### InstanceProfileList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamInstanceProfileExtraOutputTypeDef]]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPermissionsBoundaryTypeDef]

### RoleId
- **Type**: typing.Optional[str]

### RoleName
- **Type**: typing.Optional[str]

### RolePolicyList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamRolePolicyTypeDef]]

### MaxSessionDuration
- **Type**: typing.Optional[int]

### Path
- **Type**: typing.Optional[str]


# AwsIamRoleDetailsOutputTypeDef

### AssumeRolePolicyDocument
- **Type**: typing.Optional[str]

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicyTypeDef]]

### CreateDate
- **Type**: typing.Optional[str]

### InstanceProfileList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamInstanceProfileOutputTypeDef]]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPermissionsBoundaryTypeDef]

### RoleId
- **Type**: typing.Optional[str]

### RoleName
- **Type**: typing.Optional[str]

### RolePolicyList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamRolePolicyTypeDef]]

### MaxSessionDuration
- **Type**: typing.Optional[int]

### Path
- **Type**: typing.Optional[str]


# AwsIamRoleDetailsTypeDef

### AssumeRolePolicyDocument
- **Type**: typing.Optional[str]

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicyTypeDef]]

### CreateDate
- **Type**: typing.Optional[str]

### InstanceProfileList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamInstanceProfileTypeDef]]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPermissionsBoundaryTypeDef]

### RoleId
- **Type**: typing.Optional[str]

### RoleName
- **Type**: typing.Optional[str]

### RolePolicyList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamRolePolicyTypeDef]]

### MaxSessionDuration
- **Type**: typing.Optional[int]

### Path
- **Type**: typing.Optional[str]


# AwsIamRolePolicyTypeDef

### PolicyName
- **Type**: typing.Optional[str]


# AwsIamUserDetailsExtraOutputTypeDef

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicyTypeDef]]

### CreateDate
- **Type**: typing.Optional[str]

### GroupList
- **Type**: typing.Optional[typing.List[str]]

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPermissionsBoundaryTypeDef]

### UserId
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### UserPolicyList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamUserPolicyTypeDef]]


# AwsIamUserDetailsOutputTypeDef

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicyTypeDef]]

### CreateDate
- **Type**: typing.Optional[str]

### GroupList
- **Type**: typing.Optional[typing.List[str]]

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPermissionsBoundaryTypeDef]

### UserId
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### UserPolicyList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamUserPolicyTypeDef]]


# AwsIamUserDetailsTypeDef

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAttachedManagedPolicyTypeDef]]

### CreateDate
- **Type**: typing.Optional[str]

### GroupList
- **Type**: typing.Optional[typing.Sequence[str]]

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPermissionsBoundaryTypeDef]

### UserId
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### UserPolicyList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamUserPolicyTypeDef]]


# AwsIamUserPolicyTypeDef

### PolicyName
- **Type**: typing.Optional[str]


# AwsKinesisStreamDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### StreamEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsKinesisStreamStreamEncryptionDetailsTypeDef]

### ShardCount
- **Type**: typing.Optional[int]

### RetentionPeriodHours
- **Type**: typing.Optional[int]


# AwsKinesisStreamStreamEncryptionDetailsTypeDef

### EncryptionType
- **Type**: typing.Optional[str]

### KeyId
- **Type**: typing.Optional[str]


# AwsKmsKeyDetailsTypeDef

### AWSAccountId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[float]

### KeyId
- **Type**: typing.Optional[str]

### KeyManager
- **Type**: typing.Optional[str]

### KeyState
- **Type**: typing.Optional[str]

### Origin
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### KeyRotationStatus
- **Type**: typing.Optional[bool]


# AwsLambdaFunctionCodeTypeDef

### S3Bucket
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]

### S3ObjectVersion
- **Type**: typing.Optional[str]

### ZipFile
- **Type**: typing.Optional[str]


# AwsLambdaFunctionDeadLetterConfigTypeDef

### TargetArn
- **Type**: typing.Optional[str]


# AwsLambdaFunctionDetailsExtraOutputTypeDef

### Code
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionCodeTypeDef]

### CodeSha256
- **Type**: typing.Optional[str]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionDeadLetterConfigTypeDef]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionEnvironmentExtraOutputTypeDef]

### FunctionName
- **Type**: typing.Optional[str]

### Handler
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### LastModified
- **Type**: typing.Optional[str]

### Layers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionLayerTypeDef]]

### MasterArn
- **Type**: typing.Optional[str]

### MemorySize
- **Type**: typing.Optional[int]

### RevisionId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### Runtime
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### TracingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionTracingConfigTypeDef]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionVpcConfigExtraOutputTypeDef]

### Version
- **Type**: typing.Optional[str]

### Architectures
- **Type**: typing.Optional[typing.List[str]]

### PackageType
- **Type**: typing.Optional[str]


# AwsLambdaFunctionDetailsOutputTypeDef

### Code
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionCodeTypeDef]

### CodeSha256
- **Type**: typing.Optional[str]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionDeadLetterConfigTypeDef]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionEnvironmentOutputTypeDef]

### FunctionName
- **Type**: typing.Optional[str]

### Handler
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### LastModified
- **Type**: typing.Optional[str]

### Layers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionLayerTypeDef]]

### MasterArn
- **Type**: typing.Optional[str]

### MemorySize
- **Type**: typing.Optional[int]

### RevisionId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### Runtime
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### TracingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionTracingConfigTypeDef]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionVpcConfigOutputTypeDef]

### Version
- **Type**: typing.Optional[str]

### Architectures
- **Type**: typing.Optional[typing.List[str]]

### PackageType
- **Type**: typing.Optional[str]


# AwsLambdaFunctionDetailsTypeDef

### Code
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionCodeTypeDef]

### CodeSha256
- **Type**: typing.Optional[str]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionDeadLetterConfigTypeDef]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionEnvironmentTypeDef]

### FunctionName
- **Type**: typing.Optional[str]

### Handler
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### LastModified
- **Type**: typing.Optional[str]

### Layers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionLayerTypeDef]]

### MasterArn
- **Type**: typing.Optional[str]

### MemorySize
- **Type**: typing.Optional[int]

### RevisionId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### Runtime
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### TracingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionTracingConfigTypeDef]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionVpcConfigTypeDef]

### Version
- **Type**: typing.Optional[str]

### Architectures
- **Type**: typing.Optional[typing.Sequence[str]]

### PackageType
- **Type**: typing.Optional[str]


# AwsLambdaFunctionEnvironmentErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# AwsLambdaFunctionEnvironmentExtraOutputTypeDef

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionEnvironmentErrorTypeDef]


# AwsLambdaFunctionEnvironmentOutputTypeDef

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionEnvironmentErrorTypeDef]


# AwsLambdaFunctionEnvironmentTypeDef

### Variables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionEnvironmentErrorTypeDef]


# AwsLambdaFunctionLayerTypeDef

### Arn
- **Type**: typing.Optional[str]

### CodeSize
- **Type**: typing.Optional[int]


# AwsLambdaFunctionTracingConfigTypeDef

### Mode
- **Type**: typing.Optional[str]


# AwsLambdaFunctionVpcConfigExtraOutputTypeDef

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### VpcId
- **Type**: typing.Optional[str]


# AwsLambdaFunctionVpcConfigOutputTypeDef

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### VpcId
- **Type**: typing.Optional[str]


# AwsLambdaFunctionVpcConfigTypeDef

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcId
- **Type**: typing.Optional[str]


# AwsLambdaLayerVersionDetailsExtraOutputTypeDef

### Version
- **Type**: typing.Optional[int]

### CompatibleRuntimes
- **Type**: typing.Optional[typing.List[str]]

### CreatedDate
- **Type**: typing.Optional[str]


# AwsLambdaLayerVersionDetailsOutputTypeDef

### Version
- **Type**: typing.Optional[int]

### CompatibleRuntimes
- **Type**: typing.Optional[typing.List[str]]

### CreatedDate
- **Type**: typing.Optional[str]


# AwsLambdaLayerVersionDetailsTypeDef

### Version
- **Type**: typing.Optional[int]

### CompatibleRuntimes
- **Type**: typing.Optional[typing.Sequence[str]]

### CreatedDate
- **Type**: typing.Optional[str]


# AwsMountPointTypeDef

### SourceVolume
- **Type**: typing.Optional[str]

### ContainerPath
- **Type**: typing.Optional[str]


# AwsMskClusterClusterInfoClientAuthenticationDetailsExtraOutputTypeDef

### Sasl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef]

### Unauthenticated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef]

### Tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationTlsDetailsExtraOutputTypeDef]


# AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef

### Sasl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef]

### Unauthenticated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef]

### Tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef]


# AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef

### Sasl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef]

### Unauthenticated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef]

### Tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef]


# AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef

### Iam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef]

### Scram
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef]


# AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# AwsMskClusterClusterInfoClientAuthenticationTlsDetailsExtraOutputTypeDef

### CertificateAuthorityArnList
- **Type**: typing.Optional[typing.List[str]]

### Enabled
- **Type**: typing.Optional[bool]


# AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef

### CertificateAuthorityArnList
- **Type**: typing.Optional[typing.List[str]]

### Enabled
- **Type**: typing.Optional[bool]


# AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef

### CertificateAuthorityArnList
- **Type**: typing.Optional[typing.Sequence[str]]

### Enabled
- **Type**: typing.Optional[bool]


# AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# AwsMskClusterClusterInfoDetailsExtraOutputTypeDef

### EncryptionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef]

### CurrentVersion
- **Type**: typing.Optional[str]

### NumberOfBrokerNodes
- **Type**: typing.Optional[int]

### ClusterName
- **Type**: typing.Optional[str]

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationDetailsExtraOutputTypeDef]

### EnhancedMonitoring
- **Type**: typing.Optional[str]


# AwsMskClusterClusterInfoDetailsOutputTypeDef

### EncryptionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef]

### CurrentVersion
- **Type**: typing.Optional[str]

### NumberOfBrokerNodes
- **Type**: typing.Optional[int]

### ClusterName
- **Type**: typing.Optional[str]

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef]

### EnhancedMonitoring
- **Type**: typing.Optional[str]


# AwsMskClusterClusterInfoDetailsTypeDef

### EncryptionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef]

### CurrentVersion
- **Type**: typing.Optional[str]

### NumberOfBrokerNodes
- **Type**: typing.Optional[int]

### ClusterName
- **Type**: typing.Optional[str]

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef]

### EnhancedMonitoring
- **Type**: typing.Optional[str]


# AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef

### EncryptionInTransit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef]

### EncryptionAtRest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef]


# AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef

### DataVolumeKMSKeyId
- **Type**: typing.Optional[str]


# AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef

### InCluster
- **Type**: typing.Optional[bool]

### ClientBroker
- **Type**: typing.Optional[str]


# AwsMskClusterDetailsExtraOutputTypeDef

### ClusterInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoDetailsExtraOutputTypeDef]


# AwsMskClusterDetailsOutputTypeDef

### ClusterInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoDetailsOutputTypeDef]


# AwsMskClusterDetailsTypeDef

### ClusterInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterClusterInfoDetailsTypeDef]


# AwsNetworkFirewallFirewallDetailsExtraOutputTypeDef

### DeleteProtection
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallId
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]

### FirewallPolicyArn
- **Type**: typing.Optional[str]

### FirewallPolicyChangeProtection
- **Type**: typing.Optional[bool]

### SubnetChangeProtection
- **Type**: typing.Optional[bool]

### SubnetMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]]

### VpcId
- **Type**: typing.Optional[str]


# AwsNetworkFirewallFirewallDetailsOutputTypeDef

### DeleteProtection
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallId
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]

### FirewallPolicyArn
- **Type**: typing.Optional[str]

### FirewallPolicyChangeProtection
- **Type**: typing.Optional[bool]

### SubnetChangeProtection
- **Type**: typing.Optional[bool]

### SubnetMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]]

### VpcId
- **Type**: typing.Optional[str]


# AwsNetworkFirewallFirewallDetailsTypeDef

### DeleteProtection
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### FirewallArn
- **Type**: typing.Optional[str]

### FirewallId
- **Type**: typing.Optional[str]

### FirewallName
- **Type**: typing.Optional[str]

### FirewallPolicyArn
- **Type**: typing.Optional[str]

### FirewallPolicyChangeProtection
- **Type**: typing.Optional[bool]

### SubnetChangeProtection
- **Type**: typing.Optional[bool]

### SubnetMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]]

### VpcId
- **Type**: typing.Optional[str]


# AwsNetworkFirewallFirewallPolicyDetailsExtraOutputTypeDef

### FirewallPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyDetailsExtraOutputTypeDef]

### FirewallPolicyArn
- **Type**: typing.Optional[str]

### FirewallPolicyId
- **Type**: typing.Optional[str]

### FirewallPolicyName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef

### FirewallPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyDetailsOutputTypeDef]

### FirewallPolicyArn
- **Type**: typing.Optional[str]

### FirewallPolicyId
- **Type**: typing.Optional[str]

### FirewallPolicyName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# AwsNetworkFirewallFirewallPolicyDetailsTypeDef

### FirewallPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyDetailsTypeDef]

### FirewallPolicyArn
- **Type**: typing.Optional[str]

### FirewallPolicyId
- **Type**: typing.Optional[str]

### FirewallPolicyName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef

### SubnetId
- **Type**: typing.Optional[str]


# AwsNetworkFirewallRuleGroupDetailsExtraOutputTypeDef

### Capacity
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### RuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupDetailsExtraOutputTypeDef]

### RuleGroupArn
- **Type**: typing.Optional[str]

### RuleGroupId
- **Type**: typing.Optional[str]

### RuleGroupName
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsNetworkFirewallRuleGroupDetailsOutputTypeDef

### Capacity
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### RuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupDetailsOutputTypeDef]

### RuleGroupArn
- **Type**: typing.Optional[str]

### RuleGroupId
- **Type**: typing.Optional[str]

### RuleGroupName
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsNetworkFirewallRuleGroupDetailsTypeDef

### Capacity
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### RuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupDetailsTypeDef]

### RuleGroupArn
- **Type**: typing.Optional[str]

### RuleGroupId
- **Type**: typing.Optional[str]

### RuleGroupName
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### InternalUserDatabaseEnabled
- **Type**: typing.Optional[bool]

### MasterUserOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef]


# AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef

### InstanceCount
- **Type**: typing.Optional[int]

### WarmEnabled
- **Type**: typing.Optional[bool]

### WarmCount
- **Type**: typing.Optional[int]

### DedicatedMasterEnabled
- **Type**: typing.Optional[bool]

### ZoneAwarenessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef]

### DedicatedMasterCount
- **Type**: typing.Optional[int]

### InstanceType
- **Type**: typing.Optional[str]

### WarmType
- **Type**: typing.Optional[str]

### ZoneAwarenessEnabled
- **Type**: typing.Optional[bool]

### DedicatedMasterType
- **Type**: typing.Optional[str]


# AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef

### AvailabilityZoneCount
- **Type**: typing.Optional[int]


# AwsOpenSearchServiceDomainDetailsExtraOutputTypeDef

### Arn
- **Type**: typing.Optional[str]

### AccessPolicies
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### DomainEndpoint
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef]

### ServiceSoftwareOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef]

### ClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef]

### VpcOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainVpcOptionsDetailsExtraOutputTypeDef]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef]

### DomainEndpoints
- **Type**: typing.Optional[typing.Dict[str, str]]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef]


# AwsOpenSearchServiceDomainDetailsOutputTypeDef

### Arn
- **Type**: typing.Optional[str]

### AccessPolicies
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### DomainEndpoint
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef]

### ServiceSoftwareOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef]

### ClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef]

### VpcOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef]

### DomainEndpoints
- **Type**: typing.Optional[typing.Dict[str, str]]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef]


# AwsOpenSearchServiceDomainDetailsTypeDef

### Arn
- **Type**: typing.Optional[str]

### AccessPolicies
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### DomainEndpoint
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### EncryptionAtRestOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef]

### NodeToNodeEncryptionOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef]

### ServiceSoftwareOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef]

### ClusterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef]

### DomainEndpointOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef]

### VpcOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef]

### LogPublishingOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef]

### DomainEndpoints
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AdvancedSecurityOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef]


# AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef

### CustomEndpointCertificateArn
- **Type**: typing.Optional[str]

### CustomEndpointEnabled
- **Type**: typing.Optional[bool]

### EnforceHTTPS
- **Type**: typing.Optional[bool]

### CustomEndpoint
- **Type**: typing.Optional[str]

### TLSSecurityPolicy
- **Type**: typing.Optional[str]


# AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]


# AwsOpenSearchServiceDomainLogPublishingOptionTypeDef

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]


# AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef

### IndexSlowLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainLogPublishingOptionTypeDef]

### SearchSlowLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainLogPublishingOptionTypeDef]

### AuditLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainLogPublishingOptionTypeDef]


# AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef

### MasterUserArn
- **Type**: typing.Optional[str]

### MasterUserName
- **Type**: typing.Optional[str]

### MasterUserPassword
- **Type**: typing.Optional[str]


# AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef

### AutomatedUpdateDate
- **Type**: typing.Optional[str]

### Cancellable
- **Type**: typing.Optional[bool]

### CurrentVersion
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### NewVersion
- **Type**: typing.Optional[str]

### UpdateAvailable
- **Type**: typing.Optional[bool]

### UpdateStatus
- **Type**: typing.Optional[str]

### OptionalDeployment
- **Type**: typing.Optional[bool]


# AwsOpenSearchServiceDomainVpcOptionsDetailsExtraOutputTypeDef

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]


# AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]


# AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsRdsDbClusterAssociatedRoleTypeDef

### RoleArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRdsDbClusterDetailsExtraOutputTypeDef

### AllocatedStorage
- **Type**: typing.Optional[int]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### ReaderEndpoint
- **Type**: typing.Optional[str]

### CustomEndpoints
- **Type**: typing.Optional[typing.List[str]]

### MultiAz
- **Type**: typing.Optional[bool]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### MasterUsername
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ReadReplicaIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceVpcSecurityGroupTypeDef]]

### HostedZoneId
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### DbClusterResourceId
- **Type**: typing.Optional[str]

### AssociatedRoles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterAssociatedRoleTypeDef]]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### EnabledCloudWatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### EngineMode
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### HttpEndpointEnabled
- **Type**: typing.Optional[bool]

### ActivityStreamStatus
- **Type**: typing.Optional[str]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### CrossAccountClone
- **Type**: typing.Optional[bool]

### DomainMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbDomainMembershipTypeDef]]

### DbClusterParameterGroup
- **Type**: typing.Optional[str]

### DbSubnetGroup
- **Type**: typing.Optional[str]

### DbClusterOptionGroupMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterOptionGroupMembershipTypeDef]]

### DbClusterIdentifier
- **Type**: typing.Optional[str]

### DbClusterMembers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterMemberTypeDef]]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]


# AwsRdsDbClusterDetailsOutputTypeDef

### AllocatedStorage
- **Type**: typing.Optional[int]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### ReaderEndpoint
- **Type**: typing.Optional[str]

### CustomEndpoints
- **Type**: typing.Optional[typing.List[str]]

### MultiAz
- **Type**: typing.Optional[bool]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### MasterUsername
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ReadReplicaIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceVpcSecurityGroupTypeDef]]

### HostedZoneId
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### DbClusterResourceId
- **Type**: typing.Optional[str]

### AssociatedRoles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterAssociatedRoleTypeDef]]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### EnabledCloudWatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### EngineMode
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### HttpEndpointEnabled
- **Type**: typing.Optional[bool]

### ActivityStreamStatus
- **Type**: typing.Optional[str]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### CrossAccountClone
- **Type**: typing.Optional[bool]

### DomainMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbDomainMembershipTypeDef]]

### DbClusterParameterGroup
- **Type**: typing.Optional[str]

### DbSubnetGroup
- **Type**: typing.Optional[str]

### DbClusterOptionGroupMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterOptionGroupMembershipTypeDef]]

### DbClusterIdentifier
- **Type**: typing.Optional[str]

### DbClusterMembers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterMemberTypeDef]]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]


# AwsRdsDbClusterDetailsTypeDef

### AllocatedStorage
- **Type**: typing.Optional[int]

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DatabaseName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Endpoint
- **Type**: typing.Optional[str]

### ReaderEndpoint
- **Type**: typing.Optional[str]

### CustomEndpoints
- **Type**: typing.Optional[typing.Sequence[str]]

### MultiAz
- **Type**: typing.Optional[bool]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### MasterUsername
- **Type**: typing.Optional[str]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### ReadReplicaIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceVpcSecurityGroupTypeDef]]

### HostedZoneId
- **Type**: typing.Optional[str]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### DbClusterResourceId
- **Type**: typing.Optional[str]

### AssociatedRoles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterAssociatedRoleTypeDef]]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### EnabledCloudWatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### EngineMode
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### HttpEndpointEnabled
- **Type**: typing.Optional[bool]

### ActivityStreamStatus
- **Type**: typing.Optional[str]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### CrossAccountClone
- **Type**: typing.Optional[bool]

### DomainMemberships
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbDomainMembershipTypeDef]]

### DbClusterParameterGroup
- **Type**: typing.Optional[str]

### DbSubnetGroup
- **Type**: typing.Optional[str]

### DbClusterOptionGroupMemberships
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterOptionGroupMembershipTypeDef]]

### DbClusterIdentifier
- **Type**: typing.Optional[str]

### DbClusterMembers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterMemberTypeDef]]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]


# AwsRdsDbClusterMemberTypeDef

### IsClusterWriter
- **Type**: typing.Optional[bool]

### PromotionTier
- **Type**: typing.Optional[int]

### DbInstanceIdentifier
- **Type**: typing.Optional[str]

### DbClusterParameterGroupStatus
- **Type**: typing.Optional[str]


# AwsRdsDbClusterOptionGroupMembershipTypeDef

### DbClusterOptionGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeExtraOutputTypeDef

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValues
- **Type**: typing.Optional[typing.List[str]]


# AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValues
- **Type**: typing.Optional[typing.List[str]]


# AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValues
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsRdsDbClusterSnapshotDetailsExtraOutputTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### SnapshotCreateTime
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### VpcId
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[int]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### DbClusterIdentifier
- **Type**: typing.Optional[str]

### DbClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### DbClusterSnapshotAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeExtraOutputTypeDef]]


# AwsRdsDbClusterSnapshotDetailsOutputTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### SnapshotCreateTime
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### VpcId
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[int]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### DbClusterIdentifier
- **Type**: typing.Optional[str]

### DbClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### DbClusterSnapshotAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef]]


# AwsRdsDbClusterSnapshotDetailsTypeDef

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### SnapshotCreateTime
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### VpcId
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[int]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### DbClusterIdentifier
- **Type**: typing.Optional[str]

### DbClusterSnapshotIdentifier
- **Type**: typing.Optional[str]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### DbClusterSnapshotAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef]]


# AwsRdsDbDomainMembershipTypeDef

### Domain
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Fqdn
- **Type**: typing.Optional[str]

### IamRoleName
- **Type**: typing.Optional[str]


# AwsRdsDbInstanceAssociatedRoleTypeDef

### RoleArn
- **Type**: typing.Optional[str]

### FeatureName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRdsDbInstanceDetailsExtraOutputTypeDef

### AssociatedRoles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceAssociatedRoleTypeDef]]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### DbInstancePort
- **Type**: typing.Optional[int]

### DbiResourceId
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceEndpointTypeDef]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### InstanceCreateTime
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceVpcSecurityGroupTypeDef]]

### MultiAz
- **Type**: typing.Optional[bool]

### EnhancedMonitoringResourceArn
- **Type**: typing.Optional[str]

### DbInstanceStatus
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DbSecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### DbParameterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbParameterGroupTypeDef]]

### AvailabilityZone
- **Type**: typing.Optional[str]

### DbSubnetGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSubnetGroupExtraOutputTypeDef]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbPendingModifiedValuesExtraOutputTypeDef]

### LatestRestorableTime
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### ReadReplicaSourceDBInstanceIdentifier
- **Type**: typing.Optional[str]

### ReadReplicaDBInstanceIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### ReadReplicaDBClusterIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbOptionGroupMembershipTypeDef]]

### CharacterSetName
- **Type**: typing.Optional[str]

### SecondaryAvailabilityZone
- **Type**: typing.Optional[str]

### StatusInfos
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbStatusInfoTypeDef]]

### StorageType
- **Type**: typing.Optional[str]

### DomainMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbDomainMembershipTypeDef]]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### MonitoringInterval
- **Type**: typing.Optional[int]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### PromotionTier
- **Type**: typing.Optional[int]

### Timezone
- **Type**: typing.Optional[str]

### PerformanceInsightsEnabled
- **Type**: typing.Optional[bool]

### PerformanceInsightsKmsKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### EnabledCloudWatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeatureTypeDef]]

### ListenerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceEndpointTypeDef]

### MaxAllocatedStorage
- **Type**: typing.Optional[int]


# AwsRdsDbInstanceDetailsOutputTypeDef

### AssociatedRoles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceAssociatedRoleTypeDef]]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### DbInstancePort
- **Type**: typing.Optional[int]

### DbiResourceId
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceEndpointTypeDef]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### InstanceCreateTime
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceVpcSecurityGroupTypeDef]]

### MultiAz
- **Type**: typing.Optional[bool]

### EnhancedMonitoringResourceArn
- **Type**: typing.Optional[str]

### DbInstanceStatus
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DbSecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### DbParameterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbParameterGroupTypeDef]]

### AvailabilityZone
- **Type**: typing.Optional[str]

### DbSubnetGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSubnetGroupOutputTypeDef]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbPendingModifiedValuesOutputTypeDef]

### LatestRestorableTime
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### ReadReplicaSourceDBInstanceIdentifier
- **Type**: typing.Optional[str]

### ReadReplicaDBInstanceIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### ReadReplicaDBClusterIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbOptionGroupMembershipTypeDef]]

### CharacterSetName
- **Type**: typing.Optional[str]

### SecondaryAvailabilityZone
- **Type**: typing.Optional[str]

### StatusInfos
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbStatusInfoTypeDef]]

### StorageType
- **Type**: typing.Optional[str]

### DomainMemberships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbDomainMembershipTypeDef]]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### MonitoringInterval
- **Type**: typing.Optional[int]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### PromotionTier
- **Type**: typing.Optional[int]

### Timezone
- **Type**: typing.Optional[str]

### PerformanceInsightsEnabled
- **Type**: typing.Optional[bool]

### PerformanceInsightsKmsKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### EnabledCloudWatchLogsExports
- **Type**: typing.Optional[typing.List[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeatureTypeDef]]

### ListenerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceEndpointTypeDef]

### MaxAllocatedStorage
- **Type**: typing.Optional[int]


# AwsRdsDbInstanceDetailsTypeDef

### AssociatedRoles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceAssociatedRoleTypeDef]]

### CACertificateIdentifier
- **Type**: typing.Optional[str]

### DBClusterIdentifier
- **Type**: typing.Optional[str]

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DBInstanceClass
- **Type**: typing.Optional[str]

### DbInstancePort
- **Type**: typing.Optional[int]

### DbiResourceId
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### DeletionProtection
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceEndpointTypeDef]

### Engine
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### IAMDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### InstanceCreateTime
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### StorageEncrypted
- **Type**: typing.Optional[bool]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceVpcSecurityGroupTypeDef]]

### MultiAz
- **Type**: typing.Optional[bool]

### EnhancedMonitoringResourceArn
- **Type**: typing.Optional[str]

### DbInstanceStatus
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### PreferredBackupWindow
- **Type**: typing.Optional[str]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### DbSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### DbParameterGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbParameterGroupTypeDef]]

### AvailabilityZone
- **Type**: typing.Optional[str]

### DbSubnetGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSubnetGroupTypeDef]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbPendingModifiedValuesTypeDef]

### LatestRestorableTime
- **Type**: typing.Optional[str]

### AutoMinorVersionUpgrade
- **Type**: typing.Optional[bool]

### ReadReplicaSourceDBInstanceIdentifier
- **Type**: typing.Optional[str]

### ReadReplicaDBInstanceIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### ReadReplicaDBClusterIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupMemberships
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbOptionGroupMembershipTypeDef]]

### CharacterSetName
- **Type**: typing.Optional[str]

### SecondaryAvailabilityZone
- **Type**: typing.Optional[str]

### StatusInfos
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbStatusInfoTypeDef]]

### StorageType
- **Type**: typing.Optional[str]

### DomainMemberships
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbDomainMembershipTypeDef]]

### CopyTagsToSnapshot
- **Type**: typing.Optional[bool]

### MonitoringInterval
- **Type**: typing.Optional[int]

### MonitoringRoleArn
- **Type**: typing.Optional[str]

### PromotionTier
- **Type**: typing.Optional[int]

### Timezone
- **Type**: typing.Optional[str]

### PerformanceInsightsEnabled
- **Type**: typing.Optional[bool]

### PerformanceInsightsKmsKeyId
- **Type**: typing.Optional[str]

### PerformanceInsightsRetentionPeriod
- **Type**: typing.Optional[int]

### EnabledCloudWatchLogsExports
- **Type**: typing.Optional[typing.Sequence[str]]

### ProcessorFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeatureTypeDef]]

### ListenerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceEndpointTypeDef]

### MaxAllocatedStorage
- **Type**: typing.Optional[int]


# AwsRdsDbInstanceEndpointTypeDef

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### HostedZoneId
- **Type**: typing.Optional[str]


# AwsRdsDbInstanceVpcSecurityGroupTypeDef

### VpcSecurityGroupId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRdsDbOptionGroupMembershipTypeDef

### OptionGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRdsDbParameterGroupTypeDef

### DbParameterGroupName
- **Type**: typing.Optional[str]

### ParameterApplyStatus
- **Type**: typing.Optional[str]


# AwsRdsDbPendingModifiedValuesExtraOutputTypeDef

### DbInstanceClass
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### MasterUserPassword
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### MultiAZ
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### DbInstanceIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### CaCertificateIdentifier
- **Type**: typing.Optional[str]

### DbSubnetGroupName
- **Type**: typing.Optional[str]

### PendingCloudWatchLogsExports
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsPendingCloudWatchLogsExportsExtraOutputTypeDef]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeatureTypeDef]]


# AwsRdsDbPendingModifiedValuesOutputTypeDef

### DbInstanceClass
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### MasterUserPassword
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### MultiAZ
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### DbInstanceIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### CaCertificateIdentifier
- **Type**: typing.Optional[str]

### DbSubnetGroupName
- **Type**: typing.Optional[str]

### PendingCloudWatchLogsExports
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsPendingCloudWatchLogsExportsOutputTypeDef]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeatureTypeDef]]


# AwsRdsDbPendingModifiedValuesTypeDef

### DbInstanceClass
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### MasterUserPassword
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### BackupRetentionPeriod
- **Type**: typing.Optional[int]

### MultiAZ
- **Type**: typing.Optional[bool]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### DbInstanceIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### CaCertificateIdentifier
- **Type**: typing.Optional[str]

### DbSubnetGroupName
- **Type**: typing.Optional[str]

### PendingCloudWatchLogsExports
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsPendingCloudWatchLogsExportsTypeDef]

### ProcessorFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeatureTypeDef]]


# AwsRdsDbProcessorFeatureTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsRdsDbSecurityGroupDetailsExtraOutputTypeDef

### DbSecurityGroupArn
- **Type**: typing.Optional[str]

### DbSecurityGroupDescription
- **Type**: typing.Optional[str]

### DbSecurityGroupName
- **Type**: typing.Optional[str]

### Ec2SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]]

### IpRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSecurityGroupIpRangeTypeDef]]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# AwsRdsDbSecurityGroupDetailsOutputTypeDef

### DbSecurityGroupArn
- **Type**: typing.Optional[str]

### DbSecurityGroupDescription
- **Type**: typing.Optional[str]

### DbSecurityGroupName
- **Type**: typing.Optional[str]

### Ec2SecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]]

### IpRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSecurityGroupIpRangeTypeDef]]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# AwsRdsDbSecurityGroupDetailsTypeDef

### DbSecurityGroupArn
- **Type**: typing.Optional[str]

### DbSecurityGroupDescription
- **Type**: typing.Optional[str]

### DbSecurityGroupName
- **Type**: typing.Optional[str]

### Ec2SecurityGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]]

### IpRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSecurityGroupIpRangeTypeDef]]

### OwnerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef

### Ec2SecurityGroupId
- **Type**: typing.Optional[str]

### Ec2SecurityGroupName
- **Type**: typing.Optional[str]

### Ec2SecurityGroupOwnerId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRdsDbSecurityGroupIpRangeTypeDef

### CidrIp
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRdsDbSnapshotDetailsExtraOutputTypeDef

### DbSnapshotIdentifier
- **Type**: typing.Optional[str]

### DbInstanceIdentifier
- **Type**: typing.Optional[str]

### SnapshotCreateTime
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### InstanceCreateTime
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupName
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[int]

### SourceRegion
- **Type**: typing.Optional[str]

### SourceDbSnapshotIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### Timezone
- **Type**: typing.Optional[str]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeatureTypeDef]]

### DbiResourceId
- **Type**: typing.Optional[str]


# AwsRdsDbSnapshotDetailsOutputTypeDef

### DbSnapshotIdentifier
- **Type**: typing.Optional[str]

### DbInstanceIdentifier
- **Type**: typing.Optional[str]

### SnapshotCreateTime
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### InstanceCreateTime
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupName
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[int]

### SourceRegion
- **Type**: typing.Optional[str]

### SourceDbSnapshotIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### Timezone
- **Type**: typing.Optional[str]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### ProcessorFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeatureTypeDef]]

### DbiResourceId
- **Type**: typing.Optional[str]


# AwsRdsDbSnapshotDetailsTypeDef

### DbSnapshotIdentifier
- **Type**: typing.Optional[str]

### DbInstanceIdentifier
- **Type**: typing.Optional[str]

### SnapshotCreateTime
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### AllocatedStorage
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### InstanceCreateTime
- **Type**: typing.Optional[str]

### MasterUsername
- **Type**: typing.Optional[str]

### EngineVersion
- **Type**: typing.Optional[str]

### LicenseModel
- **Type**: typing.Optional[str]

### SnapshotType
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### OptionGroupName
- **Type**: typing.Optional[str]

### PercentProgress
- **Type**: typing.Optional[int]

### SourceRegion
- **Type**: typing.Optional[str]

### SourceDbSnapshotIdentifier
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[str]

### TdeCredentialArn
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### Timezone
- **Type**: typing.Optional[str]

### IamDatabaseAuthenticationEnabled
- **Type**: typing.Optional[bool]

### ProcessorFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbProcessorFeatureTypeDef]]

### DbiResourceId
- **Type**: typing.Optional[str]


# AwsRdsDbStatusInfoTypeDef

### StatusType
- **Type**: typing.Optional[str]

### Normal
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# AwsRdsDbSubnetGroupExtraOutputTypeDef

### DbSubnetGroupName
- **Type**: typing.Optional[str]

### DbSubnetGroupDescription
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetGroupStatus
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSubnetGroupSubnetTypeDef]]

### DbSubnetGroupArn
- **Type**: typing.Optional[str]


# AwsRdsDbSubnetGroupOutputTypeDef

### DbSubnetGroupName
- **Type**: typing.Optional[str]

### DbSubnetGroupDescription
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetGroupStatus
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSubnetGroupSubnetTypeDef]]

### DbSubnetGroupArn
- **Type**: typing.Optional[str]


# AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef

### Name
- **Type**: typing.Optional[str]


# AwsRdsDbSubnetGroupSubnetTypeDef

### SubnetIdentifier
- **Type**: typing.Optional[str]

### SubnetAvailabilityZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef]

### SubnetStatus
- **Type**: typing.Optional[str]


# AwsRdsDbSubnetGroupTypeDef

### DbSubnetGroupName
- **Type**: typing.Optional[str]

### DbSubnetGroupDescription
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetGroupStatus
- **Type**: typing.Optional[str]

### Subnets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSubnetGroupSubnetTypeDef]]

### DbSubnetGroupArn
- **Type**: typing.Optional[str]


# AwsRdsEventSubscriptionDetailsExtraOutputTypeDef

### CustSubscriptionId
- **Type**: typing.Optional[str]

### CustomerAwsId
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### EventCategoriesList
- **Type**: typing.Optional[typing.List[str]]

### EventSubscriptionArn
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### SourceIdsList
- **Type**: typing.Optional[typing.List[str]]

### SourceType
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### SubscriptionCreationTime
- **Type**: typing.Optional[str]


# AwsRdsEventSubscriptionDetailsOutputTypeDef

### CustSubscriptionId
- **Type**: typing.Optional[str]

### CustomerAwsId
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### EventCategoriesList
- **Type**: typing.Optional[typing.List[str]]

### EventSubscriptionArn
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### SourceIdsList
- **Type**: typing.Optional[typing.List[str]]

### SourceType
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### SubscriptionCreationTime
- **Type**: typing.Optional[str]


# AwsRdsEventSubscriptionDetailsTypeDef

### CustSubscriptionId
- **Type**: typing.Optional[str]

### CustomerAwsId
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### EventCategoriesList
- **Type**: typing.Optional[typing.Sequence[str]]

### EventSubscriptionArn
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### SourceIdsList
- **Type**: typing.Optional[typing.Sequence[str]]

### SourceType
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### SubscriptionCreationTime
- **Type**: typing.Optional[str]


# AwsRdsPendingCloudWatchLogsExportsExtraOutputTypeDef

### LogTypesToEnable
- **Type**: typing.Optional[typing.List[str]]

### LogTypesToDisable
- **Type**: typing.Optional[typing.List[str]]


# AwsRdsPendingCloudWatchLogsExportsOutputTypeDef

### LogTypesToEnable
- **Type**: typing.Optional[typing.List[str]]

### LogTypesToDisable
- **Type**: typing.Optional[typing.List[str]]


# AwsRdsPendingCloudWatchLogsExportsTypeDef

### LogTypesToEnable
- **Type**: typing.Optional[typing.Sequence[str]]

### LogTypesToDisable
- **Type**: typing.Optional[typing.Sequence[str]]


# AwsRedshiftClusterClusterNodeTypeDef

### NodeRole
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]

### PublicIpAddress
- **Type**: typing.Optional[str]


# AwsRedshiftClusterClusterParameterGroupExtraOutputTypeDef

### ClusterParameterStatusList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterParameterStatusTypeDef]]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### ParameterGroupName
- **Type**: typing.Optional[str]


# AwsRedshiftClusterClusterParameterGroupOutputTypeDef

### ClusterParameterStatusList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterParameterStatusTypeDef]]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### ParameterGroupName
- **Type**: typing.Optional[str]


# AwsRedshiftClusterClusterParameterGroupTypeDef

### ClusterParameterStatusList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterParameterStatusTypeDef]]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### ParameterGroupName
- **Type**: typing.Optional[str]


# AwsRedshiftClusterClusterParameterStatusTypeDef

### ParameterName
- **Type**: typing.Optional[str]

### ParameterApplyStatus
- **Type**: typing.Optional[str]

### ParameterApplyErrorDescription
- **Type**: typing.Optional[str]


# AwsRedshiftClusterClusterSecurityGroupTypeDef

### ClusterSecurityGroupName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef

### DestinationRegion
- **Type**: typing.Optional[str]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### RetentionPeriod
- **Type**: typing.Optional[int]

### SnapshotCopyGrantName
- **Type**: typing.Optional[str]


# AwsRedshiftClusterDeferredMaintenanceWindowTypeDef

### DeferMaintenanceEndTime
- **Type**: typing.Optional[str]

### DeferMaintenanceIdentifier
- **Type**: typing.Optional[str]

### DeferMaintenanceStartTime
- **Type**: typing.Optional[str]


# AwsRedshiftClusterDetailsExtraOutputTypeDef

### AllowVersionUpgrade
- **Type**: typing.Optional[bool]

### AutomatedSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### ClusterAvailabilityStatus
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ClusterNodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterNodeTypeDef]]

### ClusterParameterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterParameterGroupExtraOutputTypeDef]]

### ClusterPublicKey
- **Type**: typing.Optional[str]

### ClusterRevisionNumber
- **Type**: typing.Optional[str]

### ClusterSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterSecurityGroupTypeDef]]

### ClusterSnapshotCopyStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef]

### ClusterStatus
- **Type**: typing.Optional[str]

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### ClusterVersion
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### DeferredMaintenanceWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]]

### ElasticIpStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterElasticIpStatusTypeDef]

### ElasticResizeNumberOfNodeOptions
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterEndpointTypeDef]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### ExpectedNextSnapshotScheduleTime
- **Type**: typing.Optional[str]

### ExpectedNextSnapshotScheduleTimeStatus
- **Type**: typing.Optional[str]

### HsmStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterHsmStatusTypeDef]

### IamRoles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterIamRoleTypeDef]]

### KmsKeyId
- **Type**: typing.Optional[str]

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### MasterUsername
- **Type**: typing.Optional[str]

### NextMaintenanceWindowStartTime
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### PendingActions
- **Type**: typing.Optional[typing.List[str]]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterPendingModifiedValuesTypeDef]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### ResizeInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterResizeInfoTypeDef]

### RestoreStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterRestoreStatusTypeDef]

### SnapshotScheduleIdentifier
- **Type**: typing.Optional[str]

### SnapshotScheduleState
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterVpcSecurityGroupTypeDef]]

### LoggingStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterLoggingStatusTypeDef]


# AwsRedshiftClusterDetailsOutputTypeDef

### AllowVersionUpgrade
- **Type**: typing.Optional[bool]

### AutomatedSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### ClusterAvailabilityStatus
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ClusterNodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterNodeTypeDef]]

### ClusterParameterGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterParameterGroupOutputTypeDef]]

### ClusterPublicKey
- **Type**: typing.Optional[str]

### ClusterRevisionNumber
- **Type**: typing.Optional[str]

### ClusterSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterSecurityGroupTypeDef]]

### ClusterSnapshotCopyStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef]

### ClusterStatus
- **Type**: typing.Optional[str]

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### ClusterVersion
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### DeferredMaintenanceWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]]

### ElasticIpStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterElasticIpStatusTypeDef]

### ElasticResizeNumberOfNodeOptions
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterEndpointTypeDef]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### ExpectedNextSnapshotScheduleTime
- **Type**: typing.Optional[str]

### ExpectedNextSnapshotScheduleTimeStatus
- **Type**: typing.Optional[str]

### HsmStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterHsmStatusTypeDef]

### IamRoles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterIamRoleTypeDef]]

### KmsKeyId
- **Type**: typing.Optional[str]

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### MasterUsername
- **Type**: typing.Optional[str]

### NextMaintenanceWindowStartTime
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### PendingActions
- **Type**: typing.Optional[typing.List[str]]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterPendingModifiedValuesTypeDef]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### ResizeInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterResizeInfoTypeDef]

### RestoreStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterRestoreStatusTypeDef]

### SnapshotScheduleIdentifier
- **Type**: typing.Optional[str]

### SnapshotScheduleState
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterVpcSecurityGroupTypeDef]]

### LoggingStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterLoggingStatusTypeDef]


# AwsRedshiftClusterDetailsTypeDef

### AllowVersionUpgrade
- **Type**: typing.Optional[bool]

### AutomatedSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]

### ClusterAvailabilityStatus
- **Type**: typing.Optional[str]

### ClusterCreateTime
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ClusterNodes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterNodeTypeDef]]

### ClusterParameterGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterParameterGroupTypeDef]]

### ClusterPublicKey
- **Type**: typing.Optional[str]

### ClusterRevisionNumber
- **Type**: typing.Optional[str]

### ClusterSecurityGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterSecurityGroupTypeDef]]

### ClusterSnapshotCopyStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef]

### ClusterStatus
- **Type**: typing.Optional[str]

### ClusterSubnetGroupName
- **Type**: typing.Optional[str]

### ClusterVersion
- **Type**: typing.Optional[str]

### DBName
- **Type**: typing.Optional[str]

### DeferredMaintenanceWindows
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]]

### ElasticIpStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterElasticIpStatusTypeDef]

### ElasticResizeNumberOfNodeOptions
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterEndpointTypeDef]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### ExpectedNextSnapshotScheduleTime
- **Type**: typing.Optional[str]

### ExpectedNextSnapshotScheduleTimeStatus
- **Type**: typing.Optional[str]

### HsmStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterHsmStatusTypeDef]

### IamRoles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterIamRoleTypeDef]]

### KmsKeyId
- **Type**: typing.Optional[str]

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### ManualSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### MasterUsername
- **Type**: typing.Optional[str]

### NextMaintenanceWindowStartTime
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### PendingActions
- **Type**: typing.Optional[typing.Sequence[str]]

### PendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterPendingModifiedValuesTypeDef]

### PreferredMaintenanceWindow
- **Type**: typing.Optional[str]

### PubliclyAccessible
- **Type**: typing.Optional[bool]

### ResizeInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterResizeInfoTypeDef]

### RestoreStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterRestoreStatusTypeDef]

### SnapshotScheduleIdentifier
- **Type**: typing.Optional[str]

### SnapshotScheduleState
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### VpcSecurityGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterVpcSecurityGroupTypeDef]]

### LoggingStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterLoggingStatusTypeDef]


# AwsRedshiftClusterElasticIpStatusTypeDef

### ElasticIp
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRedshiftClusterEndpointTypeDef

### Address
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]


# AwsRedshiftClusterHsmStatusTypeDef

### HsmClientCertificateIdentifier
- **Type**: typing.Optional[str]

### HsmConfigurationIdentifier
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# AwsRedshiftClusterIamRoleTypeDef

### ApplyStatus
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]


# AwsRedshiftClusterLoggingStatusTypeDef

### BucketName
- **Type**: typing.Optional[str]

### LastFailureMessage
- **Type**: typing.Optional[str]

### LastFailureTime
- **Type**: typing.Optional[str]

### LastSuccessfulDeliveryTime
- **Type**: typing.Optional[str]

### LoggingEnabled
- **Type**: typing.Optional[bool]

### S3KeyPrefix
- **Type**: typing.Optional[str]


# AwsRedshiftClusterPendingModifiedValuesTypeDef

### AutomatedSnapshotRetentionPeriod
- **Type**: typing.Optional[int]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ClusterType
- **Type**: typing.Optional[str]

### ClusterVersion
- **Type**: typing.Optional[str]

### EncryptionType
- **Type**: typing.Optional[str]

### EnhancedVpcRouting
- **Type**: typing.Optional[bool]

### MaintenanceTrackName
- **Type**: typing.Optional[str]

### MasterUserPassword
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[str]

### NumberOfNodes
- **Type**: typing.Optional[int]

### PubliclyAccessible
- **Type**: typing.Optional[bool]


# AwsRedshiftClusterResizeInfoTypeDef

### AllowCancelResize
- **Type**: typing.Optional[bool]

### ResizeType
- **Type**: typing.Optional[str]


# AwsRedshiftClusterRestoreStatusTypeDef

### CurrentRestoreRateInMegaBytesPerSecond
- **Type**: typing.Optional[float]

### ElapsedTimeInSeconds
- **Type**: typing.Optional[int]

### EstimatedTimeToCompletionInSeconds
- **Type**: typing.Optional[int]

### ProgressInMegaBytes
- **Type**: typing.Optional[int]

### SnapshotSizeInMegaBytes
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[str]


# AwsRedshiftClusterVpcSecurityGroupTypeDef

### Status
- **Type**: typing.Optional[str]

### VpcSecurityGroupId
- **Type**: typing.Optional[str]


# AwsRoute53HostedZoneConfigDetailsTypeDef

### Comment
- **Type**: typing.Optional[str]


# AwsRoute53HostedZoneDetailsExtraOutputTypeDef

### HostedZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneObjectDetailsTypeDef]

### Vpcs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneVpcDetailsTypeDef]]

### NameServers
- **Type**: typing.Optional[typing.List[str]]

### QueryLoggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53QueryLoggingConfigDetailsTypeDef]


# AwsRoute53HostedZoneDetailsOutputTypeDef

### HostedZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneObjectDetailsTypeDef]

### Vpcs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneVpcDetailsTypeDef]]

### NameServers
- **Type**: typing.Optional[typing.List[str]]

### QueryLoggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53QueryLoggingConfigDetailsTypeDef]


# AwsRoute53HostedZoneDetailsTypeDef

### HostedZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneObjectDetailsTypeDef]

### Vpcs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneVpcDetailsTypeDef]]

### NameServers
- **Type**: typing.Optional[typing.Sequence[str]]

### QueryLoggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53QueryLoggingConfigDetailsTypeDef]


# AwsRoute53HostedZoneObjectDetailsTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneConfigDetailsTypeDef]


# AwsRoute53HostedZoneVpcDetailsTypeDef

### Id
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# AwsRoute53QueryLoggingConfigDetailsTypeDef

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.CloudWatchLogsLogGroupArnConfigDetailsTypeDef]


# AwsS3AccessPointDetailsTypeDef

### AccessPointArn
- **Type**: typing.Optional[str]

### Alias
- **Type**: typing.Optional[str]

### Bucket
- **Type**: typing.Optional[str]

### BucketAccountId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### NetworkOrigin
- **Type**: typing.Optional[str]

### PublicAccessBlockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccountPublicAccessBlockDetailsTypeDef]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccessPointVpcConfigurationDetailsTypeDef]


# AwsS3AccessPointVpcConfigurationDetailsTypeDef

### VpcId
- **Type**: typing.Optional[str]


# AwsS3AccountPublicAccessBlockDetailsTypeDef

### BlockPublicAcls
- **Type**: typing.Optional[bool]

### BlockPublicPolicy
- **Type**: typing.Optional[bool]

### IgnorePublicAcls
- **Type**: typing.Optional[bool]

### RestrictPublicBuckets
- **Type**: typing.Optional[bool]


# AwsS3BucketBucketLifecycleConfigurationDetailsExtraOutputTypeDef

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesDetailsExtraOutputTypeDef]]


# AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef]]


# AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef]]


# AwsS3BucketBucketLifecycleConfigurationRulesDetailsExtraOutputTypeDef

### AbortIncompleteMultipartUpload
- **Type**: typing.Optional[mypy_boto3_securityhub.type_defs.AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef]

### ExpirationDate
- **Type**: typing.Optional[str]

### ExpirationInDays
- **Type**: typing.Optional[int]

### ExpiredObjectDeleteMarker
- **Type**: typing.Optional[bool]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsExtraOutputTypeDef]

### ID
- **Type**: typing.Optional[str]

### NoncurrentVersionExpirationInDays
- **Type**: typing.Optional[int]

### NoncurrentVersionTransitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef]]

### Prefix
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Transitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]]


# AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef

### AbortIncompleteMultipartUpload
- **Type**: typing.Optional[mypy_boto3_securityhub.type_defs.AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef]

### ExpirationDate
- **Type**: typing.Optional[str]

### ExpirationInDays
- **Type**: typing.Optional[int]

### ExpiredObjectDeleteMarker
- **Type**: typing.Optional[bool]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef]

### ID
- **Type**: typing.Optional[str]

### NoncurrentVersionExpirationInDays
- **Type**: typing.Optional[int]

### NoncurrentVersionTransitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef]]

### Prefix
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Transitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]]


# AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef

### AbortIncompleteMultipartUpload
- **Type**: typing.Optional[mypy_boto3_securityhub.type_defs.AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef]

### ExpirationDate
- **Type**: typing.Optional[str]

### ExpirationInDays
- **Type**: typing.Optional[int]

### ExpiredObjectDeleteMarker
- **Type**: typing.Optional[bool]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef]

### ID
- **Type**: typing.Optional[str]

### NoncurrentVersionExpirationInDays
- **Type**: typing.Optional[int]

### NoncurrentVersionTransitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef]]

### Prefix
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Transitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]]


# AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsExtraOutputTypeDef

### Predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsExtraOutputTypeDef]


# AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef

### Predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef]


# AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef

### Predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef]


# AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsExtraOutputTypeDef

### Operands
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef]]

### Prefix
- **Type**: typing.Optional[str]

### Tag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef]

### Type
- **Type**: typing.Optional[str]


# AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef

### Operands
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef]]

### Prefix
- **Type**: typing.Optional[str]

### Tag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef]

### Type
- **Type**: typing.Optional[str]


# AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef

### Operands
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef]]

### Prefix
- **Type**: typing.Optional[str]

### Tag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef]

### Type
- **Type**: typing.Optional[str]


# AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef

### Prefix
- **Type**: typing.Optional[str]

### Tag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef]

### Type
- **Type**: typing.Optional[str]


# AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef

### Days
- **Type**: typing.Optional[int]

### StorageClass
- **Type**: typing.Optional[str]


# AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef

### Date
- **Type**: typing.Optional[str]

### Days
- **Type**: typing.Optional[int]

### StorageClass
- **Type**: typing.Optional[str]


# AwsS3BucketBucketVersioningConfigurationTypeDef

### IsMfaDeleteEnabled
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[str]


# AwsS3BucketDetailsExtraOutputTypeDef

### OwnerId
- **Type**: typing.Optional[str]

### OwnerName
- **Type**: typing.Optional[str]

### OwnerAccountId
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### ServerSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketServerSideEncryptionConfigurationExtraOutputTypeDef]

### BucketLifecycleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationDetailsExtraOutputTypeDef]

### PublicAccessBlockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccountPublicAccessBlockDetailsTypeDef]

### AccessControlList
- **Type**: typing.Optional[str]

### BucketLoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketLoggingConfigurationTypeDef]

### BucketWebsiteConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationExtraOutputTypeDef]

### BucketNotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationExtraOutputTypeDef]

### BucketVersioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketVersioningConfigurationTypeDef]

### ObjectLockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketObjectLockConfigurationTypeDef]

### Name
- **Type**: typing.Optional[str]


# AwsS3BucketDetailsOutputTypeDef

### OwnerId
- **Type**: typing.Optional[str]

### OwnerName
- **Type**: typing.Optional[str]

### OwnerAccountId
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### ServerSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef]

### BucketLifecycleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef]

### PublicAccessBlockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccountPublicAccessBlockDetailsTypeDef]

### AccessControlList
- **Type**: typing.Optional[str]

### BucketLoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketLoggingConfigurationTypeDef]

### BucketWebsiteConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationOutputTypeDef]

### BucketNotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationOutputTypeDef]

### BucketVersioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketVersioningConfigurationTypeDef]

### ObjectLockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketObjectLockConfigurationTypeDef]

### Name
- **Type**: typing.Optional[str]


# AwsS3BucketDetailsTypeDef

### OwnerId
- **Type**: typing.Optional[str]

### OwnerName
- **Type**: typing.Optional[str]

### OwnerAccountId
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### ServerSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketServerSideEncryptionConfigurationTypeDef]

### BucketLifecycleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef]

### PublicAccessBlockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccountPublicAccessBlockDetailsTypeDef]

### AccessControlList
- **Type**: typing.Optional[str]

### BucketLoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketLoggingConfigurationTypeDef]

### BucketWebsiteConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationTypeDef]

### BucketNotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationTypeDef]

### BucketVersioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketBucketVersioningConfigurationTypeDef]

### ObjectLockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketObjectLockConfigurationTypeDef]

### Name
- **Type**: typing.Optional[str]


# AwsS3BucketLoggingConfigurationTypeDef

### DestinationBucketName
- **Type**: typing.Optional[str]

### LogFilePrefix
- **Type**: typing.Optional[str]


# AwsS3BucketNotificationConfigurationDetailExtraOutputTypeDef

### Events
- **Type**: typing.Optional[typing.List[str]]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationFilterExtraOutputTypeDef]

### Destination
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsS3BucketNotificationConfigurationDetailOutputTypeDef

### Events
- **Type**: typing.Optional[typing.List[str]]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationFilterOutputTypeDef]

### Destination
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsS3BucketNotificationConfigurationDetailTypeDef

### Events
- **Type**: typing.Optional[typing.Sequence[str]]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationFilterTypeDef]

### Destination
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsS3BucketNotificationConfigurationExtraOutputTypeDef

### Configurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationDetailExtraOutputTypeDef]]


# AwsS3BucketNotificationConfigurationFilterExtraOutputTypeDef

### S3KeyFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationS3KeyFilterExtraOutputTypeDef]


# AwsS3BucketNotificationConfigurationFilterOutputTypeDef

### S3KeyFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef]


# AwsS3BucketNotificationConfigurationFilterTypeDef

### S3KeyFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef]


# AwsS3BucketNotificationConfigurationOutputTypeDef

### Configurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationDetailOutputTypeDef]]


# AwsS3BucketNotificationConfigurationS3KeyFilterExtraOutputTypeDef

### FilterRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]]


# AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef

### FilterRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]]


# AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['Prefix', 'Suffix']]

### Value
- **Type**: typing.Optional[str]


# AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef

### FilterRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]]


# AwsS3BucketNotificationConfigurationTypeDef

### Configurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketNotificationConfigurationDetailTypeDef]]


# AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef

### Days
- **Type**: typing.Optional[int]

### Mode
- **Type**: typing.Optional[str]

### Years
- **Type**: typing.Optional[int]


# AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef

### DefaultRetention
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef]


# AwsS3BucketObjectLockConfigurationTypeDef

### ObjectLockEnabled
- **Type**: typing.Optional[str]

### Rule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef]


# AwsS3BucketServerSideEncryptionByDefaultTypeDef

### SSEAlgorithm
- **Type**: typing.Optional[str]

### KMSMasterKeyID
- **Type**: typing.Optional[str]


# AwsS3BucketServerSideEncryptionConfigurationExtraOutputTypeDef

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketServerSideEncryptionRuleTypeDef]]


# AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketServerSideEncryptionRuleTypeDef]]


# AwsS3BucketServerSideEncryptionConfigurationTypeDef

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketServerSideEncryptionRuleTypeDef]]


# AwsS3BucketServerSideEncryptionRuleTypeDef

### ApplyServerSideEncryptionByDefault
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketServerSideEncryptionByDefaultTypeDef]


# AwsS3BucketWebsiteConfigurationExtraOutputTypeDef

### ErrorDocument
- **Type**: typing.Optional[str]

### IndexDocumentSuffix
- **Type**: typing.Optional[str]

### RedirectAllRequestsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationRedirectToTypeDef]

### RoutingRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]]


# AwsS3BucketWebsiteConfigurationOutputTypeDef

### ErrorDocument
- **Type**: typing.Optional[str]

### IndexDocumentSuffix
- **Type**: typing.Optional[str]

### RedirectAllRequestsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationRedirectToTypeDef]

### RoutingRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]]


# AwsS3BucketWebsiteConfigurationRedirectToTypeDef

### Hostname
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[str]


# AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef

### HttpErrorCodeReturnedEquals
- **Type**: typing.Optional[str]

### KeyPrefixEquals
- **Type**: typing.Optional[str]


# AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef

### Hostname
- **Type**: typing.Optional[str]

### HttpRedirectCode
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[str]

### ReplaceKeyPrefixWith
- **Type**: typing.Optional[str]

### ReplaceKeyWith
- **Type**: typing.Optional[str]


# AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef]

### Redirect
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef]


# AwsS3BucketWebsiteConfigurationTypeDef

### ErrorDocument
- **Type**: typing.Optional[str]

### IndexDocumentSuffix
- **Type**: typing.Optional[str]

### RedirectAllRequestsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationRedirectToTypeDef]

### RoutingRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]]


# AwsS3ObjectDetailsTypeDef

### LastModified
- **Type**: typing.Optional[str]

### ETag
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]

### ServerSideEncryption
- **Type**: typing.Optional[str]

### SSEKMSKeyId
- **Type**: typing.Optional[str]


# AwsSageMakerNotebookInstanceDetailsExtraOutputTypeDef

### AcceleratorTypes
- **Type**: typing.Optional[typing.List[str]]

### AdditionalCodeRepositories
- **Type**: typing.Optional[typing.List[str]]

### DefaultCodeRepository
- **Type**: typing.Optional[str]

### DirectInternetAccess
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]

### InstanceMetadataServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef]

### InstanceType
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### NotebookInstanceArn
- **Type**: typing.Optional[str]

### NotebookInstanceLifecycleConfigName
- **Type**: typing.Optional[str]

### NotebookInstanceName
- **Type**: typing.Optional[str]

### NotebookInstanceStatus
- **Type**: typing.Optional[str]

### PlatformIdentifier
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### RootAccess
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### SubnetId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### VolumeSizeInGB
- **Type**: typing.Optional[int]


# AwsSageMakerNotebookInstanceDetailsOutputTypeDef

### AcceleratorTypes
- **Type**: typing.Optional[typing.List[str]]

### AdditionalCodeRepositories
- **Type**: typing.Optional[typing.List[str]]

### DefaultCodeRepository
- **Type**: typing.Optional[str]

### DirectInternetAccess
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]

### InstanceMetadataServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef]

### InstanceType
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### NotebookInstanceArn
- **Type**: typing.Optional[str]

### NotebookInstanceLifecycleConfigName
- **Type**: typing.Optional[str]

### NotebookInstanceName
- **Type**: typing.Optional[str]

### NotebookInstanceStatus
- **Type**: typing.Optional[str]

### PlatformIdentifier
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### RootAccess
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### SubnetId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### VolumeSizeInGB
- **Type**: typing.Optional[int]


# AwsSageMakerNotebookInstanceDetailsTypeDef

### AcceleratorTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### AdditionalCodeRepositories
- **Type**: typing.Optional[typing.Sequence[str]]

### DefaultCodeRepository
- **Type**: typing.Optional[str]

### DirectInternetAccess
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]

### InstanceMetadataServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef]

### InstanceType
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### NotebookInstanceArn
- **Type**: typing.Optional[str]

### NotebookInstanceLifecycleConfigName
- **Type**: typing.Optional[str]

### NotebookInstanceName
- **Type**: typing.Optional[str]

### NotebookInstanceStatus
- **Type**: typing.Optional[str]

### PlatformIdentifier
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### RootAccess
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### VolumeSizeInGB
- **Type**: typing.Optional[int]


# AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef

### MinimumInstanceMetadataServiceVersion
- **Type**: typing.Optional[str]


# AwsSecretsManagerSecretDetailsTypeDef

### RotationRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecretsManagerSecretRotationRulesTypeDef]

### RotationOccurredWithinFrequency
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### RotationEnabled
- **Type**: typing.Optional[bool]

### RotationLambdaArn
- **Type**: typing.Optional[str]

### Deleted
- **Type**: typing.Optional[bool]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# AwsSecretsManagerSecretRotationRulesTypeDef

### AutomaticallyAfterDays
- **Type**: typing.Optional[int]


# AwsSecurityFindingExtraOutputTypeDef

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ProductArn
- **Type**: <class 'str'>
- **Required**: Yes

### GeneratorId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ResourceExtraOutputTypeDef]
- **Required**: Yes

### ProductName
- **Type**: typing.Optional[str]

### CompanyName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Types
- **Type**: typing.Optional[typing.List[str]]

### FirstObservedAt
- **Type**: typing.Optional[str]

### LastObservedAt
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SeverityTypeDef]

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### Remediation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RemediationTypeDef]

### SourceUrl
- **Type**: typing.Optional[str]

### ProductFields
- **Type**: typing.Optional[typing.Dict[str, str]]

### UserDefinedFields
- **Type**: typing.Optional[typing.Dict[str, str]]

### Malware
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MalwareTypeDef]]

### Network
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkTypeDef]

### NetworkPath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NetworkPathComponentExtraOutputTypeDef]]

### Process
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ProcessDetailsTypeDef]

### Threats
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ThreatExtraOutputTypeDef]]

### ThreatIntelIndicators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ThreatIntelIndicatorTypeDef]]

### Compliance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ComplianceExtraOutputTypeDef]

### VerificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### WorkflowState
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'DEFERRED', 'IN_PROGRESS', 'NEW', 'RESOLVED']]

### Workflow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WorkflowTypeDef]

### RecordState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### RelatedFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFindingTypeDef]]

### Note
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NoteTypeDef]

### Vulnerabilities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityExtraOutputTypeDef]]

### PatchSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PatchSummaryTypeDef]

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionExtraOutputTypeDef]

### FindingProviderFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FindingProviderFieldsExtraOutputTypeDef]

### Sample
- **Type**: typing.Optional[bool]

### GeneratorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.GeneratorDetailsExtraOutputTypeDef]

### ProcessedAt
- **Type**: typing.Optional[str]

### AwsAccountName
- **Type**: typing.Optional[str]


# AwsSecurityFindingFiltersExtraOutputTypeDef

### ProductArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### AwsAccountId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Id
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### GeneratorId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Region
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Type
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FirstObservedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### LastObservedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### CreatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### UpdatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### SeverityProduct
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### SeverityNormalized
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### SeverityLabel
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Confidence
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### Criticality
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### Title
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Description
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RecommendationText
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### SourceUrl
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ProductFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ProductName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### CompanyName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### UserDefinedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### MalwareName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### MalwareType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### MalwarePath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### MalwareState
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkDirection
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkProtocol
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkSourceIpV4
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### NetworkSourceIpV6
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### NetworkSourcePort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### NetworkSourceDomain
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkSourceMac
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkDestinationIpV4
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### NetworkDestinationIpV6
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### NetworkDestinationPort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### NetworkDestinationDomain
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ProcessName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ProcessPath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ProcessPid
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### ProcessParentPid
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### ProcessLaunchedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ProcessTerminatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ThreatIntelIndicatorType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ThreatIntelIndicatorValue
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ThreatIntelIndicatorCategory
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ThreatIntelIndicatorLastObservedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ThreatIntelIndicatorSource
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ThreatIntelIndicatorSourceUrl
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourcePartition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceRegion
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ResourceAwsEc2InstanceType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceImageId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceIpV4Addresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### ResourceAwsEc2InstanceIpV6Addresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### ResourceAwsEc2InstanceKeyName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceIamInstanceProfileArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceVpcId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceSubnetId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceLaunchedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ResourceAwsS3BucketOwnerId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsS3BucketOwnerName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsIamAccessKeyUserName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsIamAccessKeyPrincipalName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsIamAccessKeyStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsIamAccessKeyCreatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ResourceAwsIamUserUserName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceContainerName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceContainerImageId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceContainerImageName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceContainerLaunchedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ResourceDetailsOther
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ComplianceStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### VerificationState
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### WorkflowState
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### WorkflowStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RecordState
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RelatedFindingsProductArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RelatedFindingsId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NoteText
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NoteUpdatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### NoteUpdatedBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Keyword
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.KeywordFilterTypeDef]]

### FindingProviderFieldsConfidence
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### FindingProviderFieldsCriticality
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### FindingProviderFieldsRelatedFindingsId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FindingProviderFieldsRelatedFindingsProductArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FindingProviderFieldsSeverityLabel
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FindingProviderFieldsSeverityOriginal
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FindingProviderFieldsTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Sample
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.BooleanFilterTypeDef]]

### ComplianceSecurityControlId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ComplianceAssociatedStandardsId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### VulnerabilitiesExploitAvailable
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### VulnerabilitiesFixAvailable
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ComplianceSecurityControlParametersName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ComplianceSecurityControlParametersValue
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### AwsAccountName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceApplicationName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceApplicationArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]


# AwsSecurityFindingFiltersOutputTypeDef

### ProductArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### AwsAccountId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Id
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### GeneratorId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Region
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Type
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FirstObservedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### LastObservedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### CreatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### UpdatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### SeverityProduct
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### SeverityNormalized
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### SeverityLabel
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Confidence
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### Criticality
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### Title
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Description
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RecommendationText
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### SourceUrl
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ProductFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ProductName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### CompanyName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### UserDefinedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### MalwareName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### MalwareType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### MalwarePath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### MalwareState
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkDirection
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkProtocol
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkSourceIpV4
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### NetworkSourceIpV6
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### NetworkSourcePort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### NetworkSourceDomain
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkSourceMac
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkDestinationIpV4
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### NetworkDestinationIpV6
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### NetworkDestinationPort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### NetworkDestinationDomain
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ProcessName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ProcessPath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ProcessPid
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### ProcessParentPid
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### ProcessLaunchedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ProcessTerminatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ThreatIntelIndicatorType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ThreatIntelIndicatorValue
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ThreatIntelIndicatorCategory
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ThreatIntelIndicatorLastObservedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ThreatIntelIndicatorSource
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ThreatIntelIndicatorSourceUrl
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourcePartition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceRegion
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ResourceAwsEc2InstanceType
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceImageId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceIpV4Addresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### ResourceAwsEc2InstanceIpV6Addresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### ResourceAwsEc2InstanceKeyName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceIamInstanceProfileArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceVpcId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceSubnetId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceLaunchedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ResourceAwsS3BucketOwnerId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsS3BucketOwnerName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsIamAccessKeyUserName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsIamAccessKeyPrincipalName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsIamAccessKeyStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsIamAccessKeyCreatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ResourceAwsIamUserUserName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceContainerName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceContainerImageId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceContainerImageName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceContainerLaunchedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ResourceDetailsOther
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ComplianceStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### VerificationState
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### WorkflowState
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### WorkflowStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RecordState
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RelatedFindingsProductArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RelatedFindingsId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NoteText
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NoteUpdatedAt
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### NoteUpdatedBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Keyword
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.KeywordFilterTypeDef]]

### FindingProviderFieldsConfidence
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### FindingProviderFieldsCriticality
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### FindingProviderFieldsRelatedFindingsId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FindingProviderFieldsRelatedFindingsProductArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FindingProviderFieldsSeverityLabel
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FindingProviderFieldsSeverityOriginal
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FindingProviderFieldsTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Sample
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.BooleanFilterTypeDef]]

### ComplianceSecurityControlId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ComplianceAssociatedStandardsId
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### VulnerabilitiesExploitAvailable
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### VulnerabilitiesFixAvailable
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ComplianceSecurityControlParametersName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ComplianceSecurityControlParametersValue
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### AwsAccountName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceApplicationName
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceApplicationArn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]


# AwsSecurityFindingFiltersTypeDef

### ProductArn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### AwsAccountId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Id
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### GeneratorId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Region
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Type
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FirstObservedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### LastObservedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### CreatedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### UpdatedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### SeverityProduct
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### SeverityNormalized
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### SeverityLabel
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Confidence
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### Criticality
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### Title
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Description
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RecommendationText
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### SourceUrl
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ProductFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ProductName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### CompanyName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### UserDefinedFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### MalwareName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### MalwareType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### MalwarePath
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### MalwareState
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkDirection
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkProtocol
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkSourceIpV4
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### NetworkSourceIpV6
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### NetworkSourcePort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### NetworkSourceDomain
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkSourceMac
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NetworkDestinationIpV4
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### NetworkDestinationIpV6
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### NetworkDestinationPort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### NetworkDestinationDomain
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ProcessName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ProcessPath
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ProcessPid
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### ProcessParentPid
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### ProcessLaunchedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ProcessTerminatedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ThreatIntelIndicatorType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ThreatIntelIndicatorValue
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ThreatIntelIndicatorCategory
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ThreatIntelIndicatorLastObservedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ThreatIntelIndicatorSource
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ThreatIntelIndicatorSourceUrl
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourcePartition
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceRegion
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ResourceAwsEc2InstanceType
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceImageId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceIpV4Addresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### ResourceAwsEc2InstanceIpV6Addresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.IpFilterTypeDef]]

### ResourceAwsEc2InstanceKeyName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceIamInstanceProfileArn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceVpcId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceSubnetId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsEc2InstanceLaunchedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ResourceAwsS3BucketOwnerId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsS3BucketOwnerName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsIamAccessKeyUserName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsIamAccessKeyPrincipalName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsIamAccessKeyStatus
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceAwsIamAccessKeyCreatedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ResourceAwsIamUserUserName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceContainerName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceContainerImageId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceContainerImageName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceContainerLaunchedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### ResourceDetailsOther
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.MapFilterTypeDef]]

### ComplianceStatus
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### VerificationState
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### WorkflowState
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### WorkflowStatus
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RecordState
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RelatedFindingsProductArn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### RelatedFindingsId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NoteText
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### NoteUpdatedAt
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.DateFilterTypeDef]]

### NoteUpdatedBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Keyword
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.KeywordFilterTypeDef]]

### FindingProviderFieldsConfidence
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### FindingProviderFieldsCriticality
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NumberFilterTypeDef]]

### FindingProviderFieldsRelatedFindingsId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FindingProviderFieldsRelatedFindingsProductArn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FindingProviderFieldsSeverityLabel
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FindingProviderFieldsSeverityOriginal
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### FindingProviderFieldsTypes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### Sample
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.BooleanFilterTypeDef]]

### ComplianceSecurityControlId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ComplianceAssociatedStandardsId
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### VulnerabilitiesExploitAvailable
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### VulnerabilitiesFixAvailable
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ComplianceSecurityControlParametersName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ComplianceSecurityControlParametersValue
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### AwsAccountName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceApplicationName
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]

### ResourceApplicationArn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StringFilterTypeDef]]


# AwsSecurityFindingIdentifierTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ProductArn
- **Type**: <class 'str'>
- **Required**: Yes


# AwsSecurityFindingOutputTypeDef

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ProductArn
- **Type**: <class 'str'>
- **Required**: Yes

### GeneratorId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ResourceOutputTypeDef]
- **Required**: Yes

### ProductName
- **Type**: typing.Optional[str]

### CompanyName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Types
- **Type**: typing.Optional[typing.List[str]]

### FirstObservedAt
- **Type**: typing.Optional[str]

### LastObservedAt
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SeverityTypeDef]

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### Remediation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RemediationTypeDef]

### SourceUrl
- **Type**: typing.Optional[str]

### ProductFields
- **Type**: typing.Optional[typing.Dict[str, str]]

### UserDefinedFields
- **Type**: typing.Optional[typing.Dict[str, str]]

### Malware
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MalwareTypeDef]]

### Network
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkTypeDef]

### NetworkPath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.NetworkPathComponentOutputTypeDef]]

### Process
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ProcessDetailsTypeDef]

### Threats
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ThreatOutputTypeDef]]

### ThreatIntelIndicators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ThreatIntelIndicatorTypeDef]]

### Compliance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ComplianceOutputTypeDef]

### VerificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### WorkflowState
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'DEFERRED', 'IN_PROGRESS', 'NEW', 'RESOLVED']]

### Workflow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WorkflowTypeDef]

### RecordState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### RelatedFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFindingTypeDef]]

### Note
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NoteTypeDef]

### Vulnerabilities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityOutputTypeDef]]

### PatchSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PatchSummaryTypeDef]

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionOutputTypeDef]

### FindingProviderFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FindingProviderFieldsOutputTypeDef]

### Sample
- **Type**: typing.Optional[bool]

### GeneratorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.GeneratorDetailsOutputTypeDef]

### ProcessedAt
- **Type**: typing.Optional[str]

### AwsAccountName
- **Type**: typing.Optional[str]


# AwsSecurityFindingTypeDef

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ProductArn
- **Type**: <class 'str'>
- **Required**: Yes

### GeneratorId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.ResourceTypeDef]
- **Required**: Yes

### ProductName
- **Type**: typing.Optional[str]

### CompanyName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Types
- **Type**: typing.Optional[typing.Sequence[str]]

### FirstObservedAt
- **Type**: typing.Optional[str]

### LastObservedAt
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SeverityTypeDef]

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### Remediation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RemediationTypeDef]

### SourceUrl
- **Type**: typing.Optional[str]

### ProductFields
- **Type**: typing.Optional[typing.Mapping[str, str]]

### UserDefinedFields
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Malware
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.MalwareTypeDef]]

### Network
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkTypeDef]

### NetworkPath
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.NetworkPathComponentTypeDef]]

### Process
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ProcessDetailsTypeDef]

### Threats
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.ThreatTypeDef]]

### ThreatIntelIndicators
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.ThreatIntelIndicatorTypeDef]]

### Compliance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ComplianceTypeDef]

### VerificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### WorkflowState
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'DEFERRED', 'IN_PROGRESS', 'NEW', 'RESOLVED']]

### Workflow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WorkflowTypeDef]

### RecordState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]

### RelatedFindings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFindingTypeDef]]

### Note
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NoteTypeDef]

### Vulnerabilities
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityTypeDef]]

### PatchSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PatchSummaryTypeDef]

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionTypeDef]

### FindingProviderFields
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FindingProviderFieldsTypeDef]

### Sample
- **Type**: typing.Optional[bool]

### GeneratorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.GeneratorDetailsTypeDef]

### ProcessedAt
- **Type**: typing.Optional[str]

### AwsAccountName
- **Type**: typing.Optional[str]


# AwsSnsTopicDetailsExtraOutputTypeDef

### KmsMasterKeyId
- **Type**: typing.Optional[str]

### Subscription
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsSnsTopicSubscriptionTypeDef]]

### TopicName
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### SqsSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### SqsFailureFeedbackRoleArn
- **Type**: typing.Optional[str]

### ApplicationSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### FirehoseSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### FirehoseFailureFeedbackRoleArn
- **Type**: typing.Optional[str]

### HttpSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### HttpFailureFeedbackRoleArn
- **Type**: typing.Optional[str]


# AwsSnsTopicDetailsOutputTypeDef

### KmsMasterKeyId
- **Type**: typing.Optional[str]

### Subscription
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsSnsTopicSubscriptionTypeDef]]

### TopicName
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### SqsSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### SqsFailureFeedbackRoleArn
- **Type**: typing.Optional[str]

### ApplicationSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### FirehoseSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### FirehoseFailureFeedbackRoleArn
- **Type**: typing.Optional[str]

### HttpSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### HttpFailureFeedbackRoleArn
- **Type**: typing.Optional[str]


# AwsSnsTopicDetailsTypeDef

### KmsMasterKeyId
- **Type**: typing.Optional[str]

### Subscription
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsSnsTopicSubscriptionTypeDef]]

### TopicName
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### SqsSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### SqsFailureFeedbackRoleArn
- **Type**: typing.Optional[str]

### ApplicationSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### FirehoseSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### FirehoseFailureFeedbackRoleArn
- **Type**: typing.Optional[str]

### HttpSuccessFeedbackRoleArn
- **Type**: typing.Optional[str]

### HttpFailureFeedbackRoleArn
- **Type**: typing.Optional[str]


# AwsSnsTopicSubscriptionTypeDef

### Endpoint
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[str]


# AwsSqsQueueDetailsTypeDef

### KmsDataKeyReusePeriodSeconds
- **Type**: typing.Optional[int]

### KmsMasterKeyId
- **Type**: typing.Optional[str]

### QueueName
- **Type**: typing.Optional[str]

### DeadLetterTargetArn
- **Type**: typing.Optional[str]


# AwsSsmComplianceSummaryTypeDef

### Status
- **Type**: typing.Optional[str]

### CompliantCriticalCount
- **Type**: typing.Optional[int]

### CompliantHighCount
- **Type**: typing.Optional[int]

### CompliantMediumCount
- **Type**: typing.Optional[int]

### ExecutionType
- **Type**: typing.Optional[str]

### NonCompliantCriticalCount
- **Type**: typing.Optional[int]

### CompliantInformationalCount
- **Type**: typing.Optional[int]

### NonCompliantInformationalCount
- **Type**: typing.Optional[int]

### CompliantUnspecifiedCount
- **Type**: typing.Optional[int]

### NonCompliantLowCount
- **Type**: typing.Optional[int]

### NonCompliantHighCount
- **Type**: typing.Optional[int]

### CompliantLowCount
- **Type**: typing.Optional[int]

### ComplianceType
- **Type**: typing.Optional[str]

### PatchBaselineId
- **Type**: typing.Optional[str]

### OverallSeverity
- **Type**: typing.Optional[str]

### NonCompliantMediumCount
- **Type**: typing.Optional[int]

### NonCompliantUnspecifiedCount
- **Type**: typing.Optional[int]

### PatchGroup
- **Type**: typing.Optional[str]


# AwsSsmPatchComplianceDetailsTypeDef

### Patch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSsmPatchTypeDef]


# AwsSsmPatchTypeDef

### ComplianceSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSsmComplianceSummaryTypeDef]


# AwsStepFunctionStateMachineDetailsExtraOutputTypeDef

### Label
- **Type**: typing.Optional[str]

### LoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineLoggingConfigurationDetailsExtraOutputTypeDef]

### Name
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### StateMachineArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### TracingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef]

### Type
- **Type**: typing.Optional[str]


# AwsStepFunctionStateMachineDetailsOutputTypeDef

### Label
- **Type**: typing.Optional[str]

### LoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef]

### Name
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### StateMachineArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### TracingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef]

### Type
- **Type**: typing.Optional[str]


# AwsStepFunctionStateMachineDetailsTypeDef

### Label
- **Type**: typing.Optional[str]

### LoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef]

### Name
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### StateMachineArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### TracingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef]

### Type
- **Type**: typing.Optional[str]


# AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef

### LogGroupArn
- **Type**: typing.Optional[str]


# AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef

### CloudWatchLogsLogGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef]


# AwsStepFunctionStateMachineLoggingConfigurationDetailsExtraOutputTypeDef

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]]

### IncludeExecutionData
- **Type**: typing.Optional[bool]

### Level
- **Type**: typing.Optional[str]


# AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]]

### IncludeExecutionData
- **Type**: typing.Optional[bool]

### Level
- **Type**: typing.Optional[str]


# AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]]

### IncludeExecutionData
- **Type**: typing.Optional[bool]

### Level
- **Type**: typing.Optional[str]


# AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# AwsWafRateBasedRuleDetailsExtraOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RateKey
- **Type**: typing.Optional[str]

### RateLimit
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### MatchPredicates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRateBasedRuleMatchPredicateTypeDef]]


# AwsWafRateBasedRuleDetailsOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RateKey
- **Type**: typing.Optional[str]

### RateLimit
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### MatchPredicates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRateBasedRuleMatchPredicateTypeDef]]


# AwsWafRateBasedRuleDetailsTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RateKey
- **Type**: typing.Optional[str]

### RateLimit
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### MatchPredicates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRateBasedRuleMatchPredicateTypeDef]]


# AwsWafRateBasedRuleMatchPredicateTypeDef

### DataId
- **Type**: typing.Optional[str]

### Negated
- **Type**: typing.Optional[bool]

### Type
- **Type**: typing.Optional[str]


# AwsWafRegionalRateBasedRuleDetailsExtraOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RateKey
- **Type**: typing.Optional[str]

### RateLimit
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### MatchPredicates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]]


# AwsWafRegionalRateBasedRuleDetailsOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RateKey
- **Type**: typing.Optional[str]

### RateLimit
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### MatchPredicates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]]


# AwsWafRegionalRateBasedRuleDetailsTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RateKey
- **Type**: typing.Optional[str]

### RateLimit
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### MatchPredicates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]]


# AwsWafRegionalRateBasedRuleMatchPredicateTypeDef

### DataId
- **Type**: typing.Optional[str]

### Negated
- **Type**: typing.Optional[bool]

### Type
- **Type**: typing.Optional[str]


# AwsWafRegionalRuleDetailsExtraOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PredicateList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRulePredicateListDetailsTypeDef]]

### RuleId
- **Type**: typing.Optional[str]


# AwsWafRegionalRuleDetailsOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PredicateList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRulePredicateListDetailsTypeDef]]

### RuleId
- **Type**: typing.Optional[str]


# AwsWafRegionalRuleDetailsTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PredicateList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRulePredicateListDetailsTypeDef]]

### RuleId
- **Type**: typing.Optional[str]


# AwsWafRegionalRuleGroupDetailsExtraOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RuleGroupId
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRuleGroupRulesDetailsTypeDef]]


# AwsWafRegionalRuleGroupDetailsOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RuleGroupId
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRuleGroupRulesDetailsTypeDef]]


# AwsWafRegionalRuleGroupDetailsTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RuleGroupId
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRuleGroupRulesDetailsTypeDef]]


# AwsWafRegionalRuleGroupRulesActionDetailsTypeDef

### Type
- **Type**: typing.Optional[str]


# AwsWafRegionalRuleGroupRulesDetailsTypeDef

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRuleGroupRulesActionDetailsTypeDef]

### Priority
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsWafRegionalRulePredicateListDetailsTypeDef

### DataId
- **Type**: typing.Optional[str]

### Negated
- **Type**: typing.Optional[bool]

### Type
- **Type**: typing.Optional[str]


# AwsWafRegionalWebAclDetailsExtraOutputTypeDef

### DefaultAction
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RulesList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalWebAclRulesListDetailsTypeDef]]

### WebAclId
- **Type**: typing.Optional[str]


# AwsWafRegionalWebAclDetailsOutputTypeDef

### DefaultAction
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RulesList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalWebAclRulesListDetailsTypeDef]]

### WebAclId
- **Type**: typing.Optional[str]


# AwsWafRegionalWebAclDetailsTypeDef

### DefaultAction
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RulesList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalWebAclRulesListDetailsTypeDef]]

### WebAclId
- **Type**: typing.Optional[str]


# AwsWafRegionalWebAclRulesListActionDetailsTypeDef

### Type
- **Type**: typing.Optional[str]


# AwsWafRegionalWebAclRulesListDetailsTypeDef

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalWebAclRulesListActionDetailsTypeDef]

### OverrideAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef]

### Priority
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef

### Type
- **Type**: typing.Optional[str]


# AwsWafRuleDetailsExtraOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PredicateList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRulePredicateListDetailsTypeDef]]

### RuleId
- **Type**: typing.Optional[str]


# AwsWafRuleDetailsOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PredicateList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRulePredicateListDetailsTypeDef]]

### RuleId
- **Type**: typing.Optional[str]


# AwsWafRuleDetailsTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PredicateList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRulePredicateListDetailsTypeDef]]

### RuleId
- **Type**: typing.Optional[str]


# AwsWafRuleGroupDetailsExtraOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RuleGroupId
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRuleGroupRulesDetailsTypeDef]]


# AwsWafRuleGroupDetailsOutputTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RuleGroupId
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRuleGroupRulesDetailsTypeDef]]


# AwsWafRuleGroupDetailsTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RuleGroupId
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRuleGroupRulesDetailsTypeDef]]


# AwsWafRuleGroupRulesActionDetailsTypeDef

### Type
- **Type**: typing.Optional[str]


# AwsWafRuleGroupRulesDetailsTypeDef

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRuleGroupRulesActionDetailsTypeDef]

### Priority
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsWafRulePredicateListDetailsTypeDef

### DataId
- **Type**: typing.Optional[str]

### Negated
- **Type**: typing.Optional[bool]

### Type
- **Type**: typing.Optional[str]


# AwsWafWebAclDetailsExtraOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### DefaultAction
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafWebAclRuleExtraOutputTypeDef]]

### WebAclId
- **Type**: typing.Optional[str]


# AwsWafWebAclDetailsOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### DefaultAction
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafWebAclRuleOutputTypeDef]]

### WebAclId
- **Type**: typing.Optional[str]


# AwsWafWebAclDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### DefaultAction
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafWebAclRuleTypeDef]]

### WebAclId
- **Type**: typing.Optional[str]


# AwsWafWebAclRuleExtraOutputTypeDef

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WafActionTypeDef]

### ExcludedRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.WafExcludedRuleTypeDef]]

### OverrideAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WafOverrideActionTypeDef]

### Priority
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsWafWebAclRuleOutputTypeDef

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WafActionTypeDef]

### ExcludedRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.WafExcludedRuleTypeDef]]

### OverrideAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WafOverrideActionTypeDef]

### Priority
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsWafWebAclRuleTypeDef

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WafActionTypeDef]

### ExcludedRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.WafExcludedRuleTypeDef]]

### OverrideAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WafOverrideActionTypeDef]

### Priority
- **Type**: typing.Optional[int]

### RuleId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AwsWafv2ActionAllowDetailsExtraOutputTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsExtraOutputTypeDef]


# AwsWafv2ActionAllowDetailsOutputTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsOutputTypeDef]


# AwsWafv2ActionAllowDetailsTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsTypeDef]


# AwsWafv2ActionBlockDetailsExtraOutputTypeDef

### CustomResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomResponseDetailsExtraOutputTypeDef]


# AwsWafv2ActionBlockDetailsOutputTypeDef

### CustomResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomResponseDetailsOutputTypeDef]


# AwsWafv2ActionBlockDetailsTypeDef

### CustomResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomResponseDetailsTypeDef]


# AwsWafv2CustomHttpHeaderTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AwsWafv2CustomRequestHandlingDetailsExtraOutputTypeDef

### InsertHeaders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomHttpHeaderTypeDef]]


# AwsWafv2CustomRequestHandlingDetailsOutputTypeDef

### InsertHeaders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomHttpHeaderTypeDef]]


# AwsWafv2CustomRequestHandlingDetailsTypeDef

### InsertHeaders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomHttpHeaderTypeDef]]


# AwsWafv2CustomResponseDetailsExtraOutputTypeDef

### CustomResponseBodyKey
- **Type**: typing.Optional[str]

### ResponseCode
- **Type**: typing.Optional[int]

### ResponseHeaders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomHttpHeaderTypeDef]]


# AwsWafv2CustomResponseDetailsOutputTypeDef

### CustomResponseBodyKey
- **Type**: typing.Optional[str]

### ResponseCode
- **Type**: typing.Optional[int]

### ResponseHeaders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomHttpHeaderTypeDef]]


# AwsWafv2CustomResponseDetailsTypeDef

### CustomResponseBodyKey
- **Type**: typing.Optional[str]

### ResponseCode
- **Type**: typing.Optional[int]

### ResponseHeaders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomHttpHeaderTypeDef]]


# AwsWafv2RuleGroupDetailsExtraOutputTypeDef

### Capacity
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesDetailsExtraOutputTypeDef]]

### Scope
- **Type**: typing.Optional[str]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetailsTypeDef]


# AwsWafv2RuleGroupDetailsOutputTypeDef

### Capacity
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesDetailsOutputTypeDef]]

### Scope
- **Type**: typing.Optional[str]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetailsTypeDef]


# AwsWafv2RuleGroupDetailsTypeDef

### Capacity
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesDetailsTypeDef]]

### Scope
- **Type**: typing.Optional[str]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetailsTypeDef]


# AwsWafv2RulesActionCaptchaDetailsExtraOutputTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsExtraOutputTypeDef]


# AwsWafv2RulesActionCaptchaDetailsOutputTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsOutputTypeDef]


# AwsWafv2RulesActionCaptchaDetailsTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsTypeDef]


# AwsWafv2RulesActionCountDetailsExtraOutputTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsExtraOutputTypeDef]


# AwsWafv2RulesActionCountDetailsOutputTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsOutputTypeDef]


# AwsWafv2RulesActionCountDetailsTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2CustomRequestHandlingDetailsTypeDef]


# AwsWafv2RulesActionDetailsExtraOutputTypeDef

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionAllowDetailsExtraOutputTypeDef]

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionBlockDetailsExtraOutputTypeDef]

### Captcha
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionCaptchaDetailsExtraOutputTypeDef]

### Count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionCountDetailsExtraOutputTypeDef]


# AwsWafv2RulesActionDetailsOutputTypeDef

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionAllowDetailsOutputTypeDef]

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionBlockDetailsOutputTypeDef]

### Captcha
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionCaptchaDetailsOutputTypeDef]

### Count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionCountDetailsOutputTypeDef]


# AwsWafv2RulesActionDetailsTypeDef

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionAllowDetailsTypeDef]

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionBlockDetailsTypeDef]

### Captcha
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionCaptchaDetailsTypeDef]

### Count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionCountDetailsTypeDef]


# AwsWafv2RulesDetailsExtraOutputTypeDef

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionDetailsExtraOutputTypeDef]

### Name
- **Type**: typing.Optional[str]

### OverrideAction
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetailsTypeDef]


# AwsWafv2RulesDetailsOutputTypeDef

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionDetailsOutputTypeDef]

### Name
- **Type**: typing.Optional[str]

### OverrideAction
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetailsTypeDef]


# AwsWafv2RulesDetailsTypeDef

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesActionDetailsTypeDef]

### Name
- **Type**: typing.Optional[str]

### OverrideAction
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetailsTypeDef]


# AwsWafv2VisibilityConfigDetailsTypeDef

### CloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### MetricName
- **Type**: typing.Optional[str]

### SampledRequestsEnabled
- **Type**: typing.Optional[bool]


# AwsWafv2WebAclActionDetailsExtraOutputTypeDef

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionAllowDetailsExtraOutputTypeDef]

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionBlockDetailsExtraOutputTypeDef]


# AwsWafv2WebAclActionDetailsOutputTypeDef

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionAllowDetailsOutputTypeDef]

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionBlockDetailsOutputTypeDef]


# AwsWafv2WebAclActionDetailsTypeDef

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionAllowDetailsTypeDef]

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2ActionBlockDetailsTypeDef]


# AwsWafv2WebAclCaptchaConfigDetailsTypeDef

### ImmunityTimeProperty
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef]


# AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef

### ImmunityTime
- **Type**: typing.Optional[int]


# AwsWafv2WebAclDetailsExtraOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### ManagedbyFirewallManager
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### Capacity
- **Type**: typing.Optional[int]

### CaptchaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclCaptchaConfigDetailsTypeDef]

### DefaultAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclActionDetailsExtraOutputTypeDef]

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesDetailsExtraOutputTypeDef]]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetailsTypeDef]


# AwsWafv2WebAclDetailsOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### ManagedbyFirewallManager
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### Capacity
- **Type**: typing.Optional[int]

### CaptchaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclCaptchaConfigDetailsTypeDef]

### DefaultAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclActionDetailsOutputTypeDef]

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesDetailsOutputTypeDef]]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetailsTypeDef]


# AwsWafv2WebAclDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### ManagedbyFirewallManager
- **Type**: typing.Optional[bool]

### Id
- **Type**: typing.Optional[str]

### Capacity
- **Type**: typing.Optional[int]

### CaptchaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclCaptchaConfigDetailsTypeDef]

### DefaultAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclActionDetailsTypeDef]

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RulesDetailsTypeDef]]

### VisibilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2VisibilityConfigDetailsTypeDef]


# AwsXrayEncryptionConfigDetailsTypeDef

### KeyId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteAutomationRulesRequestRequestTypeDef

### AutomationRulesArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeleteAutomationRulesResponseTypeDef

### ProcessedAutomationRules
- **Type**: typing.List[str]
- **Required**: Yes

### UnprocessedAutomationRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.UnprocessedAutomationRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDisableStandardsRequestRequestTypeDef

### StandardsSubscriptionArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDisableStandardsResponseTypeDef

### StandardsSubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StandardsSubscriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchEnableStandardsRequestRequestTypeDef

### StandardsSubscriptionRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StandardsSubscriptionRequestTypeDef]
- **Required**: Yes


# BatchEnableStandardsResponseTypeDef

### StandardsSubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StandardsSubscriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetAutomationRulesRequestRequestTypeDef

### AutomationRulesArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetAutomationRulesResponseTypeDef

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesConfigTypeDef]
- **Required**: Yes

### UnprocessedAutomationRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.UnprocessedAutomationRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetConfigurationPolicyAssociationsRequestRequestTypeDef

### ConfigurationPolicyAssociationIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.ConfigurationPolicyAssociationTypeDef]
- **Required**: Yes


# BatchGetConfigurationPolicyAssociationsResponseTypeDef

### ConfigurationPolicyAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ConfigurationPolicyAssociationSummaryTypeDef]
- **Required**: Yes

### UnprocessedConfigurationPolicyAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.UnprocessedConfigurationPolicyAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetSecurityControlsRequestRequestTypeDef

### SecurityControlIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetSecurityControlsResponseTypeDef

### SecurityControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlTypeDef]
- **Required**: Yes

### UnprocessedIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.UnprocessedSecurityControlTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetStandardsControlAssociationsRequestRequestTypeDef

### StandardsControlAssociationIds
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StandardsControlAssociationIdTypeDef]
- **Required**: Yes


# BatchGetStandardsControlAssociationsResponseTypeDef

### StandardsControlAssociationDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StandardsControlAssociationDetailTypeDef]
- **Required**: Yes

### UnprocessedAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.UnprocessedStandardsControlAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchImportFindingsRequestRequestTypeDef

### Findings
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingTypeDef, aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingExtraOutputTypeDef]]
- **Required**: Yes


# BatchImportFindingsResponseTypeDef

### FailedCount
- **Type**: <class 'int'>
- **Required**: Yes

### SuccessCount
- **Type**: <class 'int'>
- **Required**: Yes

### FailedFindings
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ImportFindingsErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchUpdateAutomationRulesRequestRequestTypeDef

### UpdateAutomationRulesRequestItems
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.UpdateAutomationRulesRequestItemTypeDef]
- **Required**: Yes


# BatchUpdateAutomationRulesResponseTypeDef

### ProcessedAutomationRules
- **Type**: typing.List[str]
- **Required**: Yes

### UnprocessedAutomationRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.UnprocessedAutomationRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchUpdateFindingsRequestRequestTypeDef

### FindingIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingIdentifierTypeDef]
- **Required**: Yes

### Note
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NoteUpdateTypeDef]

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SeverityUpdateTypeDef]

### VerificationState
- **Type**: typing.Optional[typing.Literal['BENIGN_POSITIVE', 'FALSE_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']]

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### Types
- **Type**: typing.Optional[typing.Sequence[str]]

### UserDefinedFields
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Workflow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.WorkflowUpdateTypeDef]

### RelatedFindings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFindingTypeDef]]


# BatchUpdateFindingsResponseTypeDef

### ProcessedFindings
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingIdentifierTypeDef]
- **Required**: Yes

### UnprocessedFindings
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.BatchUpdateFindingsUnprocessedFindingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchUpdateFindingsUnprocessedFindingTypeDef

### FindingIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingIdentifierTypeDef'>
- **Required**: Yes

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# BatchUpdateStandardsControlAssociationsRequestRequestTypeDef

### StandardsControlAssociationUpdates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StandardsControlAssociationUpdateTypeDef]
- **Required**: Yes


# BatchUpdateStandardsControlAssociationsResponseTypeDef

### UnprocessedAssociationUpdates
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.UnprocessedStandardsControlAssociationUpdateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BooleanConfigurationOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[bool]


# BooleanFilterTypeDef

### Value
- **Type**: typing.Optional[bool]


# CellTypeDef

### Column
- **Type**: typing.Optional[int]

### Row
- **Type**: typing.Optional[int]

### ColumnName
- **Type**: typing.Optional[str]

### CellReference
- **Type**: typing.Optional[str]


# CidrBlockAssociationTypeDef

### AssociationId
- **Type**: typing.Optional[str]

### CidrBlock
- **Type**: typing.Optional[str]

### CidrBlockState
- **Type**: typing.Optional[str]


# CityTypeDef

### CityName
- **Type**: typing.Optional[str]


# ClassificationResultExtraOutputTypeDef

### MimeType
- **Type**: typing.Optional[str]

### SizeClassified
- **Type**: typing.Optional[int]

### AdditionalOccurrences
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ClassificationStatusTypeDef]

### SensitiveData
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SensitiveDataResultExtraOutputTypeDef]]

### CustomDataIdentifiers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.CustomDataIdentifiersResultExtraOutputTypeDef]


# ClassificationResultOutputTypeDef

### MimeType
- **Type**: typing.Optional[str]

### SizeClassified
- **Type**: typing.Optional[int]

### AdditionalOccurrences
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ClassificationStatusTypeDef]

### SensitiveData
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SensitiveDataResultOutputTypeDef]]

### CustomDataIdentifiers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.CustomDataIdentifiersResultOutputTypeDef]


# ClassificationResultTypeDef

### MimeType
- **Type**: typing.Optional[str]

### SizeClassified
- **Type**: typing.Optional[int]

### AdditionalOccurrences
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ClassificationStatusTypeDef]

### SensitiveData
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SensitiveDataResultTypeDef]]

### CustomDataIdentifiers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.CustomDataIdentifiersResultTypeDef]


# ClassificationStatusTypeDef

### Code
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]


# CloudWatchLogsLogGroupArnConfigDetailsTypeDef

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### HostedZoneId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]


# CodeVulnerabilitiesFilePathTypeDef

### EndLine
- **Type**: typing.Optional[int]

### FileName
- **Type**: typing.Optional[str]

### FilePath
- **Type**: typing.Optional[str]

### StartLine
- **Type**: typing.Optional[int]


# ComplianceExtraOutputTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'NOT_AVAILABLE', 'PASSED', 'WARNING']]

### RelatedRequirements
- **Type**: typing.Optional[typing.List[str]]

### StatusReasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StatusReasonTypeDef]]

### SecurityControlId
- **Type**: typing.Optional[str]

### AssociatedStandards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AssociatedStandardTypeDef]]

### SecurityControlParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlParameterExtraOutputTypeDef]]


# ComplianceOutputTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'NOT_AVAILABLE', 'PASSED', 'WARNING']]

### RelatedRequirements
- **Type**: typing.Optional[typing.List[str]]

### StatusReasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StatusReasonTypeDef]]

### SecurityControlId
- **Type**: typing.Optional[str]

### AssociatedStandards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AssociatedStandardTypeDef]]

### SecurityControlParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlParameterOutputTypeDef]]


# ComplianceTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'NOT_AVAILABLE', 'PASSED', 'WARNING']]

### RelatedRequirements
- **Type**: typing.Optional[typing.Sequence[str]]

### StatusReasons
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StatusReasonTypeDef]]

### SecurityControlId
- **Type**: typing.Optional[str]

### AssociatedStandards
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AssociatedStandardTypeDef]]

### SecurityControlParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlParameterTypeDef]]


# ConfigurationOptionsTypeDef

### Integer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.IntegerConfigurationOptionsTypeDef]

### IntegerList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.IntegerListConfigurationOptionsTypeDef]

### Double
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.DoubleConfigurationOptionsTypeDef]

### String
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StringConfigurationOptionsTypeDef]

### StringList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StringListConfigurationOptionsTypeDef]

### Boolean
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.BooleanConfigurationOptionsTypeDef]

### Enum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.EnumConfigurationOptionsTypeDef]

### EnumList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.EnumListConfigurationOptionsTypeDef]


# ConfigurationPolicyAssociationSummaryTypeDef

### ConfigurationPolicyId
- **Type**: typing.Optional[str]

### TargetId
- **Type**: typing.Optional[str]

### TargetType
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT', 'ROOT']]

### AssociationType
- **Type**: typing.Optional[typing.Literal['APPLIED', 'INHERITED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### AssociationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCESS']]

### AssociationStatusMessage
- **Type**: typing.Optional[str]


# ConfigurationPolicyAssociationTypeDef

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.TargetTypeDef]


# ConfigurationPolicySummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### ServiceEnabled
- **Type**: typing.Optional[bool]


# ContainerDetailsExtraOutputTypeDef

### ContainerRuntime
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### ImageName
- **Type**: typing.Optional[str]

### LaunchedAt
- **Type**: typing.Optional[str]

### VolumeMounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VolumeMountTypeDef]]

### Privileged
- **Type**: typing.Optional[bool]


# ContainerDetailsOutputTypeDef

### ContainerRuntime
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### ImageName
- **Type**: typing.Optional[str]

### LaunchedAt
- **Type**: typing.Optional[str]

### VolumeMounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VolumeMountTypeDef]]

### Privileged
- **Type**: typing.Optional[bool]


# ContainerDetailsTypeDef

### ContainerRuntime
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### ImageName
- **Type**: typing.Optional[str]

### LaunchedAt
- **Type**: typing.Optional[str]

### VolumeMounts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.VolumeMountTypeDef]]

### Privileged
- **Type**: typing.Optional[bool]


# CountryTypeDef

### CountryCode
- **Type**: typing.Optional[str]

### CountryName
- **Type**: typing.Optional[str]


# CreateActionTargetRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# CreateActionTargetResponseTypeDef

### ActionTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAutomationRuleRequestRequestTypeDef

### RuleOrder
- **Type**: <class 'int'>
- **Required**: Yes

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Criteria
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesFindingFiltersTypeDef'>
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesActionTypeDef, aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesActionOutputTypeDef]]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RuleStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### IsTerminal
- **Type**: typing.Optional[bool]


# CreateAutomationRuleResponseTypeDef

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfigurationPolicyRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.PolicyTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConfigurationPolicyResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ConfigurationPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.PolicyOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFindingAggregatorRequestRequestTypeDef

### RegionLinkingMode
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateFindingAggregatorResponseTypeDef

### FindingAggregatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### FindingAggregationRegion
- **Type**: <class 'str'>
- **Required**: Yes

### RegionLinkingMode
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInsightRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingFiltersTypeDef'>
- **Required**: Yes

### GroupByAttribute
- **Type**: <class 'str'>
- **Required**: Yes


# CreateInsightResponseTypeDef

### InsightArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMembersRequestRequestTypeDef

### AccountDetails
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AccountDetailsTypeDef]
- **Required**: Yes


# CreateMembersResponseTypeDef

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomDataIdentifiersDetectionsExtraOutputTypeDef

### Count
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Occurrences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.OccurrencesExtraOutputTypeDef]


# CustomDataIdentifiersDetectionsOutputTypeDef

### Count
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Occurrences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.OccurrencesOutputTypeDef]


# CustomDataIdentifiersDetectionsTypeDef

### Count
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Occurrences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.OccurrencesTypeDef]


# CustomDataIdentifiersResultExtraOutputTypeDef

### Detections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.CustomDataIdentifiersDetectionsExtraOutputTypeDef]]

### TotalCount
- **Type**: typing.Optional[int]


# CustomDataIdentifiersResultOutputTypeDef

### Detections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.CustomDataIdentifiersDetectionsOutputTypeDef]]

### TotalCount
- **Type**: typing.Optional[int]


# CustomDataIdentifiersResultTypeDef

### Detections
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.CustomDataIdentifiersDetectionsTypeDef]]

### TotalCount
- **Type**: typing.Optional[int]


# CvssExtraOutputTypeDef

### Version
- **Type**: typing.Optional[str]

### BaseScore
- **Type**: typing.Optional[float]

### BaseVector
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### Adjustments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AdjustmentTypeDef]]


# CvssOutputTypeDef

### Version
- **Type**: typing.Optional[str]

### BaseScore
- **Type**: typing.Optional[float]

### BaseVector
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### Adjustments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AdjustmentTypeDef]]


# CvssTypeDef

### Version
- **Type**: typing.Optional[str]

### BaseScore
- **Type**: typing.Optional[float]

### BaseVector
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### Adjustments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AdjustmentTypeDef]]


# DataClassificationDetailsExtraOutputTypeDef

### DetailedResultsLocation
- **Type**: typing.Optional[str]

### Result
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ClassificationResultExtraOutputTypeDef]


# DataClassificationDetailsOutputTypeDef

### DetailedResultsLocation
- **Type**: typing.Optional[str]

### Result
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ClassificationResultOutputTypeDef]


# DataClassificationDetailsTypeDef

### DetailedResultsLocation
- **Type**: typing.Optional[str]

### Result
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ClassificationResultTypeDef]


# DateFilterTypeDef

### Start
- **Type**: typing.Optional[str]

### End
- **Type**: typing.Optional[str]

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.DateRangeTypeDef]


# DateRangeTypeDef

### Value
- **Type**: typing.Optional[int]

### Unit
- **Type**: typing.Optional[typing.Literal['DAYS']]


# DeclineInvitationsRequestRequestTypeDef

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeclineInvitationsResponseTypeDef

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteActionTargetRequestRequestTypeDef

### ActionTargetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteActionTargetResponseTypeDef

### ActionTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteConfigurationPolicyRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFindingAggregatorRequestRequestTypeDef

### FindingAggregatorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInsightRequestRequestTypeDef

### InsightArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInsightResponseTypeDef

### InsightArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteInvitationsRequestRequestTypeDef

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteInvitationsResponseTypeDef

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMembersRequestRequestTypeDef

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteMembersResponseTypeDef

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeActionTargetsRequestDescribeActionTargetsPaginateTypeDef

### ActionTargetArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# DescribeActionTargetsRequestRequestTypeDef

### ActionTargetArns
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeActionTargetsResponseTypeDef

### ActionTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ActionTargetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeHubRequestRequestTypeDef

### HubArn
- **Type**: typing.Optional[str]


# DescribeHubResponseTypeDef

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### SubscribedAt
- **Type**: <class 'str'>
- **Required**: Yes

### AutoEnableControls
- **Type**: <class 'bool'>
- **Required**: Yes

### ControlFindingGenerator
- **Type**: typing.Literal['SECURITY_CONTROL', 'STANDARD_CONTROL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOrganizationConfigurationResponseTypeDef

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes

### MemberAccountLimitReached
- **Type**: <class 'bool'>
- **Required**: Yes

### AutoEnableStandards
- **Type**: typing.Literal['DEFAULT', 'NONE']
- **Required**: Yes

### OrganizationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.OrganizationConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProductsRequestDescribeProductsPaginateTypeDef

### ProductArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# DescribeProductsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ProductArn
- **Type**: typing.Optional[str]


# DescribeProductsResponseTypeDef

### Products
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ProductTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef

### StandardsSubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# DescribeStandardsControlsRequestRequestTypeDef

### StandardsSubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeStandardsControlsResponseTypeDef

### Controls
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StandardsControlTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStandardsRequestDescribeStandardsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# DescribeStandardsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeStandardsResponseTypeDef

### Standards
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StandardTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisableImportFindingsForProductRequestRequestTypeDef

### ProductSubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisableOrganizationAdminAccountRequestRequestTypeDef

### AdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMembersRequestRequestTypeDef

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DnsRequestActionTypeDef

### Domain
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[str]

### Blocked
- **Type**: typing.Optional[bool]


# DoubleConfigurationOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[float]

### Min
- **Type**: typing.Optional[float]

### Max
- **Type**: typing.Optional[float]


# EnableImportFindingsForProductRequestRequestTypeDef

### ProductArn
- **Type**: <class 'str'>
- **Required**: Yes


# EnableImportFindingsForProductResponseTypeDef

### ProductSubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableOrganizationAdminAccountRequestRequestTypeDef

### AdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# EnableSecurityHubRequestRequestTypeDef

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### EnableDefaultStandards
- **Type**: typing.Optional[bool]

### ControlFindingGenerator
- **Type**: typing.Optional[typing.Literal['SECURITY_CONTROL', 'STANDARD_CONTROL']]


# EnumConfigurationOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[typing.List[str]]


# EnumListConfigurationOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[typing.List[str]]

### MaxItems
- **Type**: typing.Optional[int]

### AllowedValues
- **Type**: typing.Optional[typing.List[str]]


# FilePathsTypeDef

### FilePath
- **Type**: typing.Optional[str]

### FileName
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### Hash
- **Type**: typing.Optional[str]


# FindingAggregatorTypeDef

### FindingAggregatorArn
- **Type**: typing.Optional[str]


# FindingHistoryRecordTypeDef

### FindingIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingIdentifierTypeDef]

### UpdateTime
- **Type**: typing.Optional[datetime.datetime]

### FindingCreated
- **Type**: typing.Optional[bool]

### UpdateSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FindingHistoryUpdateSourceTypeDef]

### Updates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FindingHistoryUpdateTypeDef]]

### NextToken
- **Type**: typing.Optional[str]


# FindingHistoryUpdateSourceTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['BATCH_IMPORT_FINDINGS', 'BATCH_UPDATE_FINDINGS']]

### Identity
- **Type**: typing.Optional[str]


# FindingHistoryUpdateTypeDef

### UpdatedField
- **Type**: typing.Optional[str]

### OldValue
- **Type**: typing.Optional[str]

### NewValue
- **Type**: typing.Optional[str]


# FindingProviderFieldsExtraOutputTypeDef

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### RelatedFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFindingTypeDef]]

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FindingProviderSeverityTypeDef]

### Types
- **Type**: typing.Optional[typing.List[str]]


# FindingProviderFieldsOutputTypeDef

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### RelatedFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFindingTypeDef]]

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FindingProviderSeverityTypeDef]

### Types
- **Type**: typing.Optional[typing.List[str]]


# FindingProviderFieldsTypeDef

### Confidence
- **Type**: typing.Optional[int]

### Criticality
- **Type**: typing.Optional[int]

### RelatedFindings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RelatedFindingTypeDef]]

### Severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.FindingProviderSeverityTypeDef]

### Types
- **Type**: typing.Optional[typing.Sequence[str]]


# FindingProviderSeverityTypeDef

### Label
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM']]

### Original
- **Type**: typing.Optional[str]


# FirewallPolicyDetailsExtraOutputTypeDef

### StatefulRuleGroupReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]]

### StatelessCustomActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatelessCustomActionsDetailsExtraOutputTypeDef]]

### StatelessDefaultActions
- **Type**: typing.Optional[typing.List[str]]

### StatelessFragmentDefaultActions
- **Type**: typing.Optional[typing.List[str]]

### StatelessRuleGroupReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]]


# FirewallPolicyDetailsOutputTypeDef

### StatefulRuleGroupReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]]

### StatelessCustomActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef]]

### StatelessDefaultActions
- **Type**: typing.Optional[typing.List[str]]

### StatelessFragmentDefaultActions
- **Type**: typing.Optional[typing.List[str]]

### StatelessRuleGroupReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]]


# FirewallPolicyDetailsTypeDef

### StatefulRuleGroupReferences
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]]

### StatelessCustomActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatelessCustomActionsDetailsTypeDef]]

### StatelessDefaultActions
- **Type**: typing.Optional[typing.Sequence[str]]

### StatelessFragmentDefaultActions
- **Type**: typing.Optional[typing.Sequence[str]]

### StatelessRuleGroupReferences
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]]


# FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef

### ResourceArn
- **Type**: typing.Optional[str]


# FirewallPolicyStatelessCustomActionsDetailsExtraOutputTypeDef

### ActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomActionDefinitionExtraOutputTypeDef]

### ActionName
- **Type**: typing.Optional[str]


# FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef

### ActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomActionDefinitionOutputTypeDef]

### ActionName
- **Type**: typing.Optional[str]


# FirewallPolicyStatelessCustomActionsDetailsTypeDef

### ActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomActionDefinitionTypeDef]

### ActionName
- **Type**: typing.Optional[str]


# FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef

### Priority
- **Type**: typing.Optional[int]

### ResourceArn
- **Type**: typing.Optional[str]


# GeneratorDetailsExtraOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Labels
- **Type**: typing.Optional[typing.List[str]]


# GeneratorDetailsOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Labels
- **Type**: typing.Optional[typing.List[str]]


# GeneratorDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Labels
- **Type**: typing.Optional[typing.Sequence[str]]


# GeoLocationTypeDef

### Lon
- **Type**: typing.Optional[float]

### Lat
- **Type**: typing.Optional[float]


# GetAdministratorAccountResponseTypeDef

### Administrator
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.InvitationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfigurationPolicyAssociationRequestRequestTypeDef

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.TargetTypeDef'>
- **Required**: Yes


# GetConfigurationPolicyAssociationResponseTypeDef

### ConfigurationPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetType
- **Type**: typing.Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT', 'ROOT']
- **Required**: Yes

### AssociationType
- **Type**: typing.Literal['APPLIED', 'INHERITED']
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AssociationStatus
- **Type**: typing.Literal['FAILED', 'PENDING', 'SUCCESS']
- **Required**: Yes

### AssociationStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfigurationPolicyRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationPolicyResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ConfigurationPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.PolicyOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEnabledStandardsRequestGetEnabledStandardsPaginateTypeDef

### StandardsSubscriptionArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# GetEnabledStandardsRequestRequestTypeDef

### StandardsSubscriptionArns
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetEnabledStandardsResponseTypeDef

### StandardsSubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StandardsSubscriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetFindingAggregatorRequestRequestTypeDef

### FindingAggregatorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetFindingAggregatorResponseTypeDef

### FindingAggregatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### FindingAggregationRegion
- **Type**: <class 'str'>
- **Required**: Yes

### RegionLinkingMode
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFindingHistoryRequestGetFindingHistoryPaginateTypeDef

### FindingIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingIdentifierTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# GetFindingHistoryRequestRequestTypeDef

### FindingIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingIdentifierTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetFindingHistoryResponseTypeDef

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FindingHistoryRecordTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetFindingsRequestGetFindingsPaginateTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingFiltersTypeDef]

### SortCriteria
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SortCriterionTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# GetFindingsRequestRequestTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingFiltersTypeDef]

### SortCriteria
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SortCriterionTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetFindingsResponseTypeDef

### Findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetInsightResultsRequestRequestTypeDef

### InsightArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetInsightResultsResponseTypeDef

### InsightResults
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.InsightResultsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInsightsRequestGetInsightsPaginateTypeDef

### InsightArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# GetInsightsRequestRequestTypeDef

### InsightArns
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetInsightsResponseTypeDef

### Insights
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.InsightTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetInvitationsCountResponseTypeDef

### InvitationsCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMasterAccountResponseTypeDef

### Master
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.InvitationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMembersRequestRequestTypeDef

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetMembersResponseTypeDef

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MemberTypeDef]
- **Required**: Yes

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSecurityControlDefinitionRequestRequestTypeDef

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSecurityControlDefinitionResponseTypeDef

### SecurityControlDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlDefinitionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IcmpTypeCodeTypeDef

### Code
- **Type**: typing.Optional[int]

### Type
- **Type**: typing.Optional[int]


# ImportFindingsErrorTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# InsightResultValueTypeDef

### GroupByAttributeValue
- **Type**: <class 'str'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes


# InsightResultsTypeDef

### InsightArn
- **Type**: <class 'str'>
- **Required**: Yes

### GroupByAttribute
- **Type**: <class 'str'>
- **Required**: Yes

### ResultValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.InsightResultValueTypeDef]
- **Required**: Yes


# InsightTypeDef

### InsightArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingFiltersOutputTypeDef'>
- **Required**: Yes

### GroupByAttribute
- **Type**: <class 'str'>
- **Required**: Yes


# IntegerConfigurationOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[int]

### Min
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]


# IntegerListConfigurationOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[typing.List[int]]

### Min
- **Type**: typing.Optional[int]

### Max
- **Type**: typing.Optional[int]

### MaxItems
- **Type**: typing.Optional[int]


# InvitationTypeDef

### AccountId
- **Type**: typing.Optional[str]

### InvitationId
- **Type**: typing.Optional[str]

### InvitedAt
- **Type**: typing.Optional[datetime.datetime]

### MemberStatus
- **Type**: typing.Optional[str]


# InviteMembersRequestRequestTypeDef

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# InviteMembersResponseTypeDef

### UnprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IpFilterTypeDef

### Cidr
- **Type**: typing.Optional[str]


# IpOrganizationDetailsTypeDef

### Asn
- **Type**: typing.Optional[int]

### AsnOrg
- **Type**: typing.Optional[str]

### Isp
- **Type**: typing.Optional[str]

### Org
- **Type**: typing.Optional[str]


# Ipv6CidrBlockAssociationTypeDef

### AssociationId
- **Type**: typing.Optional[str]

### Ipv6CidrBlock
- **Type**: typing.Optional[str]

### CidrBlockState
- **Type**: typing.Optional[str]


# KeywordFilterTypeDef

### Value
- **Type**: typing.Optional[str]


# ListAutomationRulesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAutomationRulesResponseTypeDef

### AutomationRulesMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationPoliciesRequestListConfigurationPoliciesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# ListConfigurationPoliciesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListConfigurationPoliciesResponseTypeDef

### ConfigurationPolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ConfigurationPolicySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationPolicyAssociationsRequestListConfigurationPolicyAssociationsPaginateTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AssociationFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# ListConfigurationPolicyAssociationsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AssociationFiltersTypeDef]


# ListConfigurationPolicyAssociationsResponseTypeDef

### ConfigurationPolicyAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.ConfigurationPolicyAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEnabledProductsForImportRequestListEnabledProductsForImportPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# ListEnabledProductsForImportRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEnabledProductsForImportResponseTypeDef

### ProductSubscriptions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFindingAggregatorsRequestListFindingAggregatorsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# ListFindingAggregatorsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFindingAggregatorsResponseTypeDef

### FindingAggregators
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FindingAggregatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInvitationsRequestListInvitationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# ListInvitationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInvitationsResponseTypeDef

### Invitations
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.InvitationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMembersRequestListMembersPaginateTypeDef

### OnlyAssociated
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# ListMembersRequestRequestTypeDef

### OnlyAssociated
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMembersResponseTypeDef

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.MemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# ListOrganizationAdminAccountsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationAdminAccountsResponseTypeDef

### AdminAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.AdminAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityControlDefinitionsRequestListSecurityControlDefinitionsPaginateTypeDef

### StandardsArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# ListSecurityControlDefinitionsRequestRequestTypeDef

### StandardsArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSecurityControlDefinitionsResponseTypeDef

### SecurityControlDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PaginatorConfigTypeDef]


# ListStandardsControlAssociationsRequestRequestTypeDef

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListStandardsControlAssociationsResponseTypeDef

### StandardsControlAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StandardsControlAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoadBalancerStateTypeDef

### Code
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]


# MalwareTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['ADWARE', 'BLENDED_THREAT', 'BOTNET_AGENT', 'COIN_MINER', 'EXPLOIT_KIT', 'KEYLOGGER', 'MACRO', 'POTENTIALLY_UNWANTED', 'RANSOMWARE', 'REMOTE_ACCESS', 'ROOTKIT', 'SPYWARE', 'TROJAN', 'VIRUS', 'WORM']]

### Path
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['OBSERVED', 'REMOVAL_FAILED', 'REMOVED']]


# MapFilterTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Comparison
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQUALS', 'NOT_CONTAINS', 'NOT_EQUALS']]


# MemberTypeDef

### AccountId
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### MasterId
- **Type**: typing.Optional[str]

### AdministratorId
- **Type**: typing.Optional[str]

### MemberStatus
- **Type**: typing.Optional[str]

### InvitedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# NetworkConnectionActionTypeDef

### ConnectionDirection
- **Type**: typing.Optional[str]

### RemoteIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionRemoteIpDetailsTypeDef]

### RemotePortDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionRemotePortDetailsTypeDef]

### LocalPortDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionLocalPortDetailsTypeDef]

### Protocol
- **Type**: typing.Optional[str]

### Blocked
- **Type**: typing.Optional[bool]


# NetworkHeaderExtraOutputTypeDef

### Protocol
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkPathComponentDetailsExtraOutputTypeDef]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkPathComponentDetailsExtraOutputTypeDef]


# NetworkHeaderOutputTypeDef

### Protocol
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkPathComponentDetailsOutputTypeDef]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkPathComponentDetailsOutputTypeDef]


# NetworkHeaderTypeDef

### Protocol
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkPathComponentDetailsTypeDef]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkPathComponentDetailsTypeDef]


# NetworkPathComponentDetailsExtraOutputTypeDef

### Address
- **Type**: typing.Optional[typing.List[str]]

### PortRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.PortRangeTypeDef]]


# NetworkPathComponentDetailsOutputTypeDef

### Address
- **Type**: typing.Optional[typing.List[str]]

### PortRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.PortRangeTypeDef]]


# NetworkPathComponentDetailsTypeDef

### Address
- **Type**: typing.Optional[typing.Sequence[str]]

### PortRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.PortRangeTypeDef]]


# NetworkPathComponentExtraOutputTypeDef

### ComponentId
- **Type**: typing.Optional[str]

### ComponentType
- **Type**: typing.Optional[str]

### Egress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkHeaderExtraOutputTypeDef]

### Ingress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkHeaderExtraOutputTypeDef]


# NetworkPathComponentOutputTypeDef

### ComponentId
- **Type**: typing.Optional[str]

### ComponentType
- **Type**: typing.Optional[str]

### Egress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkHeaderOutputTypeDef]

### Ingress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkHeaderOutputTypeDef]


# NetworkPathComponentTypeDef

### ComponentId
- **Type**: typing.Optional[str]

### ComponentType
- **Type**: typing.Optional[str]

### Egress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkHeaderTypeDef]

### Ingress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NetworkHeaderTypeDef]


# NetworkTypeDef

### Direction
- **Type**: typing.Optional[typing.Literal['IN', 'OUT']]

### Protocol
- **Type**: typing.Optional[str]

### OpenPortRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PortRangeTypeDef]

### SourceIpV4
- **Type**: typing.Optional[str]

### SourceIpV6
- **Type**: typing.Optional[str]

### SourcePort
- **Type**: typing.Optional[int]

### SourceDomain
- **Type**: typing.Optional[str]

### SourceMac
- **Type**: typing.Optional[str]

### DestinationIpV4
- **Type**: typing.Optional[str]

### DestinationIpV6
- **Type**: typing.Optional[str]

### DestinationPort
- **Type**: typing.Optional[int]

### DestinationDomain
- **Type**: typing.Optional[str]


# NoteTypeDef

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'str'>
- **Required**: Yes


# NoteUpdateTypeDef

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedBy
- **Type**: <class 'str'>
- **Required**: Yes


# NumberFilterTypeDef

### Gte
- **Type**: typing.Optional[float]

### Lte
- **Type**: typing.Optional[float]

### Gt
- **Type**: typing.Optional[float]

### Lt
- **Type**: typing.Optional[float]

### Eq
- **Type**: typing.Optional[float]


# OccurrencesExtraOutputTypeDef

### LineRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RangeTypeDef]]

### OffsetRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RangeTypeDef]]

### Pages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.PageTypeDef]]

### Records
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RecordTypeDef]]

### Cells
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.CellTypeDef]]


# OccurrencesOutputTypeDef

### LineRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RangeTypeDef]]

### OffsetRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RangeTypeDef]]

### Pages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.PageTypeDef]]

### Records
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RecordTypeDef]]

### Cells
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.CellTypeDef]]


# OccurrencesTypeDef

### LineRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RangeTypeDef]]

### OffsetRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RangeTypeDef]]

### Pages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.PageTypeDef]]

### Records
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RecordTypeDef]]

### Cells
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.CellTypeDef]]


# OrganizationConfigurationTypeDef

### ConfigurationType
- **Type**: typing.Optional[typing.Literal['CENTRAL', 'LOCAL']]

### Status
- **Type**: typing.Optional[typing.Literal['ENABLED', 'FAILED', 'PENDING']]

### StatusMessage
- **Type**: typing.Optional[str]


# PageTypeDef

### PageNumber
- **Type**: typing.Optional[int]

### LineRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RangeTypeDef]

### OffsetRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RangeTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterConfigurationOutputTypeDef

### ValueType
- **Type**: typing.Literal['CUSTOM', 'DEFAULT']
- **Required**: Yes

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ParameterValueOutputTypeDef]


# ParameterConfigurationTypeDef

### ValueType
- **Type**: typing.Literal['CUSTOM', 'DEFAULT']
- **Required**: Yes

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ParameterValueTypeDef]


# ParameterDefinitionTypeDef

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ConfigurationOptionsTypeDef'>
- **Required**: Yes


# ParameterValueOutputTypeDef

### Integer
- **Type**: typing.Optional[int]

### IntegerList
- **Type**: typing.Optional[typing.List[int]]

### Double
- **Type**: typing.Optional[float]

### String
- **Type**: typing.Optional[str]

### StringList
- **Type**: typing.Optional[typing.List[str]]

### Boolean
- **Type**: typing.Optional[bool]

### Enum
- **Type**: typing.Optional[str]

### EnumList
- **Type**: typing.Optional[typing.List[str]]


# ParameterValueTypeDef

### Integer
- **Type**: typing.Optional[int]

### IntegerList
- **Type**: typing.Optional[typing.Sequence[int]]

### Double
- **Type**: typing.Optional[float]

### String
- **Type**: typing.Optional[str]

### StringList
- **Type**: typing.Optional[typing.Sequence[str]]

### Boolean
- **Type**: typing.Optional[bool]

### Enum
- **Type**: typing.Optional[str]

### EnumList
- **Type**: typing.Optional[typing.Sequence[str]]


# PatchSummaryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InstalledCount
- **Type**: typing.Optional[int]

### MissingCount
- **Type**: typing.Optional[int]

### FailedCount
- **Type**: typing.Optional[int]

### InstalledOtherCount
- **Type**: typing.Optional[int]

### InstalledRejectedCount
- **Type**: typing.Optional[int]

### InstalledPendingReboot
- **Type**: typing.Optional[int]

### OperationStartTime
- **Type**: typing.Optional[str]

### OperationEndTime
- **Type**: typing.Optional[str]

### RebootOption
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]


# PolicyOutputTypeDef

### SecurityHub
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SecurityHubPolicyOutputTypeDef]


# PolicyTypeDef

### SecurityHub
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SecurityHubPolicyTypeDef]


# PortProbeActionExtraOutputTypeDef

### PortProbeDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.PortProbeDetailTypeDef]]

### Blocked
- **Type**: typing.Optional[bool]


# PortProbeActionOutputTypeDef

### PortProbeDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.PortProbeDetailTypeDef]]

### Blocked
- **Type**: typing.Optional[bool]


# PortProbeActionTypeDef

### PortProbeDetails
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.PortProbeDetailTypeDef]]

### Blocked
- **Type**: typing.Optional[bool]


# PortProbeDetailTypeDef

### LocalPortDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionLocalPortDetailsTypeDef]

### LocalIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionLocalIpDetailsTypeDef]

### RemoteIpDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ActionRemoteIpDetailsTypeDef]


# PortRangeFromToTypeDef

### From
- **Type**: typing.Optional[int]

### To
- **Type**: typing.Optional[int]


# PortRangeTypeDef

### Begin
- **Type**: typing.Optional[int]

### End
- **Type**: typing.Optional[int]


# ProcessDetailsTypeDef

### Name
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Pid
- **Type**: typing.Optional[int]

### ParentPid
- **Type**: typing.Optional[int]

### LaunchedAt
- **Type**: typing.Optional[str]

### TerminatedAt
- **Type**: typing.Optional[str]


# ProductTypeDef

### ProductArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProductName
- **Type**: typing.Optional[str]

### CompanyName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Categories
- **Type**: typing.Optional[typing.List[str]]

### IntegrationTypes
- **Type**: typing.Optional[typing.List[typing.Literal['RECEIVE_FINDINGS_FROM_SECURITY_HUB', 'SEND_FINDINGS_TO_SECURITY_HUB', 'UPDATE_FINDINGS_IN_SECURITY_HUB']]]

### MarketplaceUrl
- **Type**: typing.Optional[str]

### ActivationUrl
- **Type**: typing.Optional[str]

### ProductSubscriptionResourcePolicy
- **Type**: typing.Optional[str]


# PropagatingVgwSetDetailsTypeDef

### GatewayId
- **Type**: typing.Optional[str]


# RangeTypeDef

### Start
- **Type**: typing.Optional[int]

### End
- **Type**: typing.Optional[int]

### StartColumn
- **Type**: typing.Optional[int]


# RecommendationTypeDef

### Text
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# RecordTypeDef

### JsonPath
- **Type**: typing.Optional[str]

### RecordIndex
- **Type**: typing.Optional[int]


# RelatedFindingTypeDef

### ProductArn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# RemediationTypeDef

### Recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RecommendationTypeDef]


# ResourceDetailsExtraOutputTypeDef

### AwsAutoScalingAutoScalingGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupDetailsExtraOutputTypeDef]

### AwsCodeBuildProject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectDetailsExtraOutputTypeDef]

### AwsCloudFrontDistribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionDetailsExtraOutputTypeDef]

### AwsEc2Instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2InstanceDetailsExtraOutputTypeDef]

### AwsEc2NetworkInterface
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceDetailsExtraOutputTypeDef]

### AwsEc2SecurityGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupDetailsExtraOutputTypeDef]

### AwsEc2Volume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VolumeDetailsExtraOutputTypeDef]

### AwsEc2Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcDetailsExtraOutputTypeDef]

### AwsEc2Eip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2EipDetailsTypeDef]

### AwsEc2Subnet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SubnetDetailsExtraOutputTypeDef]

### AwsEc2NetworkAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkAclDetailsExtraOutputTypeDef]

### AwsElbv2LoadBalancer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbv2LoadBalancerDetailsExtraOutputTypeDef]

### AwsElasticBeanstalkEnvironment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentDetailsExtraOutputTypeDef]

### AwsElasticsearchDomain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainDetailsExtraOutputTypeDef]

### AwsS3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketDetailsExtraOutputTypeDef]

### AwsS3AccountPublicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccountPublicAccessBlockDetailsTypeDef]

### AwsS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3ObjectDetailsTypeDef]

### AwsSecretsManagerSecret
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecretsManagerSecretDetailsTypeDef]

### AwsIamAccessKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAccessKeyDetailsTypeDef]

### AwsIamUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamUserDetailsExtraOutputTypeDef]

### AwsIamPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPolicyDetailsExtraOutputTypeDef]

### AwsApiGatewayV2Stage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2StageDetailsExtraOutputTypeDef]

### AwsApiGatewayV2Api
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2ApiDetailsExtraOutputTypeDef]

### AwsDynamoDbTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableDetailsExtraOutputTypeDef]

### AwsApiGatewayStage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayStageDetailsExtraOutputTypeDef]

### AwsApiGatewayRestApi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayRestApiDetailsExtraOutputTypeDef]

### AwsCloudTrailTrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudTrailTrailDetailsTypeDef]

### AwsSsmPatchCompliance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSsmPatchComplianceDetailsTypeDef]

### AwsCertificateManagerCertificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateDetailsExtraOutputTypeDef]

### AwsRedshiftCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterDetailsExtraOutputTypeDef]

### AwsElbLoadBalancer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerDetailsExtraOutputTypeDef]

### AwsIamGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamGroupDetailsExtraOutputTypeDef]

### AwsIamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamRoleDetailsExtraOutputTypeDef]

### AwsKmsKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsKmsKeyDetailsTypeDef]

### AwsLambdaFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionDetailsExtraOutputTypeDef]

### AwsLambdaLayerVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaLayerVersionDetailsExtraOutputTypeDef]

### AwsRdsDbInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceDetailsExtraOutputTypeDef]

### AwsSnsTopic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSnsTopicDetailsExtraOutputTypeDef]

### AwsSqsQueue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSqsQueueDetailsTypeDef]

### AwsWafWebAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafWebAclDetailsExtraOutputTypeDef]

### AwsRdsDbSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSnapshotDetailsExtraOutputTypeDef]

### AwsRdsDbClusterSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterSnapshotDetailsExtraOutputTypeDef]

### AwsRdsDbCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterDetailsExtraOutputTypeDef]

### AwsEcsCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterDetailsExtraOutputTypeDef]

### AwsEcsContainer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsContainerDetailsExtraOutputTypeDef]

### AwsEcsTaskDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionDetailsExtraOutputTypeDef]

### Container
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ContainerDetailsExtraOutputTypeDef]

### Other
- **Type**: typing.Optional[typing.Dict[str, str]]

### AwsRdsEventSubscription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsEventSubscriptionDetailsExtraOutputTypeDef]

### AwsEcsService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceDetailsExtraOutputTypeDef]

### AwsAutoScalingLaunchConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationDetailsExtraOutputTypeDef]

### AwsEc2VpnConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionDetailsExtraOutputTypeDef]

### AwsEcrContainerImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcrContainerImageDetailsExtraOutputTypeDef]

### AwsOpenSearchServiceDomain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainDetailsExtraOutputTypeDef]

### AwsEc2VpcEndpointService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcEndpointServiceDetailsExtraOutputTypeDef]

### AwsXrayEncryptionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsXrayEncryptionConfigDetailsTypeDef]

### AwsWafRateBasedRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRateBasedRuleDetailsExtraOutputTypeDef]

### AwsWafRegionalRateBasedRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRateBasedRuleDetailsExtraOutputTypeDef]

### AwsEcrRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcrRepositoryDetailsTypeDef]

### AwsEksCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterDetailsExtraOutputTypeDef]

### AwsNetworkFirewallFirewallPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsNetworkFirewallFirewallPolicyDetailsExtraOutputTypeDef]

### AwsNetworkFirewallFirewall
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsNetworkFirewallFirewallDetailsExtraOutputTypeDef]

### AwsNetworkFirewallRuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsNetworkFirewallRuleGroupDetailsExtraOutputTypeDef]

### AwsRdsDbSecurityGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSecurityGroupDetailsExtraOutputTypeDef]

### AwsKinesisStream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsKinesisStreamDetailsTypeDef]

### AwsEc2TransitGateway
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2TransitGatewayDetailsExtraOutputTypeDef]

### AwsEfsAccessPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointDetailsExtraOutputTypeDef]

### AwsCloudFormationStack
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFormationStackDetailsExtraOutputTypeDef]

### AwsCloudWatchAlarm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudWatchAlarmDetailsExtraOutputTypeDef]

### AwsEc2VpcPeeringConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionDetailsExtraOutputTypeDef]

### AwsWafRegionalRuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRuleGroupDetailsExtraOutputTypeDef]

### AwsWafRegionalRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRuleDetailsExtraOutputTypeDef]

### AwsWafRegionalWebAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalWebAclDetailsExtraOutputTypeDef]

### AwsWafRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRuleDetailsExtraOutputTypeDef]

### AwsWafRuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRuleGroupDetailsExtraOutputTypeDef]

### AwsEcsTask
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDetailsExtraOutputTypeDef]

### AwsBackupBackupVault
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupVaultDetailsExtraOutputTypeDef]

### AwsBackupBackupPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanDetailsExtraOutputTypeDef]

### AwsBackupRecoveryPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupRecoveryPointDetailsTypeDef]

### AwsEc2LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDetailsExtraOutputTypeDef]

### AwsSageMakerNotebookInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSageMakerNotebookInstanceDetailsExtraOutputTypeDef]

### AwsWafv2WebAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclDetailsExtraOutputTypeDef]

### AwsWafv2RuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RuleGroupDetailsExtraOutputTypeDef]

### AwsEc2RouteTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2RouteTableDetailsExtraOutputTypeDef]

### AwsAmazonMqBroker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerDetailsExtraOutputTypeDef]

### AwsAppSyncGraphQlApi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiDetailsExtraOutputTypeDef]

### AwsEventSchemasRegistry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventSchemasRegistryDetailsTypeDef]

### AwsGuardDutyDetector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDetailsExtraOutputTypeDef]

### AwsStepFunctionStateMachine
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineDetailsExtraOutputTypeDef]

### AwsAthenaWorkGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAthenaWorkGroupDetailsTypeDef]

### AwsEventsEventbus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEventbusDetailsTypeDef]

### AwsDmsEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsEndpointDetailsTypeDef]

### AwsEventsEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointDetailsExtraOutputTypeDef]

### AwsDmsReplicationTask
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationTaskDetailsTypeDef]

### AwsDmsReplicationInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationInstanceDetailsExtraOutputTypeDef]

### AwsRoute53HostedZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneDetailsExtraOutputTypeDef]

### AwsMskCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterDetailsExtraOutputTypeDef]

### AwsS3AccessPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccessPointDetailsTypeDef]

### AwsEc2ClientVpnEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointDetailsExtraOutputTypeDef]


# ResourceDetailsOutputTypeDef

### AwsAutoScalingAutoScalingGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef]

### AwsCodeBuildProject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectDetailsOutputTypeDef]

### AwsCloudFrontDistribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionDetailsOutputTypeDef]

### AwsEc2Instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2InstanceDetailsOutputTypeDef]

### AwsEc2NetworkInterface
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceDetailsOutputTypeDef]

### AwsEc2SecurityGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupDetailsOutputTypeDef]

### AwsEc2Volume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VolumeDetailsOutputTypeDef]

### AwsEc2Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcDetailsOutputTypeDef]

### AwsEc2Eip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2EipDetailsTypeDef]

### AwsEc2Subnet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SubnetDetailsOutputTypeDef]

### AwsEc2NetworkAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkAclDetailsOutputTypeDef]

### AwsElbv2LoadBalancer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbv2LoadBalancerDetailsOutputTypeDef]

### AwsElasticBeanstalkEnvironment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef]

### AwsElasticsearchDomain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainDetailsOutputTypeDef]

### AwsS3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketDetailsOutputTypeDef]

### AwsS3AccountPublicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccountPublicAccessBlockDetailsTypeDef]

### AwsS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3ObjectDetailsTypeDef]

### AwsSecretsManagerSecret
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecretsManagerSecretDetailsTypeDef]

### AwsIamAccessKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAccessKeyDetailsTypeDef]

### AwsIamUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamUserDetailsOutputTypeDef]

### AwsIamPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPolicyDetailsOutputTypeDef]

### AwsApiGatewayV2Stage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2StageDetailsOutputTypeDef]

### AwsApiGatewayV2Api
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2ApiDetailsOutputTypeDef]

### AwsDynamoDbTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableDetailsOutputTypeDef]

### AwsApiGatewayStage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayStageDetailsOutputTypeDef]

### AwsApiGatewayRestApi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayRestApiDetailsOutputTypeDef]

### AwsCloudTrailTrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudTrailTrailDetailsTypeDef]

### AwsSsmPatchCompliance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSsmPatchComplianceDetailsTypeDef]

### AwsCertificateManagerCertificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateDetailsOutputTypeDef]

### AwsRedshiftCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterDetailsOutputTypeDef]

### AwsElbLoadBalancer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerDetailsOutputTypeDef]

### AwsIamGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamGroupDetailsOutputTypeDef]

### AwsIamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamRoleDetailsOutputTypeDef]

### AwsKmsKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsKmsKeyDetailsTypeDef]

### AwsLambdaFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionDetailsOutputTypeDef]

### AwsLambdaLayerVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaLayerVersionDetailsOutputTypeDef]

### AwsRdsDbInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceDetailsOutputTypeDef]

### AwsSnsTopic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSnsTopicDetailsOutputTypeDef]

### AwsSqsQueue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSqsQueueDetailsTypeDef]

### AwsWafWebAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafWebAclDetailsOutputTypeDef]

### AwsRdsDbSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSnapshotDetailsOutputTypeDef]

### AwsRdsDbClusterSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterSnapshotDetailsOutputTypeDef]

### AwsRdsDbCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterDetailsOutputTypeDef]

### AwsEcsCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterDetailsOutputTypeDef]

### AwsEcsContainer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsContainerDetailsOutputTypeDef]

### AwsEcsTaskDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionDetailsOutputTypeDef]

### Container
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ContainerDetailsOutputTypeDef]

### Other
- **Type**: typing.Optional[typing.Dict[str, str]]

### AwsRdsEventSubscription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsEventSubscriptionDetailsOutputTypeDef]

### AwsEcsService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceDetailsOutputTypeDef]

### AwsAutoScalingLaunchConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef]

### AwsEc2VpnConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionDetailsOutputTypeDef]

### AwsEcrContainerImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcrContainerImageDetailsOutputTypeDef]

### AwsOpenSearchServiceDomain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainDetailsOutputTypeDef]

### AwsEc2VpcEndpointService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcEndpointServiceDetailsOutputTypeDef]

### AwsXrayEncryptionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsXrayEncryptionConfigDetailsTypeDef]

### AwsWafRateBasedRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRateBasedRuleDetailsOutputTypeDef]

### AwsWafRegionalRateBasedRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRateBasedRuleDetailsOutputTypeDef]

### AwsEcrRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcrRepositoryDetailsTypeDef]

### AwsEksCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterDetailsOutputTypeDef]

### AwsNetworkFirewallFirewallPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef]

### AwsNetworkFirewallFirewall
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsNetworkFirewallFirewallDetailsOutputTypeDef]

### AwsNetworkFirewallRuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsNetworkFirewallRuleGroupDetailsOutputTypeDef]

### AwsRdsDbSecurityGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSecurityGroupDetailsOutputTypeDef]

### AwsKinesisStream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsKinesisStreamDetailsTypeDef]

### AwsEc2TransitGateway
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2TransitGatewayDetailsOutputTypeDef]

### AwsEfsAccessPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointDetailsOutputTypeDef]

### AwsCloudFormationStack
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFormationStackDetailsOutputTypeDef]

### AwsCloudWatchAlarm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudWatchAlarmDetailsOutputTypeDef]

### AwsEc2VpcPeeringConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionDetailsOutputTypeDef]

### AwsWafRegionalRuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRuleGroupDetailsOutputTypeDef]

### AwsWafRegionalRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRuleDetailsOutputTypeDef]

### AwsWafRegionalWebAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalWebAclDetailsOutputTypeDef]

### AwsWafRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRuleDetailsOutputTypeDef]

### AwsWafRuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRuleGroupDetailsOutputTypeDef]

### AwsEcsTask
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDetailsOutputTypeDef]

### AwsBackupBackupVault
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupVaultDetailsOutputTypeDef]

### AwsBackupBackupPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanDetailsOutputTypeDef]

### AwsBackupRecoveryPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupRecoveryPointDetailsTypeDef]

### AwsEc2LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDetailsOutputTypeDef]

### AwsSageMakerNotebookInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSageMakerNotebookInstanceDetailsOutputTypeDef]

### AwsWafv2WebAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclDetailsOutputTypeDef]

### AwsWafv2RuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RuleGroupDetailsOutputTypeDef]

### AwsEc2RouteTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2RouteTableDetailsOutputTypeDef]

### AwsAmazonMqBroker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerDetailsOutputTypeDef]

### AwsAppSyncGraphQlApi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiDetailsOutputTypeDef]

### AwsEventSchemasRegistry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventSchemasRegistryDetailsTypeDef]

### AwsGuardDutyDetector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDetailsOutputTypeDef]

### AwsStepFunctionStateMachine
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineDetailsOutputTypeDef]

### AwsAthenaWorkGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAthenaWorkGroupDetailsTypeDef]

### AwsEventsEventbus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEventbusDetailsTypeDef]

### AwsDmsEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsEndpointDetailsTypeDef]

### AwsEventsEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointDetailsOutputTypeDef]

### AwsDmsReplicationTask
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationTaskDetailsTypeDef]

### AwsDmsReplicationInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationInstanceDetailsOutputTypeDef]

### AwsRoute53HostedZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneDetailsOutputTypeDef]

### AwsMskCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterDetailsOutputTypeDef]

### AwsS3AccessPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccessPointDetailsTypeDef]

### AwsEc2ClientVpnEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointDetailsOutputTypeDef]


# ResourceDetailsTypeDef

### AwsAutoScalingAutoScalingGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingAutoScalingGroupDetailsTypeDef]

### AwsCodeBuildProject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCodeBuildProjectDetailsTypeDef]

### AwsCloudFrontDistribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFrontDistributionDetailsTypeDef]

### AwsEc2Instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2InstanceDetailsTypeDef]

### AwsEc2NetworkInterface
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkInterfaceDetailsTypeDef]

### AwsEc2SecurityGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SecurityGroupDetailsTypeDef]

### AwsEc2Volume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VolumeDetailsTypeDef]

### AwsEc2Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcDetailsTypeDef]

### AwsEc2Eip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2EipDetailsTypeDef]

### AwsEc2Subnet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2SubnetDetailsTypeDef]

### AwsEc2NetworkAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2NetworkAclDetailsTypeDef]

### AwsElbv2LoadBalancer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbv2LoadBalancerDetailsTypeDef]

### AwsElasticBeanstalkEnvironment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticBeanstalkEnvironmentDetailsTypeDef]

### AwsElasticsearchDomain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElasticsearchDomainDetailsTypeDef]

### AwsS3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3BucketDetailsTypeDef]

### AwsS3AccountPublicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccountPublicAccessBlockDetailsTypeDef]

### AwsS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3ObjectDetailsTypeDef]

### AwsSecretsManagerSecret
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecretsManagerSecretDetailsTypeDef]

### AwsIamAccessKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamAccessKeyDetailsTypeDef]

### AwsIamUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamUserDetailsTypeDef]

### AwsIamPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamPolicyDetailsTypeDef]

### AwsApiGatewayV2Stage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2StageDetailsTypeDef]

### AwsApiGatewayV2Api
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayV2ApiDetailsTypeDef]

### AwsDynamoDbTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDynamoDbTableDetailsTypeDef]

### AwsApiGatewayStage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayStageDetailsTypeDef]

### AwsApiGatewayRestApi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsApiGatewayRestApiDetailsTypeDef]

### AwsCloudTrailTrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudTrailTrailDetailsTypeDef]

### AwsSsmPatchCompliance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSsmPatchComplianceDetailsTypeDef]

### AwsCertificateManagerCertificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCertificateManagerCertificateDetailsTypeDef]

### AwsRedshiftCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRedshiftClusterDetailsTypeDef]

### AwsElbLoadBalancer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsElbLoadBalancerDetailsTypeDef]

### AwsIamGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamGroupDetailsTypeDef]

### AwsIamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsIamRoleDetailsTypeDef]

### AwsKmsKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsKmsKeyDetailsTypeDef]

### AwsLambdaFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaFunctionDetailsTypeDef]

### AwsLambdaLayerVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsLambdaLayerVersionDetailsTypeDef]

### AwsRdsDbInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbInstanceDetailsTypeDef]

### AwsSnsTopic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSnsTopicDetailsTypeDef]

### AwsSqsQueue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSqsQueueDetailsTypeDef]

### AwsWafWebAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafWebAclDetailsTypeDef]

### AwsRdsDbSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSnapshotDetailsTypeDef]

### AwsRdsDbClusterSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterSnapshotDetailsTypeDef]

### AwsRdsDbCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbClusterDetailsTypeDef]

### AwsEcsCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsClusterDetailsTypeDef]

### AwsEcsContainer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsContainerDetailsTypeDef]

### AwsEcsTaskDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDefinitionDetailsTypeDef]

### Container
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ContainerDetailsTypeDef]

### Other
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AwsRdsEventSubscription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsEventSubscriptionDetailsTypeDef]

### AwsEcsService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsServiceDetailsTypeDef]

### AwsAutoScalingLaunchConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAutoScalingLaunchConfigurationDetailsTypeDef]

### AwsEc2VpnConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpnConnectionDetailsTypeDef]

### AwsEcrContainerImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcrContainerImageDetailsTypeDef]

### AwsOpenSearchServiceDomain
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsOpenSearchServiceDomainDetailsTypeDef]

### AwsEc2VpcEndpointService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcEndpointServiceDetailsTypeDef]

### AwsXrayEncryptionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsXrayEncryptionConfigDetailsTypeDef]

### AwsWafRateBasedRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRateBasedRuleDetailsTypeDef]

### AwsWafRegionalRateBasedRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRateBasedRuleDetailsTypeDef]

### AwsEcrRepository
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcrRepositoryDetailsTypeDef]

### AwsEksCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEksClusterDetailsTypeDef]

### AwsNetworkFirewallFirewallPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsNetworkFirewallFirewallPolicyDetailsTypeDef]

### AwsNetworkFirewallFirewall
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsNetworkFirewallFirewallDetailsTypeDef]

### AwsNetworkFirewallRuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsNetworkFirewallRuleGroupDetailsTypeDef]

### AwsRdsDbSecurityGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRdsDbSecurityGroupDetailsTypeDef]

### AwsKinesisStream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsKinesisStreamDetailsTypeDef]

### AwsEc2TransitGateway
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2TransitGatewayDetailsTypeDef]

### AwsEfsAccessPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEfsAccessPointDetailsTypeDef]

### AwsCloudFormationStack
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudFormationStackDetailsTypeDef]

### AwsCloudWatchAlarm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsCloudWatchAlarmDetailsTypeDef]

### AwsEc2VpcPeeringConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2VpcPeeringConnectionDetailsTypeDef]

### AwsWafRegionalRuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRuleGroupDetailsTypeDef]

### AwsWafRegionalRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalRuleDetailsTypeDef]

### AwsWafRegionalWebAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRegionalWebAclDetailsTypeDef]

### AwsWafRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRuleDetailsTypeDef]

### AwsWafRuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafRuleGroupDetailsTypeDef]

### AwsEcsTask
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEcsTaskDetailsTypeDef]

### AwsBackupBackupVault
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupVaultDetailsTypeDef]

### AwsBackupBackupPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupBackupPlanDetailsTypeDef]

### AwsBackupRecoveryPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsBackupRecoveryPointDetailsTypeDef]

### AwsEc2LaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2LaunchTemplateDetailsTypeDef]

### AwsSageMakerNotebookInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSageMakerNotebookInstanceDetailsTypeDef]

### AwsWafv2WebAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2WebAclDetailsTypeDef]

### AwsWafv2RuleGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsWafv2RuleGroupDetailsTypeDef]

### AwsEc2RouteTable
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2RouteTableDetailsTypeDef]

### AwsAmazonMqBroker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAmazonMqBrokerDetailsTypeDef]

### AwsAppSyncGraphQlApi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAppSyncGraphQlApiDetailsTypeDef]

### AwsEventSchemasRegistry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventSchemasRegistryDetailsTypeDef]

### AwsGuardDutyDetector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsGuardDutyDetectorDetailsTypeDef]

### AwsStepFunctionStateMachine
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsStepFunctionStateMachineDetailsTypeDef]

### AwsAthenaWorkGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsAthenaWorkGroupDetailsTypeDef]

### AwsEventsEventbus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEventbusDetailsTypeDef]

### AwsDmsEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsEndpointDetailsTypeDef]

### AwsEventsEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEventsEndpointDetailsTypeDef]

### AwsDmsReplicationTask
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationTaskDetailsTypeDef]

### AwsDmsReplicationInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsDmsReplicationInstanceDetailsTypeDef]

### AwsRoute53HostedZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsRoute53HostedZoneDetailsTypeDef]

### AwsMskCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsMskClusterDetailsTypeDef]

### AwsS3AccessPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsS3AccessPointDetailsTypeDef]

### AwsEc2ClientVpnEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsEc2ClientVpnEndpointDetailsTypeDef]


# ResourceExtraOutputTypeDef

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Partition
- **Type**: typing.Optional[typing.Literal['aws', 'aws-cn', 'aws-us-gov']]

### Region
- **Type**: typing.Optional[str]

### ResourceRole
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### DataClassification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.DataClassificationDetailsExtraOutputTypeDef]

### Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ResourceDetailsExtraOutputTypeDef]

### ApplicationName
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]


# ResourceOutputTypeDef

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Partition
- **Type**: typing.Optional[typing.Literal['aws', 'aws-cn', 'aws-us-gov']]

### Region
- **Type**: typing.Optional[str]

### ResourceRole
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### DataClassification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.DataClassificationDetailsOutputTypeDef]

### Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ResourceDetailsOutputTypeDef]

### ApplicationName
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]


# ResourceTypeDef

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Partition
- **Type**: typing.Optional[typing.Literal['aws', 'aws-cn', 'aws-us-gov']]

### Region
- **Type**: typing.Optional[str]

### ResourceRole
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DataClassification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.DataClassificationDetailsTypeDef]

### Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ResourceDetailsTypeDef]

### ApplicationName
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# ResultTypeDef

### AccountId
- **Type**: typing.Optional[str]

### ProcessingResult
- **Type**: typing.Optional[str]


# RouteSetDetailsTypeDef

### CarrierGatewayId
- **Type**: typing.Optional[str]

### CoreNetworkArn
- **Type**: typing.Optional[str]

### DestinationCidrBlock
- **Type**: typing.Optional[str]

### DestinationIpv6CidrBlock
- **Type**: typing.Optional[str]

### DestinationPrefixListId
- **Type**: typing.Optional[str]

### EgressOnlyInternetGatewayId
- **Type**: typing.Optional[str]

### GatewayId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceOwnerId
- **Type**: typing.Optional[str]

### LocalGatewayId
- **Type**: typing.Optional[str]

### NatGatewayId
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### Origin
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### TransitGatewayId
- **Type**: typing.Optional[str]

### VpcPeeringConnectionId
- **Type**: typing.Optional[str]


# RuleGroupDetailsExtraOutputTypeDef

### RuleVariables
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesExtraOutputTypeDef]

### RulesSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceExtraOutputTypeDef]


# RuleGroupDetailsOutputTypeDef

### RuleVariables
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesOutputTypeDef]

### RulesSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceOutputTypeDef]


# RuleGroupDetailsTypeDef

### RuleVariables
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesTypeDef]

### RulesSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceTypeDef]


# RuleGroupSourceCustomActionsDetailsExtraOutputTypeDef

### ActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomActionDefinitionExtraOutputTypeDef]

### ActionName
- **Type**: typing.Optional[str]


# RuleGroupSourceCustomActionsDetailsOutputTypeDef

### ActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomActionDefinitionOutputTypeDef]

### ActionName
- **Type**: typing.Optional[str]


# RuleGroupSourceCustomActionsDetailsTypeDef

### ActionDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomActionDefinitionTypeDef]

### ActionName
- **Type**: typing.Optional[str]


# RuleGroupSourceExtraOutputTypeDef

### RulesSourceList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceListDetailsExtraOutputTypeDef]

### RulesString
- **Type**: typing.Optional[str]

### StatefulRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesDetailsExtraOutputTypeDef]]

### StatelessRulesAndCustomActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRulesAndCustomActionsDetailsExtraOutputTypeDef]


# RuleGroupSourceListDetailsExtraOutputTypeDef

### GeneratedRulesType
- **Type**: typing.Optional[str]

### TargetTypes
- **Type**: typing.Optional[typing.List[str]]

### Targets
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupSourceListDetailsOutputTypeDef

### GeneratedRulesType
- **Type**: typing.Optional[str]

### TargetTypes
- **Type**: typing.Optional[typing.List[str]]

### Targets
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupSourceListDetailsTypeDef

### GeneratedRulesType
- **Type**: typing.Optional[str]

### TargetTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### Targets
- **Type**: typing.Optional[typing.Sequence[str]]


# RuleGroupSourceOutputTypeDef

### RulesSourceList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceListDetailsOutputTypeDef]

### RulesString
- **Type**: typing.Optional[str]

### StatefulRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesDetailsOutputTypeDef]]

### StatelessRulesAndCustomActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef]


# RuleGroupSourceStatefulRulesDetailsExtraOutputTypeDef

### Action
- **Type**: typing.Optional[str]

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesHeaderDetailsTypeDef]

### RuleOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesOptionsDetailsExtraOutputTypeDef]]


# RuleGroupSourceStatefulRulesDetailsOutputTypeDef

### Action
- **Type**: typing.Optional[str]

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesHeaderDetailsTypeDef]

### RuleOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef]]


# RuleGroupSourceStatefulRulesDetailsTypeDef

### Action
- **Type**: typing.Optional[str]

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesHeaderDetailsTypeDef]

### RuleOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesOptionsDetailsTypeDef]]


# RuleGroupSourceStatefulRulesHeaderDetailsTypeDef

### Destination
- **Type**: typing.Optional[str]

### DestinationPort
- **Type**: typing.Optional[str]

### Direction
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### SourcePort
- **Type**: typing.Optional[str]


# RuleGroupSourceStatefulRulesOptionsDetailsExtraOutputTypeDef

### Keyword
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef

### Keyword
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupSourceStatefulRulesOptionsDetailsTypeDef

### Keyword
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[typing.Sequence[str]]


# RuleGroupSourceStatelessRuleDefinitionExtraOutputTypeDef

### Actions
- **Type**: typing.Optional[typing.List[str]]

### MatchAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesExtraOutputTypeDef]


# RuleGroupSourceStatelessRuleDefinitionOutputTypeDef

### Actions
- **Type**: typing.Optional[typing.List[str]]

### MatchAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef]


# RuleGroupSourceStatelessRuleDefinitionTypeDef

### Actions
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesTypeDef]


# RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef

### FromPort
- **Type**: typing.Optional[int]

### ToPort
- **Type**: typing.Optional[int]


# RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef

### AddressDefinition
- **Type**: typing.Optional[str]


# RuleGroupSourceStatelessRuleMatchAttributesExtraOutputTypeDef

### DestinationPorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]]

### Protocols
- **Type**: typing.Optional[typing.List[int]]

### SourcePorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]]

### TcpFlags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsExtraOutputTypeDef]]


# RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef

### DestinationPorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]]

### Destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]]

### Protocols
- **Type**: typing.Optional[typing.List[int]]

### SourcePorts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]]

### TcpFlags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef]]


# RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef

### FromPort
- **Type**: typing.Optional[int]

### ToPort
- **Type**: typing.Optional[int]


# RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef

### AddressDefinition
- **Type**: typing.Optional[str]


# RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsExtraOutputTypeDef

### Flags
- **Type**: typing.Optional[typing.List[str]]

### Masks
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef

### Flags
- **Type**: typing.Optional[typing.List[str]]

### Masks
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef

### Flags
- **Type**: typing.Optional[typing.Sequence[str]]

### Masks
- **Type**: typing.Optional[typing.Sequence[str]]


# RuleGroupSourceStatelessRuleMatchAttributesTypeDef

### DestinationPorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]]

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]]

### Protocols
- **Type**: typing.Optional[typing.Sequence[int]]

### SourcePorts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]]

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]]

### TcpFlags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef]]


# RuleGroupSourceStatelessRulesAndCustomActionsDetailsExtraOutputTypeDef

### CustomActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceCustomActionsDetailsExtraOutputTypeDef]]

### StatelessRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRulesDetailsExtraOutputTypeDef]]


# RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef

### CustomActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceCustomActionsDetailsOutputTypeDef]]

### StatelessRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRulesDetailsOutputTypeDef]]


# RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef

### CustomActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceCustomActionsDetailsTypeDef]]

### StatelessRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRulesDetailsTypeDef]]


# RuleGroupSourceStatelessRulesDetailsExtraOutputTypeDef

### Priority
- **Type**: typing.Optional[int]

### RuleDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleDefinitionExtraOutputTypeDef]


# RuleGroupSourceStatelessRulesDetailsOutputTypeDef

### Priority
- **Type**: typing.Optional[int]

### RuleDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleDefinitionOutputTypeDef]


# RuleGroupSourceStatelessRulesDetailsTypeDef

### Priority
- **Type**: typing.Optional[int]

### RuleDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRuleDefinitionTypeDef]


# RuleGroupSourceTypeDef

### RulesSourceList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceListDetailsTypeDef]

### RulesString
- **Type**: typing.Optional[str]

### StatefulRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatefulRulesDetailsTypeDef]]

### StatelessRulesAndCustomActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef]


# RuleGroupVariablesExtraOutputTypeDef

### IpSets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesIpSetsDetailsExtraOutputTypeDef]

### PortSets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesPortSetsDetailsExtraOutputTypeDef]


# RuleGroupVariablesIpSetsDetailsExtraOutputTypeDef

### Definition
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupVariablesIpSetsDetailsOutputTypeDef

### Definition
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupVariablesIpSetsDetailsTypeDef

### Definition
- **Type**: typing.Optional[typing.Sequence[str]]


# RuleGroupVariablesOutputTypeDef

### IpSets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesIpSetsDetailsOutputTypeDef]

### PortSets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesPortSetsDetailsOutputTypeDef]


# RuleGroupVariablesPortSetsDetailsExtraOutputTypeDef

### Definition
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupVariablesPortSetsDetailsOutputTypeDef

### Definition
- **Type**: typing.Optional[typing.List[str]]


# RuleGroupVariablesPortSetsDetailsTypeDef

### Definition
- **Type**: typing.Optional[typing.Sequence[str]]


# RuleGroupVariablesTypeDef

### IpSets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesIpSetsDetailsTypeDef]

### PortSets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.RuleGroupVariablesPortSetsDetailsTypeDef]


# SecurityControlCustomParameterOutputTypeDef

### SecurityControlId
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.securityhub_classes.ParameterConfigurationOutputTypeDef]]


# SecurityControlCustomParameterTypeDef

### SecurityControlId
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.securityhub_classes.ParameterConfigurationTypeDef]]


# SecurityControlDefinitionTypeDef

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### RemediationUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SeverityRating
- **Type**: typing.Literal['CRITICAL', 'HIGH', 'LOW', 'MEDIUM']
- **Required**: Yes

### CurrentRegionAvailability
- **Type**: typing.Literal['AVAILABLE', 'UNAVAILABLE']
- **Required**: Yes

### CustomizableProperties
- **Type**: typing.Optional[typing.List[typing.Literal['Parameters']]]

### ParameterDefinitions
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.securityhub_classes.ParameterDefinitionTypeDef]]


# SecurityControlParameterExtraOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[typing.List[str]]


# SecurityControlParameterOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[typing.List[str]]


# SecurityControlParameterTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[typing.Sequence[str]]


# SecurityControlTypeDef

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### RemediationUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SeverityRating
- **Type**: typing.Literal['CRITICAL', 'HIGH', 'LOW', 'MEDIUM']
- **Required**: Yes

### SecurityControlStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Optional[typing.Literal['READY', 'UPDATING']]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.securityhub_classes.ParameterConfigurationOutputTypeDef]]

### LastUpdateReason
- **Type**: typing.Optional[str]


# SecurityControlsConfigurationOutputTypeDef

### EnabledSecurityControlIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### DisabledSecurityControlIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### SecurityControlCustomParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlCustomParameterOutputTypeDef]]


# SecurityControlsConfigurationTypeDef

### EnabledSecurityControlIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### DisabledSecurityControlIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityControlCustomParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlCustomParameterTypeDef]]


# SecurityHubPolicyOutputTypeDef

### ServiceEnabled
- **Type**: typing.Optional[bool]

### EnabledStandardIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### SecurityControlsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlsConfigurationOutputTypeDef]


# SecurityHubPolicyTypeDef

### ServiceEnabled
- **Type**: typing.Optional[bool]

### EnabledStandardIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityControlsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.SecurityControlsConfigurationTypeDef]


# SensitiveDataDetectionsExtraOutputTypeDef

### Count
- **Type**: typing.Optional[int]

### Type
- **Type**: typing.Optional[str]

### Occurrences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.OccurrencesExtraOutputTypeDef]


# SensitiveDataDetectionsOutputTypeDef

### Count
- **Type**: typing.Optional[int]

### Type
- **Type**: typing.Optional[str]

### Occurrences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.OccurrencesOutputTypeDef]


# SensitiveDataDetectionsTypeDef

### Count
- **Type**: typing.Optional[int]

### Type
- **Type**: typing.Optional[str]

### Occurrences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.OccurrencesTypeDef]


# SensitiveDataResultExtraOutputTypeDef

### Category
- **Type**: typing.Optional[str]

### Detections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SensitiveDataDetectionsExtraOutputTypeDef]]

### TotalCount
- **Type**: typing.Optional[int]


# SensitiveDataResultOutputTypeDef

### Category
- **Type**: typing.Optional[str]

### Detections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SensitiveDataDetectionsOutputTypeDef]]

### TotalCount
- **Type**: typing.Optional[int]


# SensitiveDataResultTypeDef

### Category
- **Type**: typing.Optional[str]

### Detections
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SensitiveDataDetectionsTypeDef]]

### TotalCount
- **Type**: typing.Optional[int]


# SeverityTypeDef

### Product
- **Type**: typing.Optional[float]

### Label
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM']]

### Normalized
- **Type**: typing.Optional[int]

### Original
- **Type**: typing.Optional[str]


# SeverityUpdateTypeDef

### Normalized
- **Type**: typing.Optional[int]

### Product
- **Type**: typing.Optional[float]

### Label
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM']]


# SoftwarePackageTypeDef

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Epoch
- **Type**: typing.Optional[str]

### Release
- **Type**: typing.Optional[str]

### Architecture
- **Type**: typing.Optional[str]

### PackageManager
- **Type**: typing.Optional[str]

### FilePath
- **Type**: typing.Optional[str]

### FixedInVersion
- **Type**: typing.Optional[str]

### Remediation
- **Type**: typing.Optional[str]

### SourceLayerHash
- **Type**: typing.Optional[str]

### SourceLayerArn
- **Type**: typing.Optional[str]


# SortCriterionTypeDef

### Field
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['asc', 'desc']]


# StandardTypeDef

### StandardsArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EnabledByDefault
- **Type**: typing.Optional[bool]

### StandardsManagedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StandardsManagedByTypeDef]


# StandardsControlAssociationDetailTypeDef

### StandardsArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### RelatedRequirements
- **Type**: typing.Optional[typing.List[str]]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedReason
- **Type**: typing.Optional[str]

### StandardsControlTitle
- **Type**: typing.Optional[str]

### StandardsControlDescription
- **Type**: typing.Optional[str]

### StandardsControlArns
- **Type**: typing.Optional[typing.List[str]]


# StandardsControlAssociationIdTypeDef

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### StandardsArn
- **Type**: <class 'str'>
- **Required**: Yes


# StandardsControlAssociationSummaryTypeDef

### StandardsArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### RelatedRequirements
- **Type**: typing.Optional[typing.List[str]]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedReason
- **Type**: typing.Optional[str]

### StandardsControlTitle
- **Type**: typing.Optional[str]

### StandardsControlDescription
- **Type**: typing.Optional[str]


# StandardsControlAssociationUpdateTypeDef

### StandardsArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### UpdatedReason
- **Type**: typing.Optional[str]


# StandardsControlTypeDef

### StandardsControlArn
- **Type**: typing.Optional[str]

### ControlStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DisabledReason
- **Type**: typing.Optional[str]

### ControlStatusUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### ControlId
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RemediationUrl
- **Type**: typing.Optional[str]

### SeverityRating
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'LOW', 'MEDIUM']]

### RelatedRequirements
- **Type**: typing.Optional[typing.List[str]]


# StandardsManagedByTypeDef

### Company
- **Type**: typing.Optional[str]

### Product
- **Type**: typing.Optional[str]


# StandardsStatusReasonTypeDef

### StatusReasonCode
- **Type**: typing.Literal['INTERNAL_ERROR', 'NO_AVAILABLE_CONFIGURATION_RECORDER']
- **Required**: Yes


# StandardsSubscriptionRequestTypeDef

### StandardsArn
- **Type**: <class 'str'>
- **Required**: Yes

### StandardsInput
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StandardsSubscriptionTypeDef

### StandardsSubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### StandardsArn
- **Type**: <class 'str'>
- **Required**: Yes

### StandardsInput
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### StandardsStatus
- **Type**: typing.Literal['DELETING', 'FAILED', 'INCOMPLETE', 'PENDING', 'READY']
- **Required**: Yes

### StandardsStatusReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StandardsStatusReasonTypeDef]


# StartConfigurationPolicyAssociationRequestRequestTypeDef

### ConfigurationPolicyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.TargetTypeDef'>
- **Required**: Yes


# StartConfigurationPolicyAssociationResponseTypeDef

### ConfigurationPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetType
- **Type**: typing.Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT', 'ROOT']
- **Required**: Yes

### AssociationType
- **Type**: typing.Literal['APPLIED', 'INHERITED']
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AssociationStatus
- **Type**: typing.Literal['FAILED', 'PENDING', 'SUCCESS']
- **Required**: Yes

### AssociationStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartConfigurationPolicyDisassociationRequestRequestTypeDef

### ConfigurationPolicyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.TargetTypeDef]


# StatelessCustomActionDefinitionExtraOutputTypeDef

### PublishMetricAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomPublishMetricActionExtraOutputTypeDef]


# StatelessCustomActionDefinitionOutputTypeDef

### PublishMetricAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomPublishMetricActionOutputTypeDef]


# StatelessCustomActionDefinitionTypeDef

### PublishMetricAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomPublishMetricActionTypeDef]


# StatelessCustomPublishMetricActionDimensionTypeDef

### Value
- **Type**: typing.Optional[str]


# StatelessCustomPublishMetricActionExtraOutputTypeDef

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomPublishMetricActionDimensionTypeDef]]


# StatelessCustomPublishMetricActionOutputTypeDef

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomPublishMetricActionDimensionTypeDef]]


# StatelessCustomPublishMetricActionTypeDef

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.StatelessCustomPublishMetricActionDimensionTypeDef]]


# StatusReasonTypeDef

### ReasonCode
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# StringConfigurationOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[str]

### Re2Expression
- **Type**: typing.Optional[str]

### ExpressionDescription
- **Type**: typing.Optional[str]


# StringFilterTypeDef

### Value
- **Type**: typing.Optional[str]

### Comparison
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQUALS', 'NOT_CONTAINS', 'NOT_EQUALS', 'PREFIX', 'PREFIX_NOT_EQUALS']]


# StringListConfigurationOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[typing.List[str]]

### Re2Expression
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### ExpressionDescription
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TargetTypeDef

### AccountId
- **Type**: typing.Optional[str]

### OrganizationalUnitId
- **Type**: typing.Optional[str]

### RootId
- **Type**: typing.Optional[str]


# ThreatExtraOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### FilePaths
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FilePathsTypeDef]]


# ThreatIntelIndicatorTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['DOMAIN', 'EMAIL_ADDRESS', 'HASH_MD5', 'HASH_SHA1', 'HASH_SHA256', 'HASH_SHA512', 'IPV4_ADDRESS', 'IPV6_ADDRESS', 'MUTEX', 'PROCESS', 'URL']]

### Value
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[typing.Literal['BACKDOOR', 'CARD_STEALER', 'COMMAND_AND_CONTROL', 'DROP_SITE', 'EXPLOIT_SITE', 'KEYLOGGER']]

### LastObservedAt
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### SourceUrl
- **Type**: typing.Optional[str]


# ThreatOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### FilePaths
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.FilePathsTypeDef]]


# ThreatTypeDef

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### ItemCount
- **Type**: typing.Optional[int]

### FilePaths
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.FilePathsTypeDef]]


# UnprocessedAutomationRuleTypeDef

### RuleArn
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[int]

### ErrorMessage
- **Type**: typing.Optional[str]


# UnprocessedConfigurationPolicyAssociationTypeDef

### ConfigurationPolicyAssociationIdentifiers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.ConfigurationPolicyAssociationTypeDef]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorReason
- **Type**: typing.Optional[str]


# UnprocessedSecurityControlTypeDef

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorCode
- **Type**: typing.Literal['ACCESS_DENIED', 'INVALID_INPUT', 'LIMIT_EXCEEDED', 'NOT_FOUND']
- **Required**: Yes

### ErrorReason
- **Type**: typing.Optional[str]


# UnprocessedStandardsControlAssociationTypeDef

### StandardsControlAssociationId
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.StandardsControlAssociationIdTypeDef'>
- **Required**: Yes

### ErrorCode
- **Type**: typing.Literal['ACCESS_DENIED', 'INVALID_INPUT', 'LIMIT_EXCEEDED', 'NOT_FOUND']
- **Required**: Yes

### ErrorReason
- **Type**: typing.Optional[str]


# UnprocessedStandardsControlAssociationUpdateTypeDef

### StandardsControlAssociationUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.StandardsControlAssociationUpdateTypeDef'>
- **Required**: Yes

### ErrorCode
- **Type**: typing.Literal['ACCESS_DENIED', 'INVALID_INPUT', 'LIMIT_EXCEEDED', 'NOT_FOUND']
- **Required**: Yes

### ErrorReason
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateActionTargetRequestRequestTypeDef

### ActionTargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateAutomationRulesRequestItemTypeDef

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### RuleStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RuleOrder
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### RuleName
- **Type**: typing.Optional[str]

### IsTerminal
- **Type**: typing.Optional[bool]

### Criteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesFindingFiltersTypeDef]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.AutomationRulesActionTypeDef]]


# UpdateConfigurationPolicyRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### UpdatedReason
- **Type**: typing.Optional[str]

### ConfigurationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.PolicyTypeDef]


# UpdateConfigurationPolicyResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ConfigurationPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.PolicyOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFindingAggregatorRequestRequestTypeDef

### FindingAggregatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### RegionLinkingMode
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateFindingAggregatorResponseTypeDef

### FindingAggregatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### FindingAggregationRegion
- **Type**: <class 'str'>
- **Required**: Yes

### RegionLinkingMode
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFindingsRequestRequestTypeDef

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingFiltersTypeDef'>
- **Required**: Yes

### Note
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.NoteUpdateTypeDef]

### RecordState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED']]


# UpdateInsightRequestRequestTypeDef

### InsightArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.AwsSecurityFindingFiltersTypeDef]

### GroupByAttribute
- **Type**: typing.Optional[str]


# UpdateOrganizationConfigurationRequestRequestTypeDef

### AutoEnable
- **Type**: <class 'bool'>
- **Required**: Yes

### AutoEnableStandards
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'NONE']]

### OrganizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.OrganizationConfigurationTypeDef]


# UpdateSecurityControlRequestRequestTypeDef

### SecurityControlId
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Mapping[str, typing.Union[aws_resource_validator.pydantic_models.securityhub_classes.ParameterConfigurationTypeDef, aws_resource_validator.pydantic_models.securityhub_classes.ParameterConfigurationOutputTypeDef]]
- **Required**: Yes

### LastUpdateReason
- **Type**: typing.Optional[str]


# UpdateSecurityHubConfigurationRequestRequestTypeDef

### AutoEnableControls
- **Type**: typing.Optional[bool]

### ControlFindingGenerator
- **Type**: typing.Optional[typing.Literal['SECURITY_CONTROL', 'STANDARD_CONTROL']]


# UpdateStandardsControlRequestRequestTypeDef

### StandardsControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### ControlStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DisabledReason
- **Type**: typing.Optional[str]


# VolumeMountTypeDef

### Name
- **Type**: typing.Optional[str]

### MountPath
- **Type**: typing.Optional[str]


# VpcInfoCidrBlockSetDetailsTypeDef

### CidrBlock
- **Type**: typing.Optional[str]


# VpcInfoIpv6CidrBlockSetDetailsTypeDef

### Ipv6CidrBlock
- **Type**: typing.Optional[str]


# VpcInfoPeeringOptionsDetailsTypeDef

### AllowDnsResolutionFromRemoteVpc
- **Type**: typing.Optional[bool]

### AllowEgressFromLocalClassicLinkToRemoteVpc
- **Type**: typing.Optional[bool]

### AllowEgressFromLocalVpcToRemoteClassicLink
- **Type**: typing.Optional[bool]


# VulnerabilityCodeVulnerabilitiesExtraOutputTypeDef

### Cwes
- **Type**: typing.Optional[typing.List[str]]

### FilePath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.CodeVulnerabilitiesFilePathTypeDef]

### SourceArn
- **Type**: typing.Optional[str]


# VulnerabilityCodeVulnerabilitiesOutputTypeDef

### Cwes
- **Type**: typing.Optional[typing.List[str]]

### FilePath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.CodeVulnerabilitiesFilePathTypeDef]

### SourceArn
- **Type**: typing.Optional[str]


# VulnerabilityCodeVulnerabilitiesTypeDef

### Cwes
- **Type**: typing.Optional[typing.Sequence[str]]

### FilePath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.CodeVulnerabilitiesFilePathTypeDef]

### SourceArn
- **Type**: typing.Optional[str]


# VulnerabilityExtraOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### VulnerablePackages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SoftwarePackageTypeDef]]

### Cvss
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.CvssExtraOutputTypeDef]]

### RelatedVulnerabilities
- **Type**: typing.Optional[typing.List[str]]

### Vendor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityVendorTypeDef]

### ReferenceUrls
- **Type**: typing.Optional[typing.List[str]]

### FixAvailable
- **Type**: typing.Optional[typing.Literal['NO', 'PARTIAL', 'YES']]

### EpssScore
- **Type**: typing.Optional[float]

### ExploitAvailable
- **Type**: typing.Optional[typing.Literal['NO', 'YES']]

### LastKnownExploitAt
- **Type**: typing.Optional[str]

### CodeVulnerabilities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityCodeVulnerabilitiesExtraOutputTypeDef]]


# VulnerabilityOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### VulnerablePackages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.SoftwarePackageTypeDef]]

### Cvss
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.CvssOutputTypeDef]]

### RelatedVulnerabilities
- **Type**: typing.Optional[typing.List[str]]

### Vendor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityVendorTypeDef]

### ReferenceUrls
- **Type**: typing.Optional[typing.List[str]]

### FixAvailable
- **Type**: typing.Optional[typing.Literal['NO', 'PARTIAL', 'YES']]

### EpssScore
- **Type**: typing.Optional[float]

### ExploitAvailable
- **Type**: typing.Optional[typing.Literal['NO', 'YES']]

### LastKnownExploitAt
- **Type**: typing.Optional[str]

### CodeVulnerabilities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityCodeVulnerabilitiesOutputTypeDef]]


# VulnerabilityTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### VulnerablePackages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.SoftwarePackageTypeDef]]

### Cvss
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.CvssTypeDef]]

### RelatedVulnerabilities
- **Type**: typing.Optional[typing.Sequence[str]]

### Vendor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityVendorTypeDef]

### ReferenceUrls
- **Type**: typing.Optional[typing.Sequence[str]]

### FixAvailable
- **Type**: typing.Optional[typing.Literal['NO', 'PARTIAL', 'YES']]

### EpssScore
- **Type**: typing.Optional[float]

### ExploitAvailable
- **Type**: typing.Optional[typing.Literal['NO', 'YES']]

### LastKnownExploitAt
- **Type**: typing.Optional[str]

### CodeVulnerabilities
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securityhub_classes.VulnerabilityCodeVulnerabilitiesTypeDef]]


# VulnerabilityVendorTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: typing.Optional[str]

### VendorSeverity
- **Type**: typing.Optional[str]

### VendorCreatedAt
- **Type**: typing.Optional[str]

### VendorUpdatedAt
- **Type**: typing.Optional[str]


# WafActionTypeDef

### Type
- **Type**: typing.Optional[str]


# WafExcludedRuleTypeDef

### RuleId
- **Type**: typing.Optional[str]


# WafOverrideActionTypeDef

### Type
- **Type**: typing.Optional[str]


# WorkflowTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['NEW', 'NOTIFIED', 'RESOLVED', 'SUPPRESSED']]


# WorkflowUpdateTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['NEW', 'NOTIFIED', 'RESOLVED', 'SUPPRESSED']]


