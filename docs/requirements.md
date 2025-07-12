### Functional Requirements
- The user must be able to upload a resume (PDF).
- The user must be able to paste or upload a job description.
- The system must extract and compare keywords from both documents.
- The system must check for grammar errors.
- The system must display missing skills or keywords.
- The system must score the match percentage (resume feedback).

Functional requirements are also represented in a [use-case diagram](../docs/AI_resume_analyzer_use_cases.pdf).

### Non-Functional Requirements
- The app must load results in < 5 seconds for most resumes.
- The UI must work on mobile and desktop browsers.
- The backend must handle file sizes up to 5MB.
- The system should provide feedback in clear, natural language.

### Assumptions
- Users will upload resumes in English.
- Users will provide resumes in PDF format only.

### Constraints
- NLP is limited to basic keyword and grammar checks.
- Only one resume and one job description per session.