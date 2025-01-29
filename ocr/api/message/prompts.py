class OCRPrompts:
    generate_general_answer = """## Task

You must analyze the attached medical document and generate a comprehensive report in **Markdown2** format. Ensure that every detail provided in the document is included, and do not omit or modify any information. Your output must strictly follow the required format.

## Report Structure

The report should be structured as follows, with each section containing only relevant information from the document:

```markdown
## Patient Information

- Name: [Patient Name]
- Age: [Patient Age]
- Date of Scan: [Date]
- Indication: [Reason for the CT scan]

## Findings

**Primary findings**:
[Describe significant abnormalities or findings relevant to the indication, e.g., "Presence of a 2 cm lesion in the right upper lung lobe, consistent with a possible neoplasm."]

** Secondary findings**:
[List incidental findings, e.g., "Mild hepatic steatosis noted."]
**No abnormalities**:
[Mention organs or systems without abnormalities, e.g., "No evidence of lymphadenopathy or pleural effusion."]

## Impression

[Summarize the findings concisely, e.g., "Findings suggest a primary lung tumor. Biopsy recommended for further evaluation."]

## Recommendations

[Include next steps or further tests, e.g., "PET scan and consultation with oncology recommended."]
```

[INST]

## Instructions

- **Do not invent or infer any information.** Only use data provided in the document.
- If any section listed in the report structure lacks corresponding information, **omit the section entirely**. Do not leave blank sections.
- Ensure that the format is followed strictly, and the output is complete without any deviations.

[/INST]"""