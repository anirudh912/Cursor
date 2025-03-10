import logging
import yagooglesearch

urls=[]
def disable_logging():
    # Disable all logging for cleaner output
    logging.getLogger().setLevel(logging.CRITICAL)
    logging.basicConfig(level=logging.CRITICAL)

    for logger_name in ["urllib3", "requests", "yagooglesearch"]:
        logging.getLogger(logger_name).setLevel(logging.CRITICAL)

def search_google(query, max_results=10):
    disable_logging()

    client = yagooglesearch.SearchClient(
        query,
        max_search_result_urls_to_return=max_results,
        verbosity=0,
        verbose_output=False,  # Only output URLs
    )

    client.assign_random_user_agent()
    return client.search()