from flask import Blueprint, render_template, redirect
from utils import get_posts_bookmarks, add_bookmarks, remove_bookmarks
from logs.log_views import *


bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates', url_prefix='/bookmarks')


@bookmarks_blueprint.route('/')
def bookmarks_page():
    posts = get_posts_bookmarks()
    log_set('./logs/bookmarks.ini', f'Запрос /bookmarks/')
    return render_template('bookmarks.html', posts=posts)


@bookmarks_blueprint.route('/add/<int:post_id>')
def add_bookmarks_page(post_id):
    add_bookmarks(post_id)
    log_set('./logs/bookmarks.ini', f'Добавление /bookmarks/add/{post_id}')
    # posts = get_posts_bookmarks()
    return redirect("/", code=302)
    # return render_template('bookmarks.html', posts=posts)


@bookmarks_blueprint.route('/remove/<int:postid>')
def remove_bookmarks_page(postid):
    remove_bookmarks(postid)
    # posts = get_posts_bookmarks()
    log_set('./logs/bookmarks.ini', f'Удаление /bookmarks/remove/{postid}')
    return redirect("/", code=302)
    # return render_template('bookmarks.html', posts=posts)
