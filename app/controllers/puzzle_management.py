from flask.templating import render_template
from ..models.puzzle import Puzzle
from flask import jsonify, request


def create_puzzle():
    """Creates a new puzzle in database"""
    if request.method == "POST":
        try:
            data = request.get_json()
            puzzle = Puzzle(data)
            puzzle.create_puzzle(puzzle)

            return jsonify({"message": f"{puzzle.get_name()} created successfully"}), 201
        except Exception as e:
            print(e)
            return jsonify({"message": "Something went wrong"}), 500
    else:
        return render_template("create_puzzle.html")


def find_puzzle(puzzle_id):
    """Gets a puzzle from database"""
    try:
        puzzle = Puzzle()
        puzzle_data = puzzle.get_puzzle(puzzle_id)
        return render_template("puzzle.html", puzzle=puzzle_data)
    except Exception as e:
        print(e)
        return render_template("view_puzzle.html", puzzle=None)


def find_puzzles():
    """Gets all puzzles from database"""
    try:
        puzzle = Puzzle()
        puzzles = puzzle.get_all_puzzles()
        return render_template("puzzles.html", puzzles=puzzles)
    except Exception as e:
        print(e)
        return render_template("puzzles.html", puzzles=None)


def update_puzzle():
    """Updates a puzzle in database"""
    if request.method == "POST":
        try:
            data = request.get_json()
            puzzle = Puzzle(data)
            updated = puzzle.update_puzzle(puzzle)

            if not updated:
                return jsonify({"message": "Puzzle not found"}), 404

            return jsonify(data), 200
        except Exception as e:
            print(e)
            return jsonify({"message": "Something went wrong"}), 500
    else:
        return render_template("update_puzzle.html")


def delete_puzzle(puzzle_id):
    """Deletes a puzzle from database"""
    try:
        puzzle = Puzzle()
        deleted = puzzle.delete_puzzle(puzzle_id)

        if not deleted:
            return jsonify({"message": "Puzzle not found"}), 404

        return jsonify(deleted), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Something went wrong"}), 500
