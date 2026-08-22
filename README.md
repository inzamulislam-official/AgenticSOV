# AgenticSOV

AgenticSOV measures how AI language models recommend, mention, compare, or omit brands when answering commercial buyer-intent questions [3].

## The Core Problem
Traditional SEO tools measure visibility in search engines [3]. They do not answer a new and increasingly important question: 
"When a buyer asks an AI system which product they should choose, does the AI recommend my brand or my competitor?" [3]

This creates a visibility gap between traditional search performance and AI-generated product discovery [3].

## The Solution
AgenticSOV programmatically submits controlled buyer-intent queries to a locally hosted LLM through Ollama [7]. It analyzes the generated responses to determine:
* Brand mentions [7]
* Brand recommendations [7]
* Sentiment [7]
* Competitor recommendations [7]
* Recommendation Share-of-Voice [7]

### Example output
* **HubSpot**: 40% [7]
* **Salesforce**: 30% [7]
* **Zoho**: 20% [7]
* **Pipedrive**: 10% [7]

---

## Current Architecture
* Python [5]
* FastAPI [5]
* Ollama [5]
* Pandas [5]
* Scikit-learn [5]

---

## Important MVP Limitations (Phase 22)
* **Local Evaluation Only**: This MVP measures LLM recommendation behavior using a locally hosted open-weight model under controlled buyer-intent prompts [1]. 
* **Not Commercial Ranking**: The results obtained using Ollama do not represent the actual real-time rankings of commercial AI systems such as ChatGPT, Gemini, Claude, or Perplexity [1, 5]. It is designed as a controlled research and measurement environment that can later support multiple model providers [5].

---

## Roadmap & Next Layers (Phase 23)
Once the core engine is stable, we plan to evolve the MVP with the following features [2, 8]:
1. **React Dashboard**: A visual frontend containing metrics like Recommendation SOV, Mention Rate, Positive/Negative Sentiment, and Omission Rate [2].
2. **Multi-model Evaluation**: Supporting cross-model SOV aggregate scores (Model A + Model B + Model C) [1, 5].
3. **Advanced AI Metrics**:
   * Historical benchmarks [5]
   * RAG/source analysis [5]
   * Semantic brand positioning [5]
   * Automated GEO (Generative Engine Optimization) recommendations [5, 9]
   * AI-agent procurement visibility [5]