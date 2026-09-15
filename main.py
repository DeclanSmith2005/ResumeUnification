from pathlib import Path

import components

from nesting_section import NestingSection
from resume_section import ResumeSection

start = components.preamble_start
end = components.preamble_end
header = components.headlineBanner
education = components.education
skills = components.skillsAndInterests
experienceStart = components.experienceStart
experienceEnd = components.experienceEnd

def quant_resume():
    projectSections = [ResumeSection(i) for i in [components.ritc, components.rileyTradingStrat, components.cpuArchitecture, components.quackstonVehicle, components.faceBell]]
    projects = NestingSection(start=components.projectStart, end=components.projectEnd, sections = projectSections)

    experienceSections = [ResumeSection(i) for i in [components.amazon2026, components.scotiabank2026, components.scotiabank2025]]
    experience = NestingSection(start=experienceStart, end=experienceEnd, sections = experienceSections)

    resume = NestingSection(start=start, end=end, sections = [header, education, skills, experience, projects]) 
    return resume

def swe_resume():
    projectSections = [ResumeSection(i) for i in [components.faceBell, components.quackstonVehicle, components.nutrientAnalysisScale, components.curate]]
    projects = NestingSection(start=components.projectStart, end=components.projectEnd, sections = projectSections)

    experienceSections = [ResumeSection(i) for i in [components.amazon2026, components.scotiabank2026, components.scotiabank2025, components.brightBridge]]
    experience = NestingSection(start=components.experienceStart, end=components.experienceEnd, sections = experienceSections)

    resume = NestingSection(start=start, end=end, sections = [header, education, skills, experience, projects])
    return resume

def main():
    output_directory = Path(__file__).resolve().parent / "generatedResumes"
    output_directory.mkdir(exist_ok=True)

    # Quant Resume
    quantresume = quant_resume()
    (output_directory / "quant_resume.tex").write_text(str(quantresume), encoding="utf-8")
    
    # SWE Resume
    sweresume = swe_resume()
    (output_directory / "swe_resume.tex").write_text(str(sweresume), encoding="utf-8")

if __name__ == "__main__":
    main()
