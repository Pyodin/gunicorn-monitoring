# gunicorn-monitoring

`gunicorn-monitoring` is a small project for Python Flask applications using Prometheus, StatsD exporters, and Grafana for visualization, all containerized with Docker and orchestrated with Docker-Compose. This project can monitor multiple applications and creates load scenarios through a Python script to help you understand how your applications behave under stress.

## Features

- **3 Dockerized Flask applications**: Each app is containerized individually to simulate different service environments.
- **Prometheus**: A powerful time-series monitoring service, pre-configured to scrape metrics from StatsD exporters.
- **StatsD-Exporters**: Collects and aggregates custom metrics from your Flask applications.
- **Grafana**: Visualizes your metrics, allowing you to build comprehensive dashboards from your StatsD and Prometheus data.
- **load.py**: A Python script to generate load on your applications, to monitor behavior under stress.

## Getting Started

### Prerequisites

- Docker
- Docker-compose

### Installation

1. Clone the repository
    ```bash
    git clone https://github.com/Pyodin/gunicorn-monitoring.git
    ```
2. Navigate to the project directory
    ```bash
    cd gunicorn-monitoring
    ```
3. Run Docker Compose
    ```bash
    docker-compose up
    ```

Once all services are up and running, you can access the Grafana dashboard at `http://localhost:3000`.

## Usage

After you have the project up and running, you can start generating load to your applications:

```bash
python load.py
```

The load.py script will start sending requests to your Flask apps, which will generate StatsD metrics. Prometheus will scrape these metrics, and they will be available in your Grafana dashboard.

## Acknowledgements

- [Grafana](https://grafana.com/)
- [Prometheus](https://prometheus.io/)
- [Docker](https://www.docker.com/)
- [Docker-Compose](https://docs.docker.com/compose/)
- [StatsD-Exporters]
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Gunicorn](https://gunicorn.org/)


