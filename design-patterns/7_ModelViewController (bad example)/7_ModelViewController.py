@app.route('/')
def example_page():
    """Searches the database for entries, then displays them."""
    db = get_db()
    query = db.execute('select * from entries order by id desc')
    entries = query.fetchall()
    return render_template('example_page.html', entries=entries)

