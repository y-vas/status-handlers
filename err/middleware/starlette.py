from err.base import HTTPException

class Request:
    pass
class JSONResponse:
    pass
class Response:
    pass

try:
    import starlette
    from starlette.requests import Request
    from starlette.responses import JSONResponse, Response
except ImportError:
    print('Starlette is not installed, exeptions may not work')


# Usage
# app.add_exception_handler(
#     err.base.HTTPException,
#     err.middleware.starlette.middleware
# )

def middleware(request: Request, exc: HTTPException) -> Response:
    """
    Build a simple JSON response that includes the details of the exeptions
    """
    response = JSONResponse(
        {
            "detail": exc.detail
        },
        status_code=exc.status_code
    )

    return response
