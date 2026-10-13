def crowd_stats(people, area_m2):
    n = len(people)
    density = n / max(area_m2, 1e-6)
    if density < 0.5:
        level = "FREE"
    elif density < 2:
        level = "MODERATE"
    elif density < 4:
        level = "DENSE"
    else:
        level = "CRITICAL"
    return {"count": n, "density_per_m2": round(density, 2), "level": level}
