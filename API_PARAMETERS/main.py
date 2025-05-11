from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

# ---------- PATH PARAMETER EXAMPLE ----------

@app.get("items/{item_id}")
async def get_item(
    item_id: int = Path(..., ge=1)
):
    return {item_id: item_id}


# ---------- QUERY PARAMETERS EXAMPLE ----------

@app.get("/items")
async def get_items(
    q: str | None = Query(
        None,
        min_length=3,
        max_length=50,
    ),

    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100)
):
    return {
        "q": q,
        "skip": skip,
        "limit": limit
    }
# ---------- MIXED: PATH + QUERY + BODY ----------

@app.put("/iteems/validated/{item_id}")

async def update_item(
    item_id: int = Path(..., ge=1),
    q:str | None = Query(
        None,
        min_length=3,
    
    ),

    item: Item | None = Body(None, 
        description="Item to be updated",
    )
):
    

    result = {"item_id" : item_id}

    if q:
        result["q"] = q

    if item:
        result["item"] = item.model_dump()
    return result