# Databricks notebook source
# MAGIC %md
# MAGIC ####Access Azure Data Lake using access keys
# MAGIC 1. Set the spark config for SAS token
# MAGIC 2. List files from demo container
# MAGIC 3. Read data from cicuits.csv file

# COMMAND ----------

formulaone_dl_sastoken_key = dbutils.secrets.get(scope='formula-one-scope', key='formula-one-dl-sastoken')

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.dformulaone.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.dformulaone.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.dformulaone.dfs.core.windows.net", formulaone_dl_sastoken_key)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@dformulaone.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@dformulaone.dfs.core.windows.net/circuits.csv"))
