from flask import render_template


def index():
    return render_template('admin/index.html')


def profile():
    return render_template('admin/profile.html')


def puzzle():
    return render_template('admin/puzzle.html')


def edit_puzzle(puzzle_id):
    return render_template('admin/edit_puzzle.html')


def create_puzzle():
    return render_template('admin/create_puzzle.html')
