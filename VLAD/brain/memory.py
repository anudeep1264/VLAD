import sqlite3
from pathlib import Path
import time

DB_PATH = Path("data")
DB_PATH.mkdir(exist_ok=True)
DB_FILE = DB_PATH / "vlad_memory.db"

class Memory:

    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE, check_same_thread=False)
        self._create_tables()

    def _create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS preferences (
            key TEXT PRIMARY KEY,
            value TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            command TEXT,
            timestamp REAL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS security_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alert TEXT,
            timestamp REAL
        )
        """)

        self.conn.commit()

    # ---------- Preferences ----------
    def set_pref(self, key, value):
        self.conn.execute(
            "INSERT OR REPLACE INTO preferences VALUES (?, ?)",
            (key, value)
        )
        self.conn.commit()

    def get_pref(self, key, default=None):
        cur = self.conn.execute(
            "SELECT value FROM preferences WHERE key=?",
            (key,)
        )
        row = cur.fetchone()
        return row[0] if row else default

    # ---------- History ----------
    def remember_command(self, command):
        self.conn.execute(
            "INSERT INTO history (command, timestamp) VALUES (?, ?)",
            (command, time.time())
        )
        self.conn.commit()

    # ---------- Security ----------
    def log_security(self, alert):
        self.conn.execute(
            "INSERT INTO security_logs (alert, timestamp) VALUES (?, ?)",
            (alert, time.time())
        )
        self.conn.commit()
