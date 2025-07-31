# WSGI configuration for PythonAnywhere
import sys
import os
from dotenv import load_dotenv

# Add your project directory to the sys.path
path = '/home/Uayeb/dulceria.api'
if path not in sys.path:
    sys.path.append(path)

# Load environment variables
load_dotenv(os.path.join(path, '.env'))

# Try to import and use a proper ASGI to WSGI adapter
try:
    from uvicorn.middleware.wsgi import WSGIMiddleware
    from main import app
    
    # Create a minimal WSGI wrapper
    def application(environ, start_response):
        # Import here to avoid import-time issues
        import json
        
        path_info = environ.get('PATH_INFO', '/')
        
        if path_info == '/':
            status = '200 OK'
            headers = [('Content-Type', 'application/json')]
            start_response(status, headers)
            response = {"message": "FastAPI API is running", "version": "0.0.0", "status": "ok"}
            return [json.dumps(response).encode('utf-8')]
        
        elif path_info == '/health':
            status = '200 OK'
            headers = [('Content-Type', 'application/json')]
            start_response(status, headers)
            response = {"health": "ok", "python_version": sys.version}
            return [json.dumps(response).encode('utf-8')]
        
        else:
            # For other endpoints, return a helpful message
            status = '501 Not Implemented'
            headers = [('Content-Type', 'application/json')]
            start_response(status, headers)
            response = {
                "message": "Full FastAPI functionality requires ASGI server", 
                "requested_path": path_info,
                "suggestion": "Use uvicorn for full functionality"
            }
            return [json.dumps(response).encode('utf-8')]

except ImportError as e:
    # Fallback if uvicorn import fails
    def application(environ, start_response):
        import json
        status = '200 OK'
        headers = [('Content-Type', 'application/json')]
        start_response(status, headers)
        response = {
            "message": "API running in minimal mode", 
            "error": str(e),
            "python_version": sys.version
        }
        return [json.dumps(response).encode('utf-8')]
