class OCRPrompts:
    generate_general_answer = """*Task:* Generate a concise and structured report based on the extracted text from a file. The report should summarize key findings, highlight any critical observations, and provide a clear conclusion.

**Instruction:**
1. **Analyze the extracted text** and identify the main themes, issues, or findings.
2. **Structure the report** into the following sections:
   - **Simple Overview:** A brief summary of the key points in the extracted text.
   - **Conclusion:** A succinct evaluation or interpretation of the findings, including any necessary recommendations or next steps.

3. **Ensure clarity and conciseness** in the report. Avoid unnecessary details but ensure all important information is retained.
4. **Use clear and professional language**, making the report easy to understand for a general audience.

**Format Example:**
```markdown
## Simple Overview of the Report

[Provide a brief and clear summary of the main points from the extracted text.]

## Conclusion

[Summarize key insights and provide any recommendations based on the findings.]
```"""