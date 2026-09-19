from fastapi import APIRouter, Header, HTTPException

router = APIRouter(tags=["Protected"])


@router.get("/public/info")
def public_info():
    return {
        "message": "This is public information"
    }


@router.get("/protected/profile")
def profile(authorization: str | None = Header(default=None)):

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Access token required"
        )

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

    return {
        "message": "Token received",
        "token": token
    }