from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, Post

post_bp = Blueprint('post', __name__)

@post_bp.route('/posts', methods=['POST'])
@login_required
def create_post():
    content = request.form.get('content')
    new_post = Post(content=content, created_by_id=current_user.user_id)
    db.session.add(new_post)
    db.session.commit()
    
    flash('Post created successfully!', 'success')
    return redirect(url_for('home'))

@post_bp.route('/posts/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if post and post.created_by_id == current_user.user_id:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted successfully!', 'success')
    else:
        flash('You are not authorized to delete this post.', 'danger')
    
    return redirect(url_for('home'))
