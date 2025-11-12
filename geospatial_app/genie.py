from databricks.sdk import WorkspaceClient
from datetime import timedelta
import pandas as pd

w = WorkspaceClient()

def start_genie_conversation(space_id, question):

  conversation = w.genie.start_conversation_and_wait(space_id, question)
  response = w.genie.get_message_attachment_query_result(
    space_id = space_id,
    conversation_id = conversation.conversation_id,
    message_id = conversation.message_id,
    attachment_id = conversation.attachments[0].attachment_id
  )

  schema_list = [i.name for i in response.statement_response.manifest.schema.columns]
  data = response.statement_response.result.data_array

  return pd.DataFrame(data, columns=schema_list), conversation.conversation_id


def genie_follow_up_questions(space_id, question, conversation_id):
  conversation = w.genie.create_message_and_wait(
    space_id = space_id,
    conversation_id=conversation_id,
    content = question
  )

  response = w.genie.get_message_attachment_query_result(
    space_id = space_id,
    conversation_id = conversation.conversation_id,
    message_id = conversation.message_id,
    attachment_id = conversation.attachments[0].attachment_id
  )

  schema_list = [i.name for i in response.statement_response.manifest.schema.columns]
  data = response.statement_response.result.data_array

  return pd.DataFrame(data, columns=schema_list)