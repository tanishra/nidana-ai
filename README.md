# Nidana AI

**Nidana AI** is a production-grade clinical decision support system (CDSS) for **symptom-based disease inference**, built using structured medical knowledge, rule-based reasoning, safe machine learning, and the OpenAI API.

The system is designed to **assist clinicians**, not replace them, by providing **explainable, conservative, and safety-first diagnostic support** based on patient-reported symptoms and clinical context.

---

## What Nidana AI Does

Nidana AI takes free-text clinical input such as:

- Symptoms  
- Patient history  
- Duration and severity  

and produces:

- A **ranked list of possible conditions**
- **Clinically realistic confidence scores**
- **Doctor-style explanations**
- **Emergency (red-flag) alerts** when applicable
- **Follow-up guidance** when information is insufficient

All outputs are **non-diagnostic** and meant strictly for clinical support.

---

## How to Run ?

Follow these steps to run Nidana AI locally.

### 1. Clone the repository
```bash
git clone https://github.com/tanishra/nidana-ai.git
cd nidana-ai
```

### 2. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a .env file in the project root and add:
```bash
OPENAI_API_KEY=your_openai_api_key
```

### 5. Run the clinical testing UI
```bash
cd frontend
npm run dev
```
---

## Core Design Principles

- **Safety first** – emergency red flags always override inference  
- **Explainability** – every suggestion is accompanied by reasoning  
- **Clinical realism** – conservative confidence, no over-diagnosis  
- **Human-in-the-loop** – doctors provide feedback that improves the system  
- **Modular architecture** – easy to extend, audit, and maintain  


---

## Medical Knowledge Base

- Diseases are encoded as **structured JSON files**
- Each disease includes:
  - Common symptoms
  - Key (discriminative) symptoms
  - Red-flag warning signs
  - Risk factors
  - Exclusion clues
- Knowledge is derived from:
  - Standard medical textbooks
  - Clinical guidelines
  - Public health references

This ensures the system remains **auditable and transparent**.

---

## Inference & Confidence Logic

- **Rules are authoritative** — ML never overrides clinical logic  
- Confidence is computed using:
  - Symptom coverage
  - Presence of key symptoms
  - Risk factors
- Minimum-evidence rules prevent overconfidence  
- Single non-specific symptoms (e.g. fever alone) always result in **low confidence**

This mirrors real clinical reasoning.

---

## Machine Learning (Assistive Only)

- ML is used **only for ranking refinement**
- Trained **offline** using doctor feedback
- No automatic or real-time retraining
- Bounded influence to prevent unsafe behavior

The model learns patterns such as:
- Overconfidence cases
- Ranking inconsistencies
- Missed conditions

---

## Doctor-in-the-Loop Learning

Doctors can provide feedback directly via the UI, including:

- Ranking quality (good / acceptable / poor)
- Accepted condition
- Missed condition
- Overconfidence / underconfidence flags
- Clinical notes

This feedback is:
- Stored locally
- Used for evaluation
- Used to retrain the ML ranker offline

---

## Evaluation & Calibration

The system includes internal evaluation tools to track:

- Top-3 acceptance rate
- Overconfidence rate
- Underconfidence rate
- Ranking quality trends
- Confidence calibration vs doctor judgment

These metrics guide **safe, incremental improvement**.

---

## What Nidana AI Is Not

- ❌ Not a diagnostic tool  
- ❌ Not patient-facing  
- ❌ Not an automated decision maker  

It is a **clinical decision support system** meant to assist qualified healthcare professionals.

---

## Current Scope

- 20+ common diseases encoded
- Symptom-based inference
- Emergency red-flag detection
- Explainable outputs
- Feedback-driven learning loop

Medication recommendation is **intentionally out of scope** at this stage.

---

## Future Roadmap (High Level)

- Expand disease coverage by clinical category
- Improve follow-up question intelligence
- Refine confidence calibration with feedback
- Introduce guideline-based treatment suggestions (later phase)

---

## Disclaimer

Nidana AI does **not provide medical diagnosis or treatment advice**.  
All outputs are for **clinical decision support only** and must be interpreted by a qualified healthcare professional.

## Contributing
Contributions are welcome and encouraged.

How to contribute

- Fork the repository
- Create a new branch for your feature or fix
- Make your changes with clear commits
- Open a pull request with a short description