import requests
import json

def prevod(rijec):
    rjecnik = {"Monday": "Ponedjeljak", "Tuesday": "Utorak", "Wednesday": "Srijeda",
    "Thursday": "Četvrtak", "Friday": "Petak", "Saturday": "Subota", "Sunday": "Nedjelja",
    "Clear": "Vedro", "Sunny": "Sunčano", "Thunderstorm": "Oluja",
    "Scattered thunderstorms": "Mjestimične oluje", "Mostly sunny": "Pretežno sunčano",
    "Isolated thunderstorms": "Lokalne oluje", "Partly cloudy": "Djelimično oblačno"}
    if rijec in rjecnik:
        return rjecnik[rijec]
    else:
        return rijec

def display_wdata(where):
    if ' ' in where:
        where = where.replace(' ', '+')
    r = requests.get(f'https://weatherdbi.herokuapp.com/data/weather/{where}')
    data = json.loads(r.text)
    try:
        region = data["region"]
    except:
        try:
            status = data["status"]
        except Exception as e:
            print(e)
        print(status, data["message"])
        return f"""<!DOCTYPE html>
        <html>
        <body>
        <p>{status}</p>
        <p>{data["message"]}</p>
        </body>
        </html>"""

    dayhour = data["currentConditions"]["dayhour"]
    dayhoursplit = dayhour.split()
    dayhour = prevod(dayhoursplit[0])+' '+' '.join(dayhoursplit[1:])
    icon = data["currentConditions"]["iconURL"]
    temp = data["currentConditions"]["temp"]["c"]
    precip = data["currentConditions"]["precip"]
    humidity = data["currentConditions"]["humidity"]
    wind = data["currentConditions"]["wind"]["km"]
    comment = data["currentConditions"]["comment"]

    next={}
    nextdays = []
    for info in data["next_days"]:
        nextdays.append(info["day"])
        next[info["day"]]={}
        next[info["day"]]["comment"]=info["comment"]
        next[info["day"]]["min_temp"]=info["min_temp"]["c"]
        next[info["day"]]["max_temp"]=info["max_temp"]["c"]
        next[info["day"]]["iconURL"]=info["iconURL"]

    return f"""<!DOCTYPE html>
<html>
<head>
<title>Vrijeme - {where.title().replace('+', ' ')}</title>
<style>
      table,
      th,
      td {{
        padding: 10px;
        border: 3px solid black;
        border-collapse: collapse;
      }}
    </style>
  </head>
<body>
<img src="{icon}"/>
<p>{prevod(comment)}</p>
<p>{region}</p>
<p>{dayhour}</p>
<p>Temperatura: {temp}°C</p>
<p>Šansa za padavine: {precip}</p>
<p>Vlažnost vazduha: {humidity}</p>
<p>Brzina vjetra: {wind}km/s</p>
<table>
<td><p id="day0">{prevod(nextdays[1])}</p>
<img src="{next[nextdays[1]]["iconURL"]}"/>
<p>{prevod(next[nextdays[1]]["comment"])}</p>
<p>{next[nextdays[1]]["min_temp"]} - {next[nextdays[1]]["max_temp"]}°C</p></td>

<td><p id="day1">{prevod(nextdays[2])}</p>
<img src="{next[nextdays[2]]["iconURL"]}"/>
<p>{prevod(next[nextdays[2]]["comment"])}</p>
<p>{next[nextdays[2]]["min_temp"]} - {next[nextdays[2]]["max_temp"]}°C</p></td>

<td><p id="day2">{prevod(nextdays[3])}</p>
<img src="{next[nextdays[3]]["iconURL"]}"/>
<p>{prevod(next[nextdays[3]]["comment"])}</p>
<p>{next[nextdays[3]]["min_temp"]} - {next[nextdays[3]]["max_temp"]}°C</p></td>

<td><p id="day3">{prevod(nextdays[4])}</p>
<img src="{next[nextdays[4]]["iconURL"]}"/>
<p>{prevod(next[nextdays[4]]["comment"])}</p>
<p>{next[nextdays[4]]["min_temp"]} - {next[nextdays[4]]["max_temp"]}°C</p></td>

<td><p id="day4">{prevod(nextdays[5])}</p>
<img src="{next[nextdays[5]]["iconURL"]}"/>
<p>{prevod(next[nextdays[5]]["comment"])}</p>
<p>{next[nextdays[5]]["min_temp"]} - {next[nextdays[5]]["max_temp"]}°C</p></td>

<td><p id="day5">{prevod(nextdays[6])}</p>
<img src="{next[nextdays[6]]["iconURL"]}"/>
<p>{prevod(next[nextdays[6]]["comment"])}</p>
<p>{next[nextdays[6]]["min_temp"]} - {next[nextdays[6]]["max_temp"]}°C</p></td>

<td><p id="day6">{prevod(nextdays[0])}</p>
<img src="{next[nextdays[0]]["iconURL"]}"/>
<p>{prevod(next[nextdays[0]]["comment"])}</p>
<p>{next[nextdays[0]]["min_temp"]} - {next[nextdays[0]]["max_temp"]}°C</p></td>
</table>
<script src="../static/script.js">

const printData = async () => {{
  const a = await data;
  console.log(a);
}};

{{
    let a;
    for (i = 0; i < 7; i++) {{
        a = "day" + i
        document.getElementById(a).innerHTML = data["nextdays"][i];
    }}
}}</script>
</body>
</html>"""