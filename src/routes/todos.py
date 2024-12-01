from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from lesson2.src.database.db import get_db


router = APIRouter(prefix='/todos', tags=['todos'])

@router.get("/")
async def get_todos():
    ...


@router.get("/{todo_id}")
async def get_todo():
   ...


@router.post("/")
async def create_todo():
    ...


@router.put("/{todo_id}")
async def update_todo():
    ...


@router.delete("/{todo_id}")
async def delete_todo():
    ...