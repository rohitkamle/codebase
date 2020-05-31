
CREATE TABLE TestSeries
(
  Team          VARCHAR(22) NOT NULL,
  Opponent      VARCHAR(22) NOT NULL,
  Date          VARCHAR (6) NOT NULL,
  Matches       INTEGER NOT NULL,
  Result        VARCHAR(9) NOT NULL,
  Won           INTEGER NOT NULL,
  Lost          INTEGER NOT NULL,
  Drawn        INTEGER NOT NULL

);


copy users from 's3://redshift-rkamle/allusers.txt'
credentials 'aws_iam_role=arn:aws:iam::923706260717:role/redshiftS3ReadUser'
delimiter '|' region 'ap-south-1';