from fastapi.responses import JSONResponse

def success_response(data):
    """
    Return a success response in the API with the given data.
    """
    return JSONResponse(content={"response": data})