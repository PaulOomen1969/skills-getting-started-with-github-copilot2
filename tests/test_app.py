from fastapi.testclient import TestClient

from src.app import app, activities


def test_unregister_participant_removes_email_from_activity():
    client = TestClient(app)
    original_participants = activities["Chess Club"]["participants"].copy()

    try:
        response = client.delete(
            "/activities/Chess Club/signup",
            params={"email": "michael@mergington.edu"},
        )

        assert response.status_code == 200
        assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]
    finally:
        activities["Chess Club"]["participants"] = original_participants
