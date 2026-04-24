# FastAPI: The framework we will use to build the web server. 
    # It is currently the industry standard for Python ML APIs because it is blisteringly fast.
# Uvicorn: The actual "server" engine that will run your FastAPI code and listen for internet traffic.
# Pydantic: A data validation tool. If a bank accidentally sends text (like "one thousand") 
    # instead of a number for the transaction amount, Pydantic will catch the error and stop the API from crashing.