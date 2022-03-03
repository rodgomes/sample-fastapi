### Sample API to test an ArgoCD deployment

To install the dependencies for this project you need [poetry](https://python-poetry.org/) installed. 

Then run:
`poetry install`

**You can start the server with the command:**
`uvicorn --app-dir=src main:app --reload` 

**Build docker image**
`docker build --no-cache -t sample-fastapi:0.0.1 .`

**Run the API in docker**
`docker run -p 8000:8000 -it sample-fastapi:0.0.1`