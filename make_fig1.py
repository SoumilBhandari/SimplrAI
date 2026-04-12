"""Generate the study design flowchart figure for the SimplrAI paper."""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Bitstream Vera Serif', 'Liberation Serif'],
    'font.size': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.edgecolor': '#2B2B2B',
    'axes.labelcolor': '#2B2B2B',
    'xtick.color': '#2B2B2B',
    'ytick.color': '#2B2B2B',
})

NAVY = '#1F3A68'
TEAL = '#2A9D8F'
CORAL = '#E76F51'
GOLD = '#E9C46A'
GRAY = '#6E7A86'
LIGHT_GRAY = '#D9DEE3'

# ============================================================
# FIGURE 1: Study Design Flowchart
# ============================================================
fig, ax = plt.subplots(figsize=(8.5, 4.2))
ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis('off')

def box(x, y, w, h, text, color, text_color='white', fontsize=9):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04",
                       linewidth=0, facecolor=color)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center',
            fontsize=fontsize, color=text_color, weight='bold')

def arrow(x1, y1, x2, y2):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='->',
                        mutation_scale=14, color='#4A4A4A', linewidth=1.3)
    ax.add_patch(a)

box(0.3, 3.7, 1.9, 0.9, "Recruitment\nN = 98", NAVY)
box(2.6, 3.7, 1.9, 0.9, "Consent &\nPre-Test", NAVY)
box(4.9, 3.7, 1.9, 0.9, "Random\nAssignment", TEAL)
box(7.2, 3.7, 2.5, 0.9, "Subject Rotation\n(Algebra · Bio · History)", TEAL)
box(0.3, 1.9, 3.0, 0.9, "SimplrAI (n = 30)\nstudy with structured AI", CORAL)
box(3.5, 1.9, 3.0, 0.9, "ChatGPT (n = 29)\nstudy with GPT-5", GOLD, text_color='#2B2B2B')
box(6.7, 1.9, 3.0, 0.9, "Control (n = 28)\ntextbook only", GRAY)
box(1.5, 0.2, 7, 0.9, "Post-Test  +  Survey (clarity · trust · helpfulness · reading difficulty)\nExpert Accuracy Review of all AI outputs (two-rater)", NAVY)

arrow(2.2, 4.15, 2.6, 4.15)
arrow(4.5, 4.15, 4.9, 4.15)
arrow(6.8, 4.15, 7.2, 4.15)
arrow(2.5, 3.7, 1.8, 2.85)
arrow(5.85, 3.7, 5.0, 2.85)
arrow(8.45, 3.7, 8.2, 2.85)
arrow(1.8, 1.9, 3.5, 1.15)
arrow(5.0, 1.9, 5.0, 1.15)
arrow(8.2, 1.9, 6.5, 1.15)

plt.tight_layout()
plt.savefig('fig1_design.pdf', bbox_inches='tight', facecolor='white')
plt.close()
print("fig1_design.pdf generated.")
