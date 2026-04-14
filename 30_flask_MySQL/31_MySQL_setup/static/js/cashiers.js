const PAGE_SIZE = 15;
let allCashiers = [];
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
    const tbody = document.querySelector('#cashiers-table tbody');
    tbody.innerHTML = '';

    const start = (currentPage - 1) * PAGE_SIZE;
    const page  = allCashiers.slice(start, start + PAGE_SIZE);

    if (page.length === 0) {
        tbody.innerHTML = '<tr><td colspan="7">No cashiers found.</td></tr>';
        return;
    }

    page.forEach(c => {
        tbody.insertAdjacentHTML('beforeend', `
            <tr>
                <td>${c.id}</td>
                <td>${c.last_name}</td>
                <td>${c.first_name}</td>
                <td>${c.gender}</td>
                <td>${c.age}</td>
                <td>${c.email}</td>
                <td class="actions-cell">
                    <button class="btn-edit"   onclick="openEdit(${c.id})">Edit</button>
                    <button class="btn-delete" onclick="openDelete(${c.id}, '${c.first_name} ${c.last_name}')">Delete</button>
                </td>
            </tr>`);
    });

    renderPagination();
}

function renderPagination() {
    const total = Math.ceil(allCashiers.length / PAGE_SIZE);
    const container = document.getElementById('cashiers-pagination');
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

// ── delete ────────────────────────────────────────────────────────────────────

let pendingDeleteId = null;

function openDelete(id, name) {
    pendingDeleteId = id;
    document.getElementById('delete-name').textContent = name;
    showModal('delete-modal');
}

document.getElementById('confirm-delete').onclick = () => {
    fetch(`/api/cashiers/${pendingDeleteId}`, { method: 'DELETE' })
        .then(res => res.json())
        .then(() => {
            allCashiers = allCashiers.filter(c => c.id !== pendingDeleteId);
            if ((currentPage - 1) * PAGE_SIZE >= allCashiers.length && currentPage > 1) currentPage--;
            renderTable();
            hideModal('delete-modal');
            showToast('Cashier deleted.');
        })
        .catch(() => showToast('Delete failed.', true));
};

document.getElementById('cancel-delete').onclick = () => hideModal('delete-modal');

// ── edit ──────────────────────────────────────────────────────────────────────

let pendingEditId = null;

function openEdit(id) {
    const c = allCashiers.find(x => x.id === id);
    pendingEditId = id;
    document.getElementById('edit-last-name').value  = c.last_name;
    document.getElementById('edit-first-name').value = c.first_name;
    document.getElementById('edit-gender').value     = c.gender;
    document.getElementById('edit-age').value        = c.age;
    document.getElementById('edit-email').value      = c.email;
    showModal('edit-modal');
}

document.getElementById('save-edit').onclick = () => {
    const payload = {
        last_name:  document.getElementById('edit-last-name').value,
        first_name: document.getElementById('edit-first-name').value,
        gender:     document.getElementById('edit-gender').value,
        age:        document.getElementById('edit-age').value,
        email:      document.getElementById('edit-email').value,
    };

    fetch(`/api/cashiers/${pendingEditId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })
        .then(res => res.json())
        .then(() => {
            const c = allCashiers.find(x => x.id === pendingEditId);
            Object.assign(c, payload);
            renderTable();
            hideModal('edit-modal');
            showToast('Cashier updated successfully.');
        })
        .catch(() => showToast('Update failed.', true));
};

document.getElementById('cancel-edit').onclick = () => hideModal('edit-modal');

// ── init ──────────────────────────────────────────────────────────────────────

fetch('/api/cashiers')
    .then(res => res.json())
    .then(data => {
        allCashiers = data;
        renderTable();
    })
    .catch(err => console.error('Failed to load cashiers:', err));
