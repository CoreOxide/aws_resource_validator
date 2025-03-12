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
from aws_resource_validator.pydantic_models.managedblockchain_query_constants import *

class AddressIdentifierFilterTypeDef(BaseValidatorModel):
    transactionEventToAddress: Sequence[str]


class ContractIdentifierTypeDef(BaseValidatorModel):
    network: QueryNetworkType
    contractAddress: str


class BlockchainInstantOutputTypeDef(BaseValidatorModel):
    time: Optional[datetime] = None


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


class GetTransactionInputTypeDef(BaseValidatorModel):
    network: QueryNetworkType
    transactionHash: Optional[str] = None
    transactionId: Optional[str] = None


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


class ListTransactionEventsInputTypeDef(BaseValidatorModel):
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


class GetAssetContractInputTypeDef(BaseValidatorModel):
    contractIdentifier: ContractIdentifierTypeDef


class BatchGetTokenBalanceErrorItemTypeDef(BaseValidatorModel):
    errorCode: str
    errorMessage: str
    errorType: ErrorTypeType
    tokenIdentifier: Optional[TokenIdentifierTypeDef] = None
    ownerIdentifier: Optional[OwnerIdentifierTypeDef] = None
    atBlockchainInstant: Optional[BlockchainInstantOutputTypeDef] = None


class BatchGetTokenBalanceOutputItemTypeDef(BaseValidatorModel):
    balance: str
    atBlockchainInstant: BlockchainInstantOutputTypeDef
    ownerIdentifier: Optional[OwnerIdentifierTypeDef] = None
    tokenIdentifier: Optional[TokenIdentifierTypeDef] = None
    lastUpdatedTime: Optional[BlockchainInstantOutputTypeDef] = None


class TokenBalanceTypeDef(BaseValidatorModel):
    balance: str
    atBlockchainInstant: BlockchainInstantOutputTypeDef
    ownerIdentifier: Optional[OwnerIdentifierTypeDef] = None
    tokenIdentifier: Optional[TokenIdentifierTypeDef] = None
    lastUpdatedTime: Optional[BlockchainInstantOutputTypeDef] = None


class GetTokenBalanceOutputTypeDef(BaseValidatorModel):
    ownerIdentifier: OwnerIdentifierTypeDef
    tokenIdentifier: TokenIdentifierTypeDef
    balance: str
    atBlockchainInstant: BlockchainInstantOutputTypeDef
    lastUpdatedTime: BlockchainInstantOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class BlockchainInstantTypeDef(BaseValidatorModel):
    time: Optional[TimestampTypeDef] = None


class ListAssetContractsInputTypeDef(BaseValidatorModel):
    contractFilter: ContractFilterTypeDef
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetAssetContractOutputTypeDef(BaseValidatorModel):
    contractIdentifier: ContractIdentifierTypeDef
    tokenStandard: QueryTokenStandardType
    deployerAddress: str
    metadata: ContractMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TransactionTypeDef(BaseValidatorModel):
    pass


class GetTransactionOutputTypeDef(BaseValidatorModel):
    transaction: TransactionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAssetContractsInputPaginateTypeDef(BaseValidatorModel):
    contractFilter: ContractFilterTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTransactionEventsInputPaginateTypeDef(BaseValidatorModel):
    network: QueryNetworkType
    transactionHash: Optional[str] = None
    transactionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTokenBalancesInputPaginateTypeDef(BaseValidatorModel):
    tokenFilter: TokenFilterTypeDef
    ownerFilter: Optional[OwnerFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTokenBalancesInputTypeDef(BaseValidatorModel):
    tokenFilter: TokenFilterTypeDef
    ownerFilter: Optional[OwnerFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTransactionsOutputTypeDef(BaseValidatorModel):
    transactions: List[TransactionOutputItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAssetContractsOutputTypeDef(BaseValidatorModel):
    contracts: List[AssetContractTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TransactionEventTypeDef(BaseValidatorModel):
    pass


class ListFilteredTransactionEventsOutputTypeDef(BaseValidatorModel):
    events: List[TransactionEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTransactionEventsOutputTypeDef(BaseValidatorModel):
    events: List[TransactionEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchGetTokenBalanceOutputTypeDef(BaseValidatorModel):
    tokenBalances: List[BatchGetTokenBalanceOutputItemTypeDef]
    errors: List[BatchGetTokenBalanceErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListTokenBalancesOutputTypeDef(BaseValidatorModel):
    tokenBalances: List[TokenBalanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BlockchainInstantUnionTypeDef(BaseValidatorModel):
    pass


class BatchGetTokenBalanceInputItemTypeDef(BaseValidatorModel):
    tokenIdentifier: TokenIdentifierTypeDef
    ownerIdentifier: OwnerIdentifierTypeDef
    atBlockchainInstant: Optional[BlockchainInstantUnionTypeDef] = None


class GetTokenBalanceInputTypeDef(BaseValidatorModel):
    tokenIdentifier: TokenIdentifierTypeDef
    ownerIdentifier: OwnerIdentifierTypeDef
    atBlockchainInstant: Optional[BlockchainInstantUnionTypeDef] = None


class ListTransactionsInputPaginateTypeDef(BaseValidatorModel):
    address: str
    network: QueryNetworkType
    fromBlockchainInstant: Optional[BlockchainInstantUnionTypeDef] = None
    toBlockchainInstant: Optional[BlockchainInstantUnionTypeDef] = None
    sort: Optional[ListTransactionsSortTypeDef] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTransactionsInputTypeDef(BaseValidatorModel):
    address: str
    network: QueryNetworkType
    fromBlockchainInstant: Optional[BlockchainInstantUnionTypeDef] = None
    toBlockchainInstant: Optional[BlockchainInstantUnionTypeDef] = None
    sort: Optional[ListTransactionsSortTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilterTypeDef] = None


class BatchGetTokenBalanceInputTypeDef(BaseValidatorModel):
    getTokenBalanceInputs: Optional[Sequence[BatchGetTokenBalanceInputItemTypeDef]] = None


class TimeFilterTypeDef(BaseValidatorModel):
    pass


class ListFilteredTransactionEventsInputPaginateTypeDef(BaseValidatorModel):
    network: str
    addressIdentifierFilter: AddressIdentifierFilterTypeDef
    timeFilter: Optional[TimeFilterTypeDef] = None
    voutFilter: Optional[VoutFilterTypeDef] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilterTypeDef] = None
    sort: Optional[ListFilteredTransactionEventsSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFilteredTransactionEventsInputTypeDef(BaseValidatorModel):
    network: str
    addressIdentifierFilter: AddressIdentifierFilterTypeDef
    timeFilter: Optional[TimeFilterTypeDef] = None
    voutFilter: Optional[VoutFilterTypeDef] = None
    confirmationStatusFilter: Optional[ConfirmationStatusFilterTypeDef] = None
    sort: Optional[ListFilteredTransactionEventsSortTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


