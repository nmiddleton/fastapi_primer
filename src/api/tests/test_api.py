import pytest

from services import openweather_service

def test_weatherapi(test_app, monkeypatch):
    # Mock the real call to openweather with some set data response
    test_data = {
        "feels_like": 20.94,
        "humidity": 60,
        "pressure": 1014,
        "temp"    : 21.2,
        "temp_max": 21.67,
        "temp_min": 21
        }
    # create a function to replace the actual call to the open weather API
    async def mock_get_openWeather(city, state, country, units):
        return test_data
    # Use pytest monkeypatch to replace the function in memory so that our mock is called instead of get_report_async
    monkeypatch.setattr(openweather_service, "get_report_async", mock_get_openWeather)

    # Pass our API to the fixture in conftest that will run up the server for us
    response = test_app.get("/api/weather/London")
    assert response.status_code == 200
    assert response.json() == test_data


