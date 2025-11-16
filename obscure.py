# obscure.py — centered alien "6" and "7" with clearer, bolder shapes
import random

# Alien glyph ranges
ALIEN_RANGES = [
    (0x13A0, 0x13FF),    # Cherokee
    (0x1E900, 0x1E95F),  # Adlam
    (0x10480, 0x104AF),  # Osmanya
    (0x1E800, 0x1E8DF),  # Mende Kikakui
]

def alien_char():
    lo, hi = random.choice(ALIEN_RANGES)
    return chr(random.randint(lo, hi))

# ======================================================
#     CLEARER, THICKER ASCII-ART TEMPLATES FOR 6 & 7
# ======================================================

BIG_SIX = [
    " 111111  ",
    "111    11",
    "111      ",
    "1111111  ",
    "111   11 ",
    "111   11 ",
    " 111111  ",
]

BIG_SEVEN = [
    "111111111",
    "       111",
    "      111 ",
    "     111  ",
    "    111   ",
    "    111   ",
    "    111   ",
]


def convert_to_alien(template):
    out = []
    for row in template:
        alien_row = ""
        for ch in row:
            alien_row += alien_char() if ch == "1" else " "
        out.append(alien_row)
    return out

# ======================================================
def giant_block_centered(total_lines=45, width=150):
    block = []

    six = convert_to_alien(BIG_SIX)
    seven = convert_to_alien(BIG_SEVEN)

    h = len(six)

    # >>> Make the center MUCH clearer with a big clean zone <<<
    SAFE_PADDING = 7     # space around the digits
    GAP = 12              # gap between 6 and 7

    safe_width = len(six[0]) + GAP + len(seven[0]) + SAFE_PADDING * 2

    start_line = total_lines // 2 - h // 2
    start_col  = width // 2 - safe_width // 2

    for i in range(total_lines):
        if start_line <= i < start_line + h:
            idx = i - start_line

            left_noise  = "".join(alien_char() for _ in range(start_col))

            safe_box_left  = " " * SAFE_PADDING
            safe_box_mid   = six[idx] + (" " * GAP) + seven[idx]
            safe_box_right = " " * SAFE_PADDING

            mid = safe_box_left + safe_box_mid + safe_box_right

            right_len   = width - len(left_noise) - len(mid)
            right_noise = "".join(alien_char() for _ in range(right_len))

            block.append(left_noise + mid + right_noise)
        else:
            block.append("".join(alien_char() for _ in range(width)))

    return "\n".join(block)


def print_obscure():
    print("\n—✦— BEGIN ALIEN DATA DUMP —✦—\n")
    print(giant_block_centered(50, 160))
    print("\n—✦— END —✦—\n")

if __name__ == "__main__":
    print_obscure()
