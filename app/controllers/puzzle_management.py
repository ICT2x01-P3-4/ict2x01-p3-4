from ..models.puzzle import Puzzle
from flask import jsonify, request


def create_puzzle():
    """Creates a new puzzle in database"""
    try:
        data = request.get_json()
        puzzle = Puzzle(data)
        puzzle.create_puzzle(puzzle)

        return jsonify({"message": f"{puzzle.get_name()} created successfully"}), 201
    except Exception as e:
        print(e)
        return jsonify({"message": "Something went wrong"}), 500


def find_puzzle(puzzle_id):
    """Gets a puzzle from database"""
    try:
        puzzle = Puzzle()
        puzzle_data = puzzle.get_puzzle(puzzle_id)
        print(puzzle_data)
        return jsonify(puzzle_data), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Something went wrong"}), 500


def find_puzzles():
    """Gets all puzzles from database"""
    try:
        puzzle = Puzzle()
        puzzles = puzzle.get_all_puzzles()
        return jsonify(puzzles), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Something went wrong"}), 500


def update_puzzle():
    """Updates a puzzle in database"""
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
