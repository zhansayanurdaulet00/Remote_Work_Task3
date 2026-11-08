# Remote Work, Boundary Blurring, and Burnout

## Project Overview
This project investigates the relationship between remote work intensity, boundary blurring, work-life balance, schedule autonomy, psychological detachment, and employee burnout.

## Research Objectives
- Examine the relationship between remote work intensity and burnout.
- Investigate boundary blurring and burnout.
- Analyze work-life balance and schedule autonomy.
- Explore psychological detachment.
- Develop a statistical model of burnout.

## Dataset Description
The study uses survey data. The analytical dataset contains 34 observations.

Main variables:
- Remote Work Intensity
- Boundary Blurring
- Burnout Score
- Work-Life Balance
- Schedule Autonomy
- Psychological Detachment
- Work Arrangement

## Data Processing
The data processing stage included:
- Missing value inspection
- Duplicate response checking
- Validation of numerical values
- Survey response conversion
- Composite score calculation

## Statistical Analysis
The following methods were applied:
- Mean, median, and standard deviation
- Percentiles
- Spearman correlation
- Multiple linear regression
- Moderation analysis
- Statistical significance testing

### Main Results
Boundary blurring showed a positive statistically significant association with burnout in the regression model:

- Coefficient: 0.843
- P-value: 0.00497

Remote work intensity did not show a statistically significant association with burnout in the correlation analysis.

## Scientific Visualization


### Figure 1. Remote Work Intensity vs Burnout

![Figure 1](figures/fig1_remote_intensity_vs_burnout.png)

### Figure 2. Burnout Distribution by Work Arrangement

![Figure 2](figures/fig2_burnout_by_arrangement.png)

## Domain Model
The conceptual model and statistical outputs are available in the `domain_model_outputs/` directory.

## Project Structure
- `data/` — survey datasets
- `domain_model_outputs/` — domain model and statistical outputs
- `figures/` — scientific visualizations
- `notebooks/` — Jupyter Notebook
- `src/` — Python modules

## How to Run

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels jupyter
```

Run data processing:

```bash
python src/process_data.py
```

Generate figures:

```bash
python src/visualize.py
```

Open the notebook:

```bash
jupyter notebook
```

## Conclusion
The results indicate that boundary blurring is positively associated with burnout. The findings should be interpreted cautiously because of the relatively small sample size.

## Tools
Python, Pandas, NumPy, Matplotlib, Seaborn, SciPy, Statsmodels, Jupyter Notebook, GitHub.
