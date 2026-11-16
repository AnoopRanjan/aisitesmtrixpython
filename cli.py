#!/usr/bin/env python3
"""
AI Tools Explorer - Interactive Command Line Interface (CLI)
=============================================================
Query, inspect, and open AI tools and their YouTube tutorials from the terminal.

Usage:
    python cli.py [list | show <id> | search <query> | open <id> | video <id>]
"""

import sys
import webbrowser
from tools_data import TOOLS_DATA


def print_header():
    print("=" * 75)
    print(" ⚡ AI POWER TOOLS DIRECTORY - COMMAND LINE INTERFACE")
    print("=" * 75)


def list_tools():
    print_header()
    print(f"{'#':<3} {'ID':<15} {'Name':<22} {'Category':<32}")
    print("-" * 75)
    for idx, t in enumerate(TOOLS_DATA, 1):
        print(f"{idx:<3} {t['id']:<15} {t['name']:<22} {t['category']:<32}")
    print("=" * 75)
    print("Run: python cli.py show <id> to view full one-paragraph details.")


def show_tool(tool_id):
    tool = next((t for t in TOOLS_DATA if t["id"].lower() == tool_id.lower()), None)
    if not tool:
        print(f"[-] Error: Tool '{tool_id}' not found.")
        print(f"Available IDs: {', '.join(t['id'] for t in TOOLS_DATA)}")
        return

    print_header()
    print(f"Tool Name   : {tool['name']}")
    print(f"Category    : {tool['category']}")
    print(f"Developer   : {tool['developer']}")
    print(f"Pricing     : {tool['pricing']}")
    print(f"Official URL: {tool['url']}")
    print(f"YouTube ID  : {tool['youtube_id']}")
    print(f"YouTube URL : https://www.youtube.com/watch?v={tool['youtube_id']}")
    print(f"Video Title : {tool['youtube_title']}")
    print("-" * 75)
    print("📌 HOW IT WORKS & HOW IT CAN HELP (ONE-PARAGRAPH SUMMARY):")
    print(tool["description"])
    print("-" * 75)
    print("⭐ KEY FEATURES:")
    for feat in tool["key_features"]:
        print(f"  • {feat}")
    print("\n💡 PRACTICAL BENEFITS:")
    for b in tool["how_it_helps"]:
        print(f"  • {b}")
    print("=" * 75)


def search_tools(query):
    print_header()
    q = query.lower()
    matches = [
        t for t in TOOLS_DATA
        if q in t["name"].lower()
        or q in t["category"].lower()
        or q in t["description"].lower()
        or q in t["tagline"].lower()
    ]
    print(f"Search results for '{query}' ({len(matches)} found):")
    print("-" * 75)
    for t in matches:
        print(f"• {t['name']} [{t['id']}] - {t['category']}")
        print(f"  URL: {t['url']}")
        print(f"  Tagline: {t['tagline']}\n")
    print("=" * 75)


def open_tool(tool_id, target="web"):
    tool = next((t for t in TOOLS_DATA if t["id"].lower() == tool_id.lower()), None)
    if not tool:
        print(f"[-] Error: Tool '{tool_id}' not found.")
        return

    if target == "video":
        url = f"https://www.youtube.com/watch?v={tool['youtube_id']}"
        print(f"[+] Opening YouTube tutorial: {url}")
    else:
        url = tool["url"]
        print(f"[+] Opening official site: {url}")

    webbrowser.open(url)


def interactive_menu():
    while True:
        print_header()
        print("1. List All 9 AI Tools")
        print("2. View Specific Tool (One-Paragraph Details & Video Info)")
        print("3. Search Tools by Keyword")
        print("4. Launch Web Browser to Official Tool")
        print("5. Launch YouTube Tutorial Video")
        print("6. Start Local Web Application (app.py)")
        print("0. Exit")
        print("-" * 75)
        choice = input("Select an option (0-6): ").strip()

        if choice == "1":
            list_tools()
            input("\nPress Enter to return to menu...")
        elif choice == "2":
            tid = input("Enter Tool ID (e.g. notebooklm, stitch, claude): ").strip()
            show_tool(tid)
            input("\nPress Enter to return to menu...")
        elif choice == "3":
            q = input("Enter search keyword: ").strip()
            search_tools(q)
            input("\nPress Enter to return to menu...")
        elif choice == "4":
            tid = input("Enter Tool ID to open in browser: ").strip()
            open_tool(tid, target="web")
        elif choice == "5":
            tid = input("Enter Tool ID to watch tutorial: ").strip()
            open_tool(tid, target="video")
        elif choice == "6":
            from app import start_server
            start_server(open_browser=True)
            break
        elif choice == "0":
            print("\nGoodbye!")
            break
        else:
            print("[!] Invalid option. Please try again.")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive_menu()
    else:
        cmd = sys.argv[1].lower()
        if cmd == "list":
            list_tools()
        elif cmd == "show" and len(sys.argv) > 2:
            show_tool(sys.argv[2])
        elif cmd == "search" and len(sys.argv) > 2:
            search_tools(" ".join(sys.argv[2:]))
        elif cmd == "open" and len(sys.argv) > 2:
            open_tool(sys.argv[2], target="web")
        elif cmd == "video" and len(sys.argv) > 2:
            open_tool(sys.argv[2], target="video")
        else:
            print("Usage: python cli.py [list | show <id> | search <query> | open <id> | video <id>]")
