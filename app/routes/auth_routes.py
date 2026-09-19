from fastapi import APIRouter, HTTPException, status
from app.main import supabase
from app.schemas import AuthRequest

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(data: AuthRequest):

    try:
        response = supabase.auth.sign_up({
            "email": data.email,
            "password": data.password
        })

        if response.user is None:
            raise HTTPException(
                status_code=400,
                detail="Signup failed"
            )

        return {
            "message": "Signup successful",
            "user": {
                "id": response.user.id,
                "email": response.user.email
            }
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/login")
def login(data: AuthRequest):

    try:
        response = supabase.auth.sign_in_with_password({
            "email": data.email,
            "password": data.password
        })

        if response.session is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid login credentials"
            )

        return {
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token,
            "token_type": "bearer"
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid login credentials"
        )