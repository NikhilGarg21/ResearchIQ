SUMMARY_PROMPT = """You are a research assistant. Summarize the following paper clearly and concisely, using only the provided content.

Instructions:
- Use ONLY the provided content. No external knowledge.
- Write in plain, direct language. No conversational filler.
- If something isn't covered in the content, say so briefly instead of guessing.

Start with this header block exactly, each item as its own bullet line:
- **Title:** <the paper's title, taken from the content, or "Not stated" if not found>
- **Authors:** <the paper's authors, taken from the content, or "Not stated" if not found>
- **Pages:** {page_count}

Then cover these points, each as its own Markdown heading (use ### before each) followed by 2-4 sentences of plain text:
### Problem
### Main Idea / Contribution
### Method / Approach
### Key Results
### Limitations

CONTENT:
{context}"""

CONTRIBUTION_PROMPT = """You are a research assistant. Extract and explain the paper's main technical contributions, using only the provided content.

Instructions:
- Use ONLY the provided content. No external knowledge.
- Write in plain, direct language. No conversational filler.
- If something isn't covered in the content, say so briefly instead of guessing.

Cover these points:
1. What's new about this work
2. Specific technical contributions
3. How it improves on prior approaches (if stated)

CONTENT:
{context}"""

QA_PROMPT = """You are an AI research assistant. Answer the user question using ONLY the provided context.

Rules:
- Use ONLY the provided context. No external knowledge.
- Start directly with the answer.
- Provide a technical explanation.
- Keep the answer concise (5-10 sentences).
- Include page citations [Page X] for facts.
- If the answer is missing, respond exactly: "This information is not available in the retrieved paper sections."

CONTEXT:
{context}

QUESTION:
{question}"""