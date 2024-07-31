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
from aws_resource_validator.pydantic_models.managedblockchain_query_constants import *

class AddressIdentifierFilterTypeDef(BaseModel):
    transactionEventToAddress: Sequence[str]

class ContractIdentifierTypeDef(BaseModel):
    network: QueryNetworkType
    contractAddress: str

class OwnerIdentifierTypeDef(BaseModel):
    address: str

class TokenIdentifierTypeDef(BaseModel):
    network: QueryNetworkType
    contractAddress: Optional[str] = None
    tokenId: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ConfirmationStatusFilterTypeDef(BaseModel):
    include: Sequence[ConfirmationStatusType]

class ContractFilterTypeDef(BaseModel):
    network: QueryNetworkType
    tokenStandard: QueryTokenStandardType
    deployerAddress: str

class ContractMetadataTypeDef(BaseModel):
    name: Optional[str] = None
    symbol: Optional[str] = None
    decimals: Optional[int] = None

class GetTransactionInputRequestTypeDef(BaseModel):
    network: QueryNetworkType
    transactionHash: Optional[str] = None
    transactionId: Optional[str] = None

class TransactionTypeDef(BaseModel):
    network: QueryNetworkType
    transactionHash: str
    transactionTimestamp: datetime
    transactionIndex: int
    numberOfTransactions: int
    to: str
    blockHash: Optional[str] = None
    blockNumber: Optional[str] = None
    from: Optional[str] = None
    contractAddress: Optional[str] = None
    gasUsed: Optional[str] = None
    cumulativeGasUsed: Optional[str] = None
    effectiveGasPrice: Optional[str] = None
    signatureV: Optional[int] = None
    signatureR: Optional[str] = None
    signatureS: Optional[str] = None
    transactionFee: Optional[str] = None
    transactionId: Optional[str] = None
    confirmationStatus: Optional[ConfirmationStatusType] = None
    executionStatus: Optional[ExecutionStatusType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListFilteredTransactionEventsSortTypeDef(BaseModel):
    sortBy: Optional[Literal["blockchainInstant"]] = None
    sortOrder: Optional[SortOrderType] = None

class VoutFilterTypeDef(BaseModel):
    voutSpent: bool

class OwnerFilterTypeDef(BaseModel):
    address: str

class TokenFilterTypeDef(BaseModel):
    network: QueryNetworkType
    contractAddress: Optional[str] = None
    tokenId: Optional[str] = None

class ListTransactionEventsInputRequestTypeDef(BaseModel):
    network: QueryNetworkType
    transactionHash: Optional[str] = None
    transactionId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTransactionsSortTypeDef(BaseModel):
    sortBy: Optional[Literal["TRANSACTION_TIMESTAMP"]] = None
    sortOrder: Optional[SortOrderType] = None

class TransactionOutputItemTypeDef(BaseModel):
    transactionHash: str
    network: QueryNetworkType
    transactionTimestamp: datetime
    transactionId: Optional[str] = None
    confirmationStatus: Optional[ConfirmationStatusType] = None

class AssetContractTypeDef(BaseModel):
    contractIdentifier: ContractIdentifierTypeDef
    tokenStandard: QueryTokenStandardType
    deployerAddress: str

class GetAssetContractInputRequestTypeDef(BaseModel):
    contractIdentifier: ContractIdentifierTypeDef

class BlockchainInstantTypeDef(BaseModel):
    time: Optional[TimestampTypeDef] = None

class ListAssetContractsInputRequestTypeDef(BaseModel):
    contractFilter: ContractFilterTypeDef
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetAssetContractOutputTypeDef(BaseModel):
    contractIdentifier: ContractIdentifierTypeDef
    tokenStandard: QueryTokenStandardType
    deployerAddress: str
    metadata: ContractMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransactionOutputTypeDef(BaseModel):
    transaction: TransactionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetContractsInputListAssetContractsPaginateTypeDef(BaseModel):
    contractFilter: ContractFilterTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTransactionEventsInputListTransactionEventsPaginateTypeDef(BaseModel):
    network: QueryNetworkType
    transactionHash: Optional[str] = None
    transactionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTokenBalancesInputListTokenBalancesPaginateTypeDef(BaseModel):
    tokenFilter: TokenFilterTypeDef
    ownerFilter: Optional[OwnerFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTokenBalancesInputRequestTypeDef(BaseModel):
    tokenFilter: TokenFilterTypeDef
    ownerFilter: Optional[OwnerFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTransactionsOutputTypeDef(BaseModel):
    transactions: List[TransactionOutputItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetContractsOutputTypeDef(BaseModel):
    contracts: List[AssetContractTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetTokenBalanceErrorItemTypeDef(BaseModel):
    errorCode: str
    errorMessage: str
    errorType: ErrorTypeType
    tokenIdentifier: Optional[TokenIdentifierTypeDef] = None
    ownerIdentifier: Optional[OwnerIdentifierTypeDef] = None
    atBlockchainInstant: Optional[BlockchainInstantTypeDef] = None

class BatchGetTokenBalanceInputItemTypeDef(BaseModel):
    tokenIdentifier: TokenIdentifierTypeDef
    ownerIdentifier: OwnerIdentifierTypeDef
    atBlockchainInstant: Optional[BlockchainInstantTypeDef] = None

class BatchGetTokenBalanceOutputItemTypeDef(BaseModel):
    balance: str
    atBlockchainInstant: BlockchainInstantTypeDef
    ownerIdentifier: Optional[OwnerIdentifierTypeDef] = None
    tokenIdentifier: Optional[TokenIdentifierTypeDef] = None
    lastUpdatedTime: Optional[BlockchainInstantTypeDef] = None

class GetTokenBalanceInputRequestTypeDef(BaseModel):
    tokenIdentifier: TokenIdentifierTypeDef
    ownerIdentifier: OwnerIdentifierTypeDef
    atBlockchainInstant: Optional[BlockchainInstantTypeDef] = None

class GetTokenBalanceOutputTypeDef(BaseModel):
    ownerIdentifier: OwnerIdentifierTypeDef
    tokenIdentifier: TokenIdentifierTypeDef
    balance: str
    atBlockchainInstant: BlockchainInstantTypeDef
    lastUpdatedTime: BlockchainInstantTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTransactionsInputListTransactionsPaginateTypeDef(BaseModel):
    address: str
    network: QueryNetworkType
    fromBlockchainInstant: Optional[BlockchainInstantTypeDef] = None
    toBlockchainInstant: Optional[BlockchainInstantTypeDef] = None
    sort: Optional[ListTransactionsSortTypeDef] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTransactionsInputRequestTypeDef(BaseModel):
    address: str
    network: QueryNetworkType
    fromBlockchainInstant: Optional[BlockchainInstantTypeDef] = None
    toBlockchainInstant: Optional[BlockchainInstantTypeDef] = None
    sort: Optional[ListTransactionsSortTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilterTypeDef] = None

class TimeFilterTypeDef(BaseModel):
    from: Optional[BlockchainInstantTypeDef] = None
    to: Optional[BlockchainInstantTypeDef] = None

class TokenBalanceTypeDef(BaseModel):
    balance: str
    atBlockchainInstant: BlockchainInstantTypeDef
    ownerIdentifier: Optional[OwnerIdentifierTypeDef] = None
    tokenIdentifier: Optional[TokenIdentifierTypeDef] = None
    lastUpdatedTime: Optional[BlockchainInstantTypeDef] = None

class TransactionEventTypeDef(BaseModel):
    network: QueryNetworkType
    transactionHash: str
    eventType: QueryTransactionEventTypeType
    from: Optional[str] = None
    to: Optional[str] = None
    value: Optional[str] = None
    contractAddress: Optional[str] = None
    tokenId: Optional[str] = None
    transactionId: Optional[str] = None
    voutIndex: Optional[int] = None
    voutSpent: Optional[bool] = None
    spentVoutTransactionId: Optional[str] = None
    spentVoutTransactionHash: Optional[str] = None
    spentVoutIndex: Optional[int] = None
    blockchainInstant: Optional[BlockchainInstantTypeDef] = None
    confirmationStatus: Optional[ConfirmationStatusType] = None

class BatchGetTokenBalanceInputRequestTypeDef(BaseModel):
    getTokenBalanceInputs: Optional[Sequence[BatchGetTokenBalanceInputItemTypeDef]] = None

class BatchGetTokenBalanceOutputTypeDef(BaseModel):
    tokenBalances: List[BatchGetTokenBalanceOutputItemTypeDef]
    errors: List[BatchGetTokenBalanceErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFilteredTransactionEventsInputListFilteredTransactionEventsPaginateTypeDef(BaseModel):
    network: str
    addressIdentifierFilter: AddressIdentifierFilterTypeDef
    timeFilter: Optional[TimeFilterTypeDef] = None
    voutFilter: Optional[VoutFilterTypeDef] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilterTypeDef] = None
    sort: Optional[ListFilteredTransactionEventsSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFilteredTransactionEventsInputRequestTypeDef(BaseModel):
    network: str
    addressIdentifierFilter: AddressIdentifierFilterTypeDef
    timeFilter: Optional[TimeFilterTypeDef] = None
    voutFilter: Optional[VoutFilterTypeDef] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilterTypeDef] = None
    sort: Optional[ListFilteredTransactionEventsSortTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTokenBalancesOutputTypeDef(BaseModel):
    tokenBalances: List[TokenBalanceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFilteredTransactionEventsOutputTypeDef(BaseModel):
    events: List[TransactionEventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTransactionEventsOutputTypeDef(BaseModel):
    events: List[TransactionEventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

