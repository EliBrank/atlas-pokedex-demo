document.addEventListener('DOMContentLoaded', (event) => {
  document.getElementById('fetchForm').addEventListener('submit', (event) => {
	event.preventDefault(); // Prevent the form from submitting the traditional way

	const query = document.getElementById('query').value;
	fetch(`http://localhost:5000/pokemon/search/${encodeURIComponent(query)}`)
	  .then(response => {
		if (!response.ok) {
		  throw new Error('Network response was not ok');
		}
		return response.json();
	  })
	  .then(data => {
		const dataList = document.getElementById('dataList');
		dataList.innerHTML = ''; // Clear existing list items

		// Assuming data is an object with properties like name, type, abilities, etc.
		const listItem = document.createElement('li');
		listItem.innerHTML = `
		<strong>Name:</strong> ${data.name} <br>
		<strong>Type:</strong> ${data.type.join(', ')} <br>
		<strong>Abilities:</strong> ${data.abilities.join(', ')} <br>
		<strong>Height:</strong> ${data.height} m <br>
		<strong>Weight:</strong> ${data.weight} kg <br>
		<img src="${data.image}" alt="${data.name}">
		`;
		dataList.appendChild(listItem);
	  })
	  .catch(error => {
		console.error('Error fetching data:', error);
	  });
  });
});
