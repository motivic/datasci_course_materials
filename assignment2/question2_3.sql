create table AB as select A.row_num, B.col_num, sum(A.value*B.value) from A inner join B on A.col_num = B.row_num group by A.row_num, B.col_num;

select tf from (select A.docid as rid, B.docid as cid, sum(A.count*B.count) as tf from frequency A inner join frequency B on A.term = B.term group by A.docid, B.docid) where rid = '10080_txt_crude' and cid = '17035_txt_earn';

create view newfreq as select * from frequency
	union
	select 'q' as docid, 'washington' as term, 1 as count
	union
	select 'q' as docid, 'taxes' as term, 1 as count
	union
	select 'q' as docid, 'treasury' as term, 1 as count;

create view similar_matrix as select A.docid as rid, B.docid as cid, sum(A.count*B.count) as tf from newfreq A inner join newfreq B on A.term = B.term group by A.docid, B.docid;

select rid, tf from similar_matrix where cid = 'q' order by tf asc; 
