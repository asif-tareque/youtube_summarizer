from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from .app import get_summary

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="YouTube Summarizer")

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": None,
            "error": None,
        },
    )


@app.post("/summarize", response_class=HTMLResponse)
async def summarize(
    request: Request,
    youtube_url: str = Form(...),
    mode: str = Form("brief"),
):
    try:
      
        result = get_summary(youtube_url)

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "result": result,
                "error": None,
                "youtube_url": youtube_url,
                "mode": mode,
            },
        )

    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "result": None,
                "error": str(e),
                "youtube_url": youtube_url,
                "mode": mode,
            },
        )