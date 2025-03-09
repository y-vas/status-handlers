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

    response = request.app.state.limiter._inject_headers(
        response, request.state.view_rate_limit
    )
    return response
