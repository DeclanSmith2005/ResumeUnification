"""Build LaTeX and PDF versions of the PE, SWE, and trading research resumes."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess

from components import read_component
from resume_section import ResumeSection


ROOT = Path(__file__).resolve().parent
OUTPUT_DIRECTORY = ROOT / "generatedResumes"

# Order within each tuple is the order on the finished resume.
# A component is read from its specialty folder first, then components/.
VARIANTS = {
    "performance_engineering": {
        "folder": "PerformanceEngineering",
        "experience": (
            "Amazon_PerformanceEngineering",
            "Scotiabank2026_PerformanceEngineering",
            "Scotiabank2025_PerformanceEngineering",
            "BrightBridge_PerformanceEngineering",
        ),
        "projects": (
            "FaceBell_PerformanceEngineering",
            "Quackston_PerformanceEngineering",
            "CPUArchitecture_PerformanceEngineering",
        ),
    },
    "swe": {
        "folder": "GenericSWE",
        "experience": (
            "amazon2026",
            "scotiabank2026",
            "scotiabank2025",
            # Optional alternative: "brightBridge",
        ),
        "projects": (
            "faceBell",
            "quackstonVehicle",
            "nutrientAnalysisScale",
            "curate",
            # Optional alternative: "cpuArchitecture",
        ),
    },
    "trading_research": {
        "folder": "TradingResearch",
        "experience": (
            "Amazon_TradingResearch",
            "Scotiabank2026_TradingResearch",
            "Scotiabank2025_TradingResearch",
        ),
        "projects": (
            "RITC_TradingResearch",
            "VolatilityStrategy_TradingResearch",
            # Rewritten alternatives for systems or algorithms applications:
            # "Quackston_TradingResearch",
            # "CPUArchitecture_TradingResearch",
        ),
    },
}


def build_resume(variant: str) -> ResumeSection:
    config = VARIANTS[variant]

    def read(name: str) -> str:
        return read_component(config["folder"], name)

    experience = ResumeSection(
        start=read("experienceStart"),
        end=read("experienceEnd"),
        sections=[ResumeSection(read(name)) for name in config["experience"]],
    )
    projects = ResumeSection(
        start=read("projectStart"),
        end=read("projectEnd"),
        sections=[ResumeSection(read(name)) for name in config["projects"]],
    )
    return ResumeSection(
        start=read("preamble_start"),
        end=read("preamble_end"),
        sections=[
            ResumeSection(read("headlineBanner")),
            ResumeSection(read("education")),
            ResumeSection(read("skillsAndInterests")),
            experience,
            projects,
        ],
    )


def performance_engineering_resume() -> ResumeSection:
    return build_resume("performance_engineering")


def swe_resume() -> ResumeSection:
    return build_resume("swe")


def trading_research_resume() -> ResumeSection:
    return build_resume("trading_research")


def find_pdflatex() -> str:
    """Find a system compiler or the project-local TinyTeX installation."""
    engine = shutil.which("pdflatex")
    if engine is not None:
        return engine
    for candidate in sorted((ROOT / ".tools" / "TinyTeX" / "bin").glob("*/pdflatex")):
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)
    raise RuntimeError(
        "pdflatex was not found. Install TinyTeX in .tools/TinyTeX or put "
        "pdflatex on PATH. Use --no-pdf to generate only LaTeX files."
    )


def compile_pdf(tex_path: Path) -> Path:
    """Compile with the original LaTeX layout and require a single page."""
    engine = find_pdflatex()
    tex_path = tex_path.resolve()
    build_directory = tex_path.parent / ".latex-build" / tex_path.stem
    build_directory.mkdir(parents=True, exist_ok=True)

    for _ in range(2):
        result = subprocess.run(
            [
                engine, "-interaction=nonstopmode", "-halt-on-error",
                "-file-line-error", "-no-shell-escape",
                f"-output-directory={build_directory}", tex_path.name,
            ],
            cwd=tex_path.parent,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
        )
        if result.returncode:
            raise RuntimeError(
                f"LaTeX compilation failed for {tex_path.name}:\n{result.stdout[-6000:]}"
            )

    log_path = build_directory / f"{tex_path.stem}.log"
    log = log_path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"Output written on .*?\((\d+) pages?[,)]", log, re.DOTALL)
    if match is None:
        raise RuntimeError(f"Could not verify the page count for {tex_path.name}.")
    if int(match.group(1)) != 1:
        raise RuntimeError(
            f"{tex_path.name} produced {match.group(1)} pages; shorten the components."
        )
    if "Overfull \\hbox" in log or "Overfull \\vbox" in log:
        raise RuntimeError(f"Layout overflow in {tex_path.name}; inspect its LaTeX log.")
    pdf_path = tex_path.with_suffix(".pdf")
    shutil.copy2(build_directory / pdf_path.name, pdf_path)
    return pdf_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pdf", action=argparse.BooleanOptionalAction, default=True,
        help="Compile and check PDFs (default); --no-pdf writes only LaTeX.",
    )
    parser.add_argument(
        "--variant", action="append", choices=VARIANTS,
        help="Build only this variant. Repeat to select more than one.",
    )
    args = parser.parse_args()
    OUTPUT_DIRECTORY.mkdir(exist_ok=True)
    tex_paths = []
    for variant in args.variant or VARIANTS:
        tex_path = OUTPUT_DIRECTORY / f"{variant}_resume.tex"
        tex_path.write_text(str(build_resume(variant)), encoding="utf-8")
        tex_paths.append(tex_path)
        print(f"Created {tex_path}")
    if args.pdf:
        try:
            for tex_path in tex_paths:
                print(f"Created {compile_pdf(tex_path)} (1 page)")
        except (RuntimeError, OSError) as error:
            parser.exit(status=1, message=f"error: {error}\n")


if __name__ == "__main__":
    main()
