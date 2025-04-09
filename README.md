# Weather Data Analysis and Visualization

This project fetches weather data for multiple cities using OpenWeatherMap's API, processes it, stores it in a SQLite database, and creates insightful visualizations.

## Features
- Retrieve live weather data (temperature, humidity, wind speed, and conditions).
- Store data in a SQLite database with timestamp tracking to avoid duplicates.
- Save data as CSV for easy analysis.
- Generate bar charts to compare weather conditions visually.
- Automate script execution with Windows Task Scheduler.

## Technologies
- **Python**: Data extraction, transformation, and automation.
- **Pandas**: Data handling and processing.
- **SQLite**: Database storage and management.
- **Matplotlib**: Visualization.
- **Task Scheduler**: Automation (Windows).
- 
## Project Outputs
### Console Output
Example console output when the script runs:
<p align="center">
<img src="https://github.com/Deepthi3245/Weather-Data--Analysis/blob/main/Outputs/output.png?raw=true" >
</p>

### Saved Chart
A visualization is saved as temperature_chart.png: Temperature Chart Example
<p align="center">
<img src="https://github.com/Deepthi3245/Weather-Data--Analysis/blob/d21b28bb822607178022c14f2f68ad40ebd72dac/Outputs/temperature_chart.png" >
</p>

## Installation
Step 1. Clone the repository:
   ```bash
- git clone https://github.com/<Deepthi3245>/Weather-Data-Project.git
- cd Weather-Data-Project

Step 2: Clone the repository:
- Install the required Python libraries using pip:
- pip install -r requirements.txt

Step 3: Obtain an API Key
- Sign up at OpenWeatherMap.
- Generate an API key and replace the placeholder in weather_project.py:API_KEY = "YOUR_API_KEY"

Step 4: Run the Python Script
- Run the script to fetch and process weather data:
- python weather_project.py

Step 5: Automate the Script
- Set up Windows Task Scheduler to run the script automatically at desired intervals.
   


