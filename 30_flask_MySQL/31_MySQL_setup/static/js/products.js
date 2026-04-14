fetch('/api/products')
    .then(res => res.json())
    .then(products => {
        const tbody = document.querySelector('#products-table tbody');

        if (products.length === 0) {
            tbody.innerHTML = '<tr><td colspan="5">No products found.</td></tr>';
            return;
        }

        products.forEach(p => {
            tbody.insertAdjacentHTML('beforeend', `
                <tr>
                    <td>${p.product_id}</td>
                    <td>${p.product_name}</td>
                    <td>${p.category ?? '—'}</td>
                    <td>₱${parseFloat(p.price).toFixed(2)}</td>
                    <td>${p.stock}</td>
                </tr>`);
        });
    })
    .catch(err => console.error('Failed to load products:', err));
