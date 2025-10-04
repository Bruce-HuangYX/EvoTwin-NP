# EvoTwin-NP: Dual-Loop Evolutionary Detection and Calibration under Neyman–Pearson Constraints

> **Dual-loop**: twin-generator inner loop + evolutionary outer loop; **NP constraints**: optimize recall under fixed false-positive budgets.  
> Covers **small drifts** to **significant anomalies**; exemplar domain: **indoor air environment** time series.

[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/Bruce-HuangYX/EvoTwin-NP/blob/main/LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0007--0674--5942-brightgreen)](https://orcid.org/0009-0007-0674-5942)
![Python](https://img.shields.io/badge/python-3.10%2B-informational)

## Highlights
- **Neyman–Pearson**: maximize detection power (recall) under fixed FPR (e.g., 0.5%/1%/5%) with threshold search & ECE calibration.
- **Dual-loop**: `G1` imputation-consistency; `G2` prototype-guided synthesis (Soft-DTW aware). Outer loop uses CMA-ES/NSGA-II.
- **Prototype-aware**: Soft-DTW clustering; coverage metrics (MMD/KID/coverage).
- **Robust evaluation**: PR-AUC, Recall@FPR≤α, ECE, latency; Friedman+Nemenyi & paired Wilcoxon tests.

## Repo Structure
```
EvoTwin-NP/
├─ src/evotwinnp/
│  ├─ __init__.py
│  ├─ cli.py
│  ├─ data.py
│  ├─ prototypes.py
│  ├─ models.py
│  ├─ losses.py
│  ├─ train.py
│  ├─ eval_np.py
│  ├─ evo_search.py
│  └─ utils.py
├─ src/scripts/
│  ├─ run_indoor_example.sh
│  └─ run_evo_search.sh
├─ examples/indoor_air/
│  ├─ README.md
│  ├─ config.yaml
│  └─ data/   (gitignored)
├─ docs/overview.md
├─ tests/test_sanity.py
├─ .github/workflows/ci.yml
├─ .gitattributes
├─ .gitignore
├─ LICENSE
├─ CITATION.cff
├─ pyproject.toml
├─ requirements.txt
└─ README.md
```

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .

# Show CLI
python -m evotwinnp.cli --help

# (Example) Train & evaluate with NP metrics
python -m evotwinnp.cli train --config examples/indoor_air/config.yaml
python -m evotwinnp.cli eval-np --config examples/indoor_air/config.yaml

# Evolutionary search
python -m evotwinnp.cli evo --config examples/indoor_air/config.yaml
```

## How to cite
```bibtex
@misc{EvoTwinNP2025,
  title        = {EvoTwin-NP: Dual-Loop Evolutionary Detection and Calibration under Neyman--Pearson Constraints},
  author       = {Huang, Yuxu},
  year         = {2025},
  howpublished = {GitHub repository},
  url          = {https://github.com/Bruce-HuangYX/EvoTwin-NP},
  note         = {ORCID: https://orcid.org/0009-0007-0674-5942}
}
```

---
*© 2025 Yuxu Huang. Initial public placeholder.*
