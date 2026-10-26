# THE SYSTEM — RIBU

Solo Leveling inspired Progress / Habit Tracker with full RPG mechanics.

## Requirements

```bash
pip install PySide6 Pillow cryptography pygame requests
```

(Python 3.11+ recommended)

## How to Run

```bash
cd RIBU_System
python main.py
```

**Login credentials (hardcoded):**
- Username: `RIBU`
- Password: `gladrebecca91`

## Features Implemented (v0.1 Foundation)

- [x] Hard login gate
- [x] Player Level / EXP / Rank system with balanced curve
- [x] Daily absence detection + 3-day progress penalty
- [x] Habits monthly table (PR, GER, MS, CD, PUMP, YTB, Q)
- [x] Instant EXP + skill points on habit completion
- [x] Quests (immutable once created)
- [x] Skill Tree (4 branches)
- [x] Goals tab
- [x] Log Book (diary)
- [x] Encrypted Storage vault
- [x] Goon tab with partner unlock by level + 1h session timer (Rule34 **stubbed**)
- [x] Music tab (pygame)
- [x] Inventory / Titles gallery
- [x] System messages log
- [x] Status window with EXP bar, rank, partner slot

## Notes

- Rule34 API is completely disabled (`RULE34_ENABLED = False`). Credentials are stored in `config.py` but never used.
- MC PNGs and partner images are placeholders.
- Sound effects and advanced animations can be expanded later.
- All data persists in `data/ribu_system.db`.

## Project Structure

See `plan.md` (in parent folder) for the full master plan this implementation follows.
