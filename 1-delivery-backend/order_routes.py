from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["Orders"])

# routes
@order_router.get("/")
async def get_orders():
    '''
    This endpoint returns a list of orders
    1. GET /orders
    '''
    return {"message": "List of orders"}