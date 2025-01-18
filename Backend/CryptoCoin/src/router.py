from fastapi import APIRouter

from src.init import cmc_client

router = APIRouter(
    prefix="/cryptocurrencies"
)

@router.get("")
async def get_cryptocurrencies():
    return await cmc_client.get_listings()

@router.get("/{currencies_id}")
async def get_cryptocurrency(currencies_id:  int):
    return await cmc_client.get_currency(currencies_id)
