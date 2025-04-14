# Databricks notebook source
# MAGIC %md
# MAGIC ### Mount Azure Data Lake using Service Principal
# MAGIC #### Steps to follow
# MAGIC 1. Get client_id, tenant_id and client_secret from key vault
# MAGIC 2. Set Spark Config with App/ Client Id, Directory/ Tenant Id & Secret
# MAGIC 3. Call file system utlity mount to mount the storage
# MAGIC 4. Explore other file system utlities related to mount (list all mounts, unmount)

# COMMAND ----------

dl_account_key = dbutils.secrets.get(scope='formula-one-scope', key='formula-one-dl-account-key')

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": <SP id>,
           "fs.azure.account.oauth2.client.secret": dl_account_key ,
           "fs.azure.account.oauth2.client.endpoint": "dformulaone.dfs.core.windows.net"}
  

# COMMAND ----------

dbutils.fs.mount(
    source = "abfss://demo@dformulaone.dfs.core.windows.net/",
    mount_point = "/mnt/dformulaone/demo",
    extra_configs = configs
)

# COMMAND ----------

display(dbutils.fs.ls("/mnt/dformulaone/demo"))

# COMMAND ----------


