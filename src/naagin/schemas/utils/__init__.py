from secrets import choice


def choices[T](population: T, *, k: int = 1) -> list[T]:
    return [choice(population) for _ in range(k)]
