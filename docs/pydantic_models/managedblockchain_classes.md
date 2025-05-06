# Managedblockchain Classes

# Accessor

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['BILLING_TOKEN']]

### BillingToken
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETED', 'PENDING_DELETION']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### Arn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### NetworkType
- **Type**: typing.Optional[typing.Literal['ETHEREUM_GOERLI', 'ETHEREUM_MAINNET', 'ETHEREUM_MAINNET_AND_GOERLI', 'POLYGON_MAINNET', 'POLYGON_MUMBAI']]


# AccessorSummary

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['BILLING_TOKEN']]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DELETED', 'PENDING_DELETION']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### Arn
- **Type**: typing.Optional[str]

### NetworkType
- **Type**: typing.Optional[typing.Literal['ETHEREUM_GOERLI', 'ETHEREUM_MAINNET', 'ETHEREUM_MAINNET_AND_GOERLI', 'POLYGON_MAINNET', 'POLYGON_MUMBAI']]


# ApprovalThresholdPolicy

### ThresholdPercentage
- **Type**: typing.Optional[int]

### ProposalDurationInHours
- **Type**: typing.Optional[int]

### ThresholdComparator
- **Type**: typing.Optional[typing.Literal['GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccessorInput

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### AccessorType
- **Type**: typing.Literal['BILLING_TOKEN']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### NetworkType
- **Type**: typing.Optional[typing.Literal['ETHEREUM_GOERLI', 'ETHEREUM_MAINNET', 'ETHEREUM_MAINNET_AND_GOERLI', 'POLYGON_MAINNET', 'POLYGON_MUMBAI']]


# CreateAccessorOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMemberInput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.MemberConfiguration'>
- **Required**: Yes


# CreateMemberOutput

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNetworkInput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.VotingPolicy'>
- **Required**: Yes

### MemberConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.MemberConfiguration'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### FrameworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NetworkFrameworkConfiguration]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateNetworkOutput

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNodeInput

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NodeConfiguration'>
- **Required**: Yes

### MemberId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateNodeOutput

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProposalInput

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ProposalActions, aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ProposalActionsOutput]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateProposalOutput

### ProposalId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAccessorInput

### AccessorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMemberInput

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNodeInput

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: typing.Optional[str]


# GetAccessorInput

### AccessorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessorOutput

### Accessor
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.Accessor'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes


# GetMemberInput

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMemberOutput

### Member
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.Member'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes


# GetNetworkInput

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkOutput

### Network
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.Network'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes


# GetNodeInput

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: typing.Optional[str]


# GetNodeOutput

### Node
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.Node'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes


# GetProposalInput

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### ProposalId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProposalOutput

### Proposal
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.Proposal'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes


# Invitation

### InvitationId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### ExpirationDate
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'ACCEPTING', 'EXPIRED', 'PENDING', 'REJECTED']]

### NetworkSummary
- **Type**: <class 'NoneType'>

### Arn
- **Type**: typing.Optional[str]


# InviteAction

### Principal
- **Type**: <class 'str'>
- **Required**: Yes


# ListAccessorsInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### NetworkType
- **Type**: typing.Optional[typing.Literal['ETHEREUM_GOERLI', 'ETHEREUM_MAINNET', 'ETHEREUM_MAINNET_AND_GOERLI', 'POLYGON_MAINNET', 'POLYGON_MUMBAI']]


# ListAccessorsInputPaginate

### NetworkType
- **Type**: typing.Optional[typing.Literal['ETHEREUM_GOERLI', 'ETHEREUM_MAINNET', 'ETHEREUM_MAINNET_AND_GOERLI', 'POLYGON_MAINNET', 'POLYGON_MUMBAI']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.PaginatorConfig]


# ListAccessorsOutput

### Accessors
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.AccessorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInvitationsInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInvitationsOutput

### Invitations
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.Invitation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMembersInput

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


# ListMembersOutput

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.MemberSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNetworksInput

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


# ListNetworksOutput

### Networks
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NetworkSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNodesInput

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


# ListNodesOutput

### Nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NodeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProposalVotesInput

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


# ListProposalVotesOutput

### ProposalVotes
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.VoteSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProposalsInput

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListProposalsOutput

### Proposals
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ProposalSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ResponseMetadata'>
- **Required**: Yes


# LogConfiguration

### Enabled
- **Type**: typing.Optional[bool]


# LogConfigurations

### Cloudwatch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.LogConfiguration]


# Member

### NetworkId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### FrameworkAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.MemberFrameworkAttributes]

### LogPublishingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.MemberLogPublishingConfiguration]

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


# MemberConfiguration

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.MemberFrameworkConfiguration'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### LogPublishingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.MemberLogPublishingConfiguration]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### KmsKeyArn
- **Type**: typing.Optional[str]


# MemberFabricAttributes

### AdminUsername
- **Type**: typing.Optional[str]

### CaEndpoint
- **Type**: typing.Optional[str]


# MemberFabricConfiguration

### AdminUsername
- **Type**: <class 'str'>
- **Required**: Yes

### AdminPassword
- **Type**: <class 'str'>
- **Required**: Yes


# MemberFabricLogPublishingConfiguration

### CaLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.LogConfigurations]


# MemberFrameworkAttributes

### Fabric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.MemberFabricAttributes]


# MemberFrameworkConfiguration

### Fabric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.MemberFabricConfiguration]


# MemberLogPublishingConfiguration

### Fabric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.MemberFabricLogPublishingConfiguration]


# MemberSummary

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


# Network

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NetworkFrameworkAttributes]

### VpcEndpointServiceName
- **Type**: typing.Optional[str]

### VotingPolicy
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETING']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Arn
- **Type**: typing.Optional[str]


# NetworkEthereumAttributes

### ChainId
- **Type**: typing.Optional[str]


# NetworkFabricAttributes

### OrderingServiceEndpoint
- **Type**: typing.Optional[str]

### Edition
- **Type**: typing.Optional[typing.Literal['STANDARD', 'STARTER']]


# NetworkFabricConfiguration

### Edition
- **Type**: typing.Literal['STANDARD', 'STARTER']
- **Required**: Yes


# NetworkFrameworkAttributes

### Fabric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NetworkFabricAttributes]

### Ethereum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NetworkEthereumAttributes]


# NetworkFrameworkConfiguration

### Fabric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NetworkFabricConfiguration]


# NetworkSummary

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


# Node

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NodeFrameworkAttributes]

### LogPublishingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NodeLogPublishingConfiguration]

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


# NodeConfiguration

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZone
- **Type**: typing.Optional[str]

### LogPublishingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NodeLogPublishingConfiguration]

### StateDB
- **Type**: typing.Optional[typing.Literal['CouchDB', 'LevelDB']]


# NodeEthereumAttributes

### HttpEndpoint
- **Type**: typing.Optional[str]

### WebSocketEndpoint
- **Type**: typing.Optional[str]


# NodeFabricAttributes

### PeerEndpoint
- **Type**: typing.Optional[str]

### PeerEventEndpoint
- **Type**: typing.Optional[str]


# NodeFabricLogPublishingConfiguration

### ChaincodeLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.LogConfigurations]

### PeerLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.LogConfigurations]


# NodeFrameworkAttributes

### Fabric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NodeFabricAttributes]

### Ethereum
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NodeEthereumAttributes]


# NodeLogPublishingConfiguration

### Fabric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NodeFabricLogPublishingConfiguration]


# NodeSummary

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


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Proposal

### ProposalId
- **Type**: typing.Optional[str]

### NetworkId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.ProposalActionsOutput]

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


# ProposalActions

### Invitations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.InviteAction]]

### Removals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.RemoveAction]]


# ProposalActionsOutput

### Invitations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.InviteAction]]

### Removals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.RemoveAction]]


# ProposalSummary

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


# RejectInvitationInput

### InvitationId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveAction

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes


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


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateMemberInput

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes

### LogPublishingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.MemberLogPublishingConfiguration]


# UpdateNodeInput

### NetworkId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: typing.Optional[str]

### LogPublishingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain.managedblockchain_classes.NodeLogPublishingConfiguration]


# VoteOnProposalInput

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


# VoteSummary

### Vote
- **Type**: typing.Optional[typing.Literal['NO', 'YES']]

### MemberName
- **Type**: typing.Optional[str]

### MemberId
- **Type**: typing.Optional[str]


# VotingPolicy

### ApprovalThresholdPolicy
- **Type**: <class 'NoneType'>


