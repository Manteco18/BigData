# tr_1: Population Evolution Data Analysis

**Project Context**: Educational data analysis practice (Práctica 1.1 — Probabilidad y Estadística) analyzing global population trends using United Nations demographic data from Our World in Data.

## Quick Start

- **Main Notebook**: [notebooks/01_evolucion_poblacional.ipynb](notebooks/01_evolucion_poblacional.ipynb) - Population evolution analysis
- **Data Sources**: 
  - `data/raw/annual-population-growth/` - Annual population changes (1951-2023, projected to 2100)
  - `data/raw/births-and-deaths-projected-to-2100/` - Birth and death statistics
- **Output**: `data/processed/` - Processed analysis results
- **Utilities**: `src/` - Reusable Python modules (currently empty, add analysis utilities here)

## Data Structure & Conventions

### Data Organization
Each raw dataset follows this structure:
```
data/raw/{dataset-name}/
├── {dataset-name}.csv          # Main data file
├── {dataset-name}.metadata.json # Detailed metadata with citation info
└── readme.md                     # Dataset description and sources
```

### Data Attribution (IMPORTANT)
All datasets come from **UN World Population Prospects (2024)** processed by **Our World in Data**. When using data:

1. **Always include proper citations** - See metadata.json for complete citations
2. **In-line citation format**: `UN, World Population Prospects (2024) – processed by Our World in Data`
3. **Full citation includes**: UN WPP original source, OWID processing, specific indicator ID
4. **Important note**: Population change is *net* (births + deaths + migration), not just natural growth

### CSV Structure
- **Column 1**: Entity (country/region name)
- **Column 2**: Code (ISO alpha-3 or custom code)
- **Column 3**: Year (annual data)
- **Remaining columns**: Time series data (varies by dataset)

## Analysis Workflow

### When Working on Notebooks
1. Load CSV data using pandas: `pd.read_csv("data/raw/{dataset}/{dataset}.csv")`
2. Store processed data in `data/processed/` (create subdirectories as needed)
3. Add markdown cells for analysis questions and key findings
4. Reference data sources with proper citations from metadata.json

### Common Analysis Tasks
- **Data Exploration**: Check shape, dtypes, missing values, entity count
- **Time Series**: Handle annual data spanning 70+ years with projections to 2100
- **Multi-entity**: Compare trends across countries and regions
- **Forecast Context**: Distinguish between historical estimates (1951-2023) and UN medium scenario projections (2024-2100)

## Dependencies & Environment

### Python Libraries
- `pandas` - Data manipulation and CSV loading
- `numpy` - Numerical operations
- `jupyter` - Interactive notebook environment

Set up environment: Create `.venv/` with standard data analysis stack (pandas, numpy, matplotlib, jupyter recommended).

## Project Structure Notes

- **Spanish-language context**: Comments, questions, and documentation are in Spanish
- **Educational focus**: Notebooks are structured with questions to answer and analysis to perform
- **Data-centric**: Emphasis on understanding data sources and proper attribution
- **Evolving codebase**: `src/` directory available for utility functions as analysis grows

## Common Pitfalls to Avoid

1. **Citation**: Don't forget to attribute data sources in analysis output
2. **Path handling**: Use relative paths from project root (`data/raw/...`, not absolute paths)
3. **Projection vs. Historical**: Be clear about data source - distinguish 1951-2023 estimates from 2024-2100 projections
4. **Missing values**: Check for NaN values and handle appropriately (common in future projections)
