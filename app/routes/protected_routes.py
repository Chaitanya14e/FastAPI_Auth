from fastapi import APIRouter, Depends, HTTPException
from app.auth_dependency import get_current_user
from app.main import supabase

router = APIRouter(tags=["Protected"])


@router.get("/public/info")
def public_info():
    return {
        "message": "This is public information"
    }


@router.get("/protected/profile")
def profile(current_user=Depends(get_current_user)):

    user = current_user["user"]

    return {
        "id": user.id,
        "email": user.email,
        "created_at": user.created_at
    }


@router.get("/protected/dashboard")
def dashboard(current_user=Depends(get_current_user)):

    user = current_user["user"]

    return {
        "message": "Welcome to the protected dashboard",
        "user_id": user.id,
        "email": user.email
    }


@router.post("/auth/logout", status_code=204)
def logout(current_user=Depends(get_current_user)):

    token = current_user["token"]

    try:
        supabase.auth.sign_out()

        return None

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Logout failed"
        )