# Weather Cli Analyzer

CSV-based weather summary CLI for quick local analysis.

## Stack

- Language: Python
- Difficulty: low
- Scope: small, self-contained service/tool with clear extension points

## Project layout

The repository keeps implementation code under `src/` where that is idiomatic, plus a short runnable entry point and a small sample payload when useful.

## Run

```bash
python weather_cli.py data/sample_weather.csv
```

## Engineering notes

The implementation keeps parsing, domain logic and output formatting separate enough to grow without turning into a script dump. Generated artifacts and dependency folders are intentionally ignored.
