# Managedblockchain Query Classes

# AddressIdentifierFilter

### transactionEventToAddress
- **Type**: typing.List[str]
- **Required**: Yes


# AssetContract

### contractIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ContractIdentifier'>
- **Required**: Yes

### tokenStandard
- **Type**: typing.Literal['ERC1155', 'ERC20', 'ERC721']
- **Required**: Yes

### deployerAddress
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetTokenBalanceErrorItem

### errorCode
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### errorType
- **Type**: typing.Literal['RESOURCE_NOT_FOUND_EXCEPTION', 'VALIDATION_EXCEPTION']
- **Required**: Yes

### tokenIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.TokenIdentifier]

### ownerIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.OwnerIdentifier]

### atBlockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput]


# BatchGetTokenBalanceInput

### getTokenBalanceInputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BatchGetTokenBalanceInputItem]]


# BatchGetTokenBalanceInputItem

### tokenIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.TokenIdentifier'>
- **Required**: Yes

### ownerIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.OwnerIdentifier'>
- **Required**: Yes

### atBlockchainInstant
- **Type**: typing.Union[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstant, aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput, NoneType]


# BatchGetTokenBalanceOutput

### tokenBalances
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BatchGetTokenBalanceOutputItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BatchGetTokenBalanceErrorItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetTokenBalanceOutputItem

### balance
- **Type**: <class 'str'>
- **Required**: Yes

### atBlockchainInstant
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput'>
- **Required**: Yes

### ownerIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.OwnerIdentifier]

### tokenIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.TokenIdentifier]

### lastUpdatedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput]


# BlockchainInstant

### time
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# BlockchainInstantOutput

### time
- **Type**: typing.Optional[datetime.datetime]


# ConfirmationStatusFilter

### include
- **Type**: typing.List[typing.Literal['FINAL', 'NONFINAL']]
- **Required**: Yes


# ContractFilter

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### tokenStandard
- **Type**: typing.Literal['ERC1155', 'ERC20', 'ERC721']
- **Required**: Yes

### deployerAddress
- **Type**: <class 'str'>
- **Required**: Yes


# ContractIdentifier

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### contractAddress
- **Type**: <class 'str'>
- **Required**: Yes


# ContractMetadata

### name
- **Type**: typing.Optional[str]

### symbol
- **Type**: typing.Optional[str]

### decimals
- **Type**: typing.Optional[int]


# GetAssetContractInput

### contractIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ContractIdentifier'>
- **Required**: Yes


# GetAssetContractOutput

### contractIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ContractIdentifier'>
- **Required**: Yes

### tokenStandard
- **Type**: typing.Literal['ERC1155', 'ERC20', 'ERC721']
- **Required**: Yes

### deployerAddress
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ContractMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ResponseMetadata'>
- **Required**: Yes


# GetTokenBalanceInput

### tokenIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.TokenIdentifier'>
- **Required**: Yes

### ownerIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.OwnerIdentifier'>
- **Required**: Yes

### atBlockchainInstant
- **Type**: typing.Union[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstant, aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput, NoneType]


# GetTokenBalanceOutput

### ownerIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.OwnerIdentifier'>
- **Required**: Yes

### tokenIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.TokenIdentifier'>
- **Required**: Yes

### balance
- **Type**: <class 'str'>
- **Required**: Yes

### atBlockchainInstant
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ResponseMetadata'>
- **Required**: Yes


# GetTransactionInput

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### transactionHash
- **Type**: typing.Optional[str]

### transactionId
- **Type**: typing.Optional[str]


# GetTransactionOutput

### transaction
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.Transaction'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ResponseMetadata'>
- **Required**: Yes


# ListAssetContractsInput

### contractFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ContractFilter'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssetContractsInputPaginate

### contractFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ContractFilter'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.PaginatorConfig]


# ListAssetContractsOutput

### contracts
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.AssetContract]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFilteredTransactionEventsInput

### network
- **Type**: <class 'str'>
- **Required**: Yes

### addressIdentifierFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.AddressIdentifierFilter'>
- **Required**: Yes

### timeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.TimeFilter]

### voutFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.VoutFilter]

### confirmationStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ConfirmationStatusFilter]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ListFilteredTransactionEventsSort]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFilteredTransactionEventsInputPaginate

### network
- **Type**: <class 'str'>
- **Required**: Yes

### addressIdentifierFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.AddressIdentifierFilter'>
- **Required**: Yes

### timeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.TimeFilter]

### voutFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.VoutFilter]

### confirmationStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ConfirmationStatusFilter]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ListFilteredTransactionEventsSort]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.PaginatorConfig]


# ListFilteredTransactionEventsOutput

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.TransactionEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFilteredTransactionEventsSort

### sortBy
- **Type**: typing.Optional[typing.Literal['blockchainInstant']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListTokenBalancesInput

### tokenFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.TokenFilter'>
- **Required**: Yes

### ownerFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.OwnerFilter]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTokenBalancesInputPaginate

### tokenFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.TokenFilter'>
- **Required**: Yes

### ownerFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.OwnerFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.PaginatorConfig]


# ListTokenBalancesOutput

### tokenBalances
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.TokenBalance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTransactionEventsInput

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### transactionHash
- **Type**: typing.Optional[str]

### transactionId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTransactionEventsInputPaginate

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### transactionHash
- **Type**: typing.Optional[str]

### transactionId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.PaginatorConfig]


# ListTransactionEventsOutput

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.TransactionEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTransactionsInput

### address
- **Type**: <class 'str'>
- **Required**: Yes

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### fromBlockchainInstant
- **Type**: typing.Union[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstant, aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput, NoneType]

### toBlockchainInstant
- **Type**: typing.Union[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstant, aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput, NoneType]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ListTransactionsSort]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### confirmationStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ConfirmationStatusFilter]


# ListTransactionsInputPaginate

### address
- **Type**: <class 'str'>
- **Required**: Yes

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### fromBlockchainInstant
- **Type**: typing.Union[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstant, aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput, NoneType]

### toBlockchainInstant
- **Type**: typing.Union[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstant, aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput, NoneType]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ListTransactionsSort]

### confirmationStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ConfirmationStatusFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.PaginatorConfig]


# ListTransactionsOutput

### transactions
- **Type**: typing.List[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.TransactionOutputItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTransactionsSort

### sortBy
- **Type**: typing.Optional[typing.Literal['TRANSACTION_TIMESTAMP']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# OwnerFilter

### address
- **Type**: <class 'str'>
- **Required**: Yes


# OwnerIdentifier

### address
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# TimeFilter

### from_
- **Type**: typing.Union[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstant, aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput, NoneType]

### to
- **Type**: typing.Union[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstant, aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput, NoneType]


# TokenBalance

### balance
- **Type**: <class 'str'>
- **Required**: Yes

### atBlockchainInstant
- **Type**: <class 'aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput'>
- **Required**: Yes

### ownerIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.OwnerIdentifier]

### tokenIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.TokenIdentifier]

### lastUpdatedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput]


# TokenFilter

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### contractAddress
- **Type**: typing.Optional[str]

### tokenId
- **Type**: typing.Optional[str]


# TokenIdentifier

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### contractAddress
- **Type**: typing.Optional[str]

### tokenId
- **Type**: typing.Optional[str]


# Transaction

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### transactionHash
- **Type**: <class 'str'>
- **Required**: Yes

### transactionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### transactionIndex
- **Type**: <class 'int'>
- **Required**: Yes

### numberOfTransactions
- **Type**: <class 'int'>
- **Required**: Yes

### to
- **Type**: <class 'str'>
- **Required**: Yes

### blockHash
- **Type**: typing.Optional[str]

### blockNumber
- **Type**: typing.Optional[str]

### from_
- **Type**: typing.Optional[str]

### contractAddress
- **Type**: typing.Optional[str]

### gasUsed
- **Type**: typing.Optional[str]

### cumulativeGasUsed
- **Type**: typing.Optional[str]

### effectiveGasPrice
- **Type**: typing.Optional[str]

### signatureV
- **Type**: typing.Optional[int]

### signatureR
- **Type**: typing.Optional[str]

### signatureS
- **Type**: typing.Optional[str]

### transactionFee
- **Type**: typing.Optional[str]

### transactionId
- **Type**: typing.Optional[str]

### confirmationStatus
- **Type**: typing.Optional[typing.Literal['FINAL', 'NONFINAL']]

### executionStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCEEDED']]


# TransactionEvent

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### transactionHash
- **Type**: <class 'str'>
- **Required**: Yes

### eventType
- **Type**: typing.Literal['BITCOIN_VIN', 'BITCOIN_VOUT', 'ERC1155_TRANSFER', 'ERC20_BURN', 'ERC20_DEPOSIT', 'ERC20_MINT', 'ERC20_TRANSFER', 'ERC20_WITHDRAWAL', 'ERC721_TRANSFER', 'ETH_TRANSFER', 'INTERNAL_ETH_TRANSFER']
- **Required**: Yes

### from_
- **Type**: typing.Optional[str]

### to
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]

### contractAddress
- **Type**: typing.Optional[str]

### tokenId
- **Type**: typing.Optional[str]

### transactionId
- **Type**: typing.Optional[str]

### voutIndex
- **Type**: typing.Optional[int]

### voutSpent
- **Type**: typing.Optional[bool]

### spentVoutTransactionId
- **Type**: typing.Optional[str]

### spentVoutTransactionHash
- **Type**: typing.Optional[str]

### spentVoutIndex
- **Type**: typing.Optional[int]

### blockchainInstant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.managedblockchain_query.managedblockchain_query_classes.BlockchainInstantOutput]

### confirmationStatus
- **Type**: typing.Optional[typing.Literal['FINAL', 'NONFINAL']]


# TransactionOutputItem

### transactionHash
- **Type**: <class 'str'>
- **Required**: Yes

### network
- **Type**: typing.Literal['BITCOIN_MAINNET', 'BITCOIN_TESTNET', 'ETHEREUM_MAINNET', 'ETHEREUM_SEPOLIA_TESTNET']
- **Required**: Yes

### transactionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### transactionId
- **Type**: typing.Optional[str]

### confirmationStatus
- **Type**: typing.Optional[typing.Literal['FINAL', 'NONFINAL']]


# VoutFilter

### voutSpent
- **Type**: <class 'bool'>
- **Required**: Yes


