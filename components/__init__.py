"""Load specialty components, falling back to shared components at this level."""

from pathlib import Path


COMPONENT_DIRECTORY = Path(__file__).resolve().parent


def read_component(specialty: str, name: str) -> str:
    """Prefer a specialty's version when it overrides a shared component."""
    specialty_path = COMPONENT_DIRECTORY / specialty / f"{name}.txt"
    shared_path = COMPONENT_DIRECTORY / f"{name}.txt"
    for path in (specialty_path, shared_path):
        if path.is_file():
            return path.read_text(encoding="utf-8")
    raise FileNotFoundError(
        f"Missing component {name!r}; checked {specialty_path} and {shared_path}."
    )
