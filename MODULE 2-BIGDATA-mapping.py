# MODULE 2: BIG DATA PROCESS MAPPING
# Case Study: Google Maps

# 1. Data Sources
data = [
    {"road": "A-B", "vehicles": 120, "speed": 40},
    {"road": "B-C", "vehicles": 200, "speed": 20},
    {"road": "A-C", "vehicles": 80, "speed": 60},
    {"road": "C-D", "vehicles": 150, "speed": 30}
]

print("BIG DATA PROCESS MAPPING")
print("------------------------")

# 2. Data Ingestion
print("\n1. DATA INGESTION")
for record in data:
    print("Received:", record)

# 3. Data Storage
storage = data.copy()
print("\n2. DATA STORAGE")
print("Records stored:", len(storage))

# 4. Data Processing
print("\n3. DATA PROCESSING")
for road in storage:
    if road["speed"] < 30:
        status = "Heavy Traffic"
    elif road["speed"] < 45:
        status = "Moderate Traffic"
    else:
        status = "Low Traffic"

    print(road["road"], ":", status)

# 5. Output
print("\n4. OUTPUT")
print("Traffic information generated successfully.")

# 6. Feedback Loop
print("\n5. FEEDBACK LOOP")
print("New vehicle data can update traffic information.")
