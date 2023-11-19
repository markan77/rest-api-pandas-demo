# rest-api-pandas-demo
RESTful API primjer pisan u Python programskom jeziku koristeći Flask i Pandas biblioteke. Aplikacija učitava podatke o država i to prikazuje korisniku kroz REST API koristeći JSON.

## Kako pokrenuti aplikaciju

Aplikacija koristi Flask biblioteku za kreiranje RESTful API-a što znači da moramo koristiti `flask` naredbu da bi pokrenuli aplikaciju.

```shell
flask --app main run
```

## URL putanje

`/api`

```json
{
"croatia": {
    "Area(sq km)": 56542,
    "Birth rate(births/1000 population)": 9.57,
    "Current account balance": -1925000000,
    "Death rate(deaths/1000 population)": 11.38,
    "Debt - external": 26400000000,
    "Electricity - consumption(kWh)": 15200000000,
    "Electricity - production(kWh)": 12510000000,
    "Exports": 7845000000,
    "GDP": 50330000000,
    "GDP - per capita": 11200,
    "GDP - real growth rate(%)": 3.7,
    "HIV/AIDS - adult prevalence rate(%)": 0.1,
    "HIV/AIDS - deaths": 10,
    "HIV/AIDS - people living with HIV/AIDS": 200,
    "Highways(km)": 28344,
    "Imports": 16700000000,
    "Industrial production growth rate(%)": 2.7,
    "Infant mortality rate(deaths/1000 live births)": 6.84,
    "Inflation rate (consumer prices)(%)": 2.5,
    "Internet hosts": 29644,
    "Internet users": 1014000,
    "Investment (gross fixed)(% of GDP)": 28.6,
    "Labor force": 1710000,
    "Life expectancy at birth(years)": 74.45,
    "Military expenditures - dollar figure": 620000000,
    "Military expenditures - percent of GDP(%)": 2.39,
    "Natural gas - consumption(cu m)": 2840000000,
    "Natural gas - exports(cu m)": 0,
    "Natural gas - imports(cu m)": 1080000000,
    "Natural gas - production(cu m)": 1760000000,
    "Natural gas - proved reserves(cu m)": 34360000000,
    "Oil - consumption(bbl/day)": 89000,
    "Oil - exports(bbl/day)": 0,
    "Oil - imports(bbl/day)": 0,
    "Oil - production(bbl/day)": 21000,
    "Oil - proved reserves(bbl)": 93600000,
    "Population": 4495904,
    "Public debt(% of GDP)": 41.7,
    "Railways(km)": 2726,
    "Reserves of foreign exchange & gold": 8563000000,
    "Telephones - main lines in use": 1825000,
    "Telephones - mobile cellular": 2553000,
    "Total fertility rate(children born/woman)": 1.39,
    "Unemployment rate(%)": 13.8
  },
  ...
}
```

`/api/<country>`

```json
{
    "Area(sq km)": 56542,
    "Birth rate(births/1000 population)": 9.57,
    "Current account balance": -1925000000,
    "Death rate(deaths/1000 population)": 11.38,
    "Debt - external": 26400000000,
    "Electricity - consumption(kWh)": 15200000000,
    "Electricity - production(kWh)": 12510000000,
    "Exports": 7845000000,
    "GDP": 50330000000,
    "GDP - per capita": 11200,
    "GDP - real growth rate(%)": 3.7,
    "HIV/AIDS - adult prevalence rate(%)": 0.1,
    "HIV/AIDS - deaths": 10,
    "HIV/AIDS - people living with HIV/AIDS": 200,
    "Highways(km)": 28344,
    "Imports": 16700000000,
    "Industrial production growth rate(%)": 2.7,
    "Infant mortality rate(deaths/1000 live births)": 6.84,
    "Inflation rate (consumer prices)(%)": 2.5,
    "Internet hosts": 29644,
    "Internet users": 1014000,
    "Investment (gross fixed)(% of GDP)": 28.6,
    "Labor force": 1710000,
    "Life expectancy at birth(years)": 74.45,
    "Military expenditures - dollar figure": 620000000,
    "Military expenditures - percent of GDP(%)": 2.39,
    "Natural gas - consumption(cu m)": 2840000000,
    "Natural gas - exports(cu m)": 0,
    "Natural gas - imports(cu m)": 1080000000,
    "Natural gas - production(cu m)": 1760000000,
    "Natural gas - proved reserves(cu m)": 34360000000,
    "Oil - consumption(bbl/day)": 89000,
    "Oil - exports(bbl/day)": 0,
    "Oil - imports(bbl/day)": 0,
    "Oil - production(bbl/day)": 21000,
    "Oil - proved reserves(bbl)": 93600000,
    "Population": 4495904,
    "Public debt(% of GDP)": 41.7,
    "Railways(km)": 2726,
    "Reserves of foreign exchange & gold": 8563000000,
    "Telephones - main lines in use": 1825000,
    "Telephones - mobile cellular": 2553000,
    "Total fertility rate(children born/woman)": 1.39,
    "Unemployment rate(%)": 13.8
}
```

## Dependencies

 - pandas
 - flask
