import sys
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.job import Job

# Init Spark and Glue Contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Read CSV from local file (mounted into container)
df = spark.read.option("header", "true").csv("file:///home/glue/input/sample.csv")
df.show()

# Write output to local dir
df.write.mode("overwrite").parquet("/tmp/glue-output")

job.commit()
