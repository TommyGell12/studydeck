# StudyDeck Plan

## Purpose
Help me study technology and prepare for certifications, starting with
Code Platoon's AI Cloud & DevOps Engineering course and the AWS
Certified Solutions Architect – Associate certification.

## Flashcard contents
- Topic: AWS or Code Platoon
- Front: a terminology question, coding question, or command task
- Back: the explanation, code snippet, or command, including what it does

## First version
Fetch a small set of cards, display a question, and reveal its answer.

## GET /api/cards — Input, Processing, Output

Input:
- course: aws or codeplatoon
- limit: a whole number of cards to retrieve

Processing:
1. Validate the course and limit.
2. If limit < 1, return HTTP 400 with:
   "Please request at least 1 card."
3. Select cards belonging to the requested course.
4. Take up to limit cards; if fewer exist, return those available.

Output:
- HTTP 200 with a JSON list of matching cards.
- Each card has a topic, front, and back.

Browser behavior:
- Show one card at a time.
- Allow repeated flips between front and back.
- Move to the next card without fetching the same set again.

Future feature:
- Support requesting all cards for a course.

FUNCTION cards(course, limit)
    IF course is not recognized
        RETURN 400, "Select a valid course"

    IF limit is not a whole number OR limit < 1
        RETURN 400, "Request a positive whole number of cards"

    GET all cards belonging to course
    CREATE an empty results list

    FOR EACH card in the course's cards
        IF results already contains limit cards
            STOP the loop
        ADD card to results

    RETURN 200, results as JSON

## Tool readiness — November 6, 2026

- Project folder: /home/tommy/installfest-lab/studydeck
- Environment: WSL Ubuntu with VS Code
- VS Code: 1.140.0
- Python: 3.14.4
- Node.js: v22.22.1
- npm: 9.2.0
- Git: 2.53.0
- GitHub CLI: 2.46.0, authenticated as TommyGell12
- Docker CLI and engine: 26.0.0
- Docker Compose: v2.26.1-desktop.1

### Checks completed

- Docker engine responds without sudo after adding my user to
  the docker group and restarting WSL.
- GitHub repository created and main pushed successfully.
- Remote upstream configured; main tracks upstream/main.
- The deck alias opens the project folder.
- The gs alias runs git status.

### Repository

https://github.com/TommyGell12/studydeck