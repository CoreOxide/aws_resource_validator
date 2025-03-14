# Managedblockchain Classes

# AccessorSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApprovalThresholdPolicyTypeDef

### ThresholdPercentage
- **Type**: typing.Optional[int]

### ProposalDurationInHours
- **Type**: typing.Optional[int]

### ThresholdComparator
- **Type**: typing.Optional[typing.Literal['GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccessorInputTypeDef

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### AccessorType
- **Type**: typing.Literal['BILLING_TOKEN']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### NetworkType
- **Type**: typing.Optional[typing.Literal['ETHEREUM_GOERLI', 'ETHEREUM_MAINNET', 'ETHEREUM_MAINNET_AND_GOERLI', 'POLYGON_MAINNET', 'POLYGON_MUMBAI']]


# CreateAccessorOutputTypeDef

### AccessorId
- **Type**: <class 'str'>
- **Required**: Yes

### BillingToken
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkType
- **Type**: typing.Literal['ETHEREUM_GOERLI', 'ETHEREUM_MAINNET', 'ETHEREUM_MAINNET_AND_GOERLI', 'POLYGON_MAINNET', 'POLYGON_MUMBAI']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMemberInputTypeDef

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### InvitationId
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.MemberConfigurationTypeDef'>
- **Required**: Yes


# CreateMemberOutputTypeDef

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNetworkInputTypeDef

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Framework
- **Type**: typing.Literal['ETHEREUM', 'HYPERLEDGER_FABRIC']
- **Required**: Yes

### FrameworkVersion
- **Type**: <class 'str'>
- **Required**: Yes

### VotingPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.VotingPolicyTypeDef'>
- **Required**: Yes

### MemberConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.MemberConfigurationTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### FrameworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.NetworkFrameworkConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateNetworkOutputTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNodeInputTypeDef

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.NodeConfigurationTypeDef'>
- **Required**: Yes

### MemberId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateNodeOutputTypeDef

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProposalInputTypeDef

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ProposalActionsUnionTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProposalOutputTypeDef

### ProposalId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAccessorInputTypeDef

### AccessorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMemberInputTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNodeInputTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: typing.Optional[str]


# GetAccessorInputTypeDef

### AccessorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessorOutputTypeDef

### Accessor
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.AccessorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMemberInputTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMemberOutputTypeDef

### Member
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.MemberTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNetworkInputTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkOutputTypeDef

### Network
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.NetworkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNodeInputTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: typing.Optional[str]


# GetNodeOutputTypeDef

### Node
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.NodeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProposalInputTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ProposalId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProposalOutputTypeDef

### Proposal
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ProposalTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InvitationTypeDef

### InvitationId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### ExpirationDate
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'ACCEPTING', 'EXPIRED', 'PENDING', 'REJECTED']]

### NetworkSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.NetworkSummaryTypeDef]

### Arn
- **Type**: typing.Optional[str]


# InviteActionTypeDef

### Principal
- **Type**: <class 'str'>
- **Required**: Yes


# ListAccessorsInputPaginateTypeDef

### NetworkType
- **Type**: typing.Optional[typing.Literal['ETHEREUM_GOERLI', 'ETHEREUM_MAINNET', 'ETHEREUM_MAINNET_AND_GOERLI', 'POLYGON_MAINNET', 'POLYGON_MUMBAI']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.PaginatorConfigTypeDef]


# ListAccessorsInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### NetworkType
- **Type**: typing.Optional[typing.Literal['ETHEREUM_GOERLI', 'ETHEREUM_MAINNET', 'ETHEREUM_MAINNET_AND_GOERLI', 'POLYGON_MAINNET', 'POLYGON_MUMBAI']]


# ListAccessorsOutputTypeDef

### Accessors
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_classes.AccessorSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInvitationsInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInvitationsOutputTypeDef

### Invitations
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_classes.InvitationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMembersInputTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'INACCESSIBLE_ENCRYPTION_KEY', 'UPDATING']]

### IsOwned
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMembersOutputTypeDef

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_classes.MemberSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNetworksInputTypeDef

### Name
- **Type**: typing.Optional[str]

### Framework
- **Type**: typing.Optional[typing.Literal['ETHEREUM', 'HYPERLEDGER_FABRIC']]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNetworksOutputTypeDef

### Networks
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_classes.NetworkSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNodesInputTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'INACCESSIBLE_ENCRYPTION_KEY', 'UNHEALTHY', 'UPDATING']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNodesOutputTypeDef

### Nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_classes.NodeSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProposalVotesInputTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ProposalId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListProposalVotesOutputTypeDef

### ProposalVotes
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_classes.VoteSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProposalsInputTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListProposalsOutputTypeDef

### Proposals
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_classes.ProposalSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogConfigurationTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# LogConfigurationsTypeDef

### Cloudwatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.LogConfigurationTypeDef]


# MemberConfigurationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_classes.MemberFrameworkConfigurationTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### LogPublishingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.MemberLogPublishingConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### KmsKeyArn
- **Type**: typing.Optional[str]


# MemberFabricAttributesTypeDef

### AdminUsername
- **Type**: typing.Optional[str]

### CaEndpoint
- **Type**: typing.Optional[str]


# MemberFabricConfigurationTypeDef

### AdminUsername
- **Type**: <class 'str'>
- **Required**: Yes

### AdminPassword
- **Type**: <class 'str'>
- **Required**: Yes


# MemberFabricLogPublishingConfigurationTypeDef

### CaLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.LogConfigurationsTypeDef]


# MemberFrameworkAttributesTypeDef

### Fabric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.MemberFabricAttributesTypeDef]


# MemberFrameworkConfigurationTypeDef

### Fabric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.MemberFabricConfigurationTypeDef]


# MemberLogPublishingConfigurationTypeDef

### Fabric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.MemberFabricLogPublishingConfigurationTypeDef]


# MemberSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'INACCESSIBLE_ENCRYPTION_KEY', 'UPDATING']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### IsOwned
- **Type**: typing.Optional[bool]

### Arn
- **Type**: typing.Optional[str]


# MemberTypeDef

### NetworkId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### FrameworkAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.MemberFrameworkAttributesTypeDef]

### LogPublishingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.MemberLogPublishingConfigurationTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'INACCESSIBLE_ENCRYPTION_KEY', 'UPDATING']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Arn
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]


# NetworkEthereumAttributesTypeDef

### ChainId
- **Type**: typing.Optional[str]


# NetworkFabricAttributesTypeDef

### OrderingServiceEndpoint
- **Type**: typing.Optional[str]

### Edition
- **Type**: typing.Optional[typing.Literal['STANDARD', 'STARTER']]


# NetworkFabricConfigurationTypeDef

### Edition
- **Type**: typing.Literal['STANDARD', 'STARTER']
- **Required**: Yes


# NetworkFrameworkAttributesTypeDef

### Fabric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.NetworkFabricAttributesTypeDef]

### Ethereum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.NetworkEthereumAttributesTypeDef]


# NetworkFrameworkConfigurationTypeDef

### Fabric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.NetworkFabricConfigurationTypeDef]


# NetworkSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Framework
- **Type**: typing.Optional[typing.Literal['ETHEREUM', 'HYPERLEDGER_FABRIC']]

### FrameworkVersion
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### Arn
- **Type**: typing.Optional[str]


# NetworkTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Framework
- **Type**: typing.Optional[typing.Literal['ETHEREUM', 'HYPERLEDGER_FABRIC']]

### FrameworkVersion
- **Type**: typing.Optional[str]

### FrameworkAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.NetworkFrameworkAttributesTypeDef]

### VpcEndpointServiceName
- **Type**: typing.Optional[str]

### VotingPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.VotingPolicyTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Arn
- **Type**: typing.Optional[str]


# NodeConfigurationTypeDef

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZone
- **Type**: typing.Optional[str]

### LogPublishingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.NodeLogPublishingConfigurationTypeDef]

### StateDB
- **Type**: typing.Optional[typing.Literal['CouchDB', 'LevelDB']]


# NodeEthereumAttributesTypeDef

### HttpEndpoint
- **Type**: typing.Optional[str]

### WebSocketEndpoint
- **Type**: typing.Optional[str]


# NodeFabricAttributesTypeDef

### PeerEndpoint
- **Type**: typing.Optional[str]

### PeerEventEndpoint
- **Type**: typing.Optional[str]


# NodeFabricLogPublishingConfigurationTypeDef

### ChaincodeLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.LogConfigurationsTypeDef]

### PeerLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.LogConfigurationsTypeDef]


# NodeFrameworkAttributesTypeDef

### Fabric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.NodeFabricAttributesTypeDef]

### Ethereum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.NodeEthereumAttributesTypeDef]


# NodeLogPublishingConfigurationTypeDef

### Fabric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.NodeFabricLogPublishingConfigurationTypeDef]


# NodeSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'INACCESSIBLE_ENCRYPTION_KEY', 'UNHEALTHY', 'UPDATING']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### AvailabilityZone
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# NodeTypeDef

### NetworkId
- **Type**: typing.Optional[str]

### MemberId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### FrameworkAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.NodeFrameworkAttributesTypeDef]

### LogPublishingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.NodeLogPublishingConfigurationTypeDef]

### StateDB
- **Type**: typing.Optional[typing.Literal['CouchDB', 'LevelDB']]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'INACCESSIBLE_ENCRYPTION_KEY', 'UNHEALTHY', 'UPDATING']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Arn
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProposalActionsOutputTypeDef

### Invitations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.managedblockchain_classes.InviteActionTypeDef]]

### Removals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.managedblockchain_classes.RemoveActionTypeDef]]


# ProposalActionsTypeDef

### Invitations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.managedblockchain_classes.InviteActionTypeDef]]

### Removals
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.managedblockchain_classes.RemoveActionTypeDef]]


# ProposalActionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProposalSummaryTypeDef

### ProposalId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ProposedByMemberId
- **Type**: typing.Optional[str]

### ProposedByMemberName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTION_FAILED', 'APPROVED', 'EXPIRED', 'IN_PROGRESS', 'REJECTED']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### ExpirationDate
- **Type**: typing.Optional[datetime.datetime]

### Arn
- **Type**: typing.Optional[str]


# ProposalTypeDef

### ProposalId
- **Type**: typing.Optional[str]

### NetworkId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.ProposalActionsOutputTypeDef]

### ProposedByMemberId
- **Type**: typing.Optional[str]

### ProposedByMemberName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTION_FAILED', 'APPROVED', 'EXPIRED', 'IN_PROGRESS', 'REJECTED']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### ExpirationDate
- **Type**: typing.Optional[datetime.datetime]

### YesVoteCount
- **Type**: typing.Optional[int]

### NoVoteCount
- **Type**: typing.Optional[int]

### OutstandingVoteCount
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Arn
- **Type**: typing.Optional[str]


# RejectInvitationInputTypeDef

### InvitationId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveActionTypeDef

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes


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


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateMemberInputTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes

### LogPublishingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.MemberLogPublishingConfigurationTypeDef]


# UpdateNodeInputTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: typing.Optional[str]

### LogPublishingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.NodeLogPublishingConfigurationTypeDef]


# VoteOnProposalInputTypeDef

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ProposalId
- **Type**: <class 'str'>
- **Required**: Yes

### VoterMemberId
- **Type**: <class 'str'>
- **Required**: Yes

### Vote
- **Type**: typing.Literal['NO', 'YES']
- **Required**: Yes


# VoteSummaryTypeDef

### Vote
- **Type**: typing.Optional[typing.Literal['NO', 'YES']]

### MemberName
- **Type**: typing.Optional[str]

### MemberId
- **Type**: typing.Optional[str]


# VotingPolicyTypeDef

### ApprovalThresholdPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_classes.ApprovalThresholdPolicyTypeDef]


