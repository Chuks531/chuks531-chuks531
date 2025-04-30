import pandas as pd
import pyodbc
import os

# Configuration
CSV_PATH = r"C:\Users\CHUKWUKA Okoli\OneDrive\Documents\Pulse_Data\Data_Reporting\Datasets\archive\latest_output_2025_04_29_15_10_34.csv"  # Update path if needed
SERVER = "PULSENG-CHUKWUK"        # Your SQL Server name
DATABASE = "AdventureWorks2016"     # Replace with your DB
TABLE_NAME = "SocialMediaKPI"

# Connect to SQL Server
conn_str = (
    f"DRIVER={{SQL Server}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"Trusted_Connection=yes;"
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Load CSV into DataFrame
df = pd.read_csv(CSV_PATH)

# Clean column names for SQL compatibility
df.columns = [col.strip().replace(" ", "_").replace("-", "_") for col in df.columns]

# Generate SQL schema from DataFrame
def generate_table_schema(df, table_name):
    sql = f"CREATE TABLE {table_name} (\n"
    for col in df.columns:
        if df[col].dtype == 'int64':
            sql += f"    [{col}] INT,\n"
        elif df[col].dtype == 'float64':
            sql += f"    [{col}] FLOAT,\n"
        else:
            sql += f"    [{col}] NVARCHAR(255),\n"
    sql = sql.rstrip(",\n") + "\n);"
    return sql

# Drop table if exists
cursor.execute(f"IF OBJECT_ID('{TABLE_NAME}', 'U') IS NOT NULL DROP TABLE {TABLE_NAME};")
conn.commit()

# Create new table
create_table_sql = generate_table_schema(df, TABLE_NAME)
cursor.execute(create_table_sql)
conn.commit()
print(f"Table '{TABLE_NAME}' created.")

# Insert data
columns = ','.join(f"[{col}]" for col in df.columns)
placeholders = ','.join('?' for _ in df.columns)
insert_sql = f"INSERT INTO {TABLE_NAME} ({columns}) VALUES ({placeholders})"

for _, row in df.iterrows():
    cleaned_row = []
    for col, val in row.items():
        if pd.isna(val) or val == "":
            cleaned_row.append(None)
        elif isinstance(val, str):
            val = val.strip().replace(",", "")
            try:
                # Try to convert to float if the column expects it
                if df[col].dtype == "float64":
                    val = float(val)
                elif df[col].dtype == "int64":
                    val = int(float(val))
            except ValueError:
                pass
            cleaned_row.append(val)
        else:
            cleaned_row.append(val)
    cursor.execute(insert_sql, tuple(cleaned_row))


conn.commit()
cursor.close()
conn.close()
print("Data loaded successfully.")
