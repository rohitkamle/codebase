
-- Second Data Demo
create table users(
  userid integer not null distkey sortkey, 
  username char(8), 
  firstname varchar(30), 
  lastname varchar(30), 
  city varchar(30), 
  state char(2), 
  email varchar(100), 
  phone char(14), 
  likesports boolean, 
  liketheatre boolean, 
  likeconcerts boolean, 
  likejazz boolean, 
  likeclassical boolean, 
  likeopera boolean, 
  likerock boolean, 
  likevegas boolean, 
  likebroadway boolean, 
  likemusicals boolean
);

copy users from 's3://rkamle-emr/redshift-demo/allusers.txt'
credentials 'aws_iam_role=arn:aws:iam::265705255777:role/RedshiftS3ReadOnly'
delimiter '|' region 'ap-south-1';


select * from users limit 10