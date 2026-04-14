from flask import Flask, render_template, jsonify, session, redirect, url_for, request
import mysql.connector
from dbconfig import config
from functools import wraps

app = Flask(__name__)
app.secret_key = 'dev_secret_key'

# ── helpers ──────────────────────────────────────────────────────────────────

def db():
    return mysql.connector.connect(**config)

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if session.get('role') != 'admin':
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated

def cashier_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if session.get('role') != 'cashier':
            return redirect(url_for('cashier_login'))
        return f(*args, **kwargs)
    return decorated

# ── public routes ─────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/adminlogin', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with db() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (username, password))
                admin = cursor.fetchone()
        if admin:
            session['role'] = 'admin'
            session['user'] = admin['username']
            return redirect(url_for('cashiers'))
        error = 'Invalid credentials.'
    return render_template('admin_login.html', error=error)

@app.route('/cashierlogin', methods=['GET', 'POST'])
def cashier_login():
    error = None
    if request.method == 'POST':
        email    = request.form['email']
        password = request.form['password']
        with db() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM cashiers WHERE email=%s AND password=%s", (email, password))
                cashier = cursor.fetchone()
        if cashier:
            session['role'] = 'cashier'
            session['user'] = cashier['email']
            return redirect(url_for('cashier_page1'))
        error = 'Invalid credentials.'
    return render_template('cashier_login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# ── admin routes ──────────────────────────────────────────────────────────────

@app.route('/cashiers')
@admin_required
def cashiers():
    return render_template('admin/cashiers.html')

@app.route('/products')
@admin_required
def products():
    return render_template('admin/products.html')

@app.route('/transactions')
@admin_required
def transactions():
    return render_template('admin/transactions.html')

# ── cashier routes ────────────────────────────────────────────────────────────

@app.route('/cashier/page1')
@cashier_required
def cashier_page1():
    return render_template('cashier/page1.html')

@app.route('/cashier/page2')
@cashier_required
def cashier_page2():
    return render_template('cashier/page2.html')

@app.route('/cashier/page3')
@cashier_required
def cashier_page3():
    return render_template('cashier/page3.html')

# ── api routes ────────────────────────────────────────────────────────────────

@app.route('/api/cashiers')
@admin_required
def api_cashiers():
    with db() as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, last_name, first_name, gender, age, email FROM cashiers")
            return jsonify(cursor.fetchall())

@app.route('/api/products')
@admin_required
def api_products():
    with db() as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT product_id, product_name, category, price, stock FROM products")
            return jsonify(cursor.fetchall())

if __name__ == '__main__':
    app.run(debug=True)
