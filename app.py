# ------------------------------------------------------------------
# Importing the required libraries
# ------------------------------------------------------------------

from dotenv import find_dotenv, load_dotenv
import os
import autogen


# ------------------------------------------------------------------
# Load environment variables
# ------------------------------------------------------------------

load_dotenv(find_dotenv())

# ------------------------------------------------------------------
# Configuration for autgen
# ------------------------------------------------------------------

config_list = [
  {
    'model': 'pt-3.5-turbo-16k',
    'api_key': {os.environ.get('OPENAI_API_KEY')}
  }
]

llm_config = {
  'request_timeout': 600,
  'seed': 42,
  'congfig_list': config_list,
  'temperature': 0,
}

assistant = autogen.AssistantAgent(name='assistent', llm_config=llm_config)

user_proxy = autogen.UserProxy(name='user_proxy',
                               human_input_mode='TERMINATE', max_consecutive_auto_reply=10, is_termination_message=lambda x: x.get("content", "").rstrip().endswith(("TERMINATE")),
                               code_execution_config={'work_dir': 'web'}, llm_config=llm_config, 
                               system_message="""Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""")

# ------------------------------------------------------------------
# Tasks
# ------------------------------------------------------------------

task = """
Give me a summary of how the stock market is doing today.
"""


# ------------------------------------------------------------------
# Start chat
# ------------------------------------------------------------------

user_proxy.inititate_chat(assistant, message=task)