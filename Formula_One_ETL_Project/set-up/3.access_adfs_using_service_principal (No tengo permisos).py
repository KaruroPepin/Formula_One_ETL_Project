# Databricks notebook source
# MAGIC %md
# MAGIC ### Access Azure Data Lake using Service Principal
# MAGIC #### Steps to follow
# MAGIC 1. Register Azure AD Application / Service Principal
# MAGIC 2. Generate a secret/ password for the Application
# MAGIC 3. Set Spark Config with App/ Client Id, Directory/ Tenant Id & Secret
# MAGIC 4. Assign Role 'Storage Blob Data Contributor' to the Data Lake.

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.dformulaone.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.dformulaone.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.dformulaone.dfs.core.windows.net", "sp=rl&st=2025-02-18T12:03:08Z&se=2025-02-18T20:03:08Z&spr=https&sv=2022-11-02&sr=c&sig=uKmnysbfzMG5T1Ry1FV7NpHRCPRZ5WNRVQZoYvnJfUU%3D")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@dformulaone.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@dformulaone.dfs.core.windows.net/circuits.csv"))
