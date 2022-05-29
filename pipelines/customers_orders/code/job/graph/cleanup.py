from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def cleanup(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("order_id"), 
        col("customer_id"), 
        col("amount"), 
        col("email"), 
        concat(col("first_name"), col("last_name")).alias("full_name")
    )
