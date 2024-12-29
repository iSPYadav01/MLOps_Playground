from feast import FeatureStore
import pandas as pd

store = FeatureStore(repo_path=".")

# Historical Features Retrieval
def get_historical_features():
    entity_df = pd.DataFrame(
        {
            "driver_id": [1001, 1002],
            "event_timestamp": ["2021-04-12 10:59:42", "2021-04-12 08:12:10"],
        }
    )
    features = store.get_historical_features(
        entity_df=entity_df,
        feature_refs=["driver.conv_rate", "driver.acc_rate", "driver.avg_daily_trips"],
    ).to_df()
    return features

# Materialize Features
store.materialize_incremental(end_date=pd.Timestamp.now().isoformat())

# Read Online Features
features = store.get_online_features(
    feature_refs=["driver.conv_rate", "driver.acc_rate"],
    entity_rows=[{"driver_id": 1001}],
).to_dict()