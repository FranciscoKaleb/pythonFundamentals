const PAGE_SIZE = 15;
let allProducts = [];
let currentPage = 1;

function showModal(id) {
    document.getElementById(id).classList.add('active');
}

function hideModal(id) {
    document.getElementById(id).classList.remove('active');
}

function showToast(message, isError = false) {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = 'toast' + (isError ? ' toast-error' : '') + ' active';
    setTimeout(() => toast.classList.remove('active'), 2500);
}

function renderTable() {
    const tbody = document.querySelector('#products-table tbody');
    tbody.innerHTML = '';

    const start = (currentPage - 1) * PAGE_SIZE;
    const page  = allProducts.slice(start, start + PAGE_SIZE);

    if (page.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6">No products found.</td></tr>';
        return;
    }

    page.forEach(p => {
        tbody.insertAdjacentHTML('beforeend', `
            <tr>
                <td>${p.product_id}</td>
                <td>${p.product_name}</td>
                <td>${p.category ?? '—'}</td>
                <td>₱${parseFloat(p.price).toFixed(2)}</td>
                <td>${p.stock}</td>
                <td class="actions-cell">
                    <button class="btn-edit"   onclick="openEdit(${p.product_id})">Edit</button>
                    <button class="btn-delete" onclick="openDelete(${p.product_id}, '${p.product_name}')">Delete</button>
                </td>
            </tr>`);
    });

    renderPagination();
}

function renderPagination() {
    const total = Math.ceil(allProducts.length / PAGE_SIZE);
    const container = document.getElementById('products-pagination');
    container.innerHTML = '';

    if (total <= 1) return;

    const prev = document.createElement('button');
    prev.textContent = '←';
    prev.disabled = currentPage === 1;
    prev.onclick = () => { currentPage--; renderTable(); };
    container.appendChild(prev);

    for (let i = 1; i <= total; i++) {
        const btn = document.createElement('button');
        btn.textContent = i;
        if (i === currentPage) btn.classList.add('page-active');
        btn.onclick = () => { currentPage = i; renderTable(); };
        container.appendChild(btn);
    }

    const next = document.createElement('button');
    next.textContent = '→';
    next.disabled = currentPage === total;
    next.onclick = () => { currentPage++; renderTable(); };
    container.appendChild(next);
}

// ── add ────────────────────────────────────────────────────────────────────────

document.getElementById('confirm-add').onclick = () => {
    const payload = {
        product_name: document.getElementById('add-product-name').value,
        category:     document.getElementById('add-category').value,
        price:        document.getElementById('add-price').value,
        stock:        document.getElementById('add-stock').value,
    };

    fetch('/api/products', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })
        .then(res => res.json())
        .then(data => {
            allProducts.push({ product_id: data.product_id, ...payload });
            renderTable();
            hideModal('add-modal');
            document.getElementById('add-product-name').value = '';
            document.getElementById('add-category').value     = '';
            document.getElementById('add-price').value        = '';
            document.getElementById('add-stock').value        = '';
            showToast('Product added successfully.');
        })
        .catch(() => showToast('Failed to add product.', true));
};

document.getElementById('cancel-add').onclick = () => hideModal('add-modal');

// ── delete ────────────────────────────────────────────────────────────────────

let pendingDeleteId = null;

function openDelete(id, name) {
    pendingDeleteId = id;
    document.getElementById('delete-name').textContent = name;
    showModal('delete-modal');
}

document.getElementById('confirm-delete').onclick = () => {
    fetch(`/api/products/${pendingDeleteId}`, { method: 'DELETE' })
        .then(res => res.json())
        .then(() => {
            allProducts = allProducts.filter(p => p.product_id !== pendingDeleteId);
            if ((currentPage - 1) * PAGE_SIZE >= allProducts.length && currentPage > 1) currentPage--;
            renderTable();
            hideModal('delete-modal');
            showToast('Product deleted.');
        })
        .catch(() => showToast('Delete failed.', true));
};

document.getElementById('cancel-delete').onclick = () => hideModal('delete-modal');

// ── edit ──────────────────────────────────────────────────────────────────────

let pendingEditId = null;

function openEdit(id) {
    const p = allProducts.find(x => x.product_id === id);
    pendingEditId = id;
    document.getElementById('edit-product-name').value = p.product_name;
    document.getElementById('edit-category').value     = p.category ?? '';
    document.getElementById('edit-price').value        = p.price;
    document.getElementById('edit-stock').value        = p.stock;
    showModal('edit-modal');
}

document.getElementById('save-edit').onclick = () => {
    const payload = {
        product_name: document.getElementById('edit-product-name').value,
        category:     document.getElementById('edit-category').value,
        price:        document.getElementById('edit-price').value,
        stock:        document.getElementById('edit-stock').value,
    };

    fetch(`/api/products/${pendingEditId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })
        .then(res => res.json())
        .then(() => {
            const p = allProducts.find(x => x.product_id === pendingEditId);
            Object.assign(p, payload);
            renderTable();
            hideModal('edit-modal');
            showToast('Product updated successfully.');
        })
        .catch(() => showToast('Update failed.', true));
};

document.getElementById('cancel-edit').onclick = () => hideModal('edit-modal');

// ── init ──────────────────────────────────────────────────────────────────────

fetch('/api/products')
    .then(res => res.json())
    .then(data => {
        allProducts = data;
        renderTable();
    })
    .catch(err => console.error('Failed to load products:', err));
