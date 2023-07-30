from fastapi import APIRouter, Depends, HTTPException
from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from global_vars import traceit

templates = Jinja2Templates(directory="templates")
router = APIRouter(
    prefix="/operation-room",
    tags=["operation-room"],
    responses={404: {"description": "Not found"}},
)

""" Note to self: let the user create a new storage or add an item to storage from here """

# This will be the route that creates a new storage
@router.post("/{room_name}/create-storage/{storage_name}")
def create_storage(room_name: str, storage_name: str):
    new_storage= traceit.add_storage(room_name, storage_name)
    return new_storage

# This will be the route that deletes a new storage
@router.delete("/{room_name}/delete-storage/{storage_name}")
def create_storage(room_name: str, storage_name: str):
    new_storage= traceit.delete_storage(room_name, storage_name)
    return new_storage

@router.post("/{room_name}/{storage_name}/create-item/{item_name}")
def add_item(room_name: str, storage_name:str, item_name: str):
    new_item= traceit.add_item(room_name, storage_name, item_name)
    return new_item

@router.delete("/{room_name}/{storage_name}/delete-item/{item_name}")
def delete_item(room_name: str, storage_name:str, item_name: str):
    del_item = traceit.del_item(room_name, storage_name, item_name)
    return del_item


