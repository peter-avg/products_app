import uvicorn
from app.api import app


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)


if __name__ == "__main__":
    main()
