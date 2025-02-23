class OCRPrompts:
    generate_general_answer = """## Task

You must analyze the text extracted from medical document and generate a simple overview in **Markdown2** format. Your output must strictly follow the required format.

## Report Structure

The report must be structured as follows, with each section containing only relevant information from the document:

```markdown
## Simple Overview of the CT Report

[Provide a brief and clear medical summary of the main points from the extracted text.]

## Conclusion

[Summarize key insights and provide any recommendations based on the findings in 2 sentences.]
```

[INST]

## Instructions

- **Do not invent or infer any information.** Only use data provided in the user request.
- Ensure that the format is followed strictly, and the output is complete without any deviations.

[/INST]"""
    extract_original_text = """## Task

You must extract all text from the attached images and return it in the **text** field. You must not include the patient's name, contact details, or demographic data.  

## Important notes

- You must extract all text but exclude any information related to the name, contact details, and demographic data."""