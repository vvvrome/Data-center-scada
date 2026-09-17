import sqlite3
import json
import logging
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "users.db"

# Directorio de logs
LOG_DIR = BASE_DIR.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

SECURITY_LOG = LOG_DIR / "security.log"


# Logger utilizado por Wazuh
security_logger = logging.getLogger("datacenter_security")
security_logger.setLevel(logging.INFO)

# Evitar añadir el handler varias veces cuando Flask recarga la aplicación
if not security_logger.handlers:
    file_handler = logging.FileHandler(
        SECURITY_LOG,
        encoding="utf-8"
    )

    file_handler.setLevel(logging.INFO)

    security_logger.addHandler(file_handler)

    security_logger.propagate = False


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_audit_database():

    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            username TEXT,

            action TEXT NOT NULL,

            result TEXT NOT NULL,

            ip_address TEXT,

            user_agent TEXT,

            details TEXT
        )
    """)

    connection.commit()
    connection.close()


def log_event(
    username,
    action,
    result,
    ip_address=None,
    user_agent=None,
    details=None
):

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO audit_log (
            username,
            action,
            result,
            ip_address,
            user_agent,
            details
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            username,
            action,
            result,
            ip_address,
            user_agent,
            details
        )
    )

    connection.commit()
    connection.close()

    # -------------------------------------------------
    # LOG PARA WAZUH
    # -------------------------------------------------

    wazuh_event = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "source": "DataCenter_Lab",
        "username": username,
        "action": action,
        "result": result,
        "ip_address": ip_address,
        "user_agent": user_agent,
        "details": details
    }

    security_logger.info(
        json.dumps(
            wazuh_event,
            ensure_ascii=False
        )
    )


def get_audit_logs(limit=200):

    connection = get_connection()

    logs = connection.execute(
        """
        SELECT
            id,
            timestamp,
            username,
            action,
            result,
            ip_address,
            user_agent,
            details
        FROM audit_log
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    ).fetchall()

    connection.close()

    return [dict(log) for log in logs]