from secrets import choice


def choices(population: str, *, k: int = 1) -> list[str]:
    return [choice(population) for _ in range(k)]
