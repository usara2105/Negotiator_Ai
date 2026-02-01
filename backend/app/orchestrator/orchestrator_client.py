import os
import requests

WATSONX_API_KEY = os.getenv("WATSONX_API_KEY")

ORCHESTRATE_URL = "https://api.us-south.watsonx.ibm.com/orchestrate/decide"


class OrchestratorClient:
    """
    watsonx Orchestrate client
    """

    def decide_meeting(self, context: dict) -> dict:
        if not WATSONX_API_KEY:
            return {"decision": "FALLBACK", "reason": "missing_api_key"}

        headers = {
            "Authorization": f"Bearer {WATSONX_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "intent": "schedule_meeting",
            "context": context
        }

        try:
            response = requests.post(
                ORCHESTRATE_URL,
                headers=headers,
                json=payload,
                timeout=10
            )
        except requests.RequestException:
            return {"decision": "FALLBACK", "reason": "network_error"}

        if response.status_code != 200:
            return {"decision": "FALLBACK", "reason": "orchestrate_unavailable"}

        return response.json()
