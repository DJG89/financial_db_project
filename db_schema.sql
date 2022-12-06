CREATE TABLE Company (
	companyName PRIMARY KEY NOT NULL,
	symbol VARCHAR REFERENCES Income_Statement(symbol),
	sector VARCHAR,
	industry VARCHAR,
	country VARCHAR
);

CREATE TABLE Income_Statement (
	symbol VARCHAR REFERENCES Company(symbol),
	calendarYear INT,
	revenue INT,
	grossProfit INT,
	grossProfitRatio REAL,
	sellingGeneralAndAdministrativeExpenses INT,
	operatingExpenses INT,
	researchAndDevelopmentExpenses INT,
	interestExpense INT,
	operatingIncome INT,
	netIncome INT,
	eps INT,
	PRIMARY KEY (symbol, calendarYear)
);

CREATE TABLE Balance_Sheet (
	symbol VARCHAR REFERENCES Company(symbol),
	calendarYear INT,
	totalAssets INT,
	totalLiabilities INT,
	netReceivables INT,
	retainedEarnings INT,
	totalStockholdersEquity INT,
	cashAndCashEquivalents INT,
	ROA_ratio REAL,
	PRIMARY KEY (symbol, calendarYear)
);