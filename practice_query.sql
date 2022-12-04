select c.companyName, c.symbol, c.sector,
	c.industry, c.country, b.calendarYear,
	b.totalAssets, b.totalLiabilities 
from Company c
join Balance_Sheet b 
	on c.symbol = b.symbol
order by 6 desc;

------

select
	b.symbol, c.companyName, 
	b.calendarYear, b.totalAssets,
	i.revenue, c.companyName
from Balance_Sheet b
join Income_Statement i
	on b.calendarYear = i.calendarYear
	and b.symbol = i.symbol
join Company c
	on b.symbol = c.symbol;

/*

PROBLEM

the first join statement in above table is broken..

ANSWER

..

*/

select
	b.symbol,
	b.calendarYear, 
	b.totalAssets
from Balance_Sheet b
where b.symbol = 'CPNG';

select
	i.symbol,
	i.calendarYear,
	b.totalAssets,
	i.revenue
from Income_Statement i
left join Balance_Sheet b
	on i.symbol = b.symbol
where i.symbol = 'CPNG';


-----
select 
	symbol, calendarYear, grossProfitRatio
from Income_Statement;


select
	b.symbol, c.companyName, 
	b.calendarYear, b.totalAssets,
	i.revenue, c.companyName
from Income_Statement i
left join Balance_Sheet b
	on b.calendarYear = i.calendarYear
	and b.symbol = i.symbol
join Company c
	on b.symbol = c.symbol;





