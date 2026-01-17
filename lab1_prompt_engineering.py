# lab1_prompt_engineering.py

class PromptTemplates:
    @staticmethod
    def task_decomposition(task):
        return f"""You are a task planning agent. Break down this task into actionable steps:

Task: {task}

Provide a numbered list of steps with clear dependencies."""

    @staticmethod
    def reasoning_chain(question, context):
        return f"""Think through this step-by-step:

Context: {context}
Question: {question}

Use this format:
1. Understanding: [Restate the problem]
2. Analysis: [Break down key components]
3. Reasoning: [Apply logical steps]
4. Conclusion: [Final answer]"""

# Test both templates
print(invoke_claude(PromptTemplates.task_decomposition(
    "Build a customer support automation system"
)))
