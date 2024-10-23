train_data = [
    ("List out My appointments", "db"),  # Use LLM for general knowledge explanation
    (
        "When will doctor XYZ will be available",
        "db",
    ),  # Web search required for recent news
    ("List out the available doctor", "db"),  # Use LLM for conceptual explanation
    (
        "Update my status to available",
        "kafka",
    ),  # Web search for real-time data
    (
        "Update my availability status to not available",
        "kafka",
    ),  # LLM for scientific concepts
    (
        "What are the hospital timings",
        "RAG",
    ),  # Web search for recent events
    (
        "Documents Needed for appointment scheduling",
        "RAG",
    ),  # RAG for detailed information retrieval
    (
        "list the available OPD's free",
        "db",
    ),  # RAG for sourcing multiple viewpoints
    (
        "List out the empty icu beds",
        "db",
    ),  # LLM for opinion-based knowledge
    (
        "List out the appointments",
        "db",
    ),  # Web search for up-to-date research
    (
        "What will be 2 + 2 equal to",
        "LLM",
    ),  # LLM for general knowledge on health
    ("When was america founder", "LLM"),  # RAG for analyzing multiple sources
    (
        "What is a Hospital?",
        "LLM",
    ),  # Web search for current data on companies
    (
        "What are the stages of Cancer",
        "LLM",
    ),  # RAG for historical data and aggregation
    ("Consulting Fees for cardiologies", "RAG"),
    ("How many orthopadic doctors are available", "db"),
    ("Is there a empty ICU bed", "db"),
    ("Is Dr bhatra Available", "db"),
    ("I am off. please log out", "db"),
    ("List the OT's available to use", "db"),
    ("Update the ICU 1042 room to occupied", "kafka"),
    ("Update the appointment 124 to completed", "kafka"),
]
