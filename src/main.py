import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from config import configure_api_keys
from api import weather_api
from services import openweather_service
from web.views import home

api = fastapi.FastAPI()


def configure():
    configure_routing()
    openweather_service.api_key = configure_api_keys.get()


def configure_routing():
    api.mount('/static', StaticFiles(directory='web/static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)


if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='0.0.0.0')
else:
    configure()
