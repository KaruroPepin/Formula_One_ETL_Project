# Databricks notebook source
# MAGIC %md
# MAGIC ####Access Azure Data Lake using access keys
# MAGIC 1. Set the spark config fs.azure.account.key
# MAGIC 2. List files from demo container
# MAGIC 3. Read data from cicuits.csv file

# COMMAND ----------

formulaone_dl_account_key = dbutils.secrets.get(scope='formula-one-scope', key='formula-one-dl-account-key')

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.dformulaone.dfs.core.windows.net",
    formulaone_dl_account_key
)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@dformulaone.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@dformulaone.dfs.core.windows.net/circuits.csv"))
