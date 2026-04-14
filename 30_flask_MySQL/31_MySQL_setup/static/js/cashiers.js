fetch('/api/cashiers')
    .then(res => res.json())
    .then(cashiers => {
        const tbody = document.querySelector('#cashiers-table tbody');

        if (cashiers.length === 0) {
            tbody.innerHTML = '<tr><td colspan="6">No cashiers found.</td></tr>';
            return;
        }

        cashiers.forEach(c => {
            tbody.insertAdjacentHTML('beforeend', `
                <tr>
                    <td>${c.id}</td>
                    <td>${c.last_name}</td>
                    <td>${c.first_name}</td>
                    <td>${c.gender}</td>
                    <td>${c.age}</td>
                    <td>${c.email}</td>
                </tr>`);
        });
    })
    .catch(err => console.error('Failed to load cashiers:', err));
