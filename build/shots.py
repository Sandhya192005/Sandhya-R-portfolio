# Draws the project card pictures: one app-screen mockup per project, written to ../assets/img/projects/*.svg
import pathlib, math

OUT = pathlib.Path(__file__).parent.parent / "assets" / "img" / "projects"
W, H = 640, 400
INK, MUTED, ACC, BG, SURF, LINE, PAPER = "#1e293b", "#64748b", "#9b1f45", "#f8fafc", "#f1f5f9", "#e2e8f0", "#ffffff"
FONT = "Hanken Grotesk, Segoe UI, Helvetica, Arial, sans-serif"
TINT = SOFT = G1 = G2 = ACC
MULTI = PASTEL = []  # set per project by theme()
THEMES = {  # one professional color per project; everything else is white or neutral grey
    "employee-wellbeing": "#9b1f45",  # maroon
    "food-nutrition":     ("#ea580c", "#eab308"),  # orange blended into yellow
    "home-layout":        "#1d4ed8",  # blue
    "mediconnect":        "#0f766e",  # teal
    "cargo-email":        "#c2410c",  # orange
    "book-swapper":       "#be185d",  # rose
    "budget-tracker":     "#6d28d9",  # violet
    "product-review":     "#b45309",  # amber
    "donor-list":         "#b91c1c",  # red
    "cgpa":               "#1e3a8a",  # navy
}
def mix(hex1, hex2, k):
    a = [int(hex1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(hex2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * k):02x}" for x, y in zip(a, b))

def theme(name):
    global ACC, TINT, SOFT, G1, G2, MULTI, PASTEL
    ACC, G2 = THEMES[name] if isinstance(THEMES[name], tuple) else (THEMES[name], mix(THEMES[name], "#000000", .25))
    TINT, SOFT = mix(ACC, "#ffffff", .9), mix(ACC, "#ffffff", .55)
    G1 = ACC
    MULTI = [mix(ACC, "#ffffff", k) for k in (0, .25, .45, .6, .15, .35, .5, .7)]   # shades of the one color
    PASTEL = [mix(ACC, "#ffffff", k) for k in (.9, .86, .92, .88, .9, .86, .92, .88)]

def r(x, y, w, h, fill, rx=6, stroke=None):
    s = f' stroke="{stroke}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}/>'

def t(x, y, s, size=12, fill=INK, weight=400, anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'

def line(x, y, w, fill=LINE, h=7):
    return r(x, y, w, h, fill, h / 2)

def c(x, y, rad, fill, stroke=None, sw=0):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{x}" cy="{y}" r="{rad}" fill="{fill}"{s}/>'

def frame(url, body):
    head = (r(0, 0, W, H, PAPER, 0) + r(0, 0, W, 32, SURF, 0) + f'<path d="M0 32H{W}" stroke="{LINE}"/>'
            + c(18, 16, 4.5, "#cbd5e1") + c(32, 16, 4.5, "#cbd5e1") + c(46, 16, 4.5, "#cbd5e1")
            + r(200, 8, 240, 16, BG, 8) + t(320, 20, url, 10, MUTED, anchor="middle"))
    bg = (f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{G1}"/><stop offset="1" stop-color="{G2}"/></linearGradient>'
          f'<clipPath id="w"><rect width="{W}" height="{H}" rx="14"/></clipPath>'
          f'<filter id="s" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000" flood-opacity=".22"/></filter></defs>'
          f'<rect width="{W}" height="{H}" fill="url(#g)"/>'
          f'<circle cx="590" cy="40" r="110" fill="#fff" opacity=".12"/><circle cx="40" cy="380" r="140" fill="#fff" opacity=".10"/>')
    win = (f'<g transform="translate(32 24) scale(.9)"><g filter="url(#s)"><rect width="{W}" height="{H}" rx="14" fill="#fff"/></g>'
           f'<g clip-path="url(#w)">{head}{body}</g></g>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{FONT}">' + bg + win + "</svg>")

def sidebar(items, active=0):
    s = r(0, 32, 132, H - 32, BG, 0) + f'<path d="M132 32V{H}" stroke="{LINE}"/>'
    s += r(16, 48, 18, 18, ACC, 5) + line(42, 54, 60, LINE)
    for i, name in enumerate(items):
        y = 92 + i * 30
        if i == active:
            s += r(10, y - 14, 112, 24, TINT, 6)
        s += t(22, y + 2, name, 11, ACC if i == active else MUTED, 600 if i == active else 400)
    return s

def stars(x, y, n, size=9):
    out = ""
    for i in range(5):
        cx = x + i * (size * 2 + 2)
        pts = " ".join(f"{cx + size * (1 if k % 2 == 0 else 0.45) * math.sin(k * math.pi / 5):.1f},"
                       f"{y - size * (1 if k % 2 == 0 else 0.45) * math.cos(k * math.pi / 5):.1f}" for k in range(10))
        out += f'<polygon points="{pts}" fill="{ACC if i < n else LINE}"/>'
    return out

shots = {}

# 1 Employee wellbeing: activity dashboard with a break reminder
theme("employee-wellbeing")
b = sidebar(["Overview", "Activity", "Goals", "Devices", "Settings"])
b += t(156, 64, "Today's activity", 16, INK, 600) + t(156, 82, "Workstation agent · synced 2 min ago", 10, MUTED)
for i, (k, v) in enumerate([("Active time", "6h 12m"), ("Focus score", "82%"), ("Breaks taken", "4")]):
    x = 156 + i * 152
    b += r(x, 98, 140, 64, PASTEL[[0, 3, 2][i]], 10) + c(x + 124, 114, 6, MULTI[[0, 3, 2][i]]) + t(x + 14, 120, k, 10, MUTED) + t(x + 14, 148, v, 20, ACC if i == 1 else INK, 600)
b += r(156, 176, 444, 196, BG, 10, LINE) + t(172, 198, "Activity by hour", 11, INK, 600)
pts = [(0, 60), (1, 75), (2, 110), (3, 95), (4, 130), (5, 70), (6, 120), (7, 140), (8, 105), (9, 125), (10, 90), (11, 100)]
xy = [(176 + i * 37, 352 - v) for i, v in pts]
path = "M" + " L".join(f"{x},{y}" for x, y in xy)
b += f'<path d="{path} L{xy[-1][0]},352 L176,352 Z" fill="{TINT}"/>' + f'<path d="{path}" fill="none" stroke="{ACC}" stroke-width="2.5" stroke-linejoin="round"/>'
for g in (262, 292, 322):
    b += f'<path d="M176 {g}H583" stroke="{LINE}" stroke-dasharray="3 4"/>'
b += r(392, 300, 232, 84, ACC, 12) + c(418, 326, 10, "#ffffff") + t(436, 330, "Time for a short break", 12, BG, 600)
b += t(436, 348, "You've been focused for 90 min.", 10, TINT) + r(436, 358, 64, 18, "#ffffff", 6) + t(468, 371, "Start", 10, ACC, 600, "middle")
shots["employee-wellbeing"] = frame("wellbeing.local/dashboard", b)

# 2 Food and nutrition: meal photo with AI calorie estimate
theme("food-nutrition")
b = r(24, 52, 280, 324, SURF, 14) + c(164, 200, 104, "#fff", LINE, 2) + c(164, 200, 84, BG)
b += c(132, 172, 34, MULTI[1]) + c(194, 176, 28, MULTI[0]) + c(176, 236, 36, MULTI[5]) + c(126, 232, 18, MULTI[4]) + c(212, 226, 14, MULTI[3])
b += r(40, 334, 150, 28, ACC, 8) + t(56, 352, "Analysed by AI vision", 10, BG, 600)
b += t(328, 74, "Lunch · 1:24 pm", 11, MUTED) + t(328, 116, "540", 40, INK, 600) + t(404, 116, "kcal", 14, MUTED)
for i, (k, v, p) in enumerate([("Protein", "28 g", .56), ("Carbs", "62 g", .78), ("Fat", "18 g", .40)]):
    y = 146 + i * 40
    b += t(328, y, k, 11, INK, 600) + t(612, y, v, 11, MUTED, anchor="end") + line(328, y + 10, 284, SURF, 8) + line(328, y + 10, 284 * p, ACC if i == 0 else SOFT, 8)
b += r(328, 272, 284, 104, BG, 12, LINE)
b += c(372, 324, 30, "none", SURF, 8) + f'<path d="M372 294 A30 30 0 1 1 343 332" fill="none" stroke="{ACC}" stroke-width="8" stroke-linecap="round"/>'
b += t(372, 329, "1.8L", 11, INK, 600, "middle") + t(420, 310, "Water goal", 11, INK, 600) + t(420, 328, "1.8 of 2.6 litres", 10, MUTED) + t(420, 346, "BMI 21.4 · BMR 1,380", 10, MUTED)
shots["food-nutrition"] = frame("foodagent.app/meal", b)

# 3 AI home layout: dimensioned floor plan with cost panel
theme("home-layout")
b = r(0, 32, W, H - 32, "#ffffff", 0)
for gx in range(20, 440, 20):
    b += f'<path d="M{gx} 48V384" stroke="{SURF}"/>'
for gy in range(48, 390, 20):
    b += f'<path d="M20 {gy}H420" stroke="{SURF}"/>'
rooms = [(40, 64, 200, 150, "Living", PASTEL[4]), (240, 64, 160, 100, "Kitchen", PASTEL[2]), (240, 164, 160, 110, "Bedroom 2", PASTEL[1]),
         (40, 214, 120, 150, "Bedroom 1", PASTEL[6]), (160, 214, 80, 70, "Bath", PASTEL[7]), (160, 284, 240, 80, "Parking", PASTEL[3])]
for x, y, w, h, n, f in rooms:
    b += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{f}" stroke="{INK}" stroke-width="2.5"/>' + t(x + w / 2, y + h / 2 + 4, n, 11, INK, 600, "middle")
b += f'<path d="M110 214h40" stroke="#ffffff" stroke-width="4"/><path d="M110 214 a40 40 0 0 1 40 -40" fill="none" stroke="{MUTED}" stroke-dasharray="3 3"/>'
b += f'<path d="M40 54H400M40 50v8M400 50v8" stroke="{ACC}" stroke-width="1.5"/>' + r(190, 46, 60, 14, "#ffffff", 3) + t(220, 57, "36 ft", 10, ACC, 600, "middle")
b += r(440, 52, 180, 332, "#fff", 12, LINE) + t(458, 78, "Plan v3", 13, INK, 600) + t(458, 96, "2 BHK · 1,180 sq ft", 10, MUTED)
for i, (k, v) in enumerate([("Vastu zoning", "On"), ("Floors", "1"), ("Facing", "East")]):
    y = 126 + i * 28
    b += t(458, y, k, 10, MUTED) + t(602, y, v, 10, INK, 600, "end") + f'<path d="M458 {y + 9}H602" stroke="{SURF}"/>'
b += t(458, 230, "Estimated cost", 10, MUTED) + t(458, 260, "₹ 24.6 L", 22, ACC, 600)
b += r(458, 284, 144, 30, ACC, 8) + t(530, 303, "View in 3D", 11, BG, 600, "middle") + r(458, 322, 144, 30, BG, 8, LINE) + t(530, 341, "Export PDF", 11, INK, 600, "middle")
shots["home-layout"] = frame("homelayout.ai/plan/3", b)

# 4 MediConnect: doctor search with live slots
theme("mediconnect")
b = r(24, 48, 592, 40, BG, 10, LINE) + t(44, 73, "Cardiology", 12, INK, 600) + f'<path d="M140 58v20" stroke="{LINE}"/>' + t(156, 73, "Chennai", 12, INK)
b += r(536, 54, 72, 28, ACC, 7) + t(572, 72, "Search", 11, BG, 600, "middle")
docs = [("Dr. Meera Nair", "Cardiology · City Care Hospital", ["09:30", "10:00", "11:30", "02:00"], 1),
        ("Dr. Arjun Rao", "Cardiology · Lakeview Clinic", ["10:30", "12:00", "04:30"], -1),
        ("Dr. Kavya Iyer", "Cardiology · Metro Heart Centre", ["09:00", "01:30", "03:00", "05:00"], -1)]
for i, (n, d, slots, sel) in enumerate(docs):
    y = 104 + i * 94
    b += r(24, y, 592, 82, "#fff", 12, LINE) + c(64, y + 41, 22, PASTEL[[4, 1, 2][i]]) + c(64, y + 35, 8, MULTI[[4, 1, 2][i]]) + f'<path d="M50 {y + 56}a14 11 0 0 1 28 0" fill="{MULTI[[4, 1, 2][i]]}"/>'
    b += t(100, y + 34, n, 13, INK, 600) + t(100, y + 54, d, 10, MUTED)
    for j, s in enumerate(slots):
        x = 336 + j * 68
        on = j == sel
        b += r(x, y + 26, 60, 28, ACC if on else BG, 7, None if on else LINE) + t(x + 30, y + 44, s, 11, BG if on else INK, 600 if on else 400, "middle")
shots["mediconnect"] = frame("mediconnect.in/doctors", b)

# 5 Cargo email automation: n8n-style workflow
theme("cargo-email")
b = r(0, 32, W, H - 32, "#ffffff", 0)
for gx in range(16, W, 22):
    for gy in range(48, H, 22):
        b += c(gx, gy, 1, LINE)
nodes = [(32, 96, "Outlook", "New email"), (182, 96, "Claude AI", "Classify"), (332, 96, "Extract", "ETA · vessel"),
         (332, 250, "Excel", "Master table"), (182, 250, "Approve", "Human check"), (32, 250, "Send", "Customer report")]
for i, (x, y, n, s) in enumerate(nodes):
    hl = n == "Claude AI"
    b += r(x, y, 120, 64, "#fff", 12, ACC if hl else LINE) + r(x + 12, y + 14, 36, 36, ACC if hl else TINT, 8)
    b += t(x + 30, y + 37, n[0], 15, "#fff" if hl else ACC, 600, "middle") + t(x + 56, y + 30, n, 11, INK, 600) + t(x + 56, y + 46, s, 9, MUTED)
edges = ["M152 128H182", "M302 128H332", "M392 160V250", "M332 282H302", "M182 282H152"]
for e in edges:
    b += f'<path d="{e}" stroke="{MUTED}" stroke-width="2" fill="none"/>'
b += r(470, 72, 146, 300, "#fff", 12, LINE) + t(486, 98, "Run log", 12, INK, 600)
for i, (k, ok) in enumerate([("MSKU 204118", 1), ("TGHU 883021", 1), ("Newsletter", 0), ("CMAU 551907", 1), ("Invoice #882", 0)]):
    y = 124 + i * 46
    b += c(494, y + 4, 5, ACC if ok else LINE) + t(508, y + 8, k, 10, INK, 600) + t(508, y + 24, "Cargo update" if ok else "Skipped", 9, MUTED)
shots["cargo-email"] = frame("n8n · cargo-email-automation", b)

# 6 Book Swapper: book grid with filters
theme("book-swapper")
b = r(24, 48, 360, 34, BG, 10, LINE) + t(42, 70, "Search title, author or city", 11, MUTED)
for i, (f, on) in enumerate([("Swap", 1), ("Borrow", 0), ("Donate", 0), ("Sell", 0)]):
    x = 400 + i * 56
    b += r(x, 52, 50, 26, ACC if on else BG, 13, None if on else LINE) + t(x + 25, 69, f, 10, BG if on else INK, 600 if on else 400, "middle")
covers = [(MULTI[0], "Swap"), (MULTI[1], "Borrow"), (MULTI[4], "Donate"), (MULTI[2], "Swap"), (MULTI[5], "Sell"), (MULTI[0], "Borrow")]
for i, (col, tag) in enumerate(covers):
    x = 24 + i * 100
    b += r(x, 100, 88, 124, col, 6) + f'<path d="M{x + 10} 100V224" stroke="rgba(255,255,255,.25)" stroke-width="2"/>'
    b += line(x + 20, 130, 52, "rgba(255,255,255,.75)", 6) + line(x + 20, 144, 36, "rgba(255,255,255,.45)", 5)
    b += line(x, 236, 80, LINE) + line(x, 252, 56, LINE, 6) + r(x, 268, 50, 18, TINT, 9) + t(x + 25, 281, tag, 9, ACC, 600, "middle")
    b += stars(x + 6, 304, 4 if i % 2 else 5, 5)
b += r(24, 326, 592, 50, BG, 10, LINE) + c(52, 351, 13, TINT) + t(76, 347, "Request to swap sent", 11, INK, 600) + t(76, 363, "Waiting for the owner to accept · Adyar, Chennai", 9, MUTED)
b += r(530, 340, 72, 22, "#fff", 6, LINE) + t(566, 355, "Track", 10, INK, 600, "middle")
shots["book-swapper"] = frame("bookswapper.app/browse", b)

# 7 Budget tracker: donut, category budgets, transactions
theme("budget-tracker")
b = t(24, 66, "November budget", 15, INK, 600) + t(24, 84, "₹ 18,450 of ₹ 25,000 spent", 10, MUTED)
cx, cy, rad = 104, 214, 64
segs = [(.38, MULTI[6]), (.22, MULTI[1]), (.18, MULTI[4]), (.12, MULTI[2]), (.10, MULTI[3])]
a = -math.pi / 2
for frac, col in segs:
    a2 = a + frac * 2 * math.pi
    large = 1 if frac > .5 else 0
    b += (f'<path d="M{cx + rad * math.cos(a):.1f} {cy + rad * math.sin(a):.1f} A{rad} {rad} 0 {large} 1 '
          f'{cx + rad * math.cos(a2):.1f} {cy + rad * math.sin(a2):.1f}" fill="none" stroke="{col}" stroke-width="22"/>')
    a = a2
b += t(cx, cy - 2, "74%", 18, INK, 600, "middle") + t(cx, cy + 16, "used", 10, MUTED, anchor="middle")
for i, (k, p, col) in enumerate([("Food", .82, MULTI[6]), ("Travel", .55, MULTI[4]), ("Shopping", .40, MULTI[2])]):
    y = 314 + i * 24
    b += t(24, y, k, 10, INK, 600) + line(90, y - 8, 120, SURF, 7) + line(90, y - 8, 120 * p, col, 7)
b += r(244, 48, 372, 328, "#fff", 12, LINE) + t(262, 74, "Recent transactions", 12, INK, 600) + r(530, 58, 70, 24, ACC, 7) + t(565, 74, "+ Add", 10, BG, 600, "middle")
tx = [("Groceries", "Food", "− ₹ 1,240"), ("Metro card", "Travel", "− ₹ 500"), ("Salary", "Income", "+ ₹ 25,000"),
      ("Lunch", "Food", "− ₹ 220"), ("Headphones", "Shopping", "− ₹ 1,899"), ("Cab", "Travel", "− ₹ 310")]
for i, (n, cat, amt) in enumerate(tx):
    y = 100 + i * 46
    inc = amt.startswith("+")
    b += f'<path d="M262 {y}H598" stroke="{SURF}"/>' + c(280, y + 22, 12, TINT if not inc else ACC) + t(302, y + 20, n, 11, INK, 600) + t(302, y + 35, cat, 9, MUTED)
    b += t(598, y + 26, amt, 11, ACC if inc else INK, 600, "end")
shots["budget-tracker"] = frame("budget.app/overview", b)

# 8 Product review system: rated product cards with search
theme("product-review")
b = t(24, 66, "Products", 15, INK, 600) + r(200, 48, 300, 30, BG, 8, LINE) + t(216, 68, "Search products", 11, MUTED)
b += r(516, 48, 100, 30, ACC, 8) + t(566, 68, "+ Add review", 10, BG, 600, "middle")
prods = [("Wireless earbuds", 4, "Clear sound, good battery for the price."), ("Steel bottle", 5, "Keeps water cold all day."),
         ("Desk lamp", 3, "Bright, but the stand feels light."), ("Backpack", 4, "Lots of pockets, fits a 15\" laptop.")]
for i, (n, s, rv) in enumerate(prods):
    x, y = 24 + (i % 2) * 300, 96 + (i // 2) * 146
    b += r(x, y, 292, 134, "#fff", 12, LINE) + r(x + 14, y + 14, 92, 106, SURF, 8)
    b += r(x + 14, y + 14, 92, 106, PASTEL[[0, 3, 2, 1][i]], 8) + c(x + 60, y + 60, 22, MULTI[[0, 3, 2, 1][i]]) + r(x + 44, y + 90, 32, 6, MULTI[[0, 3, 2, 1][i]], 3)
    b += t(x + 120, y + 36, n, 12, INK, 600) + stars(x + 128, y + 56, s, 6) + t(x + 202, y + 60, f"{s}.0", 10, MUTED)
    words = rv.split(" ")
    l1, l2 = " ".join(words[:4]), " ".join(words[4:])
    b += t(x + 120, y + 84, l1, 10, MUTED) + t(x + 120, y + 99, l2, 10, MUTED)
shots["product-review"] = frame("reviews.local/products", b)

# 9 Donor list management: searchable donor table
theme("donor-list")
b = t(24, 66, "Donors", 15, INK, 600) + t(24, 84, "128 records", 10, MUTED)
b += r(260, 52, 240, 30, BG, 8, LINE) + t(276, 72, "Kidney", 11, INK) + r(516, 52, 100, 30, ACC, 8) + t(566, 72, "+ Add donor", 10, BG, 600, "middle")
b += r(24, 100, 592, 276, "#fff", 12, LINE) + r(24, 100, 592, 34, BG, 12) + r(24, 122, 592, 12, BG, 0)
for x, h in [(44, "Name"), (220, "Donated"), (360, "City"), (470, "Date")]:
    b += t(x, 122, h, 10, MUTED, 600)
rows = [("Priya S", "Kidney", "Chennai", "02 Nov 2026"), ("Rahul K", "Kidney", "Madurai", "28 Oct 2026"), ("Anitha M", "Kidney", "Coimbatore", "19 Oct 2026"),
        ("Vijay R", "Kidney", "Trichy", "11 Oct 2026"), ("Deepa L", "Kidney", "Salem", "30 Sep 2026")]
for i, (n, o, ci, d) in enumerate(rows):
    y = 134 + i * 48
    b += f'<path d="M24 {y}H616" stroke="{SURF}"/>' + c(56, y + 24, 12, TINT) + t(56, y + 28, n[0], 10, ACC, 600, "middle") + t(76, y + 28, n, 11, INK, 600)
    b += r(220, y + 14, 56, 20, TINT, 10) + t(248, y + 28, o, 9, ACC, 600, "middle") + t(360, y + 28, ci, 11, INK) + t(470, y + 28, d, 11, MUTED)
    b += t(596, y + 28, "Edit", 10, ACC, 600, "end")
shots["donor-list"] = frame("donors.local/list", b)

# 10 CGPA calculator: semester grades and result
theme("cgpa")
b = t(24, 66, "Semester 5", 15, INK, 600) + t(24, 84, "6 subjects · 22 credits", 10, MUTED)
b += r(24, 100, 340, 276, "#fff", 12, LINE)
subs = [("Compiler Design", 4, "O"), ("Computer Networks", 4, "A+"), ("Machine Learning", 3, "A+"), ("Web Technology", 3, "A"),
        ("Software Testing", 3, "O"), ("Networks Lab", 2, "O")]
for i, (n, cr, g) in enumerate(subs):
    y = 104 + i * 44
    if i:
        b += f'<path d="M24 {y}H364" stroke="{SURF}"/>'
    b += t(42, y + 27, n, 11, INK, 600) + t(240, y + 27, f"{cr} cr", 10, MUTED)
    b += r(290, y + 11, 56, 24, TINT if g == "O" else BG, 6, None if g == "O" else LINE) + t(318, y + 27, g, 11, ACC if g == "O" else INK, 600, "middle")
b += r(384, 100, 232, 120, ACC, 12) + t(402, 128, "Overall CGPA", 11, TINT) + t(402, 180, "8.74", 40, BG, 600) + t(402, 202, "after 5 of 8 semesters", 10, TINT)
b += r(384, 232, 232, 144, "#fff", 12, LINE) + t(402, 256, "GPA by semester", 11, INK, 600)
for i, g in enumerate([8.2, 8.6, 8.9, 8.5, 9.1]):
    h = (g - 7) * 38
    x = 410 + i * 40
    b += r(x, 360 - h, 24, h, ACC if i == 4 else SOFT, 4) + t(x + 12, 354 - h, f"{g}", 9, MUTED, anchor="middle")
shots["cgpa"] = frame("cgpa-calculator.html", b)

OUT.mkdir(parents=True, exist_ok=True)
for name, svg in shots.items():
    (OUT / f"{name}.svg").write_text(svg, encoding="utf8")
print("wrote", len(shots), "pictures to", OUT)
