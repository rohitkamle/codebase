-- First Data Demo
create table newemployees (
id varchar (10),
name varchar (20),
city varchar (20))


insert into newemployees values
('emp1', 'ABC', 'Pune'),
('emp2', 'XYZ', 'Mumbai'),
('emp3', 'PQR', 'Delhi'),
('emp4', 'NCJ', 'Hyderabad'),
('emp5', 'BBA', 'Banglore')


select count(*) from newemployees

select * from newemployees

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

copy users from 's3://rkamle-emr/allusers.txt'
credentials 'aws_iam_role=arn:aws:iam::265705255777:role/RedshiftS3ReadOnly'
delimiter '|' region 'ap-south-1';


-- copy users from 's3://redshift-rkamle/allusers.txt'
-- credentials 'aws_access_key_id=AKIA5OEJO7TWUPDWSZRF;aws_secret_access_key=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'
-- delimiter '|' region 'ap-south-1';

select count(*) from users


select * from users limit 100


-- Third Data Demo

CREATE TABLE part
(
  p_partkey     INTEGER NOT NULL,
  p_name        VARCHAR(22) NOT NULL,
  p_mfgr        VARCHAR(6) NOT NULL,
  p_category    VARCHAR(7) NOT NULL,
  p_brand1      VARCHAR(9) NOT NULL,
  p_color       VARCHAR(11) NOT NULL,
  p_type        VARCHAR(25) NOT NULL,
  p_size        INTEGER NOT NULL,
  p_container   VARCHAR(10) NOT NULL
);

copy part from 's3://awssampledbuswest2/ssbgz/part'
credentials 'aws_iam_role=arn:aws:iam::923706260717:role/redshiftS3ReadUser'
gzip compupdate off region 'us-west-2';


select count(*) from part

select * from part limit 50


