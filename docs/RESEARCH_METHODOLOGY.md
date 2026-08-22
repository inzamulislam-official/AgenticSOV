# Research Methodology

## Research Objective

AgenticSOV investigates how frequently a brand is mentioned and recommended by an LLM when users ask commercial, buyer-intent questions.

The objective is to convert unstructured AI-generated answers into measurable brand visibility signals.

---

## Core Research Question

> When a potential buyer asks an AI system which product or company they should choose, how often is a target brand recommended compared with its competitors?

---

## Input

Each experiment requires:

- One target brand
- A set of competitors
- Multiple buyer-intent prompts
- A locally hosted LLM

Example:

Brand:
HubSpot

Competitors:
- Salesforce
- Zoho
- Pipedrive

Buyer-intent prompt:

"What are the best CRM platforms for a growing B2B SaaS company?"

---

## Experiment Pipeline

The system follows the following process:

1. Generate buyer-intent prompts.
2. Submit each prompt to the local LLM through Ollama.
3. Store the generated response.
4. Analyze the response for brand mentions.
5. Determine whether each brand was recommended.
6. Classify the sentiment associated with each brand.
7. Aggregate recommendation counts.
8. Calculate Recommendation Share-of-Voice.
9. Export the results as JSON and CSV.

---

## Core Metrics

### Mention Rate

Measures how frequently a brand appears in generated answers.

### Recommendation Rate

Measures how frequently the LLM explicitly recommends a brand.

### Sentiment

Classifies the detected brand perception as:

- Positive
- Neutral
- Negative
- Unknown

### Recommendation Share-of-Voice

The primary MVP metric.

Formula:

Brand Recommendation SOV =

Brand Recommendations / Total Brand Recommendations × 100

---

## Example

If the experiment produces:

- HubSpot: 4 recommendations
- Salesforce: 3 recommendations
- Zoho: 2 recommendations
- Pipedrive: 1 recommendation

Total recommendations = 10.

Therefore:

- HubSpot = 40%
- Salesforce = 30%
- Zoho = 20%
- Pipedrive = 10%

---

## Controlled Experiment Principle

The same set of buyer-intent prompts should be used when comparing brands.

This reduces variation caused by different query sets and makes competitor comparisons more consistent.

---

## Current Model Environment

The MVP uses:

- Ollama
- Llama 3.1 8B
- Local inference
- No paid LLM APIs

This makes the experiment reproducible without requiring commercial API credentials.

---

## Interpretation

A higher Recommendation Share-of-Voice indicates that the evaluated model recommended the brand more frequently within the tested prompt set.

This should be interpreted as an experimental AI visibility signal rather than a universal ranking.

---

## Future Research

Future versions can evaluate:

- Multiple LLMs
- Multiple model temperatures
- Repeated trials
- Larger prompt datasets
- Semantic similarity
- RAG source attribution
- Citation frequency
- Cross-model AI visibility
- Historical visibility changes