FROM golang:1.22

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN go build -o price_scraper .

CMD ["./price_scraper", "-interval=20"]
