from flask import Flask, render_template, url_for, redirect, request

from data_handling import json_functions as json_data

app = Flask(__name__)

@app.route('/')
def index():
    blog_posts = json_data.get_data()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        posts = json_data.get_data()
        # Auto-increment ID
        if posts:
            new_id = max(post["id"] for post in posts) + 1
        else:
            new_id = 1

        new_post = {
            "id": new_id,
            "author": request.form["author"],
            "title": request.form["title"],
            "content": request.form["content"],
            "likes": 0
        }
        json_data.add(new_post)
        return redirect(url_for("index"))

    return render_template('add.html')


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    posts = json_data.get_data()
    posts = [post for post in posts if post["id"] != post_id]
    json_data.save_data(posts)
    return redirect(url_for("index"))


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update_post(post_id):
    posts = json_data.get_data()
    # Find the post
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        return "Post not found", 404
    if request.method == 'POST':
            post["title"] = request.form["title"]
            post["content"] = request.form["content"]
            post["likes"] = 0
            json_data.save_data(posts)
            return redirect(url_for("index"))

    return render_template('update.html', post=post)


@app.route('/like/<int:post_id>', methods=['POST'])
def like_post(post_id):
    posts = json_data.get_data()
    post = next((p for p in posts if p["id"] == post_id), None)
    if post:
        post["likes"] += 1
        json_data.save_data(posts)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)