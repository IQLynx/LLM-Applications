from crewai import Task

def create_refine_task(user_prompt, agent):
    """Create a task for refining the user prompt."""
    return Task(
        description=f"Refine the following user prompt: {user_prompt}",
        expected_output="A professional, detailed, and clear version of the user's prompt.",
        agent=agent
    )

def create_verify_task(agent):
    """Create a task for verifying the refined prompt."""
    return Task(
        description="Verify and adjust the refined prompt to ensure it is clear, actionable, and professional.",
        expected_output="A final, polished prompt that is ready for use.",
        agent=agent
    )