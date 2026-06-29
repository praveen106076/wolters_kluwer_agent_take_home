def search_web(query):
    # In a real assessment, use a search API like Tavily or Serper
    return f"Search results for '{query}': [Stub data: AI Agents are evolving in 2026...]"

def read_file(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"