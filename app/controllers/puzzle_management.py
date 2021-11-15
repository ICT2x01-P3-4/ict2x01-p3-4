from ..models.puzzle import Puzzle
from flask import jsonify, request, render_template


def create_puzzle():
    """
    Creates a new puzzle in database.

    Returns:
        json response: message and status code if request method is POST.
        render_template: create_puzzle.html if request method is GET.
    """
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
    """
    Retrieve a puzzle from database.

    Args:
        puzzle_id (int): puzzle id to be retrieved.

    Returns:
        render_template: puzzle.html if puzzle is found. Otherwise, view_puzzle.html.
    """
    try:
        puzzle = Puzzle()
        puzzle_data = puzzle.get_puzzle(puzzle_id)
        return render_template("puzzle.html", puzzle=puzzle_data)
    except Exception as e:
        print(e)
        return render_template("view_puzzle.html", puzzle=None)


def find_puzzles():
    """
    Retrieve all puzzles from database.

    Returns:
        render_template: puzzle.html with puzzle list.
    """
    try:
        puzzle = Puzzle()
        puzzles = puzzle.get_all_puzzles()
        return render_template("puzzles.html", puzzles=puzzles)
    except Exception as e:
        print(e)
        return render_template("puzzles.html", puzzles=None)


def update_puzzle():
    """
    Updates a puzzle in database.

    Returns:
        json response: puzzle data and status code if request method is POST.
        render_template: update_puzzle.html if request method is GET.
    """
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
    """
    Deletes a puzzle from database.

    Args:
        puzzle_id (int): puzzle id to be deleted.

    Returns:
        json response: message and status code.
    """
    try:
        puzzle = Puzzle()
        deleted = puzzle.delete_puzzle(puzzle_id)

        if not deleted:
            return jsonify({"message": "Puzzle not found"}), 404

        return jsonify({"message": "Puzzle deleted"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Something went wrong"}), 500
