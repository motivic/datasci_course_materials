select * from frequency where docid='10398_txt_earn';

select term from frequency where docid='10398_txt_earn' and count=1;

select term from frequency where docid='10398_txt_earn' and count=1 union
select term from frequency where docid='925_txt_trade' and count=1;

select count(distinct docid) from frequency where term='law' or term='legal';

select docid from frequency group by docid having count(term) > 300;

select count(distinct a.docid) from frequency a, frequency b where a.docid=b.docid and a.term = 'transactions' and b.term = 'world';
