import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def lade_beitraege():
    try:
        with open('blog.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def speichere_beitraege(beitraege):
    with open('blog.json', 'w', encoding='utf-8') as file:
        json.dump(beitraege, file, indent=4)


@app.route('/')
def index():
    blog_posts = lade_beitraege()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        blog_posts = lade_beitraege()
        neue_id = max([p['id'] for p in blog_posts], default=0) + 1
        neuer_post = {
            "id": neue_id,
            "author": request.form.get('author'),
            "title": request.form.get('title'),
            "content": request.form.get('content'),
            "likes": 0  # Startwert für Likes
        }
        blog_posts.append(neuer_post)
        speichere_beitraege(blog_posts)
        return redirect(url_for('index'))
    return render_template('add.html')


# --- NEU: Like Route ---
@app.route('/like/<int:post_id>')
def like(post_id):
    blog_posts = lade_beitraege()
    post = next((p for p in blog_posts if p['id'] == post_id), None)

    if post:
        # Falls das Feld 'likes' noch nicht existiert, erstellen wir es
        if 'likes' not in post:
            post['likes'] = 0
        post['likes'] += 1  # Like-Zähler erhöhen
        speichere_beitraege(blog_posts)

    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    blog_posts = lade_beitraege()
    post = next((p for p in blog_posts if p['id'] == post_id), None)
    if request.method == 'POST':
        post['author'] = request.form.get('author')
        post['title'] = request.form.get('title')
        post['content'] = request.form.get('content')
        speichere_beitraege(blog_posts)
        return redirect(url_for('index'))
    return render_template('update.html', post=post)


@app.route('/delete/<int:post_id>')
def delete(post_id):
    blog_posts = lade_beitraege()
    blog_posts = [p for p in blog_posts if p['id'] != post_id]
    speichere_beitraege(blog_posts)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)