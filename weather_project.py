# Import required libraries
import requests
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Step 1: Extract - Fetch weather data from the API
API_KEY = "76bd13be8af9514443a23ba2bbaec06d"
cities = ["Denton,US", "Austin,US", "Dallas,US", "Houston,US"]
all_weather_data = []

for CITY in cities:
    BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?units=metric&q={CITY}&appid={API_KEY}"
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        weather_data = response.json()
        transformed_data = {
            "City": weather_data["name"],
            "Temperature (C)": weather_data["main"]["temp"],
            "Weather": weather_data["weather"][0]["description"],
            "Humidity (%)": weather_data["main"]["humidity"],
            "Wind Speed (m/s)": weather_data["wind"]["speed"]
        }
        all_weather_data.append(transformed_data)  # Collect data for all cities
        print(f"Data fetched for {weather_data['name']}!")
    else:
        print(f"Failed to fetch data for {CITY}. Check API or city name.")

# Step 2: Transform - Process all cities' data into a DataFrame
df = pd.DataFrame(all_weather_data)
print("\nTransformed Weather Data:\n", df)

# Optional: Sort the data by temperature in descending order
df = df.sort_values(by="Temperature (C)", ascending=False)
print("\nSorted Weather Data by Temperature (High to Low):\n", df)

# Step 3: Load - Save the transformed data to a CSV file
csv_file_name = "all_cities_weather_data.csv"  # Updated file name for clarity
df.to_csv(csv_file_name, index=False)
print(f"\nData successfully saved to {csv_file_name}!")

# Step 4: Load - Save the data to a SQLite database
# Connect to SQLite database (or create one if it doesn’t exist)
conn = sqlite3.connect("weather_data.db")
cursor = conn.cursor()

# Recreate the table with the 'timestamp' column (if needed)
cursor.execute("DROP TABLE IF EXISTS weather")
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    city TEXT,
    temperature REAL,
    weather TEXT,
    humidity INTEGER,
    wind_speed REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()
print("Recreated the weather table with the 'timestamp' column.")

# Insert each city's data into the database
for transformed_data in all_weather_data:
    cursor.execute("""
    SELECT COUNT(*) FROM weather WHERE city = ? AND DATE(timestamp) = DATE('now')
    """, (transformed_data["City"],))

    if cursor.fetchone()[0] == 0:
        cursor.execute("""
        INSERT INTO weather (city, temperature, weather, humidity, wind_speed)
        VALUES (?, ?, ?, ?, ?)
        """, (transformed_data["City"], transformed_data["Temperature (C)"], transformed_data["Weather"], transformed_data["Humidity (%)"], transformed_data["Wind Speed (m/s)"]))
        conn.commit()
        print(f"Data for {transformed_data['City']} inserted successfully!")
    else:
        print(f"Data for {transformed_data['City']} already exists. No new entry added.")

# Query the database to confirm stored data
cursor.execute("SELECT * FROM weather")
rows = cursor.fetchall()

print("\nStored Weather Data:")
for row in rows:
    print(f"City: {row[0]}, Temperature: {row[1]}°C, Weather: {row[2]}, Humidity: {row[3]}%, Wind Speed: {row[4]} m/s")

# Close the database connection
conn.close()

# Step 5: Visualize the Data - Temperature Comparison Across Cities
plt.figure(figsize=(10, 6))
plt.bar(df["City"], df["Temperature (C)"], color="skyblue")
plt.title("Temperature Comparison Across Cities")
plt.ylabel("Temperature (°C)")
plt.xlabel("Cities")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Save the chart before displaying it
plt.savefig("temperature_chart.png")
print("Chart saved as temperature_chart.png!")
plt.show()