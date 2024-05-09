from fastapi import FastAPI
from fastapi import Query

from typing import Annotated

app = FastAPI()

ITEMS = [
  {"name": "Foo"},
  {"name": "Bar"},
  {"name": "Baz"}
]

"""
@app.get("/items")
async def read_items(q: str | None = None):
  response = {"items": ITEMS}

  if q:
    response.update({"q": q})

  return response
"""

# Additional validation
"""
@app.get("/items")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
  response = {"items": ITEMS}

  if q:
    response.update({"q": q})

  return response
"""

# Add Query to Annotated in the q parameter
"""
@app.get("/items")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50)] = None):
  response = {"items": ITEMS}

  if q:
    response.update({"q": q})

  return response
"""

# Add regular expressions
"""
@app.get("/items")
async def read_items(q: Annotated[str | None, Query(min_length = 3, max_length = 50, regexp = "^fixedquery$")] = None):
  response = {"items": ITEMS}

  if q:
    response.update({"q": q})

  return response
"""

# Default values
"""
@app.get("/items")
async def read_items(q: Annotated[str | None, Query(min_length = 3)] = "fixedquery"):
  response = {"items": ITEMS}

  if q:
    response.update({"q": q})

  return response
"""

# Make it required
"""
@app.get("/items")
async def read_items(q: Annotated[str, Query(min_length = 3)]):
  response = {"items": ITEMS}

  if q:
    response.update({"q": q})

  return response
"""

# Required with Ellipsis (...)
"""
@app.get("/items")
async def read_items(q: Annotated[str, Query(min_length = 3)] = ...):
  response = {"items": ITEMS}

  if q:
    response.update({"q": q})

  return response
"""

# Required with None
"""
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3)] = ...):
  response = {"items": ITEMS}

  if q:
    response.update({"q": q})

  return response
"""

# Query parameter list / multiple values
"""
@app.get("/items")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
  response = {"items": ITEMS}

  if q:
    response.update({"q": q})

  return response
"""

# Query parameter list / multiple values with defaults¶
"""
@app.get("/items")
async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
  response = {"items": ITEMS}

  if q:
    response.update({"q": q})

  return response
"""

# Declare more metadata
"""
@app.get("/items")
async def read_items(
  q: Annotated[
    str | None,
    Query(
      title = "Query string",
      description = "Query string for the items to search in the database that have a good match",
      min_length = 3
    )
  ] = None):
  response = {"items": ITEMS}

  if q:
    response.update({"q": q})

  return response
"""

# Alias parameters
"""
@app.get("/items")
async def read_items(q: Annotated[str | None, Query(alias = "item-query")] = None):
  response = {"items": ITEMS}

  if q:
    response.update({"q": q})

  return response
"""

# Deprecating parameters
@app.get("/items")
async def read_items(
  q: Annotated[
    str | None,
    Query(
      min_length = 3,
      max_length = 50,
      pattern = "^fixedquery$",
      alias = "item-query",
      title = "Query strong",
      description = "Query string for the items to search in the database that have a good match",
      deprecated = True
    )
  ] = None
):
  response = {"items": ITEMS}

  if q:
    response.update({"q": q})

  return response
