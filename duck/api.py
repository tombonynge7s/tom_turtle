from typing import Annotated, Union
from fastapi import FastAPI, File, UploadFile
from starlette.responses import FileResponse

import quack

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/")
# async def read_index():
#     return FileResponse("site/index.html")


@app.post("/uploadgpx")
async def create_file(file: Annotated[bytes, File()]):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file), file: file}
    return quack.bounding_box(file)


@app.get("/geojson")
async def get_geojson():
    return quack.get_geojson("/home/dave/git/wahrzeichen/data/germany_1.gpx")


# @app.post("/uploadgpx")
# async def create_file(file: UploadFile):
#     if not file:
#         return {"message": "No file sent"}
#     else:
#         return {"path": file.file, "file": file}
