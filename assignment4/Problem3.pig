-- register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar
register /home/cloudera/lib/myudfs.jar;

-- load the test file into Pig
-- raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
raw = LOAD '/user/cloudera/input/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- First filter the data so you only have tuples whose subject matches 'rdfabout.com'.
-- rdfabout = FILTER ntriples BY (subject matches '.*rdfabout\\.com.*');
business = FILTER ntriples BY (subject matches '.*business.*');

-- Make another copy of the filtered collection (it's best to re-label the subject, predicate, and objects, for example to subject2, predicate2, object2).
-- rdfabout2 = FOREACH rdfabout GENERATE * as (subject2:chararray,predicate2:chararray,object2:chararray) PARALLEL 50;
business2 = FOREACH business GENERATE * as (subject2:chararray,predicate2:chararray,object2:chararray) PARALLEL 50;

-- Now join the two copies:
--   the first copy of the 'rdfabout.com' collection should match on object.
--   the second copy of the 'rdfabout.com' collection should match on subject2.
-- chain2tmp = JOIN rdfabout BY object, rdfabout2 BY subject2 PARALLEL 50;  
-- chain2 = DISTINCT chain2tmp PARALLEL 50; 
chain2tmp = JOIN business BY subject, business2 BY subject2 PARALLEL 50;  
chain2 = DISTINCT chain2tmp PARALLEL 50; 

logs_group = GROUP chain2 ALL PARALLEL 50;
log_count = FOREACH logs_group GENERATE COUNT(chain2); 
store chain2 into '/user/hadoop/3A-results/' using PigStorage(); 
