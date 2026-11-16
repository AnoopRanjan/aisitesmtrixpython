#!/usr/bin/env python3
"""
Master Launcher - AI Tools Explorer
====================================
Quick launcher for running either the Web Application, Desktop GUI, or CLI.

Usage:
    python run.py          (Default: starts Web Application on http://127.0.0.1:5000)
    python run.py --gui    (Starts native Tkinter desktop GUI)
    python run.py --cli    (Starts interactive command line interface)
"""

import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description="AI Power Tools Explorer Launcher")
    parser.add_argument("--gui", action="store_true", help="Launch native Tkinter Desktop GUI")
    parser.add_argument("--cli", action="store_true", help="Launch Interactive Terminal CLI")
    parser.add_argument("--port", type=int, default=5000, help="Web server port (default: 5000)")
    parser.add_argument("--no-browser", action="store_true", help="Do not open browser automatically")
    args = parser.parse_args()

    if args.gui:
        import gui_app
        app = gui_app.AIToolsGUI()
        app.mainloop()
    elif args.cli:
        import cli
        cli.interactive_menu()
    else:
        import app
        app.start_server(port=args.port, open_browser=not args.no_browser)


if __name__ == "__main__":
    main()
