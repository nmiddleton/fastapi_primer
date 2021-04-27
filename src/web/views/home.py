import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

templates = Jinja2Templates('web/templates')
router = fastapi.APIRouter()


@router.get('/')
def index(request: Request):
    return templates.TemplateResponse('home/index.html', {'request': request})


@router.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/web/static/img/favicon.ico')
