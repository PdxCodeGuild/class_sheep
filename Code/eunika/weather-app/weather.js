// open weather map api 
const api_root = 'https://api.openweathermap.org/data/2.5'
const icon_root = 'http://openweathermap.org/img/w/'
let api_key, app, lat, long

// grab user's location through browser (if the user allows it)
function getLocation(callback) {
  navigator.geolocation.getCurrentPosition(function(position) {
    lat = position.coords.latitude
    long = position.coords.longitude
    callback(lat, long)
  });
}

// callback to invoke getWeather using lat and long
function getLocationFromLatLong(lat, long) {
  if (lat && long) {
    getWeather(app, `lat=${lat}&lon=${long}`)
  }  
}

function getWeather(vueApp, query) {
  axios.get('keys.json')
       .then(function(res) {
          api_key = res.data.openweathermap
       })
       .catch(function(err) {
          console.log(err)
       })
       .then(function(res) {
          axios.get(`${api_root}/weather?${query}&units=imperial&appid=${api_key}`)
               .then(function(res) {
                  weather = res.data
                  console.log(weather)
                  vueApp.location = weather.name
                  vueApp.current = weather.weather[0].main
                  vueApp.description = weather.weather[0].description
                  vueApp.icon = icon_root + weather.weather[0].icon + '.png'
                  vueApp.temp = weather.main.temp
                  vueApp.min = weather.main.temp_min
                  vueApp.max = weather.main.temp_max
                  vueApp.loading = false
                })
               .catch(function(err) {
                  vueApp.error = 'Invalid zipcode'
                })
       })
}

window.onload = function() {
  app = new Vue({
    el: '#weather-body',
    data: {
      loading: true,
      error: false,
      location: null,
      icon: null,
      current: null,
      description: null,
      temp: null,
      min: null,
      max: null,
    },
    methods: {
      updateWeather: function(event) {
        getWeather(this, 'zip='+event.target.value)
      }
    }
  })  
  getLocation(getLocationFromLatLong)
}


