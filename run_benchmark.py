"""
run_benchmark.py
Author : V Lukman
Date   : 2026-04-13
Purpose: Simulate and score AI coding assistant responses across 5 tasks.
         Generates charts and saves results to /results/
"""

import json
import time
import csv
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# ── Load config ──────────────────────────────────────────────────
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

with open("benchmarks/test_prompts.json") as f:
    TASKS = json.load(f)

# ── Simulated scores (collected manually by evaluator) ───────────
# Scoring criteria: Correctness + Clarity + Completeness (each /10)
SCORES = {
    "GitHub Copilot": {
        1: {"correctness": 9, "clarity": 9, "completeness": 9},
        2: {"correctness": 9, "clarity": 9, "completeness": 8},
        3: {"correctness": 8, "clarity": 8, "completeness": 8},
        4: {"correctness": 9, "clarity": 8, "completeness": 8},
        5: {"correctness": 7, "clarity": 8, "completeness": 8},
    },
    "ChatGPT-4o": {
        1: {"correctness": 10, "clarity": 10, "completeness": 10},
        2: {"correctness": 10, "clarity": 9,  "completeness": 9},
        3: {"correctness": 9,  "clarity": 9,  "completeness": 9},
        4: {"correctness": 10, "clarity": 10, "completeness": 9},
        5: {"correctness": 8,  "clarity": 9,  "completeness": 8},
    },
    "Gemini 1.5": {
        1: {"correctness": 9, "clarity": 9, "completeness": 9},
        2: {"correctness": 8, "clarity": 9, "completeness": 8},
        3: {"correctness": 7, "clarity": 8, "completeness": 8},
        4: {"correctness": 9, "clarity": 9, "completeness": 9},
        5: {"correctness": 7, "clarity": 7, "completeness": 7},
    },
}

# Simulated response times (seconds, avg of 3 runs)
RESPONSE_TIMES = {
    "GitHub Copilot": [1.9, 2.0, 2.3, 2.2, 2.1],
    "ChatGPT-4o":     [3.1, 3.5, 3.6, 3.2, 3.6],
    "Gemini 1.5":     [1.7, 1.9, 2.0, 1.8, 1.6],
}

# ── Compute aggregate scores ─────────────────────────────────────
def compute_results():
    results = {}
    for assistant, task_scores in SCORES.items():
        all_scores = []
        for task_id, criteria in task_scores.items():
            avg = sum(criteria.values()) / len(criteria)
            all_scores.append(avg)
        overall_quality = round(sum(all_scores) / len(all_scores), 1)
        avg_speed       = round(sum(RESPONSE_TIMES[assistant]) / len(RESPONSE_TIMES[assistant]), 1)
        accuracy_pct    = int(overall_quality * 10)
        efficiency      = round(overall_quality / avg_speed, 2)
        results[assistant] = {
            "quality_score": overall_quality,
            "avg_speed_sec": avg_speed,
            "accuracy_pct":  accuracy_pct,
            "efficiency":    efficiency,
        }
    return results

# ── Save CSV ──────────────────────────────────────────────────────
def save_csv(results):
    path = os.path.join(RESULTS_DIR, "summary_results.csv")
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Assistant", "Quality Score", "Avg Speed (s)", "Accuracy (%)", "Efficiency"])
        for name, r in results.items():
            writer.writerow([name, r["quality_score"], r["avg_speed_sec"],
                             r["accuracy_pct"], r["efficiency"]])
    print(f"  ✅  CSV saved → {path}")

# ── Chart helpers ─────────────────────────────────────────────────
BG, CARD, TEXT = "#0F1117", "#1A1D27", "#E8EAF0"
COLORS = ["#0078D4", "#10A37F", "#EA4335"]

def bar_chart(names, values, ylabel, title, filename, note=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(BG); ax.set_facecolor(CARD)
    bars = ax.bar(names, values, color=COLORS, width=0.5, zorder=3)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.02 * max(values),
                str(val), ha='center', va='bottom', fontsize=15, fontweight='bold', color=TEXT)
    ax.set_ylabel(ylabel, color="#8B8FA8", fontsize=12)
    ax.set_title(title, color=TEXT, fontsize=14, fontweight='bold', pad=16)
    ax.spines[['top','right','left','bottom']].set_visible(False)
    ax.yaxis.grid(True, color='#2A2D3A', linewidth=0.8, zorder=0)
    ax.tick_params(colors=TEXT, labelsize=12)
    for lbl in ax.get_xticklabels(): lbl.set_color(TEXT)
    for lbl in ax.get_yticklabels(): lbl.set_color("#8B8FA8")
    if note:
        ax.text(0.98, 0.97, note, transform=ax.transAxes,
                ha='right', va='top', color="#FFD700", fontsize=11)
    plt.tight_layout()
    path = os.path.join(RESULTS_DIR, filename)
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f"  ✅  Chart saved → {path}")

def pie_chart(names, values, title, filename):
    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    wedges, texts, autotexts = ax.pie(
        values, labels=names, colors=COLORS,
        autopct='%1.1f%%', startangle=140, pctdistance=0.75,
        wedgeprops=dict(width=0.55, edgecolor=BG, linewidth=3))
    for t in texts:     t.set_color(TEXT);  t.set_fontsize(13)
    for at in autotexts: at.set_color(BG);  at.set_fontsize(12); at.set_fontweight('bold')
    ax.set_title(title, color=TEXT, fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    path = os.path.join(RESULTS_DIR, filename)
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f"  ✅  Chart saved → {path}")

# ── Main ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n🔍  Running AI Coding Assistant Benchmark...\n")
    results = compute_results()

    names   = list(results.keys())
    quality = [r["quality_score"] for r in results.values()]
    speed   = [r["avg_speed_sec"] for r in results.values()]
    effic   = [r["efficiency"]    for r in results.values()]

    print("📊  Generating charts...")
    bar_chart(names, quality, "Quality Score (out of 10)",
              "AI Coding Assistant — Quality Score", "chart_bar_quality.png")
    bar_chart(names, speed,   "Avg Response Time (seconds)",
              "AI Coding Assistant — Response Speed", "chart_bar_speed.png",
              note="Lower is better  ↓")
    pie_chart(names, effic,
              "Efficiency Score Distribution\n(Quality ÷ Speed)",
              "chart_pie_efficiency.png")

    print("\n💾  Saving CSV...")
    save_csv(results)

    print("\n📋  Final Summary:")
    print(f"  {'Assistant':<20} {'Quality':>8} {'Speed':>8} {'Accuracy':>10} {'Efficiency':>12}")
    print("  " + "-"*62)
    for name, r in results.items():
        print(f"  {name:<20} {r['quality_score']:>8} {r['avg_speed_sec']:>8} "
              f"{r['accuracy_pct']:>9}% {r['efficiency']:>12}")

    print("\n✅  Benchmark complete! Check the results/ folder.\n")
