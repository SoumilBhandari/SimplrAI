"""Generate the clarity-by-grade-level figure for the SimplrAI paper."""
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
# FIGURE 2: Clarity Scores by Grade Level
# ============================================================
fig, ax = plt.subplots(figsize=(7.5, 4.2))
groups = ['Middle School\n(n = 29)', 'High School\n(n = 35)', 'College\n(n = 23)']
simplr = [6.41, 6.13, 5.87]
chatgpt = [4.21, 4.86, 5.39]
gemini = [4.48, 5.02, 5.31]
simplr_err = [0.31, 0.38, 0.42]
chatgpt_err = [0.49, 0.52, 0.44]
gemini_err = [0.42, 0.51, 0.43]

x = np.arange(len(groups)); width = 0.27
ax.bar(x - width, simplr, width, yerr=simplr_err, label='SimplrAI',
       color=NAVY, capsize=4, edgecolor='white', linewidth=1.2)
ax.bar(x, chatgpt, width, yerr=chatgpt_err, label='ChatGPT (GPT-5)',
       color=CORAL, capsize=4, edgecolor='white', linewidth=1.2)
ax.bar(x + width, gemini, width, yerr=gemini_err, label='Gemini 2.5 Pro',
       color=GOLD, capsize=4, edgecolor='white', linewidth=1.2)

ax.set_ylabel('Mean clarity rating (1–7 Likert)', fontsize=10.5)
ax.set_xticks(x); ax.set_xticklabels(groups, fontsize=10)
ax.set_ylim(0, 7.5); ax.set_yticks(range(0, 8))
ax.axhline(y=4, color=LIGHT_GRAY, linestyle='--', linewidth=1, zorder=0)
ax.text(2.55, 4.08, 'neutral', fontsize=8, color=GRAY, ha='right', style='italic')
ax.legend(loc='upper center', frameon=False, fontsize=9.5, ncol=3,
          bbox_to_anchor=(0.5, 1.10))
ax.grid(axis='y', alpha=0.18, zorder=0); ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig('fig2_clarity.pdf', bbox_inches='tight', facecolor='white')
plt.close()
print("fig2_clarity.pdf generated.")
