# ============================================================
# RIBU SYSTEM - Configuration (v2 — Full Improvement Pass)
# ============================================================

from pathlib import Path

# --- Authentication ---
USERNAME = "RIBU"
PASSWORD = "gladrebecca91"

# --- Rule34 API (in-memory only) ---
RULE34_USER_ID = "6742761"
RULE34_API_KEY = "359627ee201efa5568a9b2905343b97a7520edc352a20471b0dd230e53a627d6b344ac30a6841bb57ea1299cf2ceaf736743f2dcc2cac823616195b3e79ac2aa"
RULE34_ENABLED = True

# --- Database ---
DB_PATH = str(Path(__file__).resolve().parent / "data" / "ribu_system.db")

# --- Visual Theme (more System / holographic) ---
COLORS = {
    "bg_dark": "#0a0a10",
    "bg_panel": "#12121c",
    "bg_card": "#1a1a28",
    "bg_input": "#141422",
    "accent_cyan": "#00e5ff",
    "accent_purple": "#c44dff",
    "accent_gold": "#ffd54a",
    "accent_red": "#ff3b4a",
    "accent_corruption": "#a02040",
    "text_primary": "#eef0f6",
    "text_secondary": "#9aa0b4",
    "success": "#2ef2a8",
    "warning": "#ffb020",
    "border": "#2c2c3c",
    "border_soft": "#222232",
    "glow": "#00e5ff33",
}

# --- EXP System ---
def exp_required_for_level(level: int) -> int:
    return int(850 * (level ** 1.55))

HABIT_EXP = {
    "PR": 18, "GER": 20, "MS": 22, "CD": 25,
    "PUMP": 22, "YTB": 18, "Q": 18, "LOGIN": 10,
}

PERFECT_DAY_BONUS = 60
# Linear streak EXP bonus: streak N → +N×10% on all positive EXP (NO CAP)
# final = base * (1 + STREAK_BONUS_PER_DAY * current_streak)
STREAK_BONUS_PER_DAY = 0.10
STREAK_MULTIPLIERS = {7: 1.25, 14: 1.50, 30: 1.75}  # legacy; linear streak is primary

# Variable reward system
EXP_VARIANCE_CHANCE = 0.35          # 35% chance of variance
EXP_VARIANCE_MIN = 0.15             # +15%
EXP_VARIANCE_MAX = 0.40             # +40%
CRITICAL_CLEAR_CHANCE = 0.06        # 6% chance Critical Clear
CRITICAL_CLEAR_MULTIPLIER = 2.2
SYSTEM_BONUS_DAY_CHANCE = 0.08      # 8% chance the day is a System Bonus day
SYSTEM_BONUS_MULTIPLIER = 1.5
TITLE_DROP_CHANCE = 0.04            # rare title drop on perfect day

MISSED_DAY_PENALTY_EXP = 520
PARTNER_LOCK_HOURS = 36

# --- Shadow Energy (secondary resource) ---
SHADOW_ENERGY_MAX = 100
SHADOW_ENERGY_START = 50
SHADOW_GAIN_PERFECT_DAY = 8
SHADOW_GAIN_STREAK_DAY = 3
SHADOW_LOSS_MISSED_DAY = 18
SHADOW_LOSS_FAILED_QUEST = 12
SHADOW_LOSS_MS_BREAK = 10
SHADOW_FULL_BUFF_EXP = 1.15         # +15% EXP when full
SHADOW_LOW_THRESHOLD = 20

# --- Corruption ---
CORRUPTION_MAX = 100
CORRUPTION_GAIN_MS_FAIL_AND_GOON = 12
CORRUPTION_GAIN_MS_FAIL = 4
CORRUPTION_REDUCE_CLEAN_DAY = 3      # MS done + no goon that day
CORRUPTION_REDUCE_STREAK_7 = 8

# --- Habits ---
HABITS = [
    ("LOGIN", "Daily System Login", "Spiritual"),
    ("PR", "Prayer", "Spiritual"),
    ("GER", "German Study", "Intellectual"),
    ("MS", "No Masturbation", "Spiritual"),
    ("CD", "Coding", "Intellectual"),
    ("PUMP", "Physical Training", "Physical"),
    ("YTB", "YouTube Shorts", "Skillful"),
    ("Q", "Holy Book", "Spiritual"),
]

# --- Rank System ---
RANKS = [
    (1, "E-Rank"),
    (5, "D-Rank"),
    (10, "C-Rank"),
    (18, "B-Rank"),
    (28, "A-Rank"),
    (40, "S-Rank"),
    (55, "National Level"),
]

def get_rank_for_level(level: int) -> str:
    rank = "E-Rank"
    for req, name in RANKS:
        if level >= req:
            rank = name
    return rank

# --- Partners ---
PARTNERS = [
    {"id": 1, "name": "Marin Kitagawa", "min_level": 1, "tier": "early", "tags": ["marin_kitagawa"]},
    {"id": 2, "name": "Yor Forger", "min_level": 3, "tier": "early", "tags": ["yor_forger"]},
    {"id": 3, "name": "Frieren", "min_level": 5, "tier": "early", "tags": ["frieren"]},
    {"id": 4, "name": "Violet Evergarden", "min_level": 7, "tier": "early", "tags": ["violet_evergarden"]},
    {"id": 5, "name": "Rem", "min_level": 9, "tier": "early", "tags": ["rem_(re:zero)"]},
    {"id": 6, "name": "Tashigi", "min_level": 11, "tier": "early", "tags": ["tashigi"]},
    {"id": 7, "name": "Female Goblins", "min_level": 13, "tier": "early", "tags": ["goblin_girl", "female_goblin"]},
    {"id": 8, "name": "Asuna Yuuki", "min_level": 16, "tier": "mid", "tags": ["asuna_yuuki"]},
    {"id": 9, "name": "Raphtalia", "min_level": 18, "tier": "mid", "tags": ["raphtalia"]},
    {"id": 10, "name": "Shion", "min_level": 20, "tier": "mid", "tags": ["shion_(tensei_shitara_slime_datta_ken)"]},
    {"id": 11, "name": "Zero Two", "min_level": 22, "tier": "mid", "tags": ["zero_two"]},
    {"id": 12, "name": "Carrot", "min_level": 24, "tier": "mid", "tags": ["carrot_(one_piece)"]},
    {"id": 13, "name": "Elves", "min_level": 26, "tier": "mid", "tags": ["elf", "female_elf"]},
    {"id": 14, "name": "Rias Gremory", "min_level": 31, "tier": "high", "tags": ["rias_gremory"]},
    {"id": 15, "name": "Akeno Himejima", "min_level": 34, "tier": "high", "tags": ["akeno_himejima"]},
    {"id": 16, "name": "Esdeath", "min_level": 37, "tier": "high", "tags": ["esdeath"]},
    {"id": 17, "name": "Makima", "min_level": 40, "tier": "high", "tags": ["makima"]},
    {"id": 18, "name": "Albedo", "min_level": 43, "tier": "high", "tags": ["albedo_(overlord)"]},
    {"id": 19, "name": "Boa Hancock", "min_level": 46, "tier": "high", "tags": ["boa_hancock"]},
    {"id": 20, "name": "Demoness / Female Demons", "min_level": 50, "tier": "high", "tags": ["demon_girl", "succubus", "female_demon"]},
]

# --- Titles with real power ---
TITLES = {
    "Novice": {"bonus": None, "desc": "Starting title"},
    "Disciplined": {"bonus": {"MS": 0.05}, "desc": "+5% EXP from MS"},
    "Iron Body": {"bonus": {"PUMP": 0.08}, "desc": "+8% EXP from PUMP"},
    "Scholar": {"bonus": {"GER": 0.05, "CD": 0.05}, "desc": "+5% EXP from GER & CD"},
    "Shadow Adept": {"bonus": {"punishment_reduce": 0.15}, "desc": "15% less punishment EXP loss"},
    "Consistent": {"bonus": {"all": 0.03}, "desc": "+3% all habit EXP"},
    "Perfect Hunter": {"bonus": {"perfect_day": 0.20}, "desc": "+20% Perfect Day bonus"},
    "Arise": {"bonus": {"all": 0.05}, "desc": "+5% all EXP — Rank milestone"},
}

# Corruption titles (dark / oppressive)
CORRUPTION_TITLES = {
    10: {"name": "Edge Lord", "desc": "Corruption seeps in"},
    25: {"name": "Night Crawler", "desc": "The night calls"},
    40: {"name": "Broken Discipline", "desc": "MS failures mount"},
    55: {"name": "Shadow Addict", "desc": "Goon + weakness"},
    70: {"name": "Lust-Bound", "desc": "Desire over duty"},
    85: {"name": "Guild Hooker", "desc": "Deep corruption"},
    95: {"name": "Creampie Adventurer", "desc": "Fallen far"},
    100: {"name": "Corrupted Vessel", "desc": "The System watches in silence"},
}

# --- Skill Tree (real nodes) ---
SKILL_NODES = {
    "Physical": [
        {"id": "phys_1", "name": "Endurance I", "cost": 3, "req": [], "bonus": {"PUMP": 0.05}, "desc": "+5% PUMP EXP"},
        {"id": "phys_2", "name": "Strength I", "cost": 5, "req": ["phys_1"], "bonus": {"PUMP": 0.08}, "desc": "+8% PUMP EXP"},
        {"id": "phys_3", "name": "Iron Will", "cost": 8, "req": ["phys_2"], "bonus": {"shadow_gain": 2}, "desc": "+2 Shadow Energy on perfect day"},
    ],
    "Intellectual": [
        {"id": "int_1", "name": "Focus I", "cost": 3, "req": [], "bonus": {"GER": 0.05, "CD": 0.05}, "desc": "+5% GER & CD"},
        {"id": "int_2", "name": "Memory I", "cost": 5, "req": ["int_1"], "bonus": {"GER": 0.08}, "desc": "+8% GER"},
        {"id": "int_3", "name": "Deep Work", "cost": 8, "req": ["int_2"], "bonus": {"CD": 0.10}, "desc": "+10% CD EXP"},
    ],
    "Spiritual": [
        {"id": "spi_1", "name": "Discipline I", "cost": 3, "req": [], "bonus": {"MS": 0.05, "PR": 0.05, "Q": 0.05}, "desc": "+5% Spiritual habits"},
        {"id": "spi_2", "name": "Willpower I", "cost": 5, "req": ["spi_1"], "bonus": {"punishment_reduce": 0.10}, "desc": "10% less punishment"},
        {"id": "spi_3", "name": "Purity", "cost": 8, "req": ["spi_2"], "bonus": {"corruption_resist": 0.25}, "desc": "25% less Corruption gain"},
    ],
    "Skillful": [
        {"id": "ski_1", "name": "Craft I", "cost": 3, "req": [], "bonus": {"CD": 0.05, "YTB": 0.05}, "desc": "+5% CD & YTB"},
        {"id": "ski_2", "name": "Presence I", "cost": 5, "req": ["ski_1"], "bonus": {"YTB": 0.10}, "desc": "+10% YTB"},
        {"id": "ski_3", "name": "Creator", "cost": 8, "req": ["ski_2"], "bonus": {"all": 0.03}, "desc": "+3% all EXP"},
    ],
}

SKILL_BRANCHES = list(SKILL_NODES.keys())

# --- Quest difficulty ---
QUEST_DIFFICULTY = {
    "S": {"mult": 0.6, "label": "Small"},
    "M": {"mult": 1.0, "label": "Medium"},
    "L": {"mult": 1.6, "label": "Large"},
    "XL": {"mult": 2.5, "label": "Boss"},
}

# --- Goon ---
GOON_SESSION_MINUTES = 60

# --- Health ---
DEFAULT_CALORIE_GOAL = 2200

# --- App ---
APP_NAME = "THE SYSTEM"
APP_VERSION = "0.2.0"
WINDOW_TITLE = "THE SYSTEM — RIBU"

# System voice lines
SYSTEM_LINES = {
    "login": "The System acknowledges your presence, Player.",
    "level_up": "ARISE. Your level has increased.",
    "rank_up": "Rank ascension confirmed. You grow stronger.",
    "perfect_day": "Perfect daily clear. The System is satisfied.",
    "punishment": "The System does not forgive weakness.",
    "corruption_up": "Corruption rises. Discipline frays.",
    "corruption_title": "A dark title has been forced upon you.",
    "missed": "Inactivity detected. Penalty applied.",
    "critical": "CRITICAL CLEAR. Exceptional performance.",
    "bonus_day": "SYSTEM BONUS DAY. All gains amplified.",
}
