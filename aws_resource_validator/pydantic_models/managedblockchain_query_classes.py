from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class AddressIdentifierFilterTypeDef(BaseValidatorModel):
    transactionEventToAddress: Sequence[str]

class ContractIdentifierTypeDef(BaseValidatorModel):
    network: QueryNetworkType
    contractAddress: str

class OwnerIdentifierTypeDef(BaseValidatorModel):
    address: str

class TokenIdentifierTypeDef(BaseValidatorModel):
    network: QueryNetworkType
    contractAddress: Optional[str] = None
    tokenId: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ConfirmationStatusFilterTypeDef(BaseValidatorModel):
    include: Sequence[ConfirmationStatusType]

class ContractFilterTypeDef(BaseValidatorModel):
    network: QueryNetworkType
    tokenStandard: QueryTokenStandardType
    deployerAddress: str

class ContractMetadataTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    symbol: Optional[str] = None
    decimals: Optional[int] = None

class GetTransactionInputRequestTypeDef(BaseValidatorModel):
    network: QueryNetworkType
    transactionHash: Optional[str] = None
    transactionId: Optional[str] = None

class TransactionTypeDef(BaseValidatorModel):
    network: QueryNetworkType
    transactionHash: str
    transactionTimestamp: datetime
    transactionIndex: int
    numberOfTransactions: int
    to: str
    blockHash: Optional[str] = None
    blockNumber: Optional[str] = None
    _from: Optional[str] = None
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

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListFilteredTransactionEventsSortTypeDef(BaseValidatorModel):
    sortBy: Optional[Literal["blockchainInstant"]] = None
    sortOrder: Optional[SortOrderType] = None

class VoutFilterTypeDef(BaseValidatorModel):
    voutSpent: bool

class OwnerFilterTypeDef(BaseValidatorModel):
    address: str

class TokenFilterTypeDef(BaseValidatorModel):
    network: QueryNetworkType
    contractAddress: Optional[str] = None
    tokenId: Optional[str] = None

class ListTransactionEventsInputRequestTypeDef(BaseValidatorModel):
    network: QueryNetworkType
    transactionHash: Optional[str] = None
    transactionId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTransactionsSortTypeDef(BaseValidatorModel):
    sortBy: Optional[Literal["TRANSACTION_TIMESTAMP"]] = None
    sortOrder: Optional[SortOrderType] = None

class TransactionOutputItemTypeDef(BaseValidatorModel):
    transactionHash: str
    network: QueryNetworkType
    transactionTimestamp: datetime
    transactionId: Optional[str] = None
    confirmationStatus: Optional[ConfirmationStatusType] = None

class AssetContractTypeDef(BaseValidatorModel):
    contractIdentifier: ContractIdentifierTypeDef
    tokenStandard: QueryTokenStandardType
    deployerAddress: str

class GetAssetContractInputRequestTypeDef(BaseValidatorModel):
    contractIdentifier: ContractIdentifierTypeDef

class BlockchainInstantTypeDef(BaseValidatorModel):
    time: Optional[TimestampTypeDef] = None

class ListAssetContractsInputRequestTypeDef(BaseValidatorModel):
    contractFilter: ContractFilterTypeDef
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetAssetContractOutputTypeDef(BaseValidatorModel):
    contractIdentifier: ContractIdentifierTypeDef
    tokenStandard: QueryTokenStandardType
    deployerAddress: str
    metadata: ContractMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransactionOutputTypeDef(BaseValidatorModel):
    transaction: TransactionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetContractsInputListAssetContractsPaginateTypeDef(BaseValidatorModel):
    contractFilter: ContractFilterTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTransactionEventsInputListTransactionEventsPaginateTypeDef(BaseValidatorModel):
    network: QueryNetworkType
    transactionHash: Optional[str] = None
    transactionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTokenBalancesInputListTokenBalancesPaginateTypeDef(BaseValidatorModel):
    tokenFilter: TokenFilterTypeDef
    ownerFilter: Optional[OwnerFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTokenBalancesInputRequestTypeDef(BaseValidatorModel):
    tokenFilter: TokenFilterTypeDef
    ownerFilter: Optional[OwnerFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTransactionsOutputTypeDef(BaseValidatorModel):
    transactions: List[TransactionOutputItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetContractsOutputTypeDef(BaseValidatorModel):
    contracts: List[AssetContractTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetTokenBalanceErrorItemTypeDef(BaseValidatorModel):
    errorCode: str
    errorMessage: str
    errorType: ErrorTypeType
    tokenIdentifier: Optional[TokenIdentifierTypeDef] = None
    ownerIdentifier: Optional[OwnerIdentifierTypeDef] = None
    atBlockchainInstant: Optional[BlockchainInstantTypeDef] = None

class BatchGetTokenBalanceInputItemTypeDef(BaseValidatorModel):
    tokenIdentifier: TokenIdentifierTypeDef
    ownerIdentifier: OwnerIdentifierTypeDef
    atBlockchainInstant: Optional[BlockchainInstantTypeDef] = None

class BatchGetTokenBalanceOutputItemTypeDef(BaseValidatorModel):
    balance: str
    atBlockchainInstant: BlockchainInstantTypeDef
    ownerIdentifier: Optional[OwnerIdentifierTypeDef] = None
    tokenIdentifier: Optional[TokenIdentifierTypeDef] = None
    lastUpdatedTime: Optional[BlockchainInstantTypeDef] = None

class GetTokenBalanceInputRequestTypeDef(BaseValidatorModel):
    tokenIdentifier: TokenIdentifierTypeDef
    ownerIdentifier: OwnerIdentifierTypeDef
    atBlockchainInstant: Optional[BlockchainInstantTypeDef] = None

class GetTokenBalanceOutputTypeDef(BaseValidatorModel):
    ownerIdentifier: OwnerIdentifierTypeDef
    tokenIdentifier: TokenIdentifierTypeDef
    balance: str
    atBlockchainInstant: BlockchainInstantTypeDef
    lastUpdatedTime: BlockchainInstantTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTransactionsInputListTransactionsPaginateTypeDef(BaseValidatorModel):
    address: str
    network: QueryNetworkType
    fromBlockchainInstant: Optional[BlockchainInstantTypeDef] = None
    toBlockchainInstant: Optional[BlockchainInstantTypeDef] = None
    sort: Optional[ListTransactionsSortTypeDef] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTransactionsInputRequestTypeDef(BaseValidatorModel):
    address: str
    network: QueryNetworkType
    fromBlockchainInstant: Optional[BlockchainInstantTypeDef] = None
    toBlockchainInstant: Optional[BlockchainInstantTypeDef] = None
    sort: Optional[ListTransactionsSortTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilterTypeDef] = None

class TimeFilterTypeDef(BaseValidatorModel):
    _from: Optional[BlockchainInstantTypeDef] = None
    to: Optional[BlockchainInstantTypeDef] = None

class TokenBalanceTypeDef(BaseValidatorModel):
    balance: str
    atBlockchainInstant: BlockchainInstantTypeDef
    ownerIdentifier: Optional[OwnerIdentifierTypeDef] = None
    tokenIdentifier: Optional[TokenIdentifierTypeDef] = None
    lastUpdatedTime: Optional[BlockchainInstantTypeDef] = None

class TransactionEventTypeDef(BaseValidatorModel):
    network: QueryNetworkType
    transactionHash: str
    eventType: QueryTransactionEventTypeType
    _from: Optional[str] = None
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

class BatchGetTokenBalanceInputRequestTypeDef(BaseValidatorModel):
    getTokenBalanceInputs: Optional[Sequence[BatchGetTokenBalanceInputItemTypeDef]] = None

class BatchGetTokenBalanceOutputTypeDef(BaseValidatorModel):
    tokenBalances: List[BatchGetTokenBalanceOutputItemTypeDef]
    errors: List[BatchGetTokenBalanceErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFilteredTransactionEventsInputListFilteredTransactionEventsPaginateTypeDef(BaseValidatorModel):
    network: str
    addressIdentifierFilter: AddressIdentifierFilterTypeDef
    timeFilter: Optional[TimeFilterTypeDef] = None
    voutFilter: Optional[VoutFilterTypeDef] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilterTypeDef] = None
    sort: Optional[ListFilteredTransactionEventsSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFilteredTransactionEventsInputRequestTypeDef(BaseValidatorModel):
    network: str
    addressIdentifierFilter: AddressIdentifierFilterTypeDef
    timeFilter: Optional[TimeFilterTypeDef] = None
    voutFilter: Optional[VoutFilterTypeDef] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilterTypeDef] = None
    sort: Optional[ListFilteredTransactionEventsSortTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTokenBalancesOutputTypeDef(BaseValidatorModel):
    tokenBalances: List[TokenBalanceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFilteredTransactionEventsOutputTypeDef(BaseValidatorModel):
    events: List[TransactionEventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTransactionEventsOutputTypeDef(BaseValidatorModel):
    events: List[TransactionEventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

