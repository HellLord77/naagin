from pathlib import Path

from starlette.templating import Jinja2Templates

TemplateResponse = Jinja2Templates(Path(__file__).parent.parent / "templates").TemplateResponse
