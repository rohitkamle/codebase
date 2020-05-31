# Athena Table fields 
# Date date, Country string, ConfirmedToDate int, ConfirmedSource string


# CREATE EXTERNAL TABLE IF NOT EXISTS coviddata.simplejson (
#   `date` date,
#   `country` string,
#   `confirmedtodate` int,
#   `confirmedsource` string 
# )
# ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
# WITH SERDEPROPERTIES (
#   'serialization.format' = '1'
# ) LOCATION 's3://rkamlekinesis/simplejson/'
# TBLPROPERTIES ('has_encrypted_data'='false');