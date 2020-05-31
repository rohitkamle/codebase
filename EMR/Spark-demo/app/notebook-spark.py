################# Demo one
from pyspark.sql import functions as F

from operator import add

lines = spark.read.text('s3://rkamle-newemr/spark-demo/input/input.txt').rdd.map(lambda r: r[0])
counts = lines.flatMap(lambda x: x.split(' ')) \
    .map(lambda x: (x, 1)) \
    .reduceByKey(add)
output = counts.collect()
for (word, count) in output:
    print("%s: %i" % (word, count))


##################### Demo Two
df = sqlContext.read.parquet('s3://us-east-1.elasticmapreduce.samples/flightdata/input')

df = df.select('flightdate', 'origin', 'dest',  'airtime', 'distance', 'cancelled', 'securitydelay')

df.where(df['airtime'] > 1000).show()

##################### Demo Three

df1 = spark.read.csv('s3://rkamle-newemr/spark-demo/input/testSeries.csv')
df1.show()
df1.printSchema()
df1.sort("_c0").show()
df1.groupBy("_c0", "_c1").count().show()