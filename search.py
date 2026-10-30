from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
import rich

# docker ke container se connection build kiya he
client = QdrantClient(url="http://localhost:6333")

search_result = client.query_points(
    collection_name="test_collection",
    query=[0.05, 0.61, 0.76, 0.74],
    query_filter=Filter(
        must=[FieldCondition(key="city", match=MatchValue(value="Berlin"))]
    ),
    with_payload=True,
    limit=3
).points

rich.print("search_result: ", search_result)