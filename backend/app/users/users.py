from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()
USERS = {}


class AvailabilitySlot(BaseModel):
    day: str
    start: int
    end: int


class Preferences(BaseModel):
    preferred_time_of_day: str
    avoided_days: List[str]
    max_duration: int
    flexibility: str


class UserProfile(BaseModel):
    slack_id: str
    availability: List[AvailabilitySlot]
    preferences: Preferences


@router.post("/profile")
def save_profile(profile: UserProfile):
    USERS[profile.slack_id] = profile.dict()
    return {"status": "saved"}


@router.get("/profile/{slack_id}")
def get_profile(slack_id: str):
    if slack_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return USERS[slack_id]
