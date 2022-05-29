from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def orders(spark: SparkSession) -> DataFrame:
    if Config.fabricName == "dev":
        return spark.read\
            .schema(
              StructType([
                StructField("order_id", StringType(), True), StructField("customer_id", StringType(), True), StructField("order_status", StringType(), True), StructField("order_category", StringType(), True), StructField("order_date", StringType(), True), StructField("amount", StringType(), True)
            ])
            )\
            .option("header", True)\
            .option("sep", ",")\
            .csv("dbfs:/DatabricksSession/OrdersDatasetInput.csv")
    else:
        raise Exception("No valid dataset present to read fabric")
