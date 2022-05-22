async function fetchAsync () {
    var where = document.getElementById("whereField").value
    if (!where) {return;}
    where = where.replace(' ', '+');
    where = asciiize(where)
    let response = await fetch("https://weatherdbi.herokuapp.com/data/weather/"+where);
    console.log(response);
    let data = await response.json();
    return data;
};

function asciiize(str) {
    if (str.includes("č")) {str = str.replace("č", "c");}
    if (str.includes("ć")) {str = str.replace("ć", "c");}
    if (str.includes("š")) {str = str.replace("š", "s");}
    if (str.includes("đ")) {str = str.replace("đ", "dj");}
    if (str.includes("ž")) {str = str.replace("ž", "z");}
    if (str.includes("Č")) {str = str.replace("Č", "C");}
    if (str.includes("Ć")) {str = str.replace("Ć", "C");}
    if (str.includes("Š")) {str = str.replace("Š", "S");}
    if (str.includes("Đ")) {str = str.replace("Đ", "Dj");}
    if (str.includes("Ž")) {str = str.replace("Ž", "Z");}
    return str
}

function titleCase(str) {
    var splitStr = str.toLowerCase().split(' ');
    for (var i = 0; i < splitStr.length; i++) {
        // You do not need to check if i is larger than splitStr length, as your for does that for you
        // Assign it back to the array
        splitStr[i] = splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);     
    }
    // Directly return the joined string
    return splitStr.join(' '); 
}

function prevod(rijec) {
    const rjecnik = {"Monday": "Ponedjeljak", "Tuesday": "Utorak", "Wednesday": "Srijeda",
    "Thursday": "Četvrtak", "Friday": "Petak", "Saturday": "Subota", "Sunday": "Nedjelja",
    "Clear": "Vedro", "Sunny": "Sunčano", "Thunderstorm": "Oluja",
    "Scattered thunderstorms": "Mjestimične oluje", "Mostly sunny": "Pretežno sunčano",
    "Isolated thunderstorms": "Lokalne oluje", "Partly cloudy": "Djelimično oblačno",
    "Clear with periodic clouds": "Vedro s povremenom naoblakom", "Cloudy": "Oblačno",
    "Mostly cloudy": "Pretežno oblačno", "Haze": "Izmaglica", "Widespread dust": "Naleti prašine",
    "Light rain showers": "Slabi pljuskovi"}
    if (rijec in rjecnik) {
        return rjecnik[rijec]
    }
    else {
        return rijec
    }
}

function preloadImage(url) {
    var img=new Image();
    img.src=url;
}

function setGradient(condition) {
    var r = document.querySelector(':root');
    if (condition == "overcast") {
        r.style.setProperty('--topcolor', rgb(82, 96, 100))
    }
    else {
        r.style.setProperty('--topcolor', rgb(193, 228, 240))
    }

}

function writeWeatherData() {
    document.getElementById("loading").innerHTML = "Učitavanje...";
    document.getElementById("submitBtn").disabled = true
    fetchAsync().then((data) => {
        preloadImage(data["currentConditions"]["iconURL"])
        document.getElementById("loading").innerHTML = ""
        document.getElementById("submitBtn").disabled = false
        document.title = "Vrijeme - "+titleCase(data["region"].split(',')[0])
        document.getElementById("iconToday").src = data["currentConditions"]["iconURL"]
        document.getElementById("region").innerHTML = data["region"]
        document.getElementById("commentToday").innerHTML = prevod(data["currentConditions"]["comment"])
        let dayhour = data["currentConditions"]["dayhour"].split(' ')
        document.getElementById("dayhour").innerHTML = [prevod(dayhour[0]), dayhour[1], dayhour[2]].join(' ')
        document.getElementById("temp").innerHTML = "Temperatura: " + data["currentConditions"]["temp"]["c"] + "°C"
        document.getElementById("humidity").innerHTML = "Vlažnost vazduha: " + data["currentConditions"]["humidity"]
        document.getElementById("precip").innerHTML = "Šansa za padavine: " + data["currentConditions"]["precip"]
        document.getElementById("wind").innerHTML = "Brzina vjetra: " + data["currentConditions"]["wind"]["km"] + "km/s"
        
    });
}

document.getElementById("whereField").addEventListener("keydown", (event) => {
    if (event.key == "Enter") {
        writeWeatherData()
    }
});

document.getElementById("submitBtn").addEventListener("click", () => writeWeatherData());
