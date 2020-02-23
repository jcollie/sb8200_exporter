"""Main program."""

import argparse
import http.server

import prometheus_client
import sb8200_exporter


def main():
    """Main program."""
    parser = argparse.ArgumentParser("Eagle Parser")

    parser.add_argument("--port", type=int, default=9195)
    parser.add_argument("--bind_address", default="0.0.0.0")
    parser.add_argument("--address", default="192.168.100.1")

    args = parser.parse_args()

    collector = sb8200_exporter.Collector(args.address)

    prometheus_client.REGISTRY.register(collector)

    handler = prometheus_client.MetricsHandler.factory(
            prometheus_client.REGISTRY)
    server = http.server.HTTPServer(
            (args.bind_address, args.port), handler)
    server.serve_forever()
