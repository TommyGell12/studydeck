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