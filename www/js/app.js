const https = require('https');

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('findPokemon').addEventListener('submit', (event) => {
    event.preventDefault();

    const query = document.getElementById('query').value;
    fetch(`http://localhost:5000/pokemon?query=${encodeURIComponent(query)}`)
      .then(response => response.json())
      .then(data => {
        document.getElementById('foundPokemon').innerText = JSON.stringify(data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  });
})
