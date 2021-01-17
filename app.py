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


@app.route('/ontario')
def ontario_covid():
    ontario_data = requests.get('https://api.opencovid.ca/summary?loc=ON')
    ontario_data_json = ontario_data.json()
    print(ontario_data_json)

    ontario_info = {
        'Active Cases' : (ontario_data_json['summary'][0])['active_cases'],
        'New Cases Today': (ontario_data_json['summary'][0])['cases'],
        'Deaths Today': (ontario_data_json['summary'][0])['deaths'],
        'Total Cases': (ontario_data_json['summary'][0])['cumulative_cases'],
        'Total Deaths': (ontario_data_json['summary'][0])['cumulative_deaths'],
        'Total Recovered': (ontario_data_json['summary'][0])['cumulative_recovered'],
        'Total Vaccine Doses Administered' : (ontario_data_json['summary'][0])['cumulative_avaccine']
    }
    
    
    print(ontario_info)
    return render_template('ontario.html', ontario_info=ontario_info, current_date=current_date)


@app.route('/quebec')
def quebec_covid():
    quebec_data = requests.get('https://api.opencovid.ca/summary?loc=QC')
    quebec_data_json = quebec_data.json()
    print(quebec_data_json)

    quebec_info = {
        'Active Cases' : (quebec_data_json['summary'][0])['active_cases'],
        'New Cases Today': (quebec_data_json['summary'][0])['cases'],
        'Deaths Today': (quebec_data_json['summary'][0])['deaths'],
        'Total Cases': (quebec_data_json['summary'][0])['cumulative_cases'],
        'Total Deaths': (quebec_data_json['summary'][0])['cumulative_deaths'],
        'Total Recovered': (quebec_data_json['summary'][0])['cumulative_recovered'],
        'Total Vaccine Doses Administered' : (quebec_data_json['summary'][0])['cumulative_avaccine']
    }
    
    
    print(quebec_info)
    return render_template('quebec.html', quebec_info=quebec_info, current_date=current_date)

@app.route('/manitoba')
def manitoba_covid():
    manitoba_data = requests.get('https://api.opencovid.ca/summary?loc=MB')
    manitoba_data_json = manitoba_data.json()
    print(manitoba_data_json)

    manitoba_info = {
        'Active Cases' : (manitoba_data_json['summary'][0])['active_cases'],
        'New Cases Today': (manitoba_data_json['summary'][0])['cases'],
        'Deaths Today': (manitoba_data_json['summary'][0])['deaths'],
        'Total Cases': (manitoba_data_json['summary'][0])['cumulative_cases'],
        'Total Deaths': (manitoba_data_json['summary'][0])['cumulative_deaths'],
        'Total Recovered': (manitoba_data_json['summary'][0])['cumulative_recovered'],
        'Total Vaccine Doses Administered' : (manitoba_data_json['summary'][0])['cumulative_avaccine']
    }
    
    
    print(manitoba_info)
    return render_template('manitoba.html', manitoba_info=manitoba_info, current_date=current_date)

@app.route('/saskatchewan')
def saskatchewan_covid():
    saskatchewan_data = requests.get('https://api.opencovid.ca/summary?loc=MB')
    saskatchewan_data_json = saskatchewan_data.json()
    print(saskatchewan_data_json)

    saskatchewan_info = {
        'Active Cases' : (saskatchewan_data_json['summary'][0])['active_cases'],
        'New Cases Today': (saskatchewan_data_json['summary'][0])['cases'],
        'Deaths Today': (saskatchewan_data_json['summary'][0])['deaths'],
        'Total Cases': (saskatchewan_data_json['summary'][0])['cumulative_cases'],
        'Total Deaths': (saskatchewan_data_json['summary'][0])['cumulative_deaths'],
        'Total Recovered': (saskatchewan_data_json['summary'][0])['cumulative_recovered'],
        'Total Vaccine Doses Administered' : (saskatchewan_data_json['summary'][0])['cumulative_avaccine']
    }
    
    
    print(saskatchewan_info)
    return render_template('saskatchewan.html', saskatchewan_info=saskatchewan_info, current_date=current_date)


@app.route('/alberta')
def alberta_covid():
    alberta_data = requests.get('https://api.opencovid.ca/summary?loc=AB')
    alberta_data_json = alberta_data.json()
    print(alberta_data_json)

    alberta_info = {
        'Active Cases' : (alberta_data_json['summary'][0])['active_cases'],
        'New Cases Today': (alberta_data_json['summary'][0])['cases'],
        'Deaths Today': (alberta_data_json['summary'][0])['deaths'],
        'Total Cases': (alberta_data_json['summary'][0])['cumulative_cases'],
        'Total Deaths': (alberta_data_json['summary'][0])['cumulative_deaths'],
        'Total Recovered': (alberta_data_json['summary'][0])['cumulative_recovered'],
        'Total Vaccine Doses Administered' : (alberta_data_json['summary'][0])['cumulative_avaccine']
    }
    
    print(alberta_info)
    return render_template('alberta.html', alberta_info=alberta_info, current_date=current_date)


@app.route('/britishcolumbia')
def british_columbia_covid():
    british_columbia_data = requests.get('https://api.opencovid.ca/summary?loc=BC')
    british_columbia_data_json = british_columbia_data.json()
    print(british_columbia_data_json)

    british_columbia_info = {
        'Active Cases' : (british_columbia_data_json['summary'][0])['active_cases'],
        'New Cases Today': (british_columbia_data_json['summary'][0])['cases'],
        'Deaths Today': (british_columbia_data_json['summary'][0])['deaths'],
        'Total Cases': (british_columbia_data_json['summary'][0])['cumulative_cases'],
        'Total Deaths': (british_columbia_data_json['summary'][0])['cumulative_deaths'],
        'Total Recovered': (british_columbia_data_json['summary'][0])['cumulative_recovered'],
        'Total Vaccine Doses Administered' : (british_columbia_data_json['summary'][0])['cumulative_avaccine']
    }
    
    print(british_columbia_info)
    return render_template('british_columbia.html', british_columbia_info=british_columbia_info, current_date=current_date)

@app.route('/newbrunswick')
def new_brunswick_covid():
    new_brunswick_data = requests.get('https://api.opencovid.ca/summary?loc=NB')
    new_brunswick_data_json = new_brunswick_data.json()
    print(new_brunswick_data_json)

    new_brunswick_info = {
        'Active Cases' : (new_brunswick_data_json['summary'][0])['active_cases'],
        'New Cases Today': (new_brunswick_data_json['summary'][0])['cases'],
        'Deaths Today': (new_brunswick_data_json['summary'][0])['deaths'],
        'Total Cases': (new_brunswick_data_json['summary'][0])['cumulative_cases'],
        'Total Deaths': (new_brunswick_data_json['summary'][0])['cumulative_deaths'],
        'Total Recovered': (new_brunswick_data_json['summary'][0])['cumulative_recovered'],
        'Total Vaccine Doses Administered' : (new_brunswick_data_json['summary'][0])['cumulative_avaccine']
    }
    
    print(new_brunswick_info)
    return render_template('new_brunswick.html', new_brunswick_info=new_brunswick_info, current_date=current_date)


@app.route('/newfoundland')
def newfoundland_covid():
    newfoundland_data = requests.get('https://api.opencovid.ca/summary?loc=NL')
    newfoundland_data_json = newfoundland_data.json()
    print(newfoundland_data_json)

    newfoundland_info = {
        'Active Cases' : (newfoundland_data_json['summary'][0])['active_cases'],
        'New Cases Today': (newfoundland_data_json['summary'][0])['cases'],
        'Deaths Today': (newfoundland_data_json['summary'][0])['deaths'],
        'Total Cases': (newfoundland_data_json['summary'][0])['cumulative_cases'],
        'Total Deaths': (newfoundland_data_json['summary'][0])['cumulative_deaths'],
        'Total Recovered': (newfoundland_data_json['summary'][0])['cumulative_recovered'],
        'Total Vaccine Doses Administered' : (newfoundland_data_json['summary'][0])['cumulative_avaccine']
    }
    
    print(newfoundland_info)
    return render_template('newfoundland.html', newfoundland_info=newfoundland_info, current_date=current_date)

@app.route('/novascotia')
def nova_scotia_covid():
    nova_scotia_data = requests.get('https://api.opencovid.ca/summary?loc=NS')
    nova_scotia_data_json = nova_scotia_data.json()
    print(nova_scotia_data_json)

    nova_scotia_info = {
        'Active Cases' : (nova_scotia_data_json['summary'][0])['active_cases'],
        'New Cases Today': (nova_scotia_data_json['summary'][0])['cases'],
        'Deaths Today': (nova_scotia_data_json['summary'][0])['deaths'],
        'Total Cases': (nova_scotia_data_json['summary'][0])['cumulative_cases'],
        'Total Deaths': (nova_scotia_data_json['summary'][0])['cumulative_deaths'],
        'Total Recovered': (nova_scotia_data_json['summary'][0])['cumulative_recovered'],
        'Total Vaccine Doses Administered' : (nova_scotia_data_json['summary'][0])['cumulative_avaccine']
    }
    
    print(nova_scotia_info)
    return render_template('nova_scotia.html', nova_scotia_info=nova_scotia_info, current_date=current_date)

@app.route('/pei')
def pei_covid():
    pei_data = requests.get('https://api.opencovid.ca/summary?loc=PE')
    pei_data_json = pei_data.json()
    print(pei_data_json)

    pei_info = {
        'Active Cases' : (pei_data_json['summary'][0])['active_cases'],
        'New Cases Today': (pei_data_json['summary'][0])['cases'],
        'Deaths Today': (pei_data_json['summary'][0])['deaths'],
        'Total Cases': (pei_data_json['summary'][0])['cumulative_cases'],
        'Total Deaths': (pei_data_json['summary'][0])['cumulative_deaths'],
        'Total Recovered': (pei_data_json['summary'][0])['cumulative_recovered'],
        'Total Vaccine Doses Administered' : (pei_data_json['summary'][0])['cumulative_avaccine']
    }
    print(pei_info)
    return render_template('pei.html', pei_info=pei_info, current_date=current_date)


@app.route('/yukon')
def yukon_covid():
    yukon_data = requests.get('https://api.opencovid.ca/summary?loc=YT')
    yukon_data_json = yukon_data.json()
    print(yukon_data_json)

    yukon_info = {
        'Active Cases' : (yukon_data_json['summary'][0])['active_cases'],
        'New Cases Today': (yukon_data_json['summary'][0])['cases'],
        'Deaths Today': (yukon_data_json['summary'][0])['deaths'],
        'Total Cases': (yukon_data_json['summary'][0])['cumulative_cases'],
        'Total Deaths': (yukon_data_json['summary'][0])['cumulative_deaths'],
        'Total Recovered': (yukon_data_json['summary'][0])['cumulative_recovered'],
        'Total Vaccine Doses Administered' : (yukon_data_json['summary'][0])['cumulative_avaccine']
    }
    
    print(yukon_info)
    return render_template('yukon.html', yukon_info=yukon_info, current_date=current_date)

@app.route('/nwt')
def nwt_covid():
    nwt_data = requests.get('https://api.opencovid.ca/summary?loc=NT')
    nwt_data_json = nwt_data.json()
    print(nwt_data_json)

    nwt_info = {
        'Active Cases' : (nwt_data_json['summary'][0])['active_cases'],
        'New Cases Today': (nwt_data_json['summary'][0])['cases'],
        'Deaths Today': (nwt_data_json['summary'][0])['deaths'],
        'Total Cases': (nwt_data_json['summary'][0])['cumulative_cases'],
        'Total Deaths': (nwt_data_json['summary'][0])['cumulative_deaths'],
        'Total Recovered': (nwt_data_json['summary'][0])['cumulative_recovered'],
        'Total Vaccine Doses Administered' : (nwt_data_json['summary'][0])['cumulative_avaccine']
    }
    
    print(nwt_info)
    return render_template('nwterritories.html', nwt_info=nwt_info, current_date=current_date)

@app.route('/nunavut')
def nunavut_covid():
    nunavut_data = requests.get('https://api.opencovid.ca/summary?loc=NU')
    nunavut_data_json = nunavut_data.json()
    print(nunavut_data_json)

    nunavut_info = {
        'Active Cases' : (nunavut_data_json['summary'][0])['active_cases'],
        'New Cases Today': (nunavut_data_json['summary'][0])['cases'],
        'Deaths Today': (nunavut_data_json['summary'][0])['deaths'],
        'Total Cases': (nunavut_data_json['summary'][0])['cumulative_cases'],
        'Total Deaths': (nunavut_data_json['summary'][0])['cumulative_deaths'],
        'Total Recovered': (nunavut_data_json['summary'][0])['cumulative_recovered'],
        'Total Vaccine Doses Administered' : (nunavut_data_json['summary'][0])['cumulative_avaccine']
    }
    
    print(nunavut_info)
    return render_template('nunavut.html', nunavut_info=nunavut_info, current_date=current_date)

if __name__ == '__main__':
    app.run(debug=True)