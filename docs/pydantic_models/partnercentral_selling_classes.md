# Partnercentral Selling Classes

# AcceptEngagementInvitationRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# Account

### CompanyName
- **Type**: <class 'str'>
- **Required**: Yes

### Address
- **Type**: <class 'NoneType'>

### AwsAccountId
- **Type**: typing.Optional[str]

### Duns
- **Type**: typing.Optional[str]

### Industry
- **Type**: typing.Optional[typing.Literal['Aerospace', 'Agriculture', 'Automotive', 'Computers and Electronics', 'Consumer Goods', 'Education', 'Energy - Oil and Gas', 'Energy - Power and Utilities', 'Financial Services', 'Gaming', 'Government', 'Healthcare', 'Hospitality', 'Life Sciences', 'Manufacturing', 'Marketing and Advertising', 'Media and Entertainment', 'Mining', 'Non-Profit Organization', 'Other', 'Professional Services', 'Real Estate and Construction', 'Retail', 'Software and Internet', 'Telecommunications', 'Transportation and Logistics', 'Travel', 'Wholesale and Distribution']]

### OtherIndustry
- **Type**: typing.Optional[str]

### WebsiteUrl
- **Type**: typing.Optional[str]


# AccountReceiver

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: typing.Optional[str]


# AccountSummary

### CompanyName
- **Type**: <class 'str'>
- **Required**: Yes

### Address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.AddressSummary]

### Industry
- **Type**: typing.Optional[typing.Literal['Aerospace', 'Agriculture', 'Automotive', 'Computers and Electronics', 'Consumer Goods', 'Education', 'Energy - Oil and Gas', 'Energy - Power and Utilities', 'Financial Services', 'Gaming', 'Government', 'Healthcare', 'Hospitality', 'Life Sciences', 'Manufacturing', 'Marketing and Advertising', 'Media and Entertainment', 'Mining', 'Non-Profit Organization', 'Other', 'Professional Services', 'Real Estate and Construction', 'Retail', 'Software and Internet', 'Telecommunications', 'Transportation and Logistics', 'Travel', 'Wholesale and Distribution']]

### OtherIndustry
- **Type**: typing.Optional[str]

### WebsiteUrl
- **Type**: typing.Optional[str]


# Address

### City
- **Type**: typing.Optional[str]

### CountryCode
- **Type**: typing.Optional[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]

### PostalCode
- **Type**: typing.Optional[str]

### StateOrRegion
- **Type**: typing.Optional[str]

### StreetAddress
- **Type**: typing.Optional[str]


# AddressSummary

### City
- **Type**: typing.Optional[str]

### CountryCode
- **Type**: typing.Optional[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]

### PostalCode
- **Type**: typing.Optional[str]

### StateOrRegion
- **Type**: typing.Optional[str]


# AssignOpportunityRequest

### Assignee
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.AssigneeContact'>
- **Required**: Yes

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# AssigneeContact

### BusinessTitle
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes

### FirstName
- **Type**: <class 'str'>
- **Required**: Yes

### LastName
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateOpportunityRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### OpportunityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RelatedEntityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RelatedEntityType
- **Type**: typing.Literal['AwsMarketplaceOffers', 'AwsProducts', 'Solutions']
- **Required**: Yes


# AwsOpportunityCustomer

### Contacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Contact]]


# AwsOpportunityInsights

### EngagementScore
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium']]

### NextBestActions
- **Type**: typing.Optional[str]


# AwsOpportunityLifeCycle

### ClosedLostReason
- **Type**: typing.Optional[typing.Literal['Administrative', 'Business Associate Agreement', 'Company Acquired/Dissolved', 'Competitive Offering', 'Customer Data Requirement', 'Customer Deficiency', 'Customer Experience', 'Delay / Cancellation of Project', 'Duplicate', 'Duplicate Opportunity', 'Executive Blocker', 'Failed Vetting', 'Feature Limitation', 'Financial/Commercial', 'Insufficient AWS Value', 'Insufficient Amazon Value', 'International Constraints', 'Legal / Tax / Regulatory', 'Legal Terms and Conditions', 'Lost to Competitor', 'Lost to Competitor - Google', 'Lost to Competitor - Microsoft', 'Lost to Competitor - Other', 'Lost to Competitor - Rackspace', 'Lost to Competitor - SoftLayer', 'Lost to Competitor - VMWare', 'No Customer Reference', 'No Integration Resources', 'No Opportunity', 'No Perceived Value of MP', 'No Response', 'No Update', 'Not Committed to AWS', 'On Premises Deployment', 'Other', 'Other (Details in Description)', 'Partner Gap', 'Past Due', 'People/Relationship/Governance', 'Platform Technology Limitation', 'Preference for Competitor', 'Price', 'Product Not on AWS', 'Product/Technology', 'Security / Compliance', 'Self-Service', 'Technical Limitations', 'Term Sheet Impasse']]

### NextSteps
- **Type**: typing.Optional[str]

### NextStepsHistory
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ProfileNextStepsHistory]]

### Stage
- **Type**: typing.Optional[typing.Literal['Building Integration', 'Business Validation', 'Closed Incomplete', 'Closed Lost', 'Committed', 'Completed', 'Contract Negotiation', 'Deferred to Partner', 'Engaged', 'Evaluating', 'Identified', 'In Progress', 'Launched', 'Not Started', 'On-hold', 'Onboarding', 'Prospect', 'Qualified', 'Qualify', 'Research', 'Seller Engaged', 'Seller Registered', 'Technical Validation', 'Term Sheet Negotiation']]

### TargetCloseDate
- **Type**: typing.Optional[str]


# AwsOpportunityProject

### ExpectedCustomerSpend
- **Type**: typing.Optional[typing.List[NoneType]]


# AwsOpportunityRelatedEntities

### AwsProducts
- **Type**: typing.Optional[typing.List[str]]

### Solutions
- **Type**: typing.Optional[typing.List[str]]


# AwsSubmission

### InvolvementType
- **Type**: typing.Literal['Co-Sell', 'For Visibility Only']
- **Required**: Yes

### Visibility
- **Type**: typing.Optional[typing.Literal['Full', 'Limited']]


# AwsTeamMember

### BusinessTitle
- **Type**: typing.Optional[typing.Literal['AWSAccountOwner', 'AWSSalesRep', 'ISVSM', 'PDM', 'PSM', 'WWPSPDM']]

### Email
- **Type**: typing.Optional[str]

### FirstName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Contact

### BusinessTitle
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### FirstName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]

### Phone
- **Type**: typing.Optional[str]


# CreateEngagementInvitationRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Invitation
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Invitation'>
- **Required**: Yes


# CreateEngagementInvitationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEngagementRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Contexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.EngagementContextDetails]]


# CreateEngagementResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOpportunityRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Customer
- **Type**: typing.Union[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Customer, aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.CustomerOutput, NoneType]

### LifeCycle
- **Type**: typing.Union[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.LifeCycle, aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.LifeCycleOutput, NoneType]

### Marketing
- **Type**: typing.Union[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Marketing, aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.MarketingOutput, NoneType]

### NationalSecurity
- **Type**: typing.Optional[typing.Literal['No', 'Yes']]

### OpportunityTeam
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Contact]]

### OpportunityType
- **Type**: typing.Optional[typing.Literal['Expansion', 'Flat Renewal', 'Net New Business']]

### Origin
- **Type**: typing.Optional[typing.Literal['AWS Referral', 'Partner Referral']]

### PartnerOpportunityIdentifier
- **Type**: typing.Optional[str]

### PrimaryNeedsFromAws
- **Type**: typing.Optional[typing.List[typing.Literal['Co-Sell - Architectural Validation', 'Co-Sell - Business Presentation', 'Co-Sell - Competitive Information', 'Co-Sell - Deal Support', 'Co-Sell - Pricing Assistance', 'Co-Sell - Support for Public Tender / RFx', 'Co-Sell - Technical Consultation', 'Co-Sell - Total Cost of Ownership Evaluation']]]

### Project
- **Type**: typing.Union[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Project, aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ProjectOutput, NoneType]

### SoftwareRevenue
- **Type**: <class 'NoneType'>


# CreateOpportunityResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PartnerOpportunityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourceSnapshotJobRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSnapshotTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['Opportunity']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Tag]]


# CreateResourceSnapshotJobResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourceSnapshotRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSnapshotTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['Opportunity']
- **Required**: Yes


# CreateResourceSnapshotResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Revision
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# Customer

### Account
- **Type**: <class 'NoneType'>

### Contacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Contact]]


# CustomerOutput

### Account
- **Type**: <class 'NoneType'>

### Contacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Contact]]


# CustomerProjectsContext

### Customer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.EngagementCustomer]

### Project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.EngagementCustomerProjectDetails]


# CustomerSummary

### Account
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.AccountSummary]


# DeleteResourceSnapshotJobRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSnapshotJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateOpportunityRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### OpportunityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RelatedEntityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RelatedEntityType
- **Type**: typing.Literal['AwsMarketplaceOffers', 'AwsProducts', 'Solutions']
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# EngagementContextDetails

### Type
- **Type**: typing.Literal['CustomerProject']
- **Required**: Yes

### Payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.EngagementContextPayload]


# EngagementContextPayload

### CustomerProject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.CustomerProjectsContext]


# EngagementCustomer

### CompanyName
- **Type**: <class 'str'>
- **Required**: Yes

### CountryCode
- **Type**: typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']
- **Required**: Yes

### Industry
- **Type**: typing.Literal['Aerospace', 'Agriculture', 'Automotive', 'Computers and Electronics', 'Consumer Goods', 'Education', 'Energy - Oil and Gas', 'Energy - Power and Utilities', 'Financial Services', 'Gaming', 'Government', 'Healthcare', 'Hospitality', 'Life Sciences', 'Manufacturing', 'Marketing and Advertising', 'Media and Entertainment', 'Mining', 'Non-Profit Organization', 'Other', 'Professional Services', 'Real Estate and Construction', 'Retail', 'Software and Internet', 'Telecommunications', 'Transportation and Logistics', 'Travel', 'Wholesale and Distribution']
- **Required**: Yes

### WebsiteUrl
- **Type**: <class 'str'>
- **Required**: Yes


# EngagementCustomerProjectDetails

### BusinessProblem
- **Type**: <class 'str'>
- **Required**: Yes

### TargetCompletionDate
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes


# EngagementInvitationSummary

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### EngagementId
- **Type**: typing.Optional[str]

### EngagementTitle
- **Type**: typing.Optional[str]

### ExpirationDate
- **Type**: typing.Optional[datetime.datetime]

### InvitationDate
- **Type**: typing.Optional[datetime.datetime]

### ParticipantType
- **Type**: typing.Optional[typing.Literal['RECEIVER', 'SENDER']]

### PayloadType
- **Type**: typing.Optional[typing.Literal['OpportunityInvitation']]

### Receiver
- **Type**: <class 'NoneType'>

### SenderAwsAccountId
- **Type**: typing.Optional[str]

### SenderCompanyName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'EXPIRED', 'PENDING', 'REJECTED']]


# EngagementMember

### AccountId
- **Type**: typing.Optional[str]

### CompanyName
- **Type**: typing.Optional[str]

### WebsiteUrl
- **Type**: typing.Optional[str]


# EngagementMemberSummary

### CompanyName
- **Type**: typing.Optional[str]

### WebsiteUrl
- **Type**: typing.Optional[str]


# EngagementResourceAssociationSummary

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedBy
- **Type**: typing.Optional[str]

### EngagementId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['Opportunity']]


# EngagementSort

### SortBy
- **Type**: typing.Literal['CreatedDate']
- **Required**: Yes

### SortOrder
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# EngagementSummary

### Arn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### MemberCount
- **Type**: typing.Optional[int]

### Title
- **Type**: typing.Optional[str]


# ExpectedCustomerSpend

### Amount
- **Type**: <class 'str'>
- **Required**: Yes

### CurrencyCode
- **Type**: typing.Literal['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BOV', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHE', 'CHF', 'CHW', 'CLF', 'CLP', 'CNY', 'COP', 'COU', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MXV', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'USN', 'UYI', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'XSU', 'XUA', 'YER', 'ZAR', 'ZMW', 'ZWL']
- **Required**: Yes

### Frequency
- **Type**: typing.Literal['Monthly']
- **Required**: Yes

### TargetCompany
- **Type**: <class 'str'>
- **Required**: Yes

### EstimationUrl
- **Type**: typing.Optional[str]


# GetAwsOpportunitySummaryRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### RelatedOpportunityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAwsOpportunitySummaryResponse

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Customer
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.AwsOpportunityCustomer'>
- **Required**: Yes

### Insights
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.AwsOpportunityInsights'>
- **Required**: Yes

### InvolvementType
- **Type**: typing.Literal['Co-Sell', 'For Visibility Only']
- **Required**: Yes

### InvolvementTypeChangeReason
- **Type**: typing.Literal['Change in Deal Information', 'Customer Requested', 'Expansion Opportunity', 'Risk Mitigation', 'Technical Complexity']
- **Required**: Yes

### LifeCycle
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.AwsOpportunityLifeCycle'>
- **Required**: Yes

### OpportunityTeam
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.AwsTeamMember]
- **Required**: Yes

### Origin
- **Type**: typing.Literal['AWS Referral', 'Partner Referral']
- **Required**: Yes

### Project
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.AwsOpportunityProject'>
- **Required**: Yes

### RelatedEntityIds
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.AwsOpportunityRelatedEntities'>
- **Required**: Yes

### RelatedOpportunityId
- **Type**: <class 'str'>
- **Required**: Yes

### Visibility
- **Type**: typing.Literal['Full', 'Limited']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# GetEngagementInvitationRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEngagementInvitationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementDescription
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementTitle
- **Type**: <class 'str'>
- **Required**: Yes

### ExistingMembers
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.EngagementMemberSummary]
- **Required**: Yes

### ExpirationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InvitationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InvitationMessage
- **Type**: <class 'str'>
- **Required**: Yes

### Payload
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.PayloadOutput'>
- **Required**: Yes

### PayloadType
- **Type**: typing.Literal['OpportunityInvitation']
- **Required**: Yes

### Receiver
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Receiver'>
- **Required**: Yes

### RejectionReason
- **Type**: <class 'str'>
- **Required**: Yes

### SenderAwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### SenderCompanyName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACCEPTED', 'EXPIRED', 'PENDING', 'REJECTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# GetEngagementRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetEngagementResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Contexts
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.EngagementContextDetails]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MemberCount
- **Type**: <class 'int'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# GetOpportunityRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetOpportunityResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Customer
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.CustomerOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LifeCycle
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.LifeCycleOutput'>
- **Required**: Yes

### Marketing
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.MarketingOutput'>
- **Required**: Yes

### NationalSecurity
- **Type**: typing.Literal['No', 'Yes']
- **Required**: Yes

### OpportunityTeam
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Contact]
- **Required**: Yes

### OpportunityType
- **Type**: typing.Literal['Expansion', 'Flat Renewal', 'Net New Business']
- **Required**: Yes

### PartnerOpportunityIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryNeedsFromAws
- **Type**: typing.List[typing.Literal['Co-Sell - Architectural Validation', 'Co-Sell - Business Presentation', 'Co-Sell - Competitive Information', 'Co-Sell - Deal Support', 'Co-Sell - Pricing Assistance', 'Co-Sell - Support for Public Tender / RFx', 'Co-Sell - Technical Consultation', 'Co-Sell - Total Cost of Ownership Evaluation']]
- **Required**: Yes

### Project
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ProjectOutput'>
- **Required**: Yes

### RelatedEntityIdentifiers
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.RelatedEntityIdentifiers'>
- **Required**: Yes

### SoftwareRevenue
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.SoftwareRevenue'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceSnapshotJobRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSnapshotJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceSnapshotJobResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastFailure
- **Type**: <class 'str'>
- **Required**: Yes

### LastSuccessfulExecutionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSnapshotTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['Opportunity']
- **Required**: Yes

### Status
- **Type**: typing.Literal['Running', 'Stopped']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceSnapshotRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSnapshotTemplateIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['Opportunity']
- **Required**: Yes

### Revision
- **Type**: typing.Optional[int]


# GetResourceSnapshotResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes

### Payload
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResourceSnapshotPayload'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSnapshotTemplateName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['Opportunity']
- **Required**: Yes

### Revision
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# GetSellingSystemSettingsRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes


# GetSellingSystemSettingsResponse

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSnapshotJobRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# Invitation

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Payload
- **Type**: typing.Union[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Payload, aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.PayloadOutput]
- **Required**: Yes

### Receiver
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Receiver'>
- **Required**: Yes


# LastModifiedDate

### AfterLastModifiedDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### BeforeLastModifiedDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# LifeCycle

### ClosedLostReason
- **Type**: typing.Optional[typing.Literal['Customer Deficiency', 'Customer Experience', 'Delay / Cancellation of Project', 'Financial/Commercial', 'Legal / Tax / Regulatory', 'Lost to Competitor - Google', 'Lost to Competitor - Microsoft', 'Lost to Competitor - Other', 'Lost to Competitor - SoftLayer', 'Lost to Competitor - VMWare', 'No Opportunity', 'On Premises Deployment', 'Other', 'Partner Gap', 'People/Relationship/Governance', 'Price', 'Product/Technology', 'Security / Compliance', 'Technical Limitations']]

### NextSteps
- **Type**: typing.Optional[str]

### NextStepsHistory
- **Type**: typing.Optional[typing.List[NoneType]]

### ReviewComments
- **Type**: typing.Optional[str]

### ReviewStatus
- **Type**: typing.Optional[typing.Literal['Action Required', 'Approved', 'In review', 'Pending Submission', 'Rejected', 'Submitted']]

### ReviewStatusReason
- **Type**: typing.Optional[str]

### Stage
- **Type**: typing.Optional[typing.Literal['Business Validation', 'Closed Lost', 'Committed', 'Launched', 'Prospect', 'Qualified', 'Technical Validation']]

### TargetCloseDate
- **Type**: typing.Optional[str]


# LifeCycleForView

### NextSteps
- **Type**: typing.Optional[str]

### ReviewStatus
- **Type**: typing.Optional[typing.Literal['Action Required', 'Approved', 'In review', 'Pending Submission', 'Rejected', 'Submitted']]

### Stage
- **Type**: typing.Optional[typing.Literal['Business Validation', 'Closed Lost', 'Committed', 'Launched', 'Prospect', 'Qualified', 'Technical Validation']]

### TargetCloseDate
- **Type**: typing.Optional[str]


# LifeCycleOutput

### ClosedLostReason
- **Type**: typing.Optional[typing.Literal['Customer Deficiency', 'Customer Experience', 'Delay / Cancellation of Project', 'Financial/Commercial', 'Legal / Tax / Regulatory', 'Lost to Competitor - Google', 'Lost to Competitor - Microsoft', 'Lost to Competitor - Other', 'Lost to Competitor - SoftLayer', 'Lost to Competitor - VMWare', 'No Opportunity', 'On Premises Deployment', 'Other', 'Partner Gap', 'People/Relationship/Governance', 'Price', 'Product/Technology', 'Security / Compliance', 'Technical Limitations']]

### NextSteps
- **Type**: typing.Optional[str]

### NextStepsHistory
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.NextStepsHistoryOutput]]

### ReviewComments
- **Type**: typing.Optional[str]

### ReviewStatus
- **Type**: typing.Optional[typing.Literal['Action Required', 'Approved', 'In review', 'Pending Submission', 'Rejected', 'Submitted']]

### ReviewStatusReason
- **Type**: typing.Optional[str]

### Stage
- **Type**: typing.Optional[typing.Literal['Business Validation', 'Closed Lost', 'Committed', 'Launched', 'Prospect', 'Qualified', 'Technical Validation']]

### TargetCloseDate
- **Type**: typing.Optional[str]


# LifeCycleSummary

### ClosedLostReason
- **Type**: typing.Optional[typing.Literal['Customer Deficiency', 'Customer Experience', 'Delay / Cancellation of Project', 'Financial/Commercial', 'Legal / Tax / Regulatory', 'Lost to Competitor - Google', 'Lost to Competitor - Microsoft', 'Lost to Competitor - Other', 'Lost to Competitor - SoftLayer', 'Lost to Competitor - VMWare', 'No Opportunity', 'On Premises Deployment', 'Other', 'Partner Gap', 'People/Relationship/Governance', 'Price', 'Product/Technology', 'Security / Compliance', 'Technical Limitations']]

### NextSteps
- **Type**: typing.Optional[str]

### ReviewComments
- **Type**: typing.Optional[str]

### ReviewStatus
- **Type**: typing.Optional[typing.Literal['Action Required', 'Approved', 'In review', 'Pending Submission', 'Rejected', 'Submitted']]

### ReviewStatusReason
- **Type**: typing.Optional[str]

### Stage
- **Type**: typing.Optional[typing.Literal['Business Validation', 'Closed Lost', 'Committed', 'Launched', 'Prospect', 'Qualified', 'Technical Validation']]

### TargetCloseDate
- **Type**: typing.Optional[str]


# ListEngagementByAcceptingInvitationTaskSummary

### EngagementInvitationId
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### OpportunityId
- **Type**: typing.Optional[str]

### ReasonCode
- **Type**: typing.Optional[typing.Literal['EngagementAccessDenied', 'EngagementConflict', 'EngagementInvitationConflict', 'EngagementValidationFailed', 'InternalError', 'InvitationAccessDenied', 'InvitationValidationFailed', 'OpportunityAccessDenied', 'OpportunityConflict', 'OpportunitySubmissionFailed', 'OpportunityValidationFailed', 'RequestThrottled', 'ResourceSnapshotAccessDenied', 'ResourceSnapshotConflict', 'ResourceSnapshotJobAccessDenied', 'ResourceSnapshotJobConflict', 'ResourceSnapshotJobValidationFailed', 'ResourceSnapshotValidationFailed', 'ServiceQuotaExceeded']]

### ResourceSnapshotJobId
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### TaskArn
- **Type**: typing.Optional[str]

### TaskId
- **Type**: typing.Optional[str]

### TaskStatus
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']]


# ListEngagementByAcceptingInvitationTasksRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementInvitationIdentifier
- **Type**: typing.Optional[typing.List[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### OpportunityIdentifier
- **Type**: typing.Optional[typing.List[str]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ListTasksSortBase]

### TaskIdentifier
- **Type**: typing.Optional[typing.List[str]]

### TaskStatus
- **Type**: typing.Optional[typing.List[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']]]


# ListEngagementByAcceptingInvitationTasksRequestPaginate

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementInvitationIdentifier
- **Type**: typing.Optional[typing.List[str]]

### OpportunityIdentifier
- **Type**: typing.Optional[typing.List[str]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ListTasksSortBase]

### TaskIdentifier
- **Type**: typing.Optional[typing.List[str]]

### TaskStatus
- **Type**: typing.Optional[typing.List[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.PaginatorConfig]


# ListEngagementByAcceptingInvitationTasksResponse

### TaskSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ListEngagementByAcceptingInvitationTaskSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEngagementFromOpportunityTaskSummary

### EngagementId
- **Type**: typing.Optional[str]

### EngagementInvitationId
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### OpportunityId
- **Type**: typing.Optional[str]

### ReasonCode
- **Type**: typing.Optional[typing.Literal['EngagementAccessDenied', 'EngagementConflict', 'EngagementInvitationConflict', 'EngagementValidationFailed', 'InternalError', 'InvitationAccessDenied', 'InvitationValidationFailed', 'OpportunityAccessDenied', 'OpportunityConflict', 'OpportunitySubmissionFailed', 'OpportunityValidationFailed', 'RequestThrottled', 'ResourceSnapshotAccessDenied', 'ResourceSnapshotConflict', 'ResourceSnapshotJobAccessDenied', 'ResourceSnapshotJobConflict', 'ResourceSnapshotJobValidationFailed', 'ResourceSnapshotValidationFailed', 'ServiceQuotaExceeded']]

### ResourceSnapshotJobId
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### TaskArn
- **Type**: typing.Optional[str]

### TaskId
- **Type**: typing.Optional[str]

### TaskStatus
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']]


# ListEngagementFromOpportunityTasksRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementIdentifier
- **Type**: typing.Optional[typing.List[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### OpportunityIdentifier
- **Type**: typing.Optional[typing.List[str]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ListTasksSortBase]

### TaskIdentifier
- **Type**: typing.Optional[typing.List[str]]

### TaskStatus
- **Type**: typing.Optional[typing.List[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']]]


# ListEngagementFromOpportunityTasksRequestPaginate

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementIdentifier
- **Type**: typing.Optional[typing.List[str]]

### OpportunityIdentifier
- **Type**: typing.Optional[typing.List[str]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ListTasksSortBase]

### TaskIdentifier
- **Type**: typing.Optional[typing.List[str]]

### TaskStatus
- **Type**: typing.Optional[typing.List[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.PaginatorConfig]


# ListEngagementFromOpportunityTasksResponse

### TaskSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ListEngagementFromOpportunityTaskSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEngagementInvitationsRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantType
- **Type**: typing.Literal['RECEIVER', 'SENDER']
- **Required**: Yes

### EngagementIdentifier
- **Type**: typing.Optional[typing.List[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### PayloadType
- **Type**: typing.Optional[typing.List[typing.Literal['OpportunityInvitation']]]

### SenderAwsAccountId
- **Type**: typing.Optional[typing.List[str]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.OpportunityEngagementInvitationSort]

### Status
- **Type**: typing.Optional[typing.List[typing.Literal['ACCEPTED', 'EXPIRED', 'PENDING', 'REJECTED']]]


# ListEngagementInvitationsRequestPaginate

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantType
- **Type**: typing.Literal['RECEIVER', 'SENDER']
- **Required**: Yes

### EngagementIdentifier
- **Type**: typing.Optional[typing.List[str]]

### PayloadType
- **Type**: typing.Optional[typing.List[typing.Literal['OpportunityInvitation']]]

### SenderAwsAccountId
- **Type**: typing.Optional[typing.List[str]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.OpportunityEngagementInvitationSort]

### Status
- **Type**: typing.Optional[typing.List[typing.Literal['ACCEPTED', 'EXPIRED', 'PENDING', 'REJECTED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.PaginatorConfig]


# ListEngagementInvitationsResponse

### EngagementInvitationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.EngagementInvitationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEngagementMembersRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEngagementMembersRequestPaginate

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.PaginatorConfig]


# ListEngagementMembersResponse

### EngagementMemberList
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.EngagementMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEngagementResourceAssociationsRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedBy
- **Type**: typing.Optional[str]

### EngagementIdentifier
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['Opportunity']]


# ListEngagementResourceAssociationsRequestPaginate

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedBy
- **Type**: typing.Optional[str]

### EngagementIdentifier
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['Opportunity']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.PaginatorConfig]


# ListEngagementResourceAssociationsResponse

### EngagementResourceAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.EngagementResourceAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEngagementsRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedBy
- **Type**: typing.Optional[typing.List[str]]

### EngagementIdentifier
- **Type**: typing.Optional[typing.List[str]]

### ExcludeCreatedBy
- **Type**: typing.Optional[typing.List[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.EngagementSort]


# ListEngagementsRequestPaginate

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedBy
- **Type**: typing.Optional[typing.List[str]]

### EngagementIdentifier
- **Type**: typing.Optional[typing.List[str]]

### ExcludeCreatedBy
- **Type**: typing.Optional[typing.List[str]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.EngagementSort]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.PaginatorConfig]


# ListEngagementsResponse

### EngagementSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.EngagementSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOpportunitiesRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerCompanyName
- **Type**: typing.Optional[typing.List[str]]

### Identifier
- **Type**: typing.Optional[typing.List[str]]

### LastModifiedDate
- **Type**: <class 'NoneType'>

### LifeCycleReviewStatus
- **Type**: typing.Optional[typing.List[typing.Literal['Action Required', 'Approved', 'In review', 'Pending Submission', 'Rejected', 'Submitted']]]

### LifeCycleStage
- **Type**: typing.Optional[typing.List[typing.Literal['Business Validation', 'Closed Lost', 'Committed', 'Launched', 'Prospect', 'Qualified', 'Technical Validation']]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.OpportunitySort]


# ListOpportunitiesRequestPaginate

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerCompanyName
- **Type**: typing.Optional[typing.List[str]]

### Identifier
- **Type**: typing.Optional[typing.List[str]]

### LastModifiedDate
- **Type**: <class 'NoneType'>

### LifeCycleReviewStatus
- **Type**: typing.Optional[typing.List[typing.Literal['Action Required', 'Approved', 'In review', 'Pending Submission', 'Rejected', 'Submitted']]]

### LifeCycleStage
- **Type**: typing.Optional[typing.List[typing.Literal['Business Validation', 'Closed Lost', 'Committed', 'Launched', 'Prospect', 'Qualified', 'Technical Validation']]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.OpportunitySort]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.PaginatorConfig]


# ListOpportunitiesResponse

### OpportunitySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.OpportunitySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceSnapshotJobsRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementIdentifier
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.SortObject]

### Status
- **Type**: typing.Optional[typing.Literal['Running', 'Stopped']]


# ListResourceSnapshotJobsRequestPaginate

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementIdentifier
- **Type**: typing.Optional[str]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.SortObject]

### Status
- **Type**: typing.Optional[typing.Literal['Running', 'Stopped']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.PaginatorConfig]


# ListResourceSnapshotJobsResponse

### ResourceSnapshotJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResourceSnapshotJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceSnapshotsRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedBy
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ResourceSnapshotTemplateIdentifier
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['Opportunity']]


# ListResourceSnapshotsRequestPaginate

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedBy
- **Type**: typing.Optional[str]

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ResourceSnapshotTemplateIdentifier
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['Opportunity']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.PaginatorConfig]


# ListResourceSnapshotsResponse

### ResourceSnapshotSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResourceSnapshotSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSolutionsRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Category
- **Type**: typing.Optional[typing.List[str]]

### Identifier
- **Type**: typing.Optional[typing.List[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.SolutionSort]

### Status
- **Type**: typing.Optional[typing.List[typing.Literal['Active', 'Draft', 'Inactive']]]


# ListSolutionsRequestPaginate

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Category
- **Type**: typing.Optional[typing.List[str]]

### Identifier
- **Type**: typing.Optional[typing.List[str]]

### Sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.SolutionSort]

### Status
- **Type**: typing.Optional[typing.List[typing.Literal['Active', 'Draft', 'Inactive']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.PaginatorConfig]


# ListSolutionsResponse

### SolutionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.SolutionBase]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# ListTasksSortBase

### SortBy
- **Type**: typing.Literal['StartTime']
- **Required**: Yes

### SortOrder
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# Marketing

### AwsFundingUsed
- **Type**: typing.Optional[typing.Literal['No', 'Yes']]

### CampaignName
- **Type**: typing.Optional[str]

### Channels
- **Type**: typing.Optional[typing.List[typing.Literal['AWS Marketing Central', 'Content Syndication', 'Display', 'Email', 'Live Event', 'Out Of Home (OOH)', 'Print', 'Search', 'Social', 'TV', 'Telemarketing', 'Video', 'Virtual Event']]]

### Source
- **Type**: typing.Optional[typing.Literal['Marketing Activity', 'None']]

### UseCases
- **Type**: typing.Optional[typing.List[str]]


# MarketingOutput

### AwsFundingUsed
- **Type**: typing.Optional[typing.Literal['No', 'Yes']]

### CampaignName
- **Type**: typing.Optional[str]

### Channels
- **Type**: typing.Optional[typing.List[typing.Literal['AWS Marketing Central', 'Content Syndication', 'Display', 'Email', 'Live Event', 'Out Of Home (OOH)', 'Print', 'Search', 'Social', 'TV', 'Telemarketing', 'Video', 'Virtual Event']]]

### Source
- **Type**: typing.Optional[typing.Literal['Marketing Activity', 'None']]

### UseCases
- **Type**: typing.Optional[typing.List[str]]


# MonetaryValue

### Amount
- **Type**: <class 'str'>
- **Required**: Yes

### CurrencyCode
- **Type**: typing.Literal['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BOV', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHE', 'CHF', 'CHW', 'CLF', 'CLP', 'CNY', 'COP', 'COU', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MXV', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'USN', 'UYI', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'XSU', 'XUA', 'YER', 'ZAR', 'ZMW', 'ZWL']
- **Required**: Yes


# NextStepsHistory

### Time
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# NextStepsHistoryOutput

### Time
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# OpportunityEngagementInvitationSort

### SortBy
- **Type**: typing.Literal['InvitationDate']
- **Required**: Yes

### SortOrder
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# OpportunityInvitationPayload

### Customer
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.EngagementCustomer'>
- **Required**: Yes

### Project
- **Type**: typing.Union[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ProjectDetails, aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ProjectDetailsOutput]
- **Required**: Yes

### ReceiverResponsibilities
- **Type**: typing.List[typing.Literal['Co-Sell Facilitator', 'Distributor', 'Facilitator', 'Hardware Partner', 'Managed Service Provider', 'Reseller', 'Services Partner', 'Software Partner', 'Training Partner']]
- **Required**: Yes

### SenderContacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.SenderContact]]


# OpportunityInvitationPayloadOutput

### Customer
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.EngagementCustomer'>
- **Required**: Yes

### Project
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ProjectDetailsOutput'>
- **Required**: Yes

### ReceiverResponsibilities
- **Type**: typing.List[typing.Literal['Co-Sell Facilitator', 'Distributor', 'Facilitator', 'Hardware Partner', 'Managed Service Provider', 'Reseller', 'Services Partner', 'Software Partner', 'Training Partner']]
- **Required**: Yes

### SenderContacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.SenderContact]]


# OpportunitySort

### SortBy
- **Type**: typing.Literal['CustomerCompanyName', 'Identifier', 'LastModifiedDate']
- **Required**: Yes

### SortOrder
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# OpportunitySummary

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### Customer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.CustomerSummary]

### Id
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### LifeCycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.LifeCycleSummary]

### OpportunityType
- **Type**: typing.Optional[typing.Literal['Expansion', 'Flat Renewal', 'Net New Business']]

### PartnerOpportunityIdentifier
- **Type**: typing.Optional[str]

### Project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ProjectSummary]


# OpportunitySummaryView

### Customer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.CustomerOutput]

### Lifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.LifeCycleForView]

### OpportunityTeam
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Contact]]

### OpportunityType
- **Type**: typing.Optional[typing.Literal['Expansion', 'Flat Renewal', 'Net New Business']]

### PrimaryNeedsFromAws
- **Type**: typing.Optional[typing.List[typing.Literal['Co-Sell - Architectural Validation', 'Co-Sell - Business Presentation', 'Co-Sell - Competitive Information', 'Co-Sell - Deal Support', 'Co-Sell - Pricing Assistance', 'Co-Sell - Support for Public Tender / RFx', 'Co-Sell - Technical Consultation', 'Co-Sell - Total Cost of Ownership Evaluation']]]

### Project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ProjectView]

### RelatedEntityIdentifiers
- **Type**: <class 'NoneType'>


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Payload

### OpportunityInvitation
- **Type**: typing.Union[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.OpportunityInvitationPayload, aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.OpportunityInvitationPayloadOutput, NoneType]


# PayloadOutput

### OpportunityInvitation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.OpportunityInvitationPayloadOutput]


# ProfileNextStepsHistory

### Time
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# Project

### AdditionalComments
- **Type**: typing.Optional[str]

### ApnPrograms
- **Type**: typing.Optional[typing.List[str]]

### CompetitorName
- **Type**: typing.Optional[typing.Literal['*Other', 'Akamai', 'AliCloud', 'Co-location', 'Google Cloud Platform', 'IBM Softlayer', 'Microsoft Azure', 'No Competition', 'On-Prem', 'Oracle Cloud', 'Other- Cost Optimization']]

### CustomerBusinessProblem
- **Type**: typing.Optional[str]

### CustomerUseCase
- **Type**: typing.Optional[str]

### DeliveryModels
- **Type**: typing.Optional[typing.List[typing.Literal['BYOL or AMI', 'Managed Services', 'Other', 'Professional Services', 'Resell', 'SaaS or PaaS']]]

### ExpectedCustomerSpend
- **Type**: typing.Optional[typing.List[NoneType]]

### OtherCompetitorNames
- **Type**: typing.Optional[str]

### OtherSolutionDescription
- **Type**: typing.Optional[str]

### RelatedOpportunityIdentifier
- **Type**: typing.Optional[str]

### SalesActivities
- **Type**: typing.Optional[typing.List[typing.Literal['Agreed on solution to Business Problem', 'Completed Action Plan', 'Conducted POC / Demo', 'Customer has shown interest in solution', 'Finalized Deployment Need', 'In evaluation / planning stage', 'Initialized discussions with customer', 'SOW Signed']]]

### Title
- **Type**: typing.Optional[str]


# ProjectDetails

### BusinessProblem
- **Type**: <class 'str'>
- **Required**: Yes

### ExpectedCustomerSpend
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ExpectedCustomerSpend]
- **Required**: Yes

### TargetCompletionDate
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes


# ProjectDetailsOutput

### BusinessProblem
- **Type**: <class 'str'>
- **Required**: Yes

### ExpectedCustomerSpend
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ExpectedCustomerSpend]
- **Required**: Yes

### TargetCompletionDate
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes


# ProjectOutput

### AdditionalComments
- **Type**: typing.Optional[str]

### ApnPrograms
- **Type**: typing.Optional[typing.List[str]]

### CompetitorName
- **Type**: typing.Optional[typing.Literal['*Other', 'Akamai', 'AliCloud', 'Co-location', 'Google Cloud Platform', 'IBM Softlayer', 'Microsoft Azure', 'No Competition', 'On-Prem', 'Oracle Cloud', 'Other- Cost Optimization']]

### CustomerBusinessProblem
- **Type**: typing.Optional[str]

### CustomerUseCase
- **Type**: typing.Optional[str]

### DeliveryModels
- **Type**: typing.Optional[typing.List[typing.Literal['BYOL or AMI', 'Managed Services', 'Other', 'Professional Services', 'Resell', 'SaaS or PaaS']]]

### ExpectedCustomerSpend
- **Type**: typing.Optional[typing.List[NoneType]]

### OtherCompetitorNames
- **Type**: typing.Optional[str]

### OtherSolutionDescription
- **Type**: typing.Optional[str]

### RelatedOpportunityIdentifier
- **Type**: typing.Optional[str]

### SalesActivities
- **Type**: typing.Optional[typing.List[typing.Literal['Agreed on solution to Business Problem', 'Completed Action Plan', 'Conducted POC / Demo', 'Customer has shown interest in solution', 'Finalized Deployment Need', 'In evaluation / planning stage', 'Initialized discussions with customer', 'SOW Signed']]]

### Title
- **Type**: typing.Optional[str]


# ProjectSummary

### DeliveryModels
- **Type**: typing.Optional[typing.List[typing.Literal['BYOL or AMI', 'Managed Services', 'Other', 'Professional Services', 'Resell', 'SaaS or PaaS']]]

### ExpectedCustomerSpend
- **Type**: typing.Optional[typing.List[NoneType]]


# ProjectView

### CustomerUseCase
- **Type**: typing.Optional[str]

### DeliveryModels
- **Type**: typing.Optional[typing.List[typing.Literal['BYOL or AMI', 'Managed Services', 'Other', 'Professional Services', 'Resell', 'SaaS or PaaS']]]

### ExpectedCustomerSpend
- **Type**: typing.Optional[typing.List[NoneType]]

### OtherSolutionDescription
- **Type**: typing.Optional[str]

### SalesActivities
- **Type**: typing.Optional[typing.List[typing.Literal['Agreed on solution to Business Problem', 'Completed Action Plan', 'Conducted POC / Demo', 'Customer has shown interest in solution', 'Finalized Deployment Need', 'In evaluation / planning stage', 'Initialized discussions with customer', 'SOW Signed']]]


# PutSellingSystemSettingsRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSnapshotJobRoleIdentifier
- **Type**: typing.Optional[str]


# PutSellingSystemSettingsResponse

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSnapshotJobRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# Receiver

### Account
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.AccountReceiver]


# RejectEngagementInvitationRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### RejectionReason
- **Type**: typing.Optional[str]


# RelatedEntityIdentifiers

### AwsMarketplaceOffers
- **Type**: typing.Optional[typing.List[str]]

### AwsProducts
- **Type**: typing.Optional[typing.List[str]]

### Solutions
- **Type**: typing.Optional[typing.List[str]]


# ResourceSnapshotJobSummary

### Arn
- **Type**: typing.Optional[str]

### EngagementId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Running', 'Stopped']]


# ResourceSnapshotPayload

### OpportunitySummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.OpportunitySummaryView]


# ResourceSnapshotSummary

### Arn
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ResourceSnapshotTemplateName
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['Opportunity']]

### Revision
- **Type**: typing.Optional[int]


# ResponseMetadata

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


# SenderContact

### Email
- **Type**: <class 'str'>
- **Required**: Yes

### BusinessTitle
- **Type**: typing.Optional[str]

### FirstName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]

### Phone
- **Type**: typing.Optional[str]


# SoftwareRevenue

### DeliveryModel
- **Type**: typing.Optional[typing.Literal['Contract', 'Pay-as-you-go', 'Subscription']]

### EffectiveDate
- **Type**: typing.Optional[str]

### ExpirationDate
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.MonetaryValue]


# SolutionBase

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Category
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Draft', 'Inactive']
- **Required**: Yes

### Arn
- **Type**: typing.Optional[str]


# SolutionSort

### SortBy
- **Type**: typing.Literal['Category', 'CreatedDate', 'Identifier', 'Name', 'Status']
- **Required**: Yes

### SortOrder
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# SortObject

### SortBy
- **Type**: typing.Optional[typing.Literal['CreatedDate']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# StartEngagementByAcceptingInvitationTaskRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Tag]]


# StartEngagementByAcceptingInvitationTaskResponse

### EngagementInvitationId
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### OpportunityId
- **Type**: <class 'str'>
- **Required**: Yes

### ReasonCode
- **Type**: typing.Literal['EngagementAccessDenied', 'EngagementConflict', 'EngagementInvitationConflict', 'EngagementValidationFailed', 'InternalError', 'InvitationAccessDenied', 'InvitationValidationFailed', 'OpportunityAccessDenied', 'OpportunityConflict', 'OpportunitySubmissionFailed', 'OpportunityValidationFailed', 'RequestThrottled', 'ResourceSnapshotAccessDenied', 'ResourceSnapshotConflict', 'ResourceSnapshotJobAccessDenied', 'ResourceSnapshotJobConflict', 'ResourceSnapshotJobValidationFailed', 'ResourceSnapshotValidationFailed', 'ServiceQuotaExceeded']
- **Required**: Yes

### ResourceSnapshotJobId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskStatus
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# StartEngagementFromOpportunityTaskRequest

### AwsSubmission
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.AwsSubmission'>
- **Required**: Yes

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Tag]]


# StartEngagementFromOpportunityTaskResponse

### EngagementId
- **Type**: <class 'str'>
- **Required**: Yes

### EngagementInvitationId
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### OpportunityId
- **Type**: <class 'str'>
- **Required**: Yes

### ReasonCode
- **Type**: typing.Literal['EngagementAccessDenied', 'EngagementConflict', 'EngagementInvitationConflict', 'EngagementValidationFailed', 'InternalError', 'InvitationAccessDenied', 'InvitationValidationFailed', 'OpportunityAccessDenied', 'OpportunityConflict', 'OpportunitySubmissionFailed', 'OpportunityValidationFailed', 'RequestThrottled', 'ResourceSnapshotAccessDenied', 'ResourceSnapshotConflict', 'ResourceSnapshotJobAccessDenied', 'ResourceSnapshotJobConflict', 'ResourceSnapshotJobValidationFailed', 'ResourceSnapshotValidationFailed', 'ServiceQuotaExceeded']
- **Required**: Yes

### ResourceSnapshotJobId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskStatus
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


# StartResourceSnapshotJobRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSnapshotJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StopResourceSnapshotJobRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSnapshotJobIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# SubmitOpportunityRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### InvolvementType
- **Type**: typing.Literal['Co-Sell', 'For Visibility Only']
- **Required**: Yes

### Visibility
- **Type**: typing.Optional[typing.Literal['Full', 'Limited']]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateOpportunityRequest

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Customer
- **Type**: typing.Union[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Customer, aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.CustomerOutput, NoneType]

### LifeCycle
- **Type**: typing.Union[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.LifeCycle, aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.LifeCycleOutput, NoneType]

### Marketing
- **Type**: typing.Union[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Marketing, aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.MarketingOutput, NoneType]

### NationalSecurity
- **Type**: typing.Optional[typing.Literal['No', 'Yes']]

### OpportunityType
- **Type**: typing.Optional[typing.Literal['Expansion', 'Flat Renewal', 'Net New Business']]

### PartnerOpportunityIdentifier
- **Type**: typing.Optional[str]

### PrimaryNeedsFromAws
- **Type**: typing.Optional[typing.List[typing.Literal['Co-Sell - Architectural Validation', 'Co-Sell - Business Presentation', 'Co-Sell - Competitive Information', 'Co-Sell - Deal Support', 'Co-Sell - Pricing Assistance', 'Co-Sell - Support for Public Tender / RFx', 'Co-Sell - Technical Consultation', 'Co-Sell - Total Cost of Ownership Evaluation']]]

### Project
- **Type**: typing.Union[aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.Project, aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ProjectOutput, NoneType]

### SoftwareRevenue
- **Type**: <class 'NoneType'>


# UpdateOpportunityResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.partnercentral_selling.partnercentral_selling_classes.ResponseMetadata'>
- **Required**: Yes


