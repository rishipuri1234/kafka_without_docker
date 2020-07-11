from kafka.admin import KafkaAdminClient, NewTopic


admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092")
    # client_id='test'
# )

topic_list = []
topic_list.append(NewTopic(name="metadata_input", num_partitions=1, replication_factor=1))
topic_list.append(NewTopic(name="stateful_data_of_query", num_partitions=1, replication_factor=1))
topic_list.append(NewTopic(name="change_log_of_query", num_partitions=1, replication_factor=1))
topic_list.append(NewTopic(name="Processing_completed", num_partitions=1, replication_factor=1))
topic_list.append(NewTopic(name="Prediction", num_partitions=1, replication_factor=1))
topic_list.append(NewTopic(name="Event_Error", num_partitions=1, replication_factor=1))
topic_list.append(NewTopic(name="message", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)