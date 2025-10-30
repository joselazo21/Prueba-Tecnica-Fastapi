from fastapi import HTTPException

def check_permission(user_id, post_owner_id):
    if user_id != post_owner_id:
        raise HTTPException(status_code=403, detail="You do not have permission to perform this action, you must be the owner of the post.")