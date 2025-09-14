# Price Scraper CLI

A simple Go CLI app that scrapes live prices from [tgju.org](https://www.tgju.org) and displays them in a colorful terminal table with up/down trends and percentage changes. Output is in English, with the date shown in Jalali (Shamsi) format.

## Features

- Scrapes multiple economic indicators (USD, Gold, Bitcoin, etc.)
- Terminal UI with colored output and change indicators
- Jalali (Shamsi) date format
- Auto-refresh or one-time fetch
- Docker-ready
- Fully tested (unit + parser tests)
- CI/CD via GitHub Actions

## Preview

```

Date (Jalali): 1403-06-24   |   Time: 12:45:07
+-------------+---------+------------------+
\| Item        | Price   | Change           |
+-------------+---------+------------------+
\| Dollar      | 58900   | ▲ +500 (0.85%)   |
\| Gold18K     | 2645000 | ▼ -15000 (-0.56%)|
\| Bitcoin     | 1,234M  | • —              |
...

````

## Usage

### Local

```bash
go mod tidy
go run .                # auto-refresh every 20s
go run . -once          # fetch once and exit
go run . -interval=10   # refresh every 10s
````

### Run Tests

```bash
go test ./... -v
```

### Docker

```bash
docker build -t price-scraper .
docker run --rm -it price-scraper -once
```

## GitHub Actions CI/CD

* ✅ Lint and test on every push
* ✅ Docker image builds automatically on `main`



