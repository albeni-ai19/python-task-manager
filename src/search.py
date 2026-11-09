def search_tasks(q): return [t for t in tasks if q in t]
def filter_by_status(done=True): return [t for t in tasks if t == done]
