// Send a GET request to the Java backend to retrieve the list of candidate profiles
fetch('http://localhost:8080/candidates')
    .then(response => response.json())
    .then(data => {
        // Loop through the list of profiles and add each one to the table
        data.forEach(profile => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${profile.name}</td>
                <td>${profile.bio}</td>
                <td>${profile.slogan}</td>
                <td><img src="${profile.picture}"></td>
            `;
            document.getElementById('profilesTable').appendChild(row);
        });
    });
