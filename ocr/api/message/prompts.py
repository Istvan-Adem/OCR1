class OCRPrompts:
    generate_general_answer = """## Task

You must analyze the attached medical document and generate a comprehensive report in **Markdown2** format. Ensure that every detail provided in the document is included, and do not omit or modify any information. Your output must strictly follow the required format.

## Report Structure

The report should be structured as follows, with each section containing only relevant information from the document:

1. **Diagnosis and Staging Details**  
   Include all diagnosis-related and staging information.

2. **Tumor Markers and Pathology Findings**  
   Provide detailed tumor markers and any pathology results mentioned.

3. **Imaging Results** (e.g., CT, MRI summaries)  
   Summarize all relevant imaging results provided in the document.

4. **Prior Treatments and Outcomes**  
   Detail any prior treatments and their outcomes as found in the document.

## Instructions

- Your response must be in **Markdown2** format.
- Do not use bullet points very often.
- **Do not invent or infer any information.** Only use data provided in the document.
- If any section listed in the report structure lacks corresponding information, **omit the section entirely**. Do not leave blank sections.
- Ensure that the format is followed strictly, and the output is complete without any deviations."""