# Market Abuse Watchlist

Flags synthetic trading sequences for compliance review.

## What it includes

- deterministic sample data
- scoring and ranking logic
- command line report
- unit tests
- continuous validation workflow

## Run

```bash
python3 -m market_abuse_watchlist.cli --input data/sample_orders.json
```

## Test

```bash
python3 -m unittest discover tests
```
