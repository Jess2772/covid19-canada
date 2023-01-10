from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

canada_info = requests.get('https://api.covid19tracker.ca/summary')
canada_info_json = canada_info.json()
## print(canada_info_json['data'])

current_date = (canada_info_json['data'][0])['latest_date']

@app.route('/')
def canada_data():

    canada_info = {
        'Daily Cases' : (canada_info_json['data'][0])['change_cases'],
        'Daily Fatalities' : (canada_info_json['data'][0])['change_fatalities'],
        'Daily Tests' : (canada_info_json['data'][0])['change_tests'],
        'Daily Hospitalizations' : (canada_info_json['data'][0])['change_hospitalizations'],
        'Daily Critical Condition Cases' : (canada_info_json['data'][0])['change_criticals'],
        'Recovered Today' : (canada_info_json['data'][0])['change_recoveries'],
        'Vaccinations Today' : (canada_info_json['data'][0])['change_vaccinations'],
        'Vaccines Distributed Today' : (canada_info_json['data'][0])['change_vaccines_distributed'],
        'Total Cases' : (canada_info_json['data'][0])['total_cases'],
        'Total Fatalities' : (canada_info_json['data'][0])['total_fatalities'],
        'Total Hospitilzations' : (canada_info_json['data'][0])['total_hospitalizations'],
        'Total Critical Condition Cases' : (canada_info_json['data'][0])['total_criticals'],
        'Total Recoveries' : (canada_info_json['data'][0])['total_recoveries'],    
        'Total Vaccinations' : (canada_info_json['data'][0])['total_fatalities'],
        'Total Vaccinations Distributed' : (canada_info_json['data'][0])['total_vaccines_distributed'],
        'Total Vaccinated' : (canada_info_json['data'][0])['total_vaccinated']

    }
    ## print(canada_info)
    return render_template('index.html', canada_info=canada_info, current_date=current_date)



@app.route('/about')
def about_covid():  
    return render_template('about.html', current_date=current_date)

@app.route('/data/<location>')
def province_territory_covid_data(location):
    flagFiles = {
        'ON': 'ontario', 'MB': 'manitoba', 'QC': 'quebec', 'SK': 'saskatchewan', 'AB': 'alberta', 'BC': 'british_columbia',
        'NB': 'new_brunswick', 'NF': 'newfoundland', 'NS': 'nova_scotia', 'PEI': 'pei', 'YT': 'yukon', 'NT': 'nwt', 'NU': 'nunavut'
    }
    locationName = {
        'ON': 'Ontario', 'MB': 'Manitoba', 'QC': 'Quebec', 'SK': 'Saskatchewan', 'AB': 'Alberta', 'BC': 'British Columbia',
        'NB': 'New Brunswick', 'NF': 'Newfoundland and Labrador', 'NS': 'Nova Scotia', 'PEI': 'Prince Edward Island', 'YT': 'Yukon', 'NT': 'Northwest Territories', 'NU': 'Nunavut'
    }
    locationParam = {'loc': location}
    covid_data = requests.get('https://api.opencovid.ca/summary', params=locationParam)
    covid_data_json = covid_data.json()
    print(covid_data_json)
    display_info = {
        'Total Cases': (covid_data_json['data'][0])['cases'],
        'Total Deaths': (covid_data_json['data'][0])['deaths'],
        'Total Hospitalizations': (covid_data_json['data'][0])['hospitalizations'],
        'Total ICU': (covid_data_json['data'][0])['icu'],
        'Total Tests Completed': (covid_data_json['data'][0])['tests_completed'],
        'Total Vaccine Doses Administered' : (covid_data_json['data'][0])['vaccine_administration_total_doses']
    }
    return render_template('covidTemplate.html', display_info=display_info, current_date=current_date, flag_file_name=flagFiles[location], locationName=locationName[location])

if __name__ == '__main__':
    app.run(debug=True)