#!/usr/bin/env python3
"""
AI Tools Explorer - Native Desktop GUI Application (Tkinter)
=============================================================
A native desktop GUI application featuring tabbed navigation (ttk.Notebook),
one-paragraph operational descriptions, feature checklists, and one-click
launchers for official websites and embedded YouTube tutorials.

Usage:
    python gui_app.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

from tools_data import TOOLS_DATA


class AIToolsGUI(tk.Tk):
    """Main Desktop Window for AI Tools Explorer."""

    def __init__(self):
        super().__init__()
        self.title("AI Power Tools Explorer - Multi-Tab Desktop Hub")
        self.geometry("980;680".replace(";", "x"))
        self.minsize(850, 580)
        self.configure(bg="#0f172a")

        # Configure TTK styles
        self.setup_styles()

        # Top Banner
        self.create_header()

        # Notebook (Tabbed container)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)

        # Build tabs
        self.build_overview_tab()
        for tool in TOOLS_DATA:
            self.build_tool_tab(tool)
        self.build_video_gallery_tab()
        self.build_matrix_tab()

        # Status Bar
        self.create_status_bar()

    def setup_styles(self):
        """Configure modern dark theme styles for ttk widgets."""
        style = ttk.Style(self)
        style.theme_use("clam")

        # Notebook tabs
        style.configure("TNotebook", background="#0f172a", borderwidth=0)
        style.configure(
            "TNotebook.Tab",
            background="#1e293b",
            foreground="#cbd5e1",
            font=("Segoe UI", 9, "bold"),
            padding=[12, 6],
            borderwidth=0
        )
        style.map(
            "TNotebook.Tab",
            background=[("selected", "#3b82f6"), ("active", "#334155")],
            foreground=[("selected", "#ffffff"), ("active", "#f8fafc")]
        )

        # Frames & Labels
        style.configure("Dark.TFrame", background="#0f172a")
        style.configure("Card.TFrame", background="#1e293b", relief="flat")
        style.configure("Header.TLabel", background="#0f172a", foreground="#f8fafc", font=("Segoe UI", 16, "bold"))
        style.configure("SubHeader.TLabel", background="#0f172a", foreground="#94a3b8", font=("Segoe UI", 10))
        style.configure("ToolTitle.TLabel", background="#1e293b", foreground="#ffffff", font=("Segoe UI", 15, "bold"))
        style.configure("ToolTagline.TLabel", background="#1e293b", foreground="#94a3b8", font=("Segoe UI", 10, "italic"))
        style.configure("Section.TLabel", background="#1e293b", foreground="#38bdf8", font=("Segoe UI", 11, "bold"))

        # Buttons
        style.configure(
            "Primary.TButton",
            background="#2563eb",
            foreground="#ffffff",
            font=("Segoe UI", 9, "bold"),
            padding=[10, 5],
            borderwidth=0
        )
        style.map("Primary.TButton", background=[("active", "#1d4ed8")])

        style.configure(
            "Secondary.TButton",
            background="#334155",
            foreground="#e2e8f0",
            font=("Segoe UI", 9),
            padding=[8, 4],
            borderwidth=0
        )
        style.map("Secondary.TButton", background=[("active", "#475569")])

        style.configure(
            "Video.TButton",
            background="#dc2626",
            foreground="#ffffff",
            font=("Segoe UI", 9, "bold"),
            padding=[10, 5],
            borderwidth=0
        )
        style.map("Video.TButton", background=[("active", "#b91c1c")])

    def create_header(self):
        """Create the top window header."""
        header_frame = ttk.Frame(self, style="Dark.TFrame")
        header_frame.pack(fill=tk.X, padx=16, pady=(12, 4))

        title = ttk.Label(header_frame, text="⚡ AI Power Tools Directory & Hub", style="Header.TLabel")
        title.pack(anchor=tk.W)

        subtitle = ttk.Label(
            header_frame,
            text="Explore 9 essential AI tools with one-paragraph summaries, YouTube guides, and instant web links.",
            style="SubHeader.TLabel"
        )
        subtitle.pack(anchor=tk.W)

    def create_status_bar(self):
        """Create bottom status bar."""
        status_frame = ttk.Frame(self, style="Dark.TFrame")
        status_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=12, pady=(0, 6))

        status_text = ttk.Label(
            status_frame,
            text=f"Ready • 9 AI Tools Loaded • Python Desktop Application (Tkinter)",
            style="SubHeader.TLabel"
        )
        status_text.pack(side=tk.LEFT)

        web_btn = ttk.Button(
            status_frame,
            text="Launch Web App Version",
            style="Secondary.TButton",
            command=self.open_local_web_app
        )
        web_btn.pack(side=tk.RIGHT)

    def open_local_web_app(self):
        """Open web app in default browser."""
        webbrowser.open("http://127.0.0.1:5000")

    def build_overview_tab(self):
        """Build Overview tab with list of all 9 tools."""
        tab = ttk.Frame(self.notebook, style="Dark.TFrame")
        self.notebook.add(tab, text="📋 All Tools Overview")

        # Scrollable canvas
        canvas = tk.Canvas(tab, bg="#0f172a", highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style="Dark.TFrame")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=930)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)

        # Overview cards
        for idx, tool in enumerate(TOOLS_DATA):
            card = ttk.Frame(scrollable_frame, style="Card.TFrame", padding=12)
            card.pack(fill=tk.X, expand=True, pady=6, padx=4)

            # Card Header
            row1 = ttk.Frame(card, style="Card.TFrame")
            row1.pack(fill=tk.X, expand=True)

            t_name = ttk.Label(row1, text=f"{idx+1}. {tool['name']}", style="ToolTitle.TLabel")
            t_name.pack(side=tk.LEFT)

            t_cat = tk.Label(
                row1,
                text=tool["category"],
                bg=tool["badge_color"],
                fg="#ffffff",
                font=("Segoe UI", 8, "bold"),
                padx=6,
                pady=2
            )
            t_cat.pack(side=tk.RIGHT)

            # Tagline
            t_tagline = ttk.Label(card, text=tool["tagline"], style="ToolTagline.TLabel")
            t_tagline.pack(anchor=tk.W, pady=(2, 6))

            # Description snippet
            desc_text = tk.Text(
                card,
                height=3,
                wrap=tk.WORD,
                bg="#1e293b",
                fg="#cbd5e1",
                font=("Segoe UI", 9),
                relief="flat",
                highlightthickness=0
            )
            desc_text.insert(tk.END, tool["description"])
            desc_text.config(state=tk.DISABLED)
            desc_text.pack(fill=tk.X, pady=4)

            # Actions Row
            row2 = ttk.Frame(card, style="Card.TFrame")
            row2.pack(fill=tk.X, pady=(6, 0))

            btn_details = ttk.Button(
                row2,
                text=f"View Full Tab",
                style="Primary.TButton",
                command=lambda tid=tool["id"]: self.switch_to_tool_tab(tid)
            )
            btn_details.pack(side=tk.LEFT, padx=(0, 6))

            btn_site = ttk.Button(
                row2,
                text="Visit Website",
                style="Secondary.TButton",
                command=lambda url=tool["url"]: webbrowser.open(url)
            )
            btn_site.pack(side=tk.LEFT, padx=6)

            btn_yt = ttk.Button(
                row2,
                text="Watch YouTube Video",
                style="Video.TButton",
                command=lambda yid=tool["youtube_id"]: webbrowser.open(f"https://www.youtube.com/watch?v={yid}")
            )
            btn_yt.pack(side=tk.RIGHT)

    def build_tool_tab(self, tool):
        """Build a dedicated tab for a specific tool."""
        tab = ttk.Frame(self.notebook, style="Dark.TFrame")
        self.notebook.add(tab, text=tool["name"].split()[-1])  # Short tab name

        # Container card
        container = ttk.Frame(tab, style="Card.TFrame", padding=18)
        container.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

        # Header
        top_bar = ttk.Frame(container, style="Card.TFrame")
        top_bar.pack(fill=tk.X, pady=(0, 8))

        title = ttk.Label(top_bar, text=tool["name"], style="ToolTitle.TLabel")
        title.pack(side=tk.LEFT)

        cat_badge = tk.Label(
            top_bar,
            text=f"{tool['category']} • {tool['pricing']}",
            bg=tool["badge_color"],
            fg="#ffffff",
            font=("Segoe UI", 9, "bold"),
            padx=8,
            pady=3
        )
        cat_badge.pack(side=tk.RIGHT)

        tagline = ttk.Label(container, text=tool["tagline"], style="ToolTagline.TLabel")
        tagline.pack(anchor=tk.W, pady=(0, 10))

        # Action Buttons Top
        btn_bar = ttk.Frame(container, style="Card.TFrame")
        btn_bar.pack(fill=tk.X, pady=(0, 12))

        ttk.Button(
            btn_bar,
            text=f"🌐 Open {tool['url']}",
            style="Primary.TButton",
            command=lambda: webbrowser.open(tool["url"])
        ).pack(side=tk.LEFT, padx=(0, 8))

        ttk.Button(
            btn_bar,
            text="▶ Watch Embedded YouTube Video",
            style="Video.TButton",
            command=lambda: webbrowser.open(f"https://www.youtube.com/watch?v={tool['youtube_id']}")
        ).pack(side=tk.LEFT, padx=8)

        ttk.Button(
            btn_bar,
            text="📋 Copy Description",
            style="Secondary.TButton",
            command=lambda: self.copy_to_clipboard(tool["description"])
        ).pack(side=tk.LEFT, padx=8)

        # Section: Description (One Paragraph)
        sec_desc = ttk.Label(container, text="📌 How It Works & How It Can Help (Single Paragraph):", style="Section.TLabel")
        sec_desc.pack(anchor=tk.W, pady=(6, 4))

        desc_box = tk.Text(
            container,
            height=6,
            wrap=tk.WORD,
            bg="#0f172a",
            fg="#f8fafc",
            font=("Segoe UI", 10),
            padx=10,
            pady=10,
            relief="solid",
            borderwidth=1,
            highlightbackground="#334155"
        )
        desc_box.insert(tk.END, tool["description"])
        desc_box.config(state=tk.DISABLED)
        desc_box.pack(fill=tk.X, pady=(0, 12))

        # Split Columns for Features & Benefits
        cols_frame = ttk.Frame(container, style="Card.TFrame")
        cols_frame.pack(fill=tk.BOTH, expand=True)

        col_left = ttk.Frame(cols_frame, style="Card.TFrame")
        col_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8))

        col_right = ttk.Frame(cols_frame, style="Card.TFrame")
        col_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(8, 0))

        # Key Features
        ttk.Label(col_left, text="⭐ Key Features:", style="Section.TLabel").pack(anchor=tk.W, pady=(0, 6))
        for feat in tool["key_features"]:
            f_lbl = tk.Label(
                col_left,
                text=f"✔  {feat}",
                bg="#1e293b",
                fg="#cbd5e1",
                font=("Segoe UI", 9),
                wraplength=420,
                justify=tk.LEFT,
                anchor=tk.W
            )
            f_lbl.pack(fill=tk.X, pady=2)

        # How It Helps
        ttk.Label(col_right, text="💡 Practical Benefits:", style="Section.TLabel").pack(anchor=tk.W, pady=(0, 6))
        for benefit in tool["how_it_helps"]:
            b_lbl = tk.Label(
                col_right,
                text=f"🚀  {benefit}",
                bg="#1e293b",
                fg="#38bdf8",
                font=("Segoe UI", 9),
                wraplength=420,
                justify=tk.LEFT,
                anchor=tk.W
            )
            b_lbl.pack(fill=tk.X, pady=2)

    def build_video_gallery_tab(self):
        """Build Video Gallery tab with direct YouTube launch buttons."""
        tab = ttk.Frame(self.notebook, style="Dark.TFrame")
        self.notebook.add(tab, text="🎥 Video Gallery")

        canvas = tk.Canvas(tab, bg="#0f172a", highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style="Dark.TFrame")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=930)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)

        for tool in TOOLS_DATA:
            vcard = ttk.Frame(scrollable_frame, style="Card.TFrame", padding=10)
            vcard.pack(fill=tk.X, expand=True, pady=4, padx=4)

            row = ttk.Frame(vcard, style="Card.TFrame")
            row.pack(fill=tk.X)

            info = ttk.Frame(row, style="Card.TFrame")
            info.pack(side=tk.LEFT, fill=tk.X, expand=True)

            ttk.Label(info, text=f"{tool['name']} - Tutorial Video", style="ToolTitle.TLabel").pack(anchor=tk.W)
            ttk.Label(info, text=tool["youtube_title"], style="ToolTagline.TLabel").pack(anchor=tk.W)
            ttk.Label(info, text=f"YouTube ID: {tool['youtube_id']}", style="SubHeader.TLabel").pack(anchor=tk.W)

            btn = ttk.Button(
                row,
                text="▶ Play Video",
                style="Video.TButton",
                command=lambda yid=tool["youtube_id"]: webbrowser.open(f"https://www.youtube.com/watch?v={yid}")
            )
            btn.pack(side=tk.RIGHT, padx=8)

    def build_matrix_tab(self):
        """Build comparison table tab."""
        tab = ttk.Frame(self.notebook, style="Dark.TFrame")
        self.notebook.add(tab, text="📊 Comparison Matrix")

        container = ttk.Frame(tab, style="Card.TFrame", padding=12)
        container.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

        columns = ("Name", "Category", "Developer", "Pricing", "Top Capability")
        tree = ttk.Treeview(container, columns=columns, show="headings", height=12)

        tree.heading("Name", text="Tool Name")
        tree.heading("Category", text="Primary Domain")
        tree.heading("Developer", text="Developer")
        tree.heading("Pricing", text="Pricing Model")
        tree.heading("Top Capability", text="Standout Capability")

        tree.column("Name", width=150)
        tree.column("Category", width=220)
        tree.column("Developer", width=120)
        tree.column("Pricing", width=160)
        tree.column("Top Capability", width=280)

        for tool in TOOLS_DATA:
            tree.insert(
                "",
                tk.END,
                values=(
                    tool["name"],
                    tool["category"],
                    tool["developer"],
                    tool["pricing"],
                    tool["key_features"][0]
                )
            )

        tree.pack(fill=tk.BOTH, expand=True)

    def switch_to_tool_tab(self, tool_id):
        """Switch notebook to a specific tool tab."""
        for idx, tool in enumerate(TOOLS_DATA):
            if tool["id"] == tool_id:
                # Tab index: 0 is overview, so tool tabs start at 1
                self.notebook.select(idx + 1)
                break

    def copy_to_clipboard(self, text):
        """Copy given text to system clipboard."""
        self.clipboard_clear()
        self.clipboard_append(text)
        messagebox.showinfo("Copied", "Description copied to clipboard!")


if __name__ == "__main__":
    app = AIToolsGUI()
    app.mainloop()
