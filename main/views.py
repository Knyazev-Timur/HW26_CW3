from flask import Blueprint, render_template, request
from utils import *
from logs.log_views import log_set

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates', url_prefix='/')


@main_blueprint.route('/')
def page_index():
    posts = get_posts_all()
    count_bookmarks = len(get_posts_bookmarks())
    log_set('./logs/log.ini', f'Запрос главной страницы')
    return render_template('index.html', posts=posts, count_bookmarks=count_bookmarks)


@main_blueprint.route('/posts/<int:post_id>')
def page_post(post_id):
    comments = get_comments_by_post_id(post_id)
    post = get_post_by_pk(post_id)
    count_comment = len(comments)
    log_set('./logs/log.ini', f'Запрос /posts/{post_id}')
    return render_template('post.html', post=post, comments=comments, count=count_comment)


@main_blueprint.route('/posts/<user_name>')
def page_posts_user(user_name):
    all_post_user = get_posts_by_user(user_name)
    log_set('./logs/log.ini', f'Запрос /posts/{user_name}')
    return render_template('user-feed.html', posts=all_post_user)


@main_blueprint.route('/search')
def page_search():
    query = request.args.get('q')
    if query and query != '':
        posts = search_for_posts(query)
        count_posts = len(posts)
        log_set('./logs/log.ini', f'Запрос /search/{query}')
    return render_template('search.html', posts=posts, count_posts=count_posts, tag=query)


@main_blueprint.route('/tag/<tagname>')
def page_tag(tagname):
    posts = get_tag(tagname)
    log_set('./logs/log.ini', f'Запрос /tag/{tagname}')
    return render_template('tag.html', posts=posts, tag=tagname)
