from dapr_agents import RoundRobinOrchestrator
from dotenv import load_dotenv
import asyncio
import logging


async def main():
    try:
        workflow_service = RoundRobinOrchestrator(
            name="RoundRobinOrchestrator",
            message_bus_name="messagepubsub",
            state_store_name="workflowstatestore",
            state_key="workflow_state",
            agents_registry_store_name="agentstatestore",
            agents_registry_key="agents_registry",
            broadcast_topic_name="beacon_channel",
            max_iterations=3,
        ).as_service(port=8004)

        await workflow_service.start()
    except Exception as e:
        print(f"Error starting service: {e}")


if __name__ == "__main__":
    load_dotenv()

    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
