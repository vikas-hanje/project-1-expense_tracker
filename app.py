from flask import Flask, render_template, request, redirect, url_for
from db import connect_DB

app = Flask(__name__)

@app.route('/')
def index():
    conn = connect_DB()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """select Expenses.ExpenseID, Expenses.Description, Expenses.Amount, Expenses.Expense_Date, Categories.Name
        from Expenses left join Categories on Expenses.CategoryID = Categories.CategoryID;""")
    expenses = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', expenses = expenses)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add_expense', methods=['GET','POST'])
def add_expenses():
    
    if request.method == 'POST':
        amt = request.form.get('amt')
        des = request.form.get('des')
        date = request.form.get('date')
        category = request.form.get('category')
        
        conn = connect_DB()
        cursor = conn.cursor()
        
        insert_query = "insert into Expenses(Amount, Description, Expense_Date, CategoryID) values(%s, %s, %s, %s)"
        cursor.execute(insert_query, (amt, des, date, category))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return redirect(url_for('index'))
    
    conn = connect_DB()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("select CategoryID, Name from Categories;")
    categories = cursor.fetchall()
    
    cursor.close()
    conn.close()
        
    return render_template('add_expense.html', categories = categories)

@app.route('/edit_expense/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    if request.method == 'POST':
        new_amt = request.form.get('amt')
        new_des = request.form.get('des')
        new_date = request.form.get('date')
        new_category = request.form.get('category')

        conn = connect_DB()
        cursor = conn.cursor()

        update_query = "update Expenses set Amount = %s, Description = %s, Expense_Date = %s, CategoryID = %s where ExpenseID = %s;"
        cursor.execute(update_query, (new_amt, new_des, new_date, new_category, id))
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('index'))

    conn = connect_DB()
    cursor = conn.cursor(dictionary=True)
    
    select_query = "select ExpenseID, Amount, Description, Expense_Date, CategoryID from Expenses where ExpenseID = %s;"
    cursor.execute(select_query, (id,))
    expense_to_edit = cursor.fetchone()

    cursor.execute("select CategoryID, Name from Categories;")
    categories = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('edit_expense.html', expense=expense_to_edit, categories=categories)

@app.route('/delete_expense/<int:id>', methods=['POST'])
def delete_expense(id):
    conn = connect_DB()
    cursor = conn.cursor()

    delete_query = "delete from Expenses where ExpenseID = %s;"
    cursor.execute(delete_query, (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True)