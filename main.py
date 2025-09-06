from agents import Agent, Runner,trace
from connection import config
import asyncio
from dotenv import load_dotenv
load_dotenv()
# Analyst agents
lyric_analyst_agent = Agent(
    name="Lyric Analyst Agent",
    instructions="""
    You are the Lyric Analyst Agent. Your task is  to interpret(tashreeh) poetry that 
    express personal emotion thoughts likes songs or poem about love and sadness, 
    happiness or deep personal feelings"""
)

dramatic_analyst_agent = Agent(
    name="Dramatic Analyst Agent",
    instructions="""
    You are the Dramatic Analyst Agent. Your task is  to interpret(tashreeh) poetry 
    that is meant to be performed , usually iin a theatrical setting. 
    It involves character  expressing strong emotions aloud, like in a play
    """
)

narrative_analyst_agent = Agent(
    name="Narrative Analyst Agent",
    instructions="""
    You are the Narrative Analyst Agent. Your task is  to interpret(tashreeh) poetry that
      tell a story. These poem have characters, events, and often a   plot like  a story,
        but written ina poetic form
    """


)

# Poet agent (defined after sub-agents)
poet_agent = Agent(
    name="Poet Agent",
    instructions="""
    You are the Poet Agent. Your task is to handle poetry related queries only,"\
    "Delegate  the query to:
    - Lyric Analyst Agent  if the poem is about personal emotion and feelings
    - Dramatic Analyst Agent if the poem is about theatrical or emotion performance
    - Narrative Analyst Agent if the poem is tell a story
    if the query is not related to poetry, respond with "I can only handle poetry related 
    queries.".
    
    """,
    handoffs=[lyric_analyst_agent, narrative_analyst_agent, dramatic_analyst_agent],
)

# Runner 
async def main():
    with trace("poetry agent"):
    # Example 1: Ask to write a lyric poem
       result = await Runner.run(
        poet_agent,
        """ 
         Science encompasses the systematic study of the natural and physical world through observation, 
#         experimentation, and analysis to understand its phenomena and laws.
        .""",
     run_config=config
    )

    print(result.final_output)
    print("Last Agent ==> ",result.last_agent.name)

if __name__ == "__main__":
    asyncio.run(main())

# Science encompasses the systematic study of the natural and physical world through observation, 
#         experimentation, and analysis to understand its phenomena and laws.

# Dramatic poetry
# The dramatic poet takes the stage,
# With words that roar and hearts that rage.
# They breathe new life in every line,
# Each voice and role by their design.
# They craft a world of fear and flame,
# Of love, betrayal, pride, and shame.
# Their pen becomes a spotlight's glow,
# Where human truths are set to show.

# Lyrical poetry
# The lyric poet sings the soul,
# Of love and loss, and making whole.
# With gentle words and tender tone,
# They turn deep thoughts to song alone.
# They write of dreams and silent tears,
# Of fleeting joy and hidden fears.
# Their verses flow like whispered art,
# Straight from the chambers of the heart.