from fastapi import APIRouter, Header, HTTPException
from app.main import supabase

router = APIRouter(tags=["Protected"])


@router.get("/public/info")
def public_info():
    return {
        "message": "This is public information"
    }


@router.get("/protected/profile")
def profile(authorization: str | None = Header(default=None)):

    print("AUTH HEADER:", authorization)

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Access token required"
        )

    # rest of your code...

    # Check Bearer format
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Access token required"
        )

    token = authorization.split(" ", 1)[1]

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Access token required"
        )

    # Verify token with Supabase
    try:
        response = supabase.auth.get_user(token)

        if response.user is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid or expired token"
            )

        user = response.user

        return {
            "id": user.id,
            "email": user.email,
            "created_at": user.created_at
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )