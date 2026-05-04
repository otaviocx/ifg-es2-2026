from tempo import get_temperature, parse_temperatures
import pytest

@pytest.fixture
def data_fixture():
    return {
        'temperature_2m': [25.5, 26.0, 24.8],
        'time': ['2024-06-01T00:00', '2024-06-01T01:00', '2024-06-01T02:00']
    }

@pytest.fixture
def coordenadas():
    latitude = -16.665873
    longitude = -49.2573415
    return latitude, longitude

def test_get_temperature(coordenadas):
    latitude, longitude = coordenadas

    data = get_temperature(latitude, longitude)
    assert 'temperature_2m' in data
    assert 'time' in data
    assert len(data['temperature_2m']) == len(data['time'])


def test_parse_temperatures(mocker, coordenadas):
    mock_get_temperature = mocker.patch('tempo.get_temperature')
    mock_get_temperature.return_value = {
        'temperature_2m': [25.5, 26.0, 24.8],
        'time': ['2024-06-01T00:00', '2024-06-01T01:00', '2024-06-01T02:00']
    }

    latitude, longitude = coordenadas
    df = parse_temperatures(latitude, longitude)
    assert len(df) == 3
    assert df['Temperature'][0] == '25.50°C'
    assert df['Temperature'][1] == '26.00°C'
    assert df['Temperature'][2] == '24.80°C'

def test_parse_times(mocker, coordenadas):
    mock_get_temperature = mocker.patch('tempo.get_temperature')
    mock_get_temperature.return_value = {
        'temperature_2m': [25.5, 26.0, 24.8],
        'time': ['2024-06-01T00:00', '2024-06-01T01:00', '2024-06-01T02:00']
    }

    latitude, longitude = coordenadas
    df = parse_temperatures(latitude, longitude)
    assert len(df) == 3
    assert df['Time'][0] == '2024-06-01T00:00'
    assert df['Time'][1] == '2024-06-01T01:00'
    assert df['Time'][2] == '2024-06-01T02:00'

