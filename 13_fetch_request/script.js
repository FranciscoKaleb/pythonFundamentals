

// alert("hi");


async function getTemperature() {
  const lat = 14.6760;   // Quezon City latitude
  const lon = 121.0437;  // Quezon City longitude

  const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`;

  try {
    const response = await fetch(url);
    const data = await response.json();

    const temp = data.current_weather.temperature;

    document.getElementById("temperature").textContent = "Temperature of QC fetched from api.open-meteo.com is " + temp + "°C";
  } catch (error) {
    document.getElementById("temperature").textContent = "Error loading temperature";
    console.error(error);
  }
}

getTemperature();