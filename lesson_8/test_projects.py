from dotenv import load_dotenv
import os
import pytest
import requests
import uuid

base_url = "https://ru.yougile.com/api-v2/projects/"

load_dotenv()

api_key = os.getenv('API_key')
company_id = os.getenv('companyID')


@pytest.fixture
def headers():
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }


@pytest.fixture
def project_id(headers):
    # Создание проекта для тестов GET и PUT
    project = {
        "title": "ДЗ 4 в Postman",
        "users": {
            "0850e032-1491-4909-969d-949e427e2246": "admin"
        }
    }
    response = requests.post(base_url, json=project, headers=headers)
    project_id = response.json().get("id")
    yield project_id


def test_create_project_positive(headers):
    # headers = {
    #     "Authorization": f"Bearer {api_key}",
    #     "Content-Type": "application/json"
    # }
    project = {
        "title": "ДЗ в Postman",
        "users": {
            "0850e032-1491-4909-969d-949e427e2246": "admin"
        }
    }
    response = requests.post(base_url, json=project, headers=headers)
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative_no_title(headers):
    project = {
            "users": {
                "0850e032-1491-4909-969d-949e427e2246": "admin"
            }
            }
    response = requests.post(base_url, json=project, headers=headers)
    # Ожидаем ошибку 400, так как title обязателен
    assert response.status_code == 400


def test_get_project_positive(headers, project_id):
    # headers = {
    #     "Authorization": f"Bearer {api_key}",
    #     "Content-Type": "application/json"
    # }
    response = requests.get(base_url + str(project_id), headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative_invalid_id(headers):
    invalid_id = str(uuid.uuid4())
    response = requests.get(f"{base_url}/{invalid_id}", headers=headers)
    assert response.status_code == 404


def test_update_project_positive(headers, project_id):
    new_title = "Updated Title"
    project = {"title": new_title}
    response = requests.put(
        base_url + str(project_id), json=project, headers=headers)
    assert response.status_code == 200

    get_resp = requests.get(
        base_url + str(project_id), headers=headers)
    assert get_resp.json()["title"] == new_title


def test_update_project_negative_empty_body(headers, project_id):
    response = requests.put(
        base_url + str(project_id), headers=headers)
    assert response.status_code == 200
