from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def report(spark: SparkSession, in0: DataFrame):
    if Config.fabricName == "dev":
        in0.write\
            .format("delta")\
            .option("fileFormat", "parquet")\
            .mode("overwrite")\
            .saveAsTable("prophecy_samples.report_data")
    else:
        raise Exception("No valid dataset present to read fabric")
