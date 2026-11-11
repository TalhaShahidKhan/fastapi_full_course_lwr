from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def create_user():
    return {"message": "Create User"}


@router.get("/")
async def read_users():
    return {"message": "Read Users"}


@router.get("/{user_id}")
async def read_user():
    return {"message": "Read User"}


@router.put("/{user_id}")
async def update_user():
    return {"message": "Update User"}


@router.delete("/{user_id}")
async def delete_user():
    return {"message": "Delete User"}


@router.put("/update-profile")
async def update_profile():
    return {"message": "Update Profile"}