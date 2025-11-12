# 10 Academy Week 0 - Solar Challenge

## Project Overview
Complete solar data analysis for Benin, Sierra Leone, and Togo to identify optimal solar investment locations for MoonLight Energy Solutions.

## Key Findings
- **Best Country**: Benin (242.0 W/m² average GHI)
- **Statistical Significance**: p < 0.001
- **Recommendation**: Invest in Benin for solar farm development

## Project Structure
- `notebooks/benin_analysis.ipynb` - Complete EDA and statistical analysis
- `data/` - Compressed cleaned datasets (ZIP format due to GitHub file size limits)
- `screenshots/` - Analysis visualizations and results
- `.github/workflows/ci.yml` - CI/CD pipeline

## Data Notes
- Cleaned datasets are provided as compressed ZIP files due to GitHub's 25MB file size limits
- Each ZIP file contains the corresponding cleaned CSV data for analysis
- Extract the files to reproduce the complete analysis

## How to Reproduce
```bash
git clone https://github.com/mycodebook123/10Academy-week0-solar-challenge.git
cd 10Academy-week0-solar-challenge
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
