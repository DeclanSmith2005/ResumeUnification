from __future__ import annotations


class ResumeSection:
    def __init__(
        self,
        latex_code: str = "",
        *,
        start: str = "",
        end: str = "",
        sections: list[ResumeSection] | None = None,
):
        self.latex_code = latex_code
        self.start = start
        self.end = end
        self.sections = sections if sections is not None else []

    def add_section(self, section: ResumeSection):
        self.sections.append(section)

    def __str__(self):
        parts = [self.start, self.latex_code, *(str(section) for section in self.sections), self.end]
        return "\n".join(part for part in parts if part)
