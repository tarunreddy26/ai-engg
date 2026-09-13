# My AI Engineer Journey — Master Outline

**Context for Claude:** I'm following this plan to go from Python basics + no work experience to having real, job-ready AI engineering skills. If this is a new chat, please read this whole outline and pick up from wherever I say I currently am, without re-explaining things I've already covered.

## My starting point
- Programming basics in Python. No professional work experience.
- Goal: build real AI engineering skills and eventually get a tech job.

## Overall strategy
- Based on the roadmap.sh "AI Engineer" roadmap, but learned **project-first**: build real things and learn concepts exactly when I need them, not by reading the whole roadmap up front.
- Build-in-public on **GitHub** (code + READMEs) and **X/Twitter** (short write-ups/threads). Not using LinkedIn.
- Learning loop for every project:
  1. Start from a real problem, not a tutorial
  2. Build the ugly end-to-end version fast
  3. Debug by reading primary docs, not just googling fixes
  4. Refactor in one production concern (error handling, logging, basic evals)
  5. Write a short 300–600 word write-up (what it does, why, how it works, what broke, what's next)
  6. Ship it publicly on GitHub with a real README
  7. Repeat with a harder project
  8. Get outside feedback (Discord/Reddit/X replies), contribute small PRs to tools I use

## The ~6-month roadmap phases
1. **Weeks 1–2:** Python for API work (venv, requests, JSON, .env, error handling)
2. **Weeks 3–4:** LLM APIs & prompting (Chat Completions/Messages API, temperature, tokens, system prompts) → CLI chatbot with conversation history
3. **Weeks 5–6:** Structured outputs & function/tool calling → agent that calls 2–3 real tools
4. **Weeks 7–9:** Embeddings & vector databases (Chroma/Qdrant) → semantic search over my own docs
5. **Weeks 10–13:** Full RAG app (raw SDK, then LangChain or LlamaIndex) with a simple UI (Streamlit/Flask)
6. **Weeks 14–16:** AI agents (ReAct-style, multi-step tool use) → end-to-end multi-step task agent
7. **Weeks 17–18:** Evaluation, safety, and production basics (evals, prompt injection guards, retries, cost logging) — applied back onto earlier projects
8. **Weeks 19–24:** Polish 3+ projects, contribute to open source, start applying to junior/AI-adjacent roles and freelance gigs *while still building*

## End goal (~6 months, adjustable to pace)
3–5 real, working AI projects of increasing difficulty (single API call → tool-using agent → full RAG app → multi-step agent), each on GitHub with a genuine README, plus a visible public trail on X showing the building/learning process — not just "finished the roadmap," but demonstrated ability to build and explain real things.

## Progress log (update this section as I go)
- [x] Week 1, Day 1: Set up Python venv, installed deps, got API key, wrote `.env` + `.gitignore`, wrote first script making one API call

- [x] Week 1, Day 2:Switched to Ollama after hitting OpenAi billing wall and committed code to GitHub.

- [x] Week 1, Day 3: Built a CLI chatbot with conversation memory using Ollama3.2 and committed. 

- [x] Week 1, Day 4: Added Persona to the chat and also got to know how to write some pseudo code hands-on.

- [] Week 1, Day 5: 

- [ ] Week 2: ...
- [ ] (continue logging each milestone here)

---
*Instructions for continuing in a new chat: paste this whole file, tell Claude which checkbox you're currently on, and ask for the next concrete step (keep it small — e.g. "give me a 45-minute task").*
