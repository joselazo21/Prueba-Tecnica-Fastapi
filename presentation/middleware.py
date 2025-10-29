from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import time

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        
        print(f"Request processed in {process_time} seconds")
        response.headers["X-Process-Time"] = str(process_time)
        
        return response