from crewai import Agent, LLM

def create_prompt_refiner(llm):
    """Create a Prompt Refinement Expert agent."""
    return Agent(
        role="Prompt Refinement Expert",
        goal="Refine the user's input into a professional, detailed, and clear prompt.",
        backstory="You are an expert in refining prompts to make them professional and actionable.",
        verbose=True,
        llm=llm
    )

def create_prompt_verifier(llm):
    """Create a Prompt Quality Assurance Expert agent."""
    return Agent(
        role="Prompt Quality Assurance Expert",
        goal="Verify and adjust the refined prompt to ensure it is clear, actionable, and professional.",
        backstory="You are an expert in ensuring prompts are of the highest quality and suitable for any domain.",
        verbose=True,
        llm=llm
    )