# AI Candidate Ranking System

## Overview

This project ranks candidates for a Retrieval, Search, Recommendation, and Machine Learning Engineering role using a hybrid scoring system that combines:

- Feature Engineering
- Semantic Similarity
- Career Relevance Analysis
- Behavioral Signals
- Rule-Based Filtering

The system processes large candidate datasets and generates a ranked list of candidates based on overall suitability for the target role.

---

## Problem Statement

Given:

- Candidate profiles
- Career history
- Skills
- Behavioral signals
- Job description

Rank candidates according to their relevance for a Retrieval/Search/Recommendation Engineering position.

---

## Solution Architecture

Candidate Data
↓
Feature Extraction
↓
Semantic Matching
↓
Career Matching
↓
Score Aggregation
↓
Ranking
↓
Submission CSV

---

## Features Used

### Experience Score

Rewards candidates with:

- 5–9 years experience (highest score)
- 3–5 years experience
- 9–12 years experience

---

### Skill Score

Matches candidate skills against:

- Retrieval
- Ranking
- Search
- Recommendation
- Embeddings
- Vector Databases
- LLM
- NDCG
- MRR
- Pinecone
- Qdrant
- Milvus
- Weaviate
- Elasticsearch
- OpenSearch

---

### Career Score

Measures keyword relevance across the candidate's complete career history.

---

### Title Score

Rewards titles such as:

- AI Engineer
- Machine Learning Engineer
- ML Engineer
- Applied Scientist
- Search Engineer
- Ranking Engineer
- Recommendation Systems Engineer
- Data Scientist

---

### Title Relevance

Additional binary relevance signal based on AI/Search/ML-related titles.

---

### Behavioral Score

Uses:

- Open To Work status
- Recruiter Response Rate
- GitHub Activity
- Profile Completeness
- Interview Completion Rate

---

## Semantic Matching

The system uses:

Model:
all-MiniLM-L6-v2

to compute semantic similarity between:

Job Description ↔ Candidate Profile

using cosine similarity.

---

## Career Semantic Matching

Candidate career history is converted into embeddings and compared against a retrieval/search-focused query containing concepts such as:

- Search Systems
- Recommendation Systems
- Ranking
- Retrieval
- Semantic Search
- Embeddings
- Vector Databases
- LLM Ranking

---

## Final Scoring Formula

Final Score =

0.20 × Career Score +
0.15 × Career Semantic Score +
0.20 × Behavior Score +
0.15 × Title Score +
0.10 × Skill Score +
0.10 × Experience Score +
0.10 × Semantic Score

---

## Filtering Logic

Candidates with unrelated titles receive penalties.

```python
if title_relevance == 0:
    score *= 0.5
```

Candidates with weak retrieval/search background receive additional penalties.

```python
if career_score + career_semantic_score < 0.15:
    score *= 0.4
```

## Performance Optimizations

Implemented optimizations:

- Cached JD Embedding
- Cached Career Query Embedding
- Batch Candidate Embeddings
- Batch Career Embeddings
- Single-pass Scoring

These optimizations significantly reduce runtime when processing 100,000 candidates.

---

## Project Structure

```text
resume-ranking-system/
│
├── data/
│   ├── candidates.jsonl
│   └── job_description.txt
│
├── src/
│   ├── candidate_text.py
│   ├── career_match.py
│   ├── export_results.py
│   ├── feature_engineering.py
│   ├── load_data.py
│   ├── model_loader.py
│   ├── ranker.py
│   ├── reasoning.py
│   ├── scorer.py
│   └── semantic_ranker.py
│
├── submission.csv
├── requirements.txt
├── README.md
└── main.py
```

## Running

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

Output:

```text
submission.csv
```

containing:

- candidate_id
- rank
- score
- reasoning

---

## Future Improvements

- Cross Encoder Re-ranking
- Learning-to-Rank Models
- XGBoost Ranking
- LightGBM Ranking
- LLM-Based Explanations
- Online Feedback Learning

---

## Author

Hamza Shaikh