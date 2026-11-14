from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

CARDS = [
    {
        "course": "aws",
        "topic": "S3",
        "front": "How do you list your S3 buckets from the CLI?",
        "back": "aws s3 ls --profile tommy-study",
    },
    {
        "course": "aws",
        "topic": "SNS + SQS",
        "front": "How do you fan out messages so a consumer that's offline still gets them?",
        "back": "SNS topic -> one SQS queue per consumer. SNS pushes, SQS holds messages until they're polled.",
    },
    {
        "course": "aws",
        "topic": "ALB",
        "front": "Which load balancer can route by URL path?",
        "back": "Application Load Balancer (Layer 7). NLB is Layer 4, for static IPs and extreme performance.",
    },
    {
        "course": "codeplatoon",
        "topic": "Docker",
        "front": "How do you list running containers?",
        "back": "docker ps (add -a to include stopped ones)",
    },
    {
        "course": "codeplatoon",
        "topic": "Git",
        "front": "How do you push a new branch to your fork?",
        "back": "git push -u upstream <branch>",
    },
]

@app.get("/api/cards")
def cards(course: Optional[str] = None, limit: int = 5):
    if not course:
        raise HTTPException(status_code=400, detail="Please specify a course.")
    courses = sorted({card["course"] for card in CARDS})
    if course not in courses:
        raise HTTPException(
        status_code=404,
        detail=f"Unknown course: {course}. Available courses: {', '.join(courses)}",
    )
    if (limit < 1 ):
        raise HTTPException(status_code=400, detail="Please request at least 1 card.")
    filtered_cards = [card for card in CARDS if card["course"] == course]
    cards_to_return = []

    for card in filtered_cards[:limit]:
        cards_to_return.append({
            "topic": card["topic"],
            "front": card["front"],
            "back": card["back"]
        })
    return cards_to_return