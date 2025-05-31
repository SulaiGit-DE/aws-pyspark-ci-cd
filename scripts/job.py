from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SampleETL").getOrCreate()

# Dummy data
data = [
    (1, "Alice", 5000),
    (2, "Bob", None),
    (3, "Charlie", 8000),
    (4, None, 7500)
]

columns = ["id", "name", "salary"]

df = spark.createDataFrame(data, columns)

# Clean: remove rows with nulls
df_cleaned = df.dropna()

# Transform: filter high earners
df_filtered = df_cleaned.filter(col("salary") > 6000)

# Output: print for demo
df_filtered.show() 