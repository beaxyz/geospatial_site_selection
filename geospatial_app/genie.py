from databricks.sdk import WorkspaceClient
from datetime import timedelta
import pandas as pd

w = WorkspaceClient()

def start_genie_conversation(space_id, question):

  conversation = w.genie.start_conversation_and_wait(space_id, question)

  if conversation.attachments[0].query is None:
    return {
      "response_data": None, 
      "conversation_id": conversation.conversation_id, 
      "response_text": conversation.attachments[0].text.content}

  elif conversation.attachments[0].text is not None:
    response = w.genie.get_message_attachment_query_result(
    space_id = space_id,
    conversation_id = conversation.conversation_id,
    message_id = conversation.message_id,
    attachment_id = conversation.attachments[0].attachment_id
    )
    
    schema_list = [i.name for i in response.statement_response.manifest.schema.columns]
    data = response.statement_response.result.data_array

    return {
      "response_data": pd.DataFrame(data, columns=schema_list), 
      "conversation_id": conversation.conversation_id, 
      "response_text": conversation.attachments[0].text.content}

  else:
    response = w.genie.get_message_attachment_query_result(
    space_id = space_id,
    conversation_id = conversation.conversation_id,
    message_id = conversation.message_id,
    attachment_id = conversation.attachments[0].attachment_id
    )
    
    schema_list = [i.name for i in response.statement_response.manifest.schema.columns]
    data = response.statement_response.result.data_array

    return {
      "response_data": pd.DataFrame(data, columns=schema_list), 
      "conversation_id": conversation.conversation_id, 
      "response_text": None}


def genie_follow_up_questions(space_id, question, conversation_id):
  conversation = w.genie.create_message_and_wait(
    space_id = space_id,
    conversation_id=conversation_id,
    content = question
  )

  if conversation.attachments[0].query is None:
    return {
      "response_data": None, 
      "conversation_id": conversation.conversation_id, 
      "response_text": conversation.attachments[0].text.content}

  elif conversation.attachments[0].text is not None:
    response = w.genie.get_message_attachment_query_result(
      space_id = space_id,
      conversation_id = conversation.conversation_id,
      message_id = conversation.message_id,
      attachment_id = conversation.attachments[0].attachment_id
    )

    schema_list = [i.name for i in response.statement_response.manifest.schema.columns]
    data = response.statement_response.result.data_array

    return {
      "response_data": pd.DataFrame(data, columns=schema_list), 
      "conversation_id": conversation.conversation_id, 
      "response_text": conversation.attachments[0].text.content}

  else:
    response = w.genie.get_message_attachment_query_result(
      space_id = space_id,
      conversation_id = conversation.conversation_id,
      message_id = conversation.message_id,
      attachment_id = conversation.attachments[0].attachment_id
    )

    schema_list = [i.name for i in response.statement_response.manifest.schema.columns]
    data = response.statement_response.result.data_array

    return {
      "response_data": pd.DataFrame(data, columns=schema_list), 
      "conversation_id": conversation.conversation_id, 
      "response_text": None}