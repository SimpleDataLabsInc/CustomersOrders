from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def sum_amounts(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("customer_id"))

    return df1.agg(
        count(col("order_id")).alias("orders"), 
        round(sum(col("amount"))).alias("amounts"), 
        first(col("email")).alias("email"), 
        first(col("full_name")).alias("full_name")
    )
