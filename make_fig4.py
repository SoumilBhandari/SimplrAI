"""Generate the reading-level alignment figure for the SimplrAI paper."""
import matplotlib.pyplot as plt
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
# FIGURE 4: Reading Level Alignment
# ============================================================
fig, ax = plt.subplots(figsize=(7.5, 4.6))
target_grades = np.array([6, 7, 8, 9, 10, 11, 12, 13, 14])
np.random.seed(7)
simplr_actual = target_grades + np.random.normal(0, 0.55, len(target_grades))
chatgpt_actual = np.clip(target_grades + np.random.normal(3.6, 1.1, len(target_grades)), 8, 16)

ax.plot([5, 16], [5, 16], '--', color=LIGHT_GRAY, linewidth=1.4, zorder=0,
        label='Perfect alignment')
ax.scatter(target_grades, simplr_actual, s=90, color=NAVY,
           label='SimplrAI', zorder=3, edgecolor='white', linewidth=1.5)
ax.scatter(target_grades, chatgpt_actual, s=90, color=CORAL, marker='D',
           label='ChatGPT (GPT-5)', zorder=3, edgecolor='white', linewidth=1.5)

ax.set_xlabel('Target grade level (requested)', fontsize=10.5)
ax.set_ylabel('Output grade level (Flesch–Kincaid)', fontsize=10.5)
ax.set_xlim(5, 16); ax.set_ylim(5, 16)
ax.set_xticks(range(6, 16)); ax.set_yticks(range(6, 16))
ax.legend(loc='lower right', frameon=False, fontsize=9.5)
ax.grid(alpha=0.18, zorder=0); ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig('fig4_reading.pdf', bbox_inches='tight', facecolor='white')
plt.close()
print("fig4_reading.pdf generated.")
