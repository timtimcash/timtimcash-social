import datetime as dt
P, T, S, V = "papel", "tinta", "suave", "verde"
DEZ = [("2026-12-21", P), ("2026-12-22", V), ("2026-12-23", T), ("2026-12-27", S), ("2026-12-28", P), ("2026-12-30", V)]
FUNDOS = {
 "2027-01-02": T, "2027-01-04": V, "2027-01-06": P, "2027-01-07": S, "2027-01-08": T, "2027-01-10": S, "2027-01-11": P,
 "2027-01-13": S, "2027-01-14": V, "2027-01-15": T, "2027-01-16": P, "2027-01-18": T, "2027-01-20": S, "2027-01-21": V,
 "2027-01-22": P, "2027-01-23": T, "2027-01-27": P, "2027-01-28": T, "2027-01-29": S, "2027-01-30": V,
 "2027-02-01": P, "2027-02-03": T, "2027-02-04": S, "2027-02-05": V, "2027-02-06": P, "2027-02-10": T, "2027-02-11": S,
 "2027-02-12": V, "2027-02-13": P, "2027-02-15": T, "2027-02-17": S, "2027-02-18": V, "2027-02-19": P, "2027-02-20": T,
 "2027-02-22": S, "2027-02-23": V, "2027-02-24": P, "2027-02-25": T, "2027-02-26": S, "2027-02-27": T,
}
seq = DEZ + sorted(FUNDOS.items())
erros = []
for i in range(len(DEZ), len(seq)):
    d, b = seq[i]
    for k in (1, 3):
        if seq[i - k][1] == b: erros.append(f"{d} {b} igual a {seq[i-k][0]} (distância {k})")
    if b == V:
        w = dt.date.fromisoformat(d).isocalendar()[:2]
        for dj, bj in seq[:i]:
            if bj == V and dt.date.fromisoformat(dj).isocalendar()[:2] == w: erros.append(f"{d}: dois verdes na semana ({dj})")
fmt = ["C" if i % 2 == 0 else "R" for i in range(40)]
datas = sorted(FUNDOS)
# fins de semana e alternância
for mes in ("2027-01", "2027-02"):
    ds = [d for d in datas if d.startswith(mes)]
    fims = sorted({dt.date.fromisoformat(d).isocalendar()[1] for d in ds if dt.date.fromisoformat(d).weekday() >= 5})
    print(mes, len(ds), "posts; fins de semana com post (semana ISO):", fims)
print("problemas:", erros or "nenhum")
