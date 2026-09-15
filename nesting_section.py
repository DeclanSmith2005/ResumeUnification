from __future__ import annotations
from resume_section import ResumeSection

class NestingSection:
    def __init__(self, *, start: str = "", end: str = "", sections: list[ResumeSection | NestingSection] | None = None):
        self.sections = sections if sections is not None else []
        self.start = start
        self.end = end

    def add_section(self, section: ResumeSection | NestingSection):
        self.sections.append(section)

    def add_nesting_section(self, nesting_section: NestingSection):
        self.sections.append(nesting_section)

    def __str__(self):
        return "\n".join([self.start, *(str(section) for section in self.sections), self.end])
   
