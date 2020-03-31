# Coronavirus (COVID-19): number of cases in England

Public Health England (PHE) publishes Coronavirus confirmed cases data by upper tier local authority daily on this page: https://www.gov.uk/government/publications/coronavirus-covid-19-number-of-cases-in-england/coronavirus-covid-19-number-of-cases-in-england

This little python script gets the page data through the [GOV.UK Content API](https://content-api.publishing.service.gov.uk/#gov-uk-content-api) and saves it as a `.csv` file inside the `data` folder, using the timestamp `YY-MM-DD`. The data is parsed every day around 19:00 GMT.

EDIT: Of course the data gets withdrawn a few days after I start collecting it and replaced by a proper dashboard. Oh well, I'll still leave this up as an example of how to setup Travis CI to regularly push data to a repo.
