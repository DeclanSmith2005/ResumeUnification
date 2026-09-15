from pathlib import Path

import components

from resume_section import ResumeSection

start = components.preamble_start
end = components.preamble_end
header = ResumeSection(components.headlineBanner)
education = ResumeSection(components.education)
skills = ResumeSection(components.skillsAndInterests)
experienceStart = components.experienceStart
experienceEnd = components.experienceEnd

def quant_resume():
    projectSections = [ResumeSection(i) for i in [components.ritc, components.rileyTradingStrat, components.cpuArchitecture, components.quackstonVehicle, components.faceBell]]
    projects = ResumeSection(start=components.projectStart, end=components.projectEnd, sections = projectSections)

    experienceSections = [ResumeSection(i) for i in [components.amazon2026, components.scotiabank2026, components.scotiabank2025]]
    experience = ResumeSection(start=experienceStart, end=experienceEnd, sections = experienceSections)

    resume = ResumeSection(start=start, end=end, sections = [header, education, skills, experience, projects]) 
    return resume

def swe_resume():
    projectSections = [ResumeSection(i) for i in [components.faceBell, components.quackstonVehicle, components.nutrientAnalysisScale, components.curate]]
    projects = ResumeSection(start=components.projectStart, end=components.projectEnd, sections = projectSections)

    experienceSections = [ResumeSection(i) for i in [components.amazon2026, components.scotiabank2026, components.scotiabank2025, components.brightBridge]]
    experience = ResumeSection(start=components.experienceStart, end=components.experienceEnd, sections = experienceSections)

    resume = ResumeSection(start=start, end=end, sections = [header, education, skills, experience, projects])
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
