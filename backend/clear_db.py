"""
Standalone utility to clear all tables in the MySQL database used by CodeTech.

Usage (from backend directory):
  python clear_db.py

Adjust the connection credentials below if needed.
"""

import mysql.connector


def clear_all_tables(conn):
    """Delete all data from all tables in correct dependency order.

    This disables foreign key checks, truncates child tables before parents to
    reset auto-increment IDs, then re-enables foreign key checks.
    """
    print("clear_all_tables run.")
    try:
        cursor = conn.cursor()
        # Disable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        # Truncate child tables first, then parents
        cursor.execute("TRUNCATE TABLE choices;")
        cursor.execute("TRUNCATE TABLE questions;")
        cursor.execute("TRUNCATE TABLE quizzes;")
        cursor.execute("TRUNCATE TABLE levels;")
        cursor.execute("TRUNCATE TABLE subjects;")
        cursor.execute("TRUNCATE TABLE user_activity;")
        cursor.execute("TRUNCATE TABLE user_progress;")
        cursor.execute("TRUNCATE TABLE user_quiz_progress;")
        cursor.execute("TRUNCATE TABLE users;")
        cursor.execute("TRUNCATE TABLE user_quiz_completion;")
        # Re-enable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        conn.commit()
        print("All tables cleared successfully.")
    except Exception as e:
        conn.rollback()
        print("Error clearing tables:", e)
    finally:
        cursor.close()


def main():
    # Update credentials if your local setup differs
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="adeodatus",
        database="codetech_db",
    )
    try:
        clear_all_tables(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()


