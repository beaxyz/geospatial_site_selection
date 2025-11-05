# Data Center Site Suitability Analysis

A streamlined geospatial analysis application for identifying optimal data center locations in the UK using **Databricks SQL Warehouse** and native geospatial functions.


## Features

### 🏢 Comprehensive Site Analysis
- **Multi-criteria evaluation** considering land boundary layer, size of site and distance to road network for the selection of suitable sites for building a data centre

### Key Technologies
- **Streamlit**: Interactive web application framework
- **Databricks**: Scalable geospatial processing
- **Kepler**: Map Visualisation

### Prerequisites
- DBR 17.1 and above
- Required packages (see `requirements.txt`)

### Installation
1. Clone or upload the application to your Databricks workspace
2. Configure workspace id & SQL warehouse
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Deploy using Databricks Apps:
   ```bash
   databricks apps deploy
   ```

## Data Sources
For demonstration purposes, the app includes:
- Boundary & road data from Ordnance Survey
