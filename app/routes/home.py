# Home module

from app.models import Post
from app.db import get_db

from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    #get all posts
    db = get_db()
    posts = db.query(Post).order_by(Post.created_at.desc()).all()
    return render_template('homepage.html', posts=posts)

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
    db = get_db()
    #get single post, filter acts as WHERE clause, one method instead of all
    post = db.query(Post).filter(Post.id==id).one()
    return render_template('single-post.html', post=post)

