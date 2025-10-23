# Data Center Site Suitability Analysis

A streamlined geospatial analysis application for identifying optimal data center locations in the UK using **Databricks SQL Warehouse** and native geospatial functions.

## 🎯 **Configured for Your Workspace**

- **Workspace**: `e2-demo-field-eng.cloud.databricks.com` 
- **SQL Warehouse ID**: `862f1d757f0424f7`
- **Catalog**: `beatrice_liew`
- **Schema**: `geospatial`

## Features

### 🏢 Comprehensive Site Analysis
- **Multi-criteria evaluation** considering infrastructure, environmental, and regulatory factors
- **H3 hexagonal indexing** for systematic spatial analysis
- **Interactive filtering** based on data center size requirements
- **Real-time suitability scoring** with customizable weights

### 🗺️ Advanced Mapping & Visualization
- **Interactive maps** with Folium integration
- **Red boundary highlighting** for suitable sites
- **Layer management** for different data types (residential, power grid, water bodies)
- **Dynamic filtering** and real-time updates

### 🔧 Databricks Integration
- **Native ST functions** for geospatial operations
- **H3 indexing** for efficient spatial queries
- **Scalable computation** on Databricks clusters
- **Optimized for large datasets**

## Site Selection Criteria

### Infrastructure Requirements
- ⚡ **Power Grid Access**: Maximum distance from power infrastructure
- 🛣️ **Transportation**: Proximity to major roads and highways
- 🌐 **Connectivity**: Access to fiber optic networks
- 🏗️ **Site Size**: Available land area for different data center scales

### Environmental Constraints
- 🏘️ **Residential Distance**: Minimum buffer from populated areas
- 💧 **Water Bodies**: Safe distance from rivers and lakes
- 🌿 **Protected Areas**: Avoidance of national parks and conservation zones
- 🌊 **Flood Zones**: Risk assessment and avoidance of high-risk areas
- 🦅 **Biodiversity Impact**: Consideration of ecological sensitivity

### Regulatory & Economic Factors
- 📋 **Planning Permissions**: Areas with favorable zoning
- 💰 **Land Costs**: Economic viability assessment
- 🏛️ **Local Policies**: Government incentives and restrictions

## Data Center Size Categories

| Category | Power Requirement | Typical Area | Use Case |
|----------|------------------|--------------|----------|
| **Small** | < 10 MW | 2 hectares | Edge computing, local services |
| **Medium** | 10-50 MW | 8 hectares | Regional data centers |
| **Large** | 50-100 MW | 20 hectares | Enterprise data centers |
| **Hyperscale** | > 100 MW | 50+ hectares | Cloud providers, major platforms |

## Technical Implementation

### Geospatial Analysis Engine
```python
# H3 hexagonal indexing for systematic analysis
h3_grid = create_h3_grid(uk_bounds, resolution=7)

# Distance calculations using Databricks ST functions
distances = ST_Distance(candidate_point, infrastructure_points)

# Multi-criteria scoring algorithm
suitability_score = weighted_sum([
    infrastructure_score,
    environmental_score,
    regulatory_score,
    economic_score
])
```

### Key Technologies
- **Streamlit**: Interactive web application framework
- **Databricks**: Scalable geospatial processing
- **H3**: Uber's hexagonal hierarchical spatial indexing
- **Folium**: Interactive mapping and visualization
- **GeoPandas**: Geospatial data manipulation
- **Shapely**: Geometric operations

## Getting Started

### Prerequisites
- Databricks workspace with geospatial libraries
- Python 3.10+
- Required packages (see `requirements.txt`)

### Installation
1. Clone or upload the application to your Databricks workspace
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Deploy using Databricks Apps:
   ```bash
   databricks apps deploy
   ```

### Usage
1. **Select Analysis Region**: Choose from UK regions (London, South East, etc.)
2. **Configure Criteria**: Set distance requirements and constraints
3. **Run Analysis**: Click "Analyze Site Suitability"
4. **Review Results**: Examine suitable sites on the interactive map
5. **Export Data**: Download results as CSV for further analysis

## Data Sources

### Real-World Integration
The application is designed to integrate with:
- **Ordnance Survey**: UK geographic data
- **National Grid**: Power infrastructure data
- **Environment Agency**: Flood risk and environmental data
- **OpenStreetMap**: Road networks and POI data
- **DEFRA**: Protected areas and conservation zones

### Sample Data
For demonstration purposes, the app includes:
- Synthetic UK infrastructure data
- Representative geographical features
- Realistic constraint scenarios
- Example suitability scoring

## Customization

### Adding New Criteria
```python
def custom_constraint(site_point, custom_data):
    # Implement custom suitability logic
    return score

# Add to analysis pipeline
criteria['custom_score'] = custom_constraint
```

### Modifying Scoring Weights
```python
scoring_weights = {
    'infrastructure': 0.3,
    'environmental': 0.25,
    'regulatory': 0.2,
    'economic': 0.25
}
```

## Output & Results

### Site Recommendations
- **Ranked list** of suitable locations
- **Detailed scoring** breakdown by criteria
- **Geographic coordinates** for each site
- **Available land area** estimates
- **Risk assessments** and mitigation factors

### Visualization Features
- **Red boundary polygons** marking suitable sites
- **Color-coded** infrastructure layers
- **Interactive popups** with detailed site information
- **Legend and controls** for map navigation

## Performance Optimization

### Databricks Integration
- **Distributed processing** for large-scale analysis
- **Cached computations** for repeated queries
- **Optimized spatial joins** using H3 indexing
- **Parallel processing** of multiple regions

### Scalability
- Supports analysis of entire countries
- Handles millions of candidate locations
- Real-time filtering and updates
- Efficient memory management

## Future Enhancements

### Planned Features
- 🛰️ **Satellite imagery** analysis for land use classification
- 🌡️ **Climate data** integration for cooling efficiency
- 📊 **Economic modeling** with cost optimization
- 🔄 **Real-time data** feeds for dynamic analysis
- 🤖 **Machine learning** for predictive suitability modeling

### Integration Opportunities
- **GIS systems** for enterprise workflows
- **Planning tools** for municipal authorities
- **Investment platforms** for site acquisition
- **Environmental monitoring** systems

## Support & Documentation

For technical support and detailed documentation:
- 📧 Contact: [Your contact information]
- 📖 Documentation: [Link to detailed docs]
- 🐛 Issues: [GitHub/tracking system]
- 💬 Community: [Discussion forum]

---

**Built with ❤️ using Databricks Geospatial Analytics and Streamlit**
