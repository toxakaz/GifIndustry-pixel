
Dot = tuple[int, int]
RGB = tuple[int, int, int] | tuple[float, float, float]
OKLAB = tuple[float, float, float]


def RGB_to_OKLAB(rgb_source: RGB) -> OKLAB:
    r, g, b = rgb_source
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b

    l_ = l**(1/3)
    m_ = m**(1/3)
    s_ = s**(1/3)

    return (
        0.2104542553*l_ + 0.7936177850*m_ - 0.0040720468*s_,
        1.9779984951*l_ - 2.4285922050*m_ + 0.4505937099*s_,
        0.0259040371*l_ + 0.7827717662*m_ - 0.8086757660*s_,
    )
